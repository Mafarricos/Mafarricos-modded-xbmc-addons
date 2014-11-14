import urllib,urllib2,re,cookielib,urlresolver,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
from resources.universal import playbackengine, watchhistory
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art    
wh = watchhistory.WatchHistory('plugin.video.movie25')


def YOUList(mname,durl):
        if 'gdata' in durl:
                murl=durl
        else:
                murl='https://gdata.youtube.com/feeds/api/playlists/'+durl+'?start-index=1&max-results=50'
        link=main.OPENURL(murl)
        match=re.compile("href='https://m.youtube.com/details.?v=(.+?)'/.+?<media\:descriptio[^>]+>([^<]+)</media\:description>.+?<media\:thumbnail url='([^']+)'.+?<media:title type='plain'>(.+?)/media:title>",re.DOTALL).findall(link)
        for url,desc,thumb,name in reversed(match):
                name=name.replace('<','')
                main.addPlayMs(name,url,206,thumb,desc,'','','','')
        match2=re.compile("<title type=\'text\'>.+?</title><link rel=\'alternate\' type=\'text/html\' href=\'https://www.youtube.com/watch.?v=(.+?)&feature=youtube_gdata\'/>.+?<media:title type=\'plain\'>(.+?)</media:title>").findall(link)
        
        for url,name in reversed(match2):
                name=name.replace('<','')
                main.addPlayMs(name,url,206,'','','','','','')
        tot=len(match)+len(match2)
        if tot >=49:   
            paginate=re.compile('https://gdata.youtube.com/feeds/api/playlists/(.+?).?start-index=(.+?)&max-results=50').findall(murl)
            for id, page in paginate:
                i=int(page)+50
                purl='https://gdata.youtube.com/feeds/api/playlists/'+id+'?start-index='+str(i)+'&max-results=50'
                main.addDir('[COLOR blue]Next[/COLOR]',purl,205,art+'/next2.png')
        main.GA(mname,"Youtube-List")

def YOULink(mname,url,thumb):
        ok=True
        main.GA(mname,"Watched")
        url = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+url+"&hd=1"
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        stream_url = url
        # play with bookmark
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels='', watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            wh.add_item(mname+' '+'[COLOR green]YoutubePlaylist[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
        player.KeepAlive()
        return ok
