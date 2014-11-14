import urllib,urllib2,re,cookielib,urlresolver,sys,os
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

def LISTDOC(murl):
    if murl=='doc1':
        main.GA("Documantary","DhHome")
        #main.addDir('[COLOR red]Search[/COLOR]','search',89,'')
        main.addDir('[COLOR red]Popular[/COLOR]','http://documentaryheaven.com/popular/',89,'')
        main.addDir('[COLOR red]Recent[/COLOR]','http://documentaryheaven.com/all/',87,'')
        url='http://documentaryheaven.com/'
        link=main.OPENURL(url)
        match=re.compile('<li class=".+?"><a href="(.+?)" title=".+?">(.+?)</a> </li>').findall(link)
        for url, name in match:
            main.addDir(name,'http://documentaryheaven.com'+url,87,'')
    elif murl=='doc2':
        main.GA("Documantary","TDFHome")
        main.addDir('[COLOR red]Recent[/COLOR]','http://topdocumentaryfilms.com/all/',87,'')
        main.addDir('[COLOR red]Recommended[/COLOR]','rec',89,'')
        url='http://topdocumentaryfilms.com/'
        link=main.OPENURL(url)
        match=re.compile('href="(.+?)" title=".+?">(.+?)</a>.+?</li>').findall(link)
        for url, name in match:
            main.addDir(name,url,87,'')
    elif murl=='doc3':
        main.GA("Documantary","DLHome")
        main.addDir('[COLOR red]Latest[/COLOR]','http://www.documentary-log.com/',87,'')
        main.addDir("[COLOR red]Editor's Picks[/COLOR]",'http://www.documentary-log.com/category/editors-picks/',87,'')
        url='http://www.documentary-log.com/'
        link=main.OPENURL(url)
        match=re.compile('<li class="cat-item cat-item-.+?"><a href="(.+?)" title="(.+?)">(.+?)</a> ([^<]+)').findall(link)
        for url, desc, name, leng in match:
            main.addDirc(name+'  '+leng,url,87,'',desc,'','','','')

def LISTDOC2(murl):
    
    match=re.compile('documentaryheaven').findall(murl)
    if (len(match)>0):
        main.GA("DhHome","Dh-List")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match= re.compile('href="([^<]+)" rel="bookmark" title=".+?" rel=".+?"><img class=".+?" src="(.+?)" alt="([^<]+)"/></a></div><div class=".+?">(.+?)</div>').findall(link)
        if (len(match)==0):
            match=re.compile('href="(.+?)" title="" rel=".+?"><img class=".+?" src="(.+?)" alt="(.+?)".+?</a>\n                            </div>     \n                            <div id="postDis">\n                            \t(.+?)[...]').findall(link)
        for url,thumb,name,desc in match:
            main.addPlayMs(name,url,88,thumb,desc,'','','','')
        paginate=re.compile('<a href="([^<]+)" >Next &rarr;</a>').findall(link)
        if (len(paginate)>0):
            main.addDir('[COLOR blue]Next Page[/COLOR]',paginate[0],87,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
    

    match2=re.compile('topdocumentaryfilms').findall(murl)
    if (len(match2)>0):
        i=0
        main.GA("TDFHome","TDF-List")
        link=main.OPENURL(murl)
        link=link.replace('\n','')
        url=re.compile('href="([^<]+)">Watch now').findall(link)
        match=re.compile('href=".+?".+?src="(.+?)".+?alt="(.+?)"').findall(link)
        desc=re.compile('>([^<]+)</p><p><strong>').findall(link)
        for thumb,name in match:
            main.addPlayMs(name,url[i],88,thumb,desc[i],'','','','')
            i=i+1
        paginate=re.compile('</a>.+?href="([^<]+)">Next</a></div>').findall(link)
        if (len(paginate)>0):
            for purl in paginate:
                main.addDir('[COLOR blue]Next[/COLOR]',purl,87,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))

    match3=re.compile('documentary-log').findall(murl)
    if (len(match3)>0):
        main.GA("DLHome","DL-List")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class="clear">.+?<a href="(.+?)" title=".+?">          <img src="(.+?)" alt="(.+?)" class=".+?" />          </a>          <p>(.+?)<a').findall(link)
        for url,thumb,name,desc in match:
            main.addPlayMs(name,url,88,thumb,desc,'','','','')
        paginate=re.compile("<a href='([^<]+)' class='nextpostslink'>").findall(link)
        if (len(paginate)>0):
            for purl in paginate:
                main.addDir('[COLOR blue]Next[/COLOR]',purl,87,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))

                  
