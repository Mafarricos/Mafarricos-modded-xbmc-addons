import urllib,urllib2,re,cookielib,urlresolver,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
from resources.universal import playbackengine, watchhistory
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
art = main.art
wh = watchhistory.WatchHistory(addon_id)

def LISTMOO():
        link=main.OPENURL('http://www.mooviemaniac.net/movies.htm')
        match=re.compile('<a href="http:(.+?)" target=".+?src="(.+?)" alt="(.+?)" title=',re.DOTALL).findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for url,thumb,name in reversed(match):
                main.addPlayM(name,'http:'+url,306,'http://www.mooviemaniac.net/'+thumb,'','','','','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        main.GA("INT","Mooviemaniac")

def LINKMOO(mname,murl,thumb):
        main.GA("Mooviemaniac","Watched")
        ok=True
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Opening Link,5000)")
        infoLabels =main.GETMETAT(mname,'','','')
        video_type='movie'
        season=''
        episode=''
        img=infoLabels['cover_url']
        fanart =infoLabels['backdrop_url']
        imdb_id=infoLabels['imdb_id']
        infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }
        try:
            stream_url = main.resolve_url(murl)
            if stream_url == False:
                  return                                                            
            infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre'], 'originaltitle': infoLabels['metaName']}
            # play with bookmark
            stream_url=stream_url.replace(' ','%20')
            from resources.universal import playbackengine
            player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=str(infoLabels['title']),season=str(season), episode=str(episode), year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
            #WatchHistory
            if selfAddon.getSetting("whistory") == "true":
                from resources.universal import  watchhistory
                wh = watchhistory.WatchHistory('plugin.video.movie25')
                wh.add_item(mname+' '+'[COLOR green]"Mooviemaniac"[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=img, fanart=fanart, is_folder=False)
            player.KeepAlive()
            return ok
        except Exception, e:
                if stream_url != False:
                        main.ErrorReport(e)
                return ok
