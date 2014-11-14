import urllib,re,sys,os
import xbmc,xbmcgui,xbmcaddon,xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art 

def LISTSP(murl):
        #urllist=main.OPENURL('http://oneclickwatch.org/category/movies/')+main.OPENURL('http://oneclickwatch.org/category/movies/page/2/')+main.OPENURL('http://oneclickwatch.org/category/movies/page/3/')+main.OPENURL('http://oneclickwatch.org/category/movies/page/4/')+main.OPENURL('http://oneclickwatch.org/category/movies/page/5/')+main.OPENURL('http://oneclickwatch.org/category/movies/page/6/')+main.OPENURL('http://oneclickwatch.org/category/movies/page/7/')+main.OPENURL('http://oneclickwatch.org/category/movies/page/8/')+main.OPENURL('http://oneclickwatch.org/category/movies/page/9/')+main.OPENURL('http://oneclickwatch.org/category/movies/page/10/')
        urllist=main.batchOPENURL(('http://oneclickwatch.org/category/movies/','http://oneclickwatch.org/category/movies/page/2/','http://oneclickwatch.org/category/movies/page/3/','http://oneclickwatch.org/category/movies/page/4/','http://oneclickwatch.org/category/movies/page/5/','http://oneclickwatch.org/category/movies/page/6/','http://oneclickwatch.org/category/movies/page/7/','http://oneclickwatch.org/category/movies/page/8/','http://oneclickwatch.org/category/movies/page/9/','http://oneclickwatch.org/category/movies/page/10/'))
        if urllist:
                urllist=main.unescapes(urllist)
                match=re.compile('title=".+?">([^<]+)</a></h2>.+?href=".+?<a href="(.+?)" .+?href=".+?>.+?src="(.+?)"').findall(urllist)
                dialogWait = xbmcgui.DialogProgress()
                ret = dialogWait.create('Please wait until Movie list is cached.')
                totalLinks = len(match)
                loadedLinks = 0
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
                for name,url,thumb in match:
                        name=name.replace('<strong>','').replace('</strong>','')
                        main.addPlayM(name,url,135,thumb,'','','','','')
                        loadedLinks = loadedLinks + 1
                        percent = (loadedLinks * 100)/totalLinks
                        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                        if (dialogWait.iscanceled()):
                                return False   
        dialogWait.close()
        del dialogWait
        main.CloseAllDialogs()        
        main.GA("HD","Oneclickwatch")





def LISTTV3(murl):
        #urllist=main.OPENURL('http://oneclickwatch.org/category/tv-shows/')+main.OPENURL('http://oneclickwatch.org/category/tv-shows/page/2/')+main.OPENURL('http://oneclickwatch.org/category/tv-shows/page/3/')+main.OPENURL('http://oneclickwatch.org/category/tv-shows/page/4/')+main.OPENURL('http://oneclickwatch.org/category/tv-shows/page/5/')
        urllist=main.batchOPENURL(('http://oneclickwatch.org/category/tv-shows/','http://oneclickwatch.org/category/tv-shows/page/2/','http://oneclickwatch.org/category/tv-shows/page/3/','http://oneclickwatch.org/category/tv-shows/page/4/','http://oneclickwatch.org/category/tv-shows/page/5/'))
        if urllist:
                urllist=main.unescapes(urllist)
                match=re.compile('title=".+?">([^<]+)</a></h2>.+?href=".+?<a href="(.+?)" .+?href=".+?>.+?src="(.+?)"').findall(urllist)
                dialogWait = xbmcgui.DialogProgress()
                ret = dialogWait.create('Please wait until Show list is cached.')
                totalLinks = len(match)
                loadedLinks = 0
                remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
                for name,url,thumb in match:
                        name=name.replace('\xc2\xa0','').replace('" ','').replace(' "','').replace('"','').replace("&#039;","'").replace("&amp;","and").replace("&#8217;","'").replace("amp;","and").replace("#8211;","-")
                        main.addPlayTE(name,url,134,thumb,'','','','','')
                        loadedLinks = loadedLinks + 1
                        percent = (loadedLinks * 100)/totalLinks
                        remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                        if (dialogWait.iscanceled()):
                            return False   
        dialogWait.close()
        del dialogWait
        main.GA("TV","Oneclickwatch")




