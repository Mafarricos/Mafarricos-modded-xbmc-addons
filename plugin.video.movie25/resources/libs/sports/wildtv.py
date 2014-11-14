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

def WILDTV(murl):
        main.GA("Sports","Wildtv")
        link=main.OPENURL(murl)
        match=re.compile('<option value="(.+?)">(.+?)</option>').findall(link)
        for idnum, name in match:
            url='https://www.wildtv.ca/show/'+idnum
            main.addDir(name,url,93,art+'/wildtv.png')

def LISTWT(murl):
        main.GA("Wildtv","Wildtv-list")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\xc2\xa0','')
        match=re.compile('<a title="(.+?)" alt=".+?" href="(.+?)"><img class=".+?src="(.+?)" />',re.DOTALL).findall(link)
                          
        for name, url, thumb in match:
            thumb='https:'+thumb
            url='https://www.wildtv.ca' +url
            main.addPlayMs(name,url,94,thumb,'','','','','')

def LINKWT(mname,murl):
        main.GA("Wildtv-list","Watched")
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Playing Link,3000)")
        link=main.OPENURL(murl)
        ok=True
        stream=re.compile('streamer: "(.+?)",').findall(link)
        Path=re.compile('file: "mp4:med/(.+?).mp4",').findall(link)
        if len(Path)>0:
            desc=re.compile('<meta name="description" content="(.+?)" />').findall(link)
            if len(desc)>0:
                desc=desc[0]
            else:
                desc=''
            thumb=re.compile('image: "(.+?)",').findall(link)
            if len(thumb)>0:
                thumb='https:'+thumb[0]
            else:
                thumb=''
            stream_url = stream[0]
            if selfAddon.getSetting("wild-qua") == "0":
                    playpath = 'mp4:high/'+Path[0]+'.mp4'
            elif selfAddon.getSetting("wild-qua") == "1":
                    playpath = 'mp4:med/'+Path[0]+'.mp4'
            playpath= playpath.replace('mp4:','/')
            stream_url=stream_url+playpath
            infoL={ "Title": mname, "Plot": desc}
            # play with bookmark
            player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
            #WatchHistory
            if selfAddon.getSetting("whistory") == "true":
                    wh.add_item(mname+' '+'[COLOR green]WildTv[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
            player.KeepAlive()
            return ok
        else:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link not found,3000)")
