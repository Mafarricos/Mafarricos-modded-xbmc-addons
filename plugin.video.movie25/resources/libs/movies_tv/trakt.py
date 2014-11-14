import urllib,re,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
MAINURL='https://www.trakt.tv'
prettyName='Trakt'
TRAKT_API = '4ff3c522308d31f438ec7213bfd3aa1d'

def downloadFile(url,dest):
    try:
        urllib.urlretrieve(url,dest)
    except Exception, e:
        dialog = xbmcgui.Dialog()
        main.ErrorReport(e)
        dialog.ok("Mash Up", "Report the error below at " + main.supportsite, str(e), "We will try our best to help you")

user = selfAddon.getSetting('trusername')
passw = selfAddon.getSetting('trpassword')
cookie_file = os.path.join(os.path.join(main.datapath,'Cookies'), 'trakt.cookies')
api_file = os.path.join(os.path.join(main.datapath,'Cookies'), 'trakt.api')
apifile = main.getFile(api_file)
if apifile: TRAKT_API = apifile

if user == '' or passw == '':
    if os.path.exists(cookie_file):
        try: os.remove(cookie_file)
        except: pass
    dialog = xbmcgui.Dialog()
    ret = dialog.yesno('[COLOR=FF67cc33]MashUp[/COLOR]', 'Please set your Trakt.tv credentials','or register if you don have an account','','Cancel','Login')
    if ret == 1:
        keyb = xbmc.Keyboard('', 'Enter Trakt Username')
        keyb.doModal()
        if (keyb.isConfirmed()):
            username = keyb.getText()
            keyb = xbmc.Keyboard('', 'Enter Trakt Password:')
            keyb.doModal()
            if (keyb.isConfirmed()):
                password = keyb.getText()
                selfAddon.setSetting('trusername',username)
                selfAddon.setSetting('trpassword',password)
                
user = selfAddon.getSetting('trusername')
passw = selfAddon.getSetting('trpassword')

def setCookie():
    cookieExpired = False
    if os.path.exists(cookie_file):
        try:
            cookie = open(cookie_file).read()
            expire = re.search('expires="(.*?)"',cookie, re.I)
            if expire:
                expire = str(expire.group(1))
                import time
                if time.time() > time.mktime(time.strptime(expire, '%Y-%m-%d %H:%M:%SZ')):
                   cookieExpired = True
        except: cookieExpired = True 
        loggedin = re.search('morbo',cookie, re.I)
    if not os.path.exists(cookie_file) or cookieExpired or (not loggedin and user != '' and passw != '') or not apifile:
        main.OPENURL('http://trakt.tv/auth/signin',data={'username':user,'password':passw,'remember_me':1},cookie='trakt')
    if not apifile:
        apihtml = main.OPENURL('http://trakt.tv/settings/api',cookie='trakt')
        api = re.search('(?i)name="email" value="([^"]+?)"',apihtml)
        if api: main.setFile(api_file,api.group(1),True)

def getRelativeDate(days):
    if days < -1: days = str(abs(days)) + ' days ago'
    elif days == -1: days = 'Yesterday'
    elif days == 0: days = 'Today'
    elif days == 1: days = 'Tomorrow'
    elif days > 1: days = 'In ' + str(days) + ' days'
    return str(days)

def showList(cacheOnly = False):
    if not user:
        xbmc.executebuiltin("XBMC.Notification(Sorry,Set Trakt user in settings,3000)")
        xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False, False)
        return False
    import time,datetime,calendar
    todaytimestamp = time.mktime(time.strptime(time.strftime("%Y") + "-" + time.strftime("%m") + "-" + time.strftime("%d"), "%Y-%m-%d"))
    cached_path = os.path.join(os.path.join(main.datapath,'Cache'), 'Trakt')
    cached = main.getFile(cached_path)
    if (not cached or (cached and time.mktime(datetime.date.today().timetuple()) > os.stat(cached_path).st_mtime)
         or xbmcgui.Window(10000).getProperty('Refresh_Trakt')):
        setCookie()
        import hashlib,json
        data = {'username':user,'password':hashlib.sha1(passw).hexdigest()}
        link = main.OPENURL("http://api.trakt.tv/user/calendar/shows.json/"+TRAKT_API+"/"+user+'/6daysago/14',data=data)
        fields=json.loads(link)
        tofront = []
        daysinfuture = 2
        daysinpast = 1
        for item in fields:
            timestamp =  time.mktime(time.strptime(item['date'], "%Y-%m-%d"))
            if timestamp <= todaytimestamp + daysinfuture * 86400 and timestamp >= todaytimestamp - daysinpast * 86400:
                tofront.append(item)
        for item in tofront:fields.remove(item)
        fields = tofront + fields
        if fields:
            main.setFile(cached_path,str(fields),True)
        xbmcgui.Window(10000).clearProperty('Refresh_Trakt')
    else: fields = eval(cached)
    if cacheOnly: return False
    main.GA("None","Trakt")
    main.addDir('Search for Shows','TV',430,art+'/search.png')
    main.addDir('All Tracked Shows','TV',431,art+'/sidereel.png')
    showsdisplayed = 0
    for data in fields:
        timestamp =  time.mktime(time.strptime(data['date'], "%Y-%m-%d"))
        datestring = (datetime.datetime.fromtimestamp(timestamp)).strftime('%A, %b %d')
        days = (timestamp - todaytimestamp) / 86400
        relative = getRelativeDate(days)
        main.addLink('[COLOR yellow]'+str(datestring)+'[/COLOR]  [COLOR orange]('+relative+')[/COLOR]','',art+'/link.png')
        for showdata in data['episodes']:
            if showdata['episode']['season'] < 10: sea='0'+str(showdata['episode']['season'])
            else: sea=str(showdata['episode']['season'])
            if showdata['episode']['number'] < 10: epi='0'+str(showdata['episode']['number'])
            else: epi=str(showdata['episode']['number'])
            episodenumber= 'S'+sea+'E'+epi
            airtime = showdata['show']['air_time_localized'].upper().replace("AM"," AM").replace("PM"," PM")+' on ' + showdata['show']['network']
            main.addDir(showdata['show']['title'].encode('utf-8')+' '+episodenumber+' [COLOR red]"'+showdata['episode']['title'].encode('utf-8')+
                        '"[/COLOR] [COLOR blue]'+ airtime.encode('utf-8') +'[/COLOR]','TV',20,showdata['show']['images']['poster'].encode('utf-8'))
            #            showdata['episode']['overview'].encode('utf-8'),showdata['episode']['images']['screen'].encode('utf-8'))
            showsdisplayed += 1
    if not showsdisplayed: main.removeFile(cached_path)
    
