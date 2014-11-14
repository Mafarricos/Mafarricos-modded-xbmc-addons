import urllib,urllib2,re,cookielib,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art



def COUNTRIES():
        main.GA("Live","Countries")
        link=main.OPENURL('https://raw.github.com/crusader88/MashUpStreams/master/countries.xml')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('type=playlistname=Sorted by user-assigned order','').replace('name=Sorted [COLOR=FF00FF00]by user-assigned order[/COLOR]','').replace('name=Live Tv Channels Twothumb','')
        match=re.compile('<name>(.+?)</name><link>(.+?)</link><thumbnail>(.+?)</thumbnail>').findall(link)
        for name,url,thumb in sorted(match):
            main.addDir(name,url,144,thumb)
        main.VIEWSB()
def COUNTRIESList(mname,murl):
        main.GA("Countries-"+mname,"Watched")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('type=playlistname=Sorted by user-assigned order','').replace('name=Sorted [COLOR=FF00FF00]by user-assigned order[/COLOR]','').replace('name=Live Tv Channels Twothumb','')
        match=re.compile('<title>([^<]+)</title.+?link>(.+?)</link.+?thumbnail>([^<]+)</thumbnail>',re.DOTALL).findall(link)
        for name,url,thumb in sorted(match):
            main.addPlayL(name,url,204,thumb,'','','','','',secName='By Country',secIcon=art+'/countrysec.png')

        main.VIEWSB()
def COUNTRIESLink(mname,url,thumb):
        ok = True
        if '.f4m'in url:
                from resources.universal import F4mProxy
                player=F4mProxy.f4mProxyHelper()
                proxy=None
                use_proxy_for_chunks=False
                player.playF4mLink(url, mname, proxy, use_proxy_for_chunks,'',thumb)
                if selfAddon.getSetting("whistory") == "true":
                    from resources.universal import watchhistory
                    wh = watchhistory.WatchHistory('plugin.video.movie25')
                    wh.add_item(mname+' '+'[COLOR green]My Country[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
        else:
                if '</regex>'in url:
                        url=main.doRegex(url)
                stream_url = url     
                playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                playlist.clear()
                listitem = xbmcgui.ListItem(thumbnailImage=thumb)
                infoL={'Title': mname, 'Genre': 'Live'} 
                from resources.universal import playbackengine
                player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='movie', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams='',imdb_id='')

                #WatchHistory
                if selfAddon.getSetting("whistory") == "true":
                    from resources.universal import watchhistory
                    wh = watchhistory.WatchHistory('plugin.video.movie25')
                    wh.add_item(mname+' '+'[COLOR green]My Country[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
        return ok