def LISTDOCPOP(murl):
    if murl=='search':
        keyb = xbmc.Keyboard('', 'Search Documentaries')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
                surl='http://documentaryheaven.com/find/?q='+encode
                link=main.OPENURL(surl)
        match=re.compile('<a href="(.+?)" title="" rel=".+?"><img class=".+?" src="(.+?)" alt="(.+?)".+?</a>\n                            </div>     \n                            <div id="postDis">\n                            \t(.+?)[...]').findall(link)
        if (len(match)==0):
            match=re.compile('href="(.+?)" title="" rel=".+?"><img class=".+?" src="(.+?)" alt="(.+?)".+?</a>\n                            </div>     \n                            <div id="postDis">\n                            \t(.+?)[...]').findall(link)
        for url,thumb,name,desc in match:
            main.addPlayMs(name,url,88,thumb,desc,'','','','')

        paginate=re.compile("<span class=\'page current\'>1</span></li><li><a href=\'http://documentaryheaven.com/page/2/.?s=.+?\'").findall(link)
        if (len(paginate)>0):
            main.addDir('[COLOR blue]Page 2[/COLOR]','http://documentaryheaven.com/page/2/?s='+encode,9,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
    elif murl=='rec':
        rurl='http://topdocumentaryfilms.com/'
        link=main.OPENURL(rurl)
        match=re.compile('href="([^<]+)">([^<]+)</a></li><li><a').findall(link)
        for url,name in match:
            main.addPlayMs(name,url,88,'','','','','','')
    else:
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<a href=\'(.+?)/\'><img src=\'(.+?)\'/></a></div><div class=".+?"><div class=".+?"><a href=\'.+?/\'>(.+?)</a></div><div class=".+?"><p>(.+?)</div>').findall(link)
        for url,thumb,name,desc in match:
            main.addPlayMs(name,url,88,thumb,desc,'','','','')