def PLAYOCW(mname,murl):
        sources=[]
        main.GA("OneclickwatchT","Watched")
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Collecting Hosts,5000)")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        
        match=re.compile('<a href="([^"]+?)" rel="nofollow">([^>]+?)</a>').findall(link)
        if len(match)==0:                
            match=re.compile('<a href="(.+?)">(.+?)</a><br />').findall(link)
        desc=re.compile('<.+? />Plot:(.+?)<.+? />').findall(link)
        if len(desc)>0:
                descs=desc[0]
        else:
                descs=''
        thumb=re.compile('<img alt="" src="(.+?)"').findall(link)
        if len(thumb)>0:
                thumbs=thumb[0]
        else:
               thumbs=''
        main.CloseAllDialogs()
        import urlresolver          
        for url,host in match:
                host=re.compile("http://(.+?).com/.+?").findall(url)
                for hname in host:
                        host=hname.replace('www.','')
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)

                        
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Show doesn't have playable links,5000)")
        else:
                source = urlresolver.choose_source(sources)
        try:
                if source:
                        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                        stream_url = main.resolve_url(source.get_url())
                else:
                        stream_url = False
                        return
                infoLabels =main.GETMETAEpiT(mname,thumbs,descs)
                video_type='episode'
                season=infoLabels['season']
                episode=infoLabels['episode']
                img=infoLabels['cover_url']
                fanart =infoLabels['backdrop_url']
                imdb_id=infoLabels['imdb_id']
                infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }
                infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre']}
                from resources.universal import playbackengine
                player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=str(infoLabels['title']),season=str(season), episode=str(episode), year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
                #WatchHistory
                if selfAddon.getSetting("whistory") == "true":
                    from resources.universal import watchhistory
                    wh = watchhistory.WatchHistory('plugin.video.movie25')
                    wh.add_item(mname+' '+'[COLOR green]Oneclickwatch[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=img, fanart='', is_folder=False)
                player.KeepAlive()
                return ok
        except Exception, e:
                if stream_url != False:
                        main.ErrorReport(e)
                return ok
        

def VIDEOLINKST3(mname,murl):
        sources=[]
        main.GA("OneclickwatchM","Watched")
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Collecting Hosts,5000)")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<a href="([^"]+?)" rel="nofollow">([^>]+?)</a>').findall(link)
        if len(match)==0:                
            match=re.compile('<a href="(.+?)">(.+?)</a><br />').findall(link)
        desc=re.compile('<.+? />Plot:(.+?)<.+? />').findall(link)
        if len(desc)>0:
                descs=desc[0]
        else:
                descs=''
        thumb=re.compile('<img alt="" src="(.+?)"').findall(link)
        if len(thumb)>0:
                thumbs=thumb[0]
        else:
               thumbs=''
        main.CloseAllDialogs()
        import urlresolver          
        for url,host in match:
                host=re.compile("http://(.+?).com/.+?").findall(url)
                for hname in host:
                        host=hname.replace('www.','')
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Show doesn't have playable links,5000)")
        else:
                source = urlresolver.choose_source(sources)
        try:
                if source:
                        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                        stream_url = main.resolve_url(source.get_url())
                else:   
                        stream_url = False
                        return
                print stream_url
                infoLabels =main.GETMETAT(mname,'','',thumbs)
                video_type='movie'
                season=''
                episode=''
                img=infoLabels['cover_url']
                fanart =infoLabels['backdrop_url']
                imdb_id=infoLabels['imdb_id']
                infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }

                infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre']}
                # play with bookmark
                from resources.universal import playbackengine
                player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=str(infoLabels['title']),season=str(season), episode=str(episode), year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
                #WatchHistory
                if selfAddon.getSetting("whistory") == "true":
                    from resources.universal import watchhistory
                    wh = watchhistory.WatchHistory('plugin.video.movie25')
                    wh.add_item(mname+' '+'[COLOR green]Oneclickwatch[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=img, fanart='', is_folder=False)
                player.KeepAlive()
                return ok
        except Exception, e:
                if stream_url != False:
                        main.ErrorReport(e)
                return ok
