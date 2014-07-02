# -*- coding: utf-8 -*-
#

import xbmc
import xbmcaddon
import xbmcgui
import math
import time
import copy
import re

try:
	import simplejson as json
except ImportError:
	import json

# read settings
__addon__ = xbmcaddon.Addon('script.traktBeta')

# make strptime call prior to doing anything, to try and prevent threading errors
time.strptime("1970-01-01 12:00:00", "%Y-%m-%d %H:%M:%S")

REGEX_EXPRESSIONS = [ '[Ss]([0-9]+)[][._-]*[Ee]([0-9]+)([^\\\\/]*)$',
                      '[\._ \-]([0-9]+)x([0-9]+)([^\\/]*)',                     # foo.1x09
                      '[\._ \-]([0-9]+)([0-9][0-9])([\._ \-][^\\/]*)',          # foo.109
                      '([0-9]+)([0-9][0-9])([\._ \-][^\\/]*)',
                      '[\\\\/\\._ -]([0-9]+)([0-9][0-9])[^\\/]*',
                      'Season ([0-9]+) - Episode ([0-9]+)[^\\/]*',              # Season 01 - Episode 02
                      'Season ([0-9]+) Episode ([0-9]+)[^\\/]*',                # Season 01 Episode 02
                      '[\\\\/\\._ -][0]*([0-9]+)x[0]*([0-9]+)[^\\/]*',
                      '[[Ss]([0-9]+)\]_\[[Ee]([0-9]+)([^\\/]*)',                #foo_[s01]_[e01]
                      '[\._ \-][Ss]([0-9]+)[\.\-]?[Ee]([0-9]+)([^\\/]*)',       #foo, s01e01, foo.s01.e01, foo.s01-e01
                      's([0-9]+)ep([0-9]+)[^\\/]*',                             #foo - s01ep03, foo - s1ep03
                      '[Ss]([0-9]+)[][ ._-]*[Ee]([0-9]+)([^\\\\/]*)$',
                      '[\\\\/\\._ \\[\\(-]([0-9]+)x([0-9]+)([^\\\\/]*)$'
                     ]

def Debug(msg, error=False):
	level = xbmc.LOGERROR if error else xbmc.LOGDEBUG
	xbmc.log("[trakt] %s" % msg, level=level)

def notification(header, message, time=5000, icon=__addon__.getAddonInfo('icon')):
	xbmc.executebuiltin("XBMC.Notification(%s,%s,%i,%s)" % (header, message, time, icon))

def showSettings():
	__addon__.openSettings()

def getSetting(setting):
    return __addon__.getSetting(setting).strip()

def getSettingAsBool(setting):
        return getSetting(setting).lower() == "true"

def getSettingAsFloat(setting):
    try:
        return float(getSetting(setting))
    except ValueError:
        return 0

def getSettingAsInt(setting):
    try:
        return int(getSettingAsFloat(setting))
    except ValueError:		
        return 0

def getSettingAsList(setting):
	data = getSetting(setting)
	try:
		return json.loads(data)
	except ValueError:
		return []

def setSetting(setting, value):
	__addon__.setSetting(setting, str(value))

def setSettingFromList(setting, value):
	if value is None:
		value = []
	data = json.dumps(value)
	setSetting(setting, data)

def getString(string_id):
    return __addon__.getLocalizedString(string_id).encode('utf-8', 'ignore')

def getProperty(property):
	return xbmcgui.Window(10000).getProperty(property)

def getPropertyAsBool(property):
	return getProperty(property) == "True"
	
def setProperty(property, value):
	xbmcgui.Window(10000).setProperty(property, value)

def clearProperty(property):
	xbmcgui.Window(10000).clearProperty(property)

def isMovie(type):
	return type == 'movie'

def isEpisode(type):
	return type == 'episode'

def isShow(type):
	return type == 'show'

def isSeason(type):
	return type == 'season'

def isValidMediaType(type):
	return type in ['movie', 'show', 'episode']

def xbmcJsonRequest(params):
	data = json.dumps(params)
	request = xbmc.executeJSONRPC(data)
	response = None
	try:
		response = json.loads(request)
	except UnicodeDecodeError:
		response = json.loads(request.decode('utf-8', 'ignore'))

	try:
		if 'result' in response:
			return response['result']
		return None
	except KeyError:
		Debug("[%s] %s" % (params['method'], response['error']['message']), True)
		return None