def LINKDOC(mname,murl,thumb):
    ok=True
    match=re.compile('documentaryheaven').findall(murl)
    if (len(match)>0):
        main.GA("DocumentaryHeaven","Watched")
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        link=main.OPENURL(murl)
        match=re.compile('<iframe frameborder=".+?" width=".+?" height=".+?" src="http:(.+?)">').findall(link)
        if (len(match)==0):
            match=re.compile('<iframe width=".+?" height=".+?" src="http:(.+?)" frameborder=".+?" allowfullscreen>').findall(link)
            if (len(match)==0):
                match=re.compile('<embe.+?src="http:([^<]+)".+?></embed>').findall(link)
            
        for url in match:
            url='http:'+url
            match4=re.compile('vimeo').findall(url)
            if (len(match4)>0):
                url=url.replace('?title=0&amp;byline=0&amp;portrait=0','')
                url=url.replace('http://player.vimeo.com/video','http://vimeo.com')
            match5=re.compile('dailymotion').findall(url)
            if (len(match5)>0):
                url=url.replace('http://www.dailymotion.com/embed/video','http://www.dailymotion.com/video')
            match8=re.compile('youtube').findall(url)
            if (len(match8)>0):
                    match2=re.compile('http://www.youtube.com/embed/([^<]+)').findall(url)
                    url='http://www.youtube.com/watch?v='+match2[0]
        if (len(match)==0):
            match=re.compile('<iframe src="http:(.+?)" width=".+?" height=".+?" frameborder=".+?".+?</iframe>').findall(link)
            for url in match:
                url='http:'+url
                match4=re.compile('vimeo').findall(url)
                match6=re.compile('putlocker').findall(url)
                if (len(match4)>0):
                    url=url.replace('?title=0&amp;byline=0&amp;portrait=0','')
                    url=url.replace('http://player.vimeo.com/video','http://vimeo.com')
                
                elif (len(match6)>0):
                    url=url
                else:
                    match2=re.compile('http://www.youtube.com/embed/([^<]+)').findall(url)
                    if (len(match2)==0):
                        match2=re.compile('http://www.youtube.com/p/([^<]+).?hl=.+?').findall(link)
                    url='http://www.youtube.com/watch?v='+match2[0]
        
        listitem = xbmcgui.ListItem(mname)
        try:
            xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
            stream_url = main.resolve_url(str(url))
            if(stream_url == False):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                return
        
            # play with bookmark
            player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels='', watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
            #WatchHistory
            if selfAddon.getSetting("whistory") == "true":
                wh.add_item(mname+' '+'[COLOR green]Doc-Heaven[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
            player.KeepAlive()
            return ok
        except:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Not Playable,5000)")
            return ok

    match2=re.compile('topdocumentaryfilms').findall(murl)
    if (len(match2)>0):
        sources=[]
        main.GA("TopDocumentaryFilms","Watched")
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        link=main.OPENURL(murl)
        ok=True
        link=link.replace('src="http://cdn.tdfimg.com/wp-content/uploads','')
        match=re.compile('src="(.+?)"').findall(link)
        for url in match:
            match4=re.compile('vimeo').findall(url)
            if (len(match4)>0):
                url=url.replace('?title=0&amp;byline=0&amp;portrait=0','')
                url=url.replace('http://player.vimeo.com/video','http://vimeo.com')
            match5=re.compile('dailymotion').findall(url)
            if (len(match5)>0):
                url=url.replace('http://www.dailymotion.com/embed/video','http://www.dailymotion.com/video')
            match7=re.compile('google').findall(url)
            if (len(match7)>0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,link down,3000)")
                return
            match6=re.compile('youtube').findall(url)
            if (len(match6)>0):
                match=re.compile('http://www.youtube.com/embed/n_(.+?).?rel=0&amp;iv_load_policy=3').findall(url)
                if (len(match)>0):
                    url='http://www.youtube.com/watch?feature=player_embedded&v=n_'+match[0]
                else:
                    match=re.compile('http://www.youtube.com/embed/(.+?).?rel=0&amp;iv_load_policy=3').findall(url)
                    if (len(match)>0):
                        url='http://www.youtube.com/watch?feature=player_embedded&v='+match[0]
                    match2=re.compile('videoseries').findall(url)
                    if (len(match2)>0):
                        link2=main.OPENURL(url)
                        match2=re.compile('href="/watch.?v=(.+?)"').findall(link2)
                        match3=re.compile("http://www.youtube.com/embed/videoseries.?list=(.+?)&.+?load_policy=.+?").findall(url)
                        print match3[0]
                        try:
                            url='http://www.youtube.com/watch?v='+match2[0]
                        except:
                                namelist=[]
                                urllist=[]
                                link=main.OPENURL('https://gdata.youtube.com/feeds/api/playlists/'+match3[0]+'?start-index=1&max-results=50')
                                match=re.compile("href='https://m.youtube.com/details.?v=(.+?)'/.+?<media\:descriptio[^>]+>([^<]+)</media\:description>.+?<media\:thumbnail url='([^']+)'.+?<media:title type='plain'>(.+?)/media:title>").findall(link)
                                for url,desc,thumb,name in match:
                                    name=name.replace('<','')
                                    namelist.append(name)
                                    urllist.append(url)
                                dialog = xbmcgui.Dialog()
                                answer =dialog.select("Playlist", namelist)
                                url='http://www.youtube.com/watch?v='+urllist[int(answer)]

                    else:
                        url=url.replace('?rel=0','')
        
        try:
            xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
            stream_url = main.resolve_url(str(url))
            if(stream_url == False):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                return
        
            # play with bookmark
            player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels='', watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
            #WatchHistory
            if selfAddon.getSetting("whistory") == "true":
                wh.add_item(mname+' '+'[COLOR green]Top-Doc[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
            player.KeepAlive()
            return ok
        except:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Not Playable,5000)")
            return ok

    match3=re.compile('documentary-log.com').findall(murl)
    if (len(match3)>0):        

        main.GA("Documentary-Log","Watched")
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        link=main.OPENURL(murl)
        link=link.replace('src="http://cdn.tdfimg.com/wp-content/uploads','')
        match=re.compile('src="(.+?)" .+?></iframe>').findall(link)
        if (len(match)==0):
            link=link.replace('src="http://www.documentary-log.com/wp-cont','')
            match=re.compile('src="(.+?)" .+?/>').findall(link)
        for url in match:
            match4=re.compile('vimeo').findall(url)
            if (len(match4)>0):
                url=url.replace('?title=0&amp;byline=0&amp;portrait=0','')
                url=url.replace('http://player.vimeo.com/video','http://vimeo.com')
            match5=re.compile('dailymotion').findall(url)
            if (len(match5)>0):
                url=url.replace('http://www.dailymotion.com/embed/video','http://www.dailymotion.com/video')
            match7=re.compile('google').findall(url)
            if (len(match7)>0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,link down,3000)")
                return
            match6=re.compile('youtube').findall(url)
            if (len(match6)>0):
                match=re.compile('http://www.youtube.com/embed/n_(.+?).?rel=0&amp;iv_load_policy=3').findall(url)
                if (len(match)>0):
                    url='http://www.youtube.com/watch?feature=player_embedded&v=n_'+match[0]
                else:
                    match=re.compile('http://www.youtube.com/embed/(.+?).?rel=0&amp;iv_load_policy=3').findall(url)
                    if (len(match)>0):
                        url='http://www.youtube.com/watch?feature=player_embedded&v='+match[0]
                    match2=re.compile('videoseries').findall(url)
                    if (len(match2)>0):
                        link2=main.OPENURL(url)
                        match2=re.compile('href="/watch.?v=(.+?)"').findall(link2)
                        match3=re.compile("http://www.youtube.com/embed/videoseries.?list=(.+?)&amp;iv_load_policy=3").findall(url)
                        print match3
                        url='http://www.youtube.com/watch?v='+match2[0]
                               
                    else:
                        url=url.replace('?rel=0','')
        
        print "vlink " +str(url)
        try:
            xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
            stream_url = main.resolve_url(str(url))
            if(stream_url == False):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                return
        
            # play with bookmark
            player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels='', watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
            #WatchHistory
            if selfAddon.getSetting("whistory") == "true":
                wh.add_item(mname+' '+'[COLOR green]Doc-Log[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
            player.KeepAlive()
            return ok
        except Exception, e:
            if stream_url != False:
                    main.ErrorReport(e)
            else:
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Not Playable,5000)")
            return ok

