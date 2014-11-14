import urllib,urllib2,re,cookielib,string, urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,urlresolver
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
from resources.universal import playbackengine, watchhistory
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art
    
wh = watchhistory.WatchHistory('plugin.video.movie25')


def WB():
        main.addDir('Looney Tunes','Looney Tunes',78,'http://staticswf.kidswb.com/franchise/content/images/touts/video_channel_thumbs/LooneyTunes_video.jpg')
        main.addDir('Ozzy and Drix','Ozzy & Drix',78,'http://staticswf.kidswb.com/franchise/content/images/touts/video_channel_thumbs/OzzieDrix_video.jpg')
        main.addDir('Shaggy and Scoobydoo Get A Clue','Shaggy & Scooby-Doo Get A Clue!',78,'http://staticswf.kidswb.com/franchise/content/images/touts/video_channel_thumbs/ShaggyScoobyGetAClue_video.jpg')
        main.addDir('The Smurfs','Smurfs',78,'http://staticswf.kidswb.com/franchise/content/images/touts/video_channel_thumbs/smurf_video.jpg')
        main.addDir('The Flintstones','The Flintstones',78,'http://staticswf.kidswb.com/franchise/content/images/touts/video_channel_thumbs/Flintstones_video.jpg')
        main.addDir('The Jetsons','The Jetsons',78,'http://staticswf.kidswb.com/franchise/content/images/touts/video_channel_thumbs/Jetsons_video.jpg')
        main.addDir('The New Scoobydoo Mysteries','The New Scooby-Doo Mysteries',78,'http://staticswf.kidswb.com/franchise/content/images/touts/video_channel_thumbs/ScoobyDooMysteries_video.jpg')
        main.addDir('Thundercats','ThunderCats',78,'http://staticswf.kidswb.com/franchise/content/images/touts/video_channel_thumbs/Thundercats.jpg')
        main.addDir('Tom and Jerry Tales','Tom And Jerry Tales',78,'http://staticswf.kidswb.com/franchise/content/images/touts/video_channel_thumbs/TomJerryTales_video.jpg')
        main.addDir('Xiaolin Showdown','Xiaolin Showdown',78,'http://staticswf.kidswb.com/franchise/content/images/touts/video_channel_thumbs/XiaolinShowdown_video.jpg')
        main.GA("KidZone","WBK")


def LISTWB(murl):
    furl='http://staticswf.kidswb.com/kidswb/xml/videofeedlight.xml'
    link=main.OPENURL(furl)
    link=link.replace('&quot;','').replace('&#039;','').replace('&#215;','').replace('&#038;','').replace('&#8216;','').replace('&#8211;','').replace('&#8220;','').replace('&#8221;','').replace('&#8212;','').replace('&amp;','&').replace("`",'')
    match = re.compile('<item><media:title>([^<]+)</media:title><media:description>([^<]+)</media:description><guid isPermaLink="false">([^<]+)</guid><av:show season="1">'+murl+'</av:show><media:thumbnail url="([^<]+)"/></item>').findall(link)
    for name,desc,url,thumb in match:
        main.addPlayMs(name,url,79,thumb,desc,'','','','')
    main.GA("WB","List")


def LINKWB(mname,murl):
        main.GA("WB","Watched")
        ok=True
        url='http://metaframe.digitalsmiths.tv/v2/WBtv/assets/'+murl+'/partner/11?format=json'
        link=main.OPENURL(url)
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        bit700=re.compile('"bitrate": "700", "uri": "(.+?)"').findall(link)
        bit500=re.compile('"bitrate": "500", "uri": "(.+?)"').findall(link)
        if (len(bit700)>0):
                stream_url=bit700[0]
        else:
                stream_url=bit500[0]
        desc=re.compile('"description": "(.+?)", "rating"').findall(link)
        desc=desc[0].replace('\\','')
        thumb=re.compile('"images": .+?".+?": .+?"width": .+?, "uri": "(.+?)"').findall(link)
        infoL={ "Title": mname, "Plot": desc}
        # play with bookmark
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb[0],infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            wh.add_item(mname+' '+'[COLOR green]WB Kids[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb[0], fanart='', is_folder=False)
        player.KeepAlive()
        return ok