def sqlDateToUnixDate(date):
	if not date:
		return 0
	t = time.strptime(date, "%Y-%m-%d %H:%M:%S")
	try:
		utime = int(time.mktime(t))
	except OverflowError:
		utime = None
	return utime

def chunks(l, n):
	return [l[i:i+n] for i in range(0, len(l), n)]

# check exclusion settings for filename passed as argument
def checkScrobblingExclusion(fullpath):

	if not fullpath:
		return True
	
	Debug("checkScrobblingExclusion(): Checking exclusion settings for '%s'." % fullpath)
	
	if (fullpath.find("pvr://") > -1) and getSettingAsBool('ExcludeLiveTV'):
		Debug("checkScrobblingExclusion(): Video is playing via Live TV, which is currently set as excluded location.")
		return True
				
	if (fullpath.find("http://") > -1) and getSettingAsBool('ExcludeHTTP'):
		Debug("checkScrobblingExclusion(): Video is playing via HTTP source, which is currently set as excluded location.")
		return True
		
	ExcludePath = getSetting('ExcludePath')
	if ExcludePath != "" and getSettingAsBool('ExcludePathOption'):
		if (fullpath.find(ExcludePath) > -1):
			Debug("checkScrobblingExclusion(): Video is playing from location, which is currently set as excluded path 1.")
			return True

	ExcludePath2 = getSetting('ExcludePath2')
	if ExcludePath2 != "" and getSettingAsBool('ExcludePathOption2'):
		if (fullpath.find(ExcludePath2) > -1):
			Debug("checkScrobblingExclusion(): Video is playing from location, which is currently set as excluded path 2.")
			return True

	ExcludePath3 = getSetting('ExcludePath3')
	if ExcludePath3 != "" and getSettingAsBool('ExcludePathOption3'):
		if (fullpath.find(ExcludePath3) > -1):
			Debug("checkScrobblingExclusion(): Video is playing from location, which is currently set as excluded path 3.")
			return True
	
	return False

def getFormattedItemName(type, info, short=False):
	s = None
	if isShow(type):
		s = info['title']
	elif isEpisode(type):
		if short:
			s = "S%02dE%02d - %s" % (info['episode']['season'], info['episode']['number'], info['episode']['title'])
		else:
			s = "%s - S%02dE%02d - %s" % (info['show']['title'], info['episode']['season'], info['episode']['number'], info['episode']['title'])
	elif isSeason(type):
		if info['season'] > 0:
			s = "%s - Season %d" % (info['title'], info['season'])
		else:
			s = "%s - Specials" % info['title']
	elif isMovie(type):
		s = "%s (%s)" % (info['title'], info['year'])
	return s.encode('utf-8', 'ignore')

def getShowDetailsFromXBMC(showID, fields):
	result = xbmcJsonRequest({'jsonrpc': '2.0', 'method': 'VideoLibrary.GetTVShowDetails', 'params':{'tvshowid': showID, 'properties': fields}, 'id': 1})
	Debug("getShowDetailsFromXBMC(): %s" % str(result))

	if not result:
		Debug("getEpisodeDetailsFromXbmc(): Result from XBMC was empty.")
		return None

	try:
		return result['tvshowdetails']
	except KeyError:
		Debug("getShowDetailsFromXBMC(): KeyError: result['tvshowdetails']")
		return None

# get a single episode from xbmc given the id
def getEpisodeDetailsFromXbmc(libraryId, fields):
	result = xbmcJsonRequest({'jsonrpc': '2.0', 'method': 'VideoLibrary.GetEpisodeDetails', 'params':{'episodeid': libraryId, 'properties': fields}, 'id': 1})
	Debug("getEpisodeDetailsFromXbmc(): %s" % str(result))

	if not result:
		Debug("getEpisodeDetailsFromXbmc(): Result from XBMC was empty.")
		return None

	show_data = getShowDetailsFromXBMC(result['episodedetails']['tvshowid'], ['year', 'imdbnumber'])
	
	if not show_data:
		Debug("getEpisodeDetailsFromXbmc(): Result from getShowDetailsFromXBMC() was empty.")
		return None
		
	result['episodedetails']['tvdb_id'] = show_data['imdbnumber']
	result['episodedetails']['year'] = show_data['year']
	
	try:
		return result['episodedetails']
	except KeyError:
		Debug("getEpisodeDetailsFromXbmc(): KeyError: result['episodedetails']")
		return None