def searchShow():
    search  = ''
    if len(search) < 1:
        keyb = xbmc.Keyboard('', 'Search Shows')
        keyb.doModal()
        if (keyb.isConfirmed()):
            search = keyb.getText()
            
    if not search:
        xbmcplugin.endOfDirectory(int(sys.argv[1]),False,False)
        return
        
    encode=urllib.quote(search)
    surl='http://api.trakt.tv/search/shows.json/'+TRAKT_API+'?query='+encode
    sys.argv.append(surl)
    SEARCHED(surl)

def SEARCHED(surl):
    main.GA("SideReel","Search")
    setCookie()
    import hashlib
    data = {'username':user,'password':hashlib.sha1(passw).hexdigest()}
    link = main.OPENURL(surl,data=data)
    import json
    fields=json.loads(link)
    for data in fields:
        main.addDir(data['title'].encode('utf-8'),str(data['tvdb_id']),432,data['images']['poster'])


def trackedShows():
    main.GA("SideReel","Tracked Shows")
    setCookie()
    import hashlib
    data = {'username':user,'password':hashlib.sha1(passw).hexdigest()}
    link = main.OPENURL("http://api.trakt.tv/user/watchlist/shows.json/"+TRAKT_API+"/"+user,data=data)
    import json
    fields=json.loads(link)
    for data in fields:
        main.addDir(data['title'].encode('utf-8'),str(data['tvdb_id']),433,data['images']['poster'])

def trackShow(title,track):
    dialog = xbmcgui.Dialog()
    ret = dialog.yesno('[COLOR=FF67cc33]MashUp[/COLOR]', 'Track '+title,'Do you want to track '+title+'?','','NO','YES')
    if ret == 1:
        import hashlib,json
        data = {'username':user,'password':hashlib.sha1(passw).hexdigest(),'shows':[{'tvdb_id': int(track)}]}
        link = main.OPENURL('http://api.trakt.tv/show/watchlist/'+TRAKT_API,data=data,type='json')
        if re.search('(?i)"already_exist":1',link):
            xbmc.executebuiltin("XBMC.Notification(Tracking Failed,You already track "+title+",5000,"+main.slogo+")")
        elif re.search('(?i)"inserted":1',link):
            xbmc.executebuiltin("XBMC.Notification(Tracking Successful,You now track "+title+",5000,"+main.slogo+")")
            xbmcgui.Window(10000).setProperty('Refresh_Trakt', '1')
        else:
            xbmc.executebuiltin("XBMC.Notification(Tracking Failed,Unknown reason,5000,"+main.slogo+")")
    xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False)

def untrackShow(title,track):
    dialog = xbmcgui.Dialog()
    ret = dialog.yesno('[COLOR=FF67cc33]MashUp[/COLOR]', 'Untrack '+title,'Do you want to untrack '+title+'?','','NO','YES')
    if ret == 1:
        import hashlib,json
        data = {'username':user,'password':hashlib.sha1(passw).hexdigest(),'shows':[{'tvdb_id': int(track)}]}
        link = main.OPENURL('http://api.trakt.tv/show/unwatchlist/'+TRAKT_API,data=data,type='json')
        if re.search('(?i)"1 shows removed from watchlist"',link):
            xbmc.executebuiltin("XBMC.Notification(Untracking Successful,You have untracked "+title+",3000,"+main.slogo+")")
            xbmcgui.Window(10000).setProperty('Refresh_Trakt', '1')
            xbmc.executebuiltin("XBMC.Container.Refresh")
        else:
            xbmc.executebuiltin("XBMC.Notification(Untracking Failed,Try again later,5000,"+main.slogo+")")
    xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False)
