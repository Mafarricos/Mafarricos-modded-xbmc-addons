import urllib,re,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
pattern = '(?sim)<a [^>]*?href="([^"]+?)" rel="bookmark"[^>]*?>\s*?<img src="([^"]+?)"[^>]*?title="([^"]+?)"'
prettyName = 'MyNewVideoLinks'
    
def LISTSP2(murl):
    if murl.startswith('3D'):
        main.addDir('Search Newmyvideolinks','movieNEW',102,art+'/search.png')
        subpages = 2
        max = 9
        category = "3-d-movies"
    elif murl.startswith('TV'):
        main.addDir('Search Newmyvideolinks','tvNEW',102,art+'/search.png')
        subpages = 3
        max = 50
        category = "tv-shows"
    else:
         main.addDir('Search Newmyvideolinks','movieNEW',102,art+'/search.png')
         subpages = 5
         max = 250
         category = "bluray"
    parts = murl.split('-', 1 );
    try:
        pages = parts[1].split(',', 1 );
        page = int(pages[0])
        max = int(pages[1])
        murl = parts[0]
    except:
        page = 0
    page = page * subpages;
    urllist = ''
    urls = []
    for n in range(subpages):
        if page + n + 1 > max: break
        if category == "tv-shows":
            urls.append('http://tv.myvideolinks.eu/page/'+str(page+n+1))
        else:
            urls.append('http://www.myvideolinks.me/category/movies/'+category+'/page/'+str(page+n+1))
    urllist = main.batchOPENURL(urls)
    hasNextPage = re.compile('>&rsaquo;</a>').findall(urllist)
    if category != "3-d-movies" and len(hasNextPage) < subpages or category == "3-d-movies" and subpages * page > max:
        page = None
    else:
        hasMax = re.compile("page/(\d+?)/'>&raquo;</a>").findall(urllist)
        if hasMax:
            max = hasMax[0]
    if urllist:
        urllist=main.unescapes(urllist)
        #link=main.OPENURL(xurl)
        match=re.compile(pattern).findall(urllist)
#         if not match:
#             match=re.compile('<h3><a href="()([^"]+?)"[^>]+?title="([^"]+?)"').findall(urllist)
        if match:
            dialogWait = xbmcgui.DialogProgress()
            ret = dialogWait.create('Please wait until Movie list is cached.')
            totalLinks = len(match)
            loadedLinks = 0
            remaining_display = 'Movies/Episodes Cached :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
            dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
            for url,thumb,title in match:
                if murl=='TV':
#                     if re.compile('720p').findall(title):
                        title=main.CleanTitle(title)
                        main.addDirTE(title,url,35,thumb,'','','','','')
                else:
                    title=main.CleanTitle(title)
                    main.addDirM(title,url,35,thumb,'','','','','')
                    xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies/Episodes Cached :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if dialogWait.iscanceled(): break
            if not page is None and loadedLinks >= totalLinks:
                main.addDir('Page ' + str(page/subpages+1) + ' [COLOR blue]Next Page >>>[/COLOR]',murl + "-" + str(page/subpages+1) + "," + str(max),34,art+'/next2.png')
            dialogWait.close()
            del dialogWait
    main.GA("HD-3D-HDTV","Newmyvideolinks")
    main.VIEWS()

def SearchhistoryNEW(murl):
    if murl == 'tvNEW':
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryTv')
        if not os.path.exists(SeaFile):
            url='tvNEW'
            SEARCHNEW('',url)
        else:
            main.addDir('Search','tvNEW',101,art+'/search.png')
            main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
            thumb=art+'/link.png'
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                url='tNEW'
                seahis=seahis.replace('%20',' ')
                main.addDir(seahis,url,101,thumb)
    elif murl == 'movieNEW':
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistory25')
        if not os.path.exists(SeaFile):
            url='movieNEW'
            SEARCHNEW('',url)
        else:
            main.addDir('Search','movieNEW',101,art+'/search.png')
            main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
            thumb=art+'/link.png'
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                url='mNEW'
                seahis=seahis.replace('%20',' ')
                main.addDir(seahis,url,101,thumb)

def superSearch(encode,type):
    try:
        returnList=[]
        encode = urllib.unquote(encode).replace(' ','+')
        if type=='Movies':
            surl='http://myvideolinks.me/?s='+encode
        else:
            surl='http://tv.myvideolinks.eu/?s='+encode
        link=main.OPENURL(surl,verbose=False,mobile=True)
        link=main.unescapes(link)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile(pattern).findall(link)
        for url,thumb,name in match:
            name=main.CleanTitle(name)
            if type=='TV' or type=='Movies' and not re.findall('HDTV',name):
                returnList.append((name,prettyName,url,thumb,35,True))
        return returnList
    except: return []       