# get a single movie from xbmc given the id
def getMovieDetailsFromXbmc(libraryId, fields):
	result = xbmcJsonRequest({'jsonrpc': '2.0', 'method': 'VideoLibrary.GetMovieDetails', 'params':{'movieid': libraryId, 'properties': fields}, 'id': 1})
	Debug("getMovieDetailsFromXbmc(): %s" % str(result))

	if not result:
		Debug("getMovieDetailsFromXbmc(): Result from XBMC was empty.")
		return None

	try:
		return result['moviedetails']
	except KeyError:
		Debug("getMovieDetailsFromXbmc(): KeyError: result['moviedetails']")
		return None

def findInList(list, returnIndex=False, returnCopy=False, case_sensitive=True, *args, **kwargs):
	for index in range(len(list)):
		item = list[index]
		i = 0
		for key in kwargs:
			if not key in item:
				continue
			if not case_sensitive and isinstance(item[key], basestring):
				if item[key].lower() == kwargs[key].lower():
					i = i + 1
			else:
				if item[key] == kwargs[key]:
					i = i + 1
		if i == len(kwargs):
			if returnIndex:
				return index
			else:
				if returnCopy:
					return copy.deepcopy(list[index])
				else:
					return list[index]
	return None

def findAllInList(list, key, value):
	return [item for item in list if item[key] == value]

def findMovie(movie, movies, returnIndex=False):
	result = None
	if 'imdb_id' in movie and unicode(movie['imdb_id']).startswith("tt"):
		result = findInList(movies, returnIndex=returnIndex, imdb_id=movie['imdb_id'])
	if result is None and 'tmdb_id' in movie and unicode(movie['tmdb_id']).isdigit():
		result = findInList(movies, returnIndex=returnIndex, tmdb_id=unicode(movie['tmdb_id']))
	if result is None and movie['title'] and movie['year'] > 0:
		result = findInList(movies, returnIndex=returnIndex, title=movie['title'], year=movie['year'])
	return result

def findShow(show, shows, returnIndex=False):
	result = None
	if 'tvdb_id' in show and unicode(show['tvdb_id']).isdigit():
		result = findInList(shows, returnIndex=returnIndex, tvdb_id=unicode(show['tvdb_id']))
	if result is None and 'imdb_id' in show and unicode(show['imdb_id']).startswith("tt"):
		result = findInList(shows, returnIndex=returnIndex, imdb_id=show['imdb_id'])
	if result is None and show['title'] and 'year' in show and show['year'] > 0:
		result = findInList(shows, returnIndex=returnIndex, title=show['title'], year=show['year'])
	return result

def regex_tvshow(compare, file, sub = ""):
	sub_info = ""
	tvshow = 0

  	for regex in REGEX_EXPRESSIONS:
  		response_file = re.findall(regex, file)
  		if len(response_file) > 0 :
  			Debug("regex_tvshow(): Regex File Se: %s, Ep: %s," % (str(response_file[0][0]),str(response_file[0][1]),) )
  			tvshow = 1
  			if not compare :
  				title = re.split(regex, file)[0]
  				for char in ['[', ']', '_', '(', ')','.','-']:
  					title = title.replace(char, ' ')
  				if title.endswith(" "): title = title[:-1]
  				return title,response_file[0][0], response_file[0][1]
  			else:
  				break

  	if (tvshow == 1):
  		for regex in regex_expressions:
  			response_sub = re.findall(regex, sub)
  			if len(response_sub) > 0 :
  				try :
  					sub_info = "Regex Subtitle Ep: %s," % (str(response_sub[0][1]),)
  					if (int(response_sub[0][1]) == int(response_file[0][1])):
  						return True
  				except: pass
  		return False
  	if compare :
  		return True
  	else:
  		return "","",""