# -*- coding: cp1252 -*-
import urllib,urllib2,re,cookielib,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art
from resources.universal import watchhistory
    
wh = watchhistory.WatchHistory('plugin.video.movie25')

def MUSICSTREAMS():
        main.GA("MUSIC-Streams","List")
        link=main.OPENURL('https://raw.github.com/crusader88/MashUpStreams/master/playlists/musicstreams2.xml')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<item><titl[^>]+>([^<]+)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail></item>').findall(link)
        for name,url,thumb in sorted(match):
            main.addPlayL(name,url,184,thumb,'','','','','',secName='Music Streams',secIcon=art+'/miscmusic.png')

        
        
def MUSICSTREAMSLink(mname,murl,thumb):
        main.GA("MUSIC-Streams-"+mname,"Watched")
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        stream_url = murl
        listitem = xbmcgui.ListItem(thumbnailImage=thumb)
        infoL={'Title': mname, 'Genre': 'Live'} 
        from resources.universal import playbackengine
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='movie', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams='',imdb_id='')

        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            wh.add_item(mname+' '+'[COLOR green]MusicStreams[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
        return ok