def SEARCHNEW(mname,murl):
    if murl == 'movieNEW':
        encode = main.updateSearchFile(mname,'Movies','Search')
        if not encode: return False
        surl='http://myvideolinks.me/?s='+encode
        link=main.OPENURL(surl)
        link=main.unescapes(link)
        match=re.compile(pattern).findall(link)
        if match:
            for url,thumb,name in match:
                name=main.CleanTitle(name)
                if not re.findall('HDTV',name):
                    main.addDirM(name,url,35,thumb,'','','','','')
    elif murl == 'tvNEW':
        encode = main.updateSearchFile(mname,'TV','Search')
        if not encode: return False
        surl='http://tv.myvideolinks.eu/?s='+encode
        link=main.OPENURL(surl)
        link=main.unescapes(link)
        match=re.compile(pattern).findall(link)
        if match:
            for url,thumb,name in match:
                name=main.CleanTitle(name)
                main.addDirTE(name,url,35,thumb,'','','','','')
    else:
        if murl == 'tNEW':
            encode = mname.replace(' ','+')
            surl='http://tv.myvideolinks.eu/?s='+encode
            link=main.OPENURL(surl)
            link=main.unescapes(link)
            match=re.compile(pattern).findall(link)
            if match:
                for url,thumb,name in match:
                    name=main.CleanTitle(name)
                    main.addDirTE(name,url,35,thumb,'','','','','')

        elif murl == 'mNEW':
            encode = mname.replace(' ','+')
            surl='http://myvideolinks.me/?s='+encode
            link=main.OPENURL(surl)
            link=main.unescapes(link)
            match=re.compile(pattern).findall(link)
            if match:
                for url,thumb,name in match:
                    name=main.CleanTitle(name)
                    if not re.findall('HDTV',name):
                        main.addDirM(name,url,35,thumb,'','','','','')
    main.GA("Newmyvideolinks","Search")
    
def LINKSP2(mname,url):
    link=main.OPENURL(url)
    link=main.unescapes(link)
    if selfAddon.getSetting("hide-download-instructions") != "true":
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
    
    match0=re.compile('title="[^"]+?">([^"]+?)</a>.+?</p><ul>(.+?)</ul>').findall(link)
    if not match0:
        match0=re.compile('<h4>(.+?)</h4>(.+?)</ul>').findall(link)
        if not match0:
            match0=re.compile('<p><img src=".+?" alt="([^"]+?)" /></p>.+?<ul>(.+?)</ul>').findall(link)
    for mname, links in reversed(match0):
        match1=re.compile('<li><a href="([^"]+?)"[^>]*?><img [^>]*?alt="([^"]+?)"[^>]*?></a></li>').findall(links)
        match= match1 + re.compile('<li><a href="([^"]+?)"[^>]*?>([^>]+?)</a></li>').findall(links)
        filename = False
        for murl, name in match:
            fn = re.search('/([^/]+?\.(mkv|avi|mp4))(\.html)?$',murl)
            if fn:
                filename = fn.group(1)
                break
        for murl, name in match:
            name = name[0].upper() + name[1:]
            if main.supportedHost(name):
                thumb=name.lower()
#                 if re.search('billionuploads',murl) and filename: murl += '#@#' + filename
                main.addDown2(main.CleanTitle(mname)+' [COLOR blue]'+name+'[/COLOR]',murl,209,art+'/hosts/'+thumb+".png",art+'/hosts/'+thumb+".png")

def LINKSP2B(mname,murl):
    main.GA("Newmyvideolinks","Watched") 
    ok=True
    r = re.findall('(.+?)\ss(\d+)e(\d+)\s',mname,re.I)
    if r:
        infoLabels =main.GETMETAEpiT(mname,'','')
        video_type='episode'
        season=infoLabels['season']
        episode=infoLabels['episode']
    else:
        infoLabels =main.GETMETAT(mname,'','','')
        video_type='movie'
        season=''
        episode=''
    img=infoLabels['cover_url']
    fanart =infoLabels['backdrop_url']
    imdb_id=infoLabels['imdb_id']
    infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }
    playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    playlist.clear()
    try :
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
        parts = murl.partition('#@#')
        murl = parts[0]
        filename = parts[-1]
        stream_url = main.resolve_url(murl,filename)
        infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre'], 'originaltitle': infoLabels['metaName']}
        if not video_type is 'episode': infoL['originalTitle']=main.removeColoredText(infoLabels['metaName']) 
        # play with bookmark
        from resources.universal import playbackengine
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=infoLabels['title'],season=season, episode=episode, year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            from resources.universal import watchhistory
            wh = watchhistory.WatchHistory(addon_id)
            wh.add_item(mname+' '+'[COLOR green]NewmyVideoLink[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=infoLabels['cover_url'], fanart=infoLabels['backdrop_url'], is_folder=False)
        player.KeepAlive()
        return ok
    except Exception, e:
        if stream_url != False:
                main.ErrorReport(e)
        return ok
            
def UFCNEW():
    try: 
        urllist=['http://www.myvideolinks.eu/index.php?s=ufc']
    except:
        urllist=['http://www.myvideolinks.eu/index.php?s=ufc']
    for surl in urllist:
        link=main.OPENURL(surl)
        link=main.unescapes(link)
        match=re.compile("""<a href=".+?" rel=".+?" title=".+?"> <img src="(.+?)" width=".+?" height=".+?" title="(.+?)" class=".+?"></a><h4><a href="(.+?)" rel""").findall(link)
        if len(match)>0:
            for thumb,name,url in match:
                match=re.compile('UFC').findall(name)
                if len(match)>0:
                    main.addDir(name,url,35,thumb)
    main.GA("Newmyvideolinks","UFC")
