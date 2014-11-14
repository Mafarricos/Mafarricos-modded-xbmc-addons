import urllib,urllib2,re,cookielib,urlresolver,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
from resources.universal import playbackengine, watchhistory
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art

wh = watchhistory.WatchHistory('plugin.video.movie25')

def WATCHDOC():
        main.GA("Documantary","WatchDocumentary")
        main.addDir('Search','watchdoc',164,art+'/search.png')
        main.addDir('Categories','watchdoc',162,art+'/watchdoc.png')
        main.addDir('New Documentaries','new',160,art+'/watchdoc.png')
        main.addDir('Top Documentaries of Last 14 days','top',160,art+'/watchdoc.png')
        main.addDir('Top Documentaries of All times','top2',160,art+'/watchdoc.png')
        
def CATEGORIES():
        main.GA("WatchDocumentary","Categories")
        main.addDir('9/11 & London Bombing','http://watchdocumentary.org/browse-911-and-london-bombing-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Adventure','http://watchdocumentary.org/browse-adventure-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Arts & Artists','http://watchdocumentary.org/browse-arts-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Assassination','http://watchdocumentary.org/browse-assassination-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Biography','http://watchdocumentary.org/browse-biography-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Comedy','http://watchdocumentary.org/browse-comedy-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Conspiracy','http://watchdocumentary.org/browse-conspiracy-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Crime','http://watchdocumentary.org/browse-crime-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Drugs','http://watchdocumentary.org/browse-drugs-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Environment','http://watchdocumentary.org/browse-environment-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Globalization','http://watchdocumentary.org/browse-globalization-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Health','http://watchdocumentary.org/browse-health-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('History','http://watchdocumentary.org/browse-history-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Human Rights','http://watchdocumentary.org/browse-human-rights-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Massacre','http://watchdocumentary.org/browse-massacre-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Media','http://watchdocumentary.org/browse-media-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Military','http://watchdocumentary.org/browse-military-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Money & Business','http://watchdocumentary.org/browse-money-business-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Music','http://watchdocumentary.org/browse-music-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Mystery','http://watchdocumentary.org/browse-mystery-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Nature','http://watchdocumentary.org/browse-nature-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Philosophy','http://watchdocumentary.org/browse-philosophy-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Politics','http://watchdocumentary.org/browse-politics-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Psychology','http://watchdocumentary.org/browse-psychology-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Religious','http://watchdocumentary.org/browse-religious-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Science','http://watchdocumentary.org/browse-science-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Sexuality','http://watchdocumentary.org/browse-sexuality-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Society','http://watchdocumentary.org/browse-society-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Sports','http://watchdocumentary.org/browse-sports-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Technology','http://watchdocumentary.org/browse-technology-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('Travel','http://watchdocumentary.org/browse-travel-documentaries-1-date.html',163,art+'/folder.png')
        main.addDir('War','http://watchdocumentary.org/browse-war-documentaries-1-date.html',163,art+'/folder.png')

def WATCHDOCSearch():
        keyb = xbmc.Keyboard('', 'Search Documentaries')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
                surl='http://watchdocumentary.org/search.php?keywords='+encode+'&btn='
                link=main.OPENURL(surl)
                link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                match=re.compile('<a href="([^<]+)" title="([^<]+)"><img src="([^<]+)"  alt=').findall(link)
                for url,name,thumb in match:
                    main.addPlayMs(name,url,161,thumb,'','','','','')
        paginate=re.compile('<a href="([^<]+)">next &raquo;</a>').findall(link)
        if (len(paginate)>0):
            for purl in paginate:
                main.addDir('[COLOR blue]Next[/COLOR]','http://watchdocumentary.org/'+purl,163,art+'/next2.png')

def WATCHDOCList(murl):
        main.GA("WatchDocumentary","List")
        if murl =='top':
            link=main.OPENURL('http://watchdocumentary.org/top_documentaries/')
            link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
            match=re.compile('<td align=.+?><a href=".+?"><img src="([^<]+)" alt=".+?" class=".+?" width=".+?" height=".+?" align=".+?" border=".+?" /></a></td><td class=".+?"><a href="(.+?)">(.+?)</a></td><td class=".+?">.+?</td><td class=".+?">(.+?)</td>').findall(link)
            for thumb,url,name,views in match:
                main.addPlayMs(name+'   [COLOR red]Views: '+views+'[/COLOR]',url,161,thumb,'','','','','')
        elif murl =='new':
            link=main.OPENURL('http://watchdocumentary.org/new_documentaries/')
            link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
            match=re.compile('<td align=.+?><a href=".+?"><img src="([^<]+)" alt=".+?" class=".+?" width=".+?" height=".+?" align=".+?" border=".+?" /></a></td><td class=".+?"><a href="(.+?)">(.+?)</a></td><td class=".+?">.+?</td><td class=".+?">.+?</td>').findall(link)
            for thumb,url,name in match:
                main.addPlayMs(name,url,161,thumb,'','','','','')
        if murl =='top2':
            link=main.OPENURL('http://watchdocumentary.org/top_documentaries/alltime')
            link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
            match=re.compile('<td align=.+?><a href=".+?"><img src="([^<]+)" alt=".+?" class=".+?" width=".+?" height=".+?" align=".+?" border=".+?" /></a></td><td class=".+?"><a href="(.+?)">(.+?)</a></td><td class=".+?">.+?</td><td class=".+?">(.+?)</td>').findall(link)
            for thumb,url,name,views in match:
                main.addPlayMs(name+'   [COLOR red]Views: '+views+'[/COLOR]',url,161,thumb,'','','','','')
                
def WATCHDOCList2(murl):
        main.GA("WatchDocumentary","List")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<a href="([^<]+)" title="([^<]+)"><img src="([^<]+)"  alt=').findall(link)
        for url,name,thumb in match:
            main.addPlayMs(name,url,161,thumb,'','','','','')
        paginate=re.compile('<a href="([^<]+)">next &raquo;</a>').findall(link)
        if (len(paginate)>0):
            for purl in paginate:
                main.addDir('[COLOR blue]Next[/COLOR]','http://watchdocumentary.org/'+purl,163,art+'/next2.png')

def WATCHDOCLink(mname,murl,thumb):
        main.GA("WatchDocumentary","Watched")
        ok=True
        infoL={'Title': mname, 'Genre': 'Watch Documentary'}
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Opening Link,3000)")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('{skin: \'.+?.zip\',file: \'(.+?)\',').findall(link)
        if len(match)>0:
            for url in match:
                Type=re.compile('youtube').findall(url)
                if len(Type)>0:
                    url=url.replace('https','http')
                    xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                    stream_url = main.resolve_url(str(url))
                    if(stream_url == False):
                        xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")                    
                        return
                    # play with bookmark
                    player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
                    #WatchHistory
                    if selfAddon.getSetting("whistory") == "true":
                            wh.add_item(mname+' '+'[COLOR green]Watch-Doc[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
                    player.KeepAlive()
                    return ok
                Type2=re.compile('watchdocumentary.org').findall(url)
                if len(Type2)>0:
                    stream_url=main.REDIRECT(url)
                    # play with bookmark
                    player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
                    #WatchHistory
                    if selfAddon.getSetting("whistory") == "true":
                            wh.add_item(mname+' '+'[COLOR green]Watch-Doc[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
                    player.KeepAlive()
                    return ok
        match2=re.compile('<iframe frameborder=".+?" width=".+?" height=".+?" src="(.+?)"></iframe>').findall(link)
        if len(match2)>0:
                for url in match2:
                    url=url.replace('http://www.dailymotion.com/embed/video','http://www.dailymotion.com/video')
                    print "gg "+url
                    source = urlresolver.HostedMediaFile(str(url))
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                stream_url = main.resolve_url(source.get_url())
                if(stream_url == False):
                    xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                    return
                                                        
                # play with bookmark
                player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
                #WatchHistory
                if selfAddon.getSetting("whistory") == "true":
                        wh.add_item(mname+' '+'[COLOR green]Watch-Doc[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
                player.KeepAlive()
                return ok
        match3=re.compile('src="http://clips.team-andro.com/nuevo3/embedplayer/green/nvplayer.swf.?config=(.+?)"').findall(link)
        if len(match3)>0:
                for url in match3:
                    link=main.OPENURL(url)
                    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                vlink=re.compile('<file>(.+?)</file>').findall(link)
                link2=main.OPENURL(vlink[0])
                link2=link2.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                stream_url=re.compile('<filehd>(.+?)</filehd>').findall(link2)
                # play with bookmark
                player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
                #WatchHistory
                if selfAddon.getSetting("whistory") == "true":
                        wh.add_item(mname+' '+'[COLOR green]Watch-Doc[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
                player.KeepAlive()
                return ok
        match4=re.compile('<iframe src=.+?"(.+?).?title=').findall(link)
        if len(match4)>0:
                for url in match4:
                    url=url.replace('http://player.vimeo.com/video','http://vimeo.com')
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                stream_url = main.resolve_url(str(url))
                if(stream_url == False):
                    xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                    return 
                # play with bookmark
                player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
                #WatchHistory
                if selfAddon.getSetting("whistory") == "true":
                        wh.add_item(mname+' '+'[COLOR green]Watch-Doc[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
                player.KeepAlive()
                return ok
        match5=re.compile('{skin: \'.+?.zip\',playlistfile: \'(.+?)\',').findall(link)
        if len(match5)>0:
            namelist=[]
            urllist=[]
            link=main.OPENURL(match5[0])
            match=re.compile("http\://www.youtube.com/watch\?v\=([^\&]+)\&.+?<media\:descriptio[^>]+>([^<]+)</media\:description>.+?<media\:thumbnail url='([^']+)'.+?<media:title type='plain'>(.+?)/media:title>").findall(link)
            for url,desc,thumb,name in match:
                name=name.replace('<','')
                namelist.append(name)
                urllist.append(url)
            dialog = xbmcgui.Dialog()
            answer =dialog.select("Playlist", namelist)
            stream_url = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+urllist[int(answer)]+"&hd=1"
            # play with bookmark
            player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
            #WatchHistory
            if selfAddon.getSetting("whistory") == "true":
                wh.add_item(mname+' '+'[COLOR green]Watch-Doc[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
            player.KeepAlive()
            return ok
        else:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link deleted Or unplayable,5000)")
