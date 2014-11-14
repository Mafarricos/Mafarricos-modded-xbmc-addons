import urllib,urllib2,re,cookielib,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art



def MAIN():
    link=main.OPENURL('http://m.fifaembed.com/sports-channels.php')
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.compile('<li><a href="([^"]+)">([^<]+)</a></li>').findall(link)
    for url,name in match:
        main.addDir(name,url,444,'')

def LIST(url):
    link=main.OPENURL(url)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.compile('<li><a target=".+?" href="([^"]+)">([^<]+)</a></li>').findall(link)
    for url,name in match:
        main.addPlayL(name,url,445,'','','','','','',secName='SportsPack',secIcon=art+'/spo.png')

def LINK(mname,murl,thumb):
        main.GA("SportsPack","Watched")
        stream_url=False
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Opening Stream,3000)")
        ok=True
        stream_url = murl
        listitem = xbmcgui.ListItem(thumbnailImage=thumb)
        infoL={'Title': mname, 'Genre': 'Live'} 
        from resources.universal import playbackengine
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='movie', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams='',imdb_id='')
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            from resources.universal import watchhistory
            wh = watchhistory.WatchHistory('plugin.video.movie25')
            wh.add_item(mname+' '+'[COLOR green]SportsPack[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
        return ok
