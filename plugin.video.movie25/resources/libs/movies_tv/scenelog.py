import urllib,re,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
filename = main.getFileName(__file__)
prettyName = 'SceneLog'
    
def ListSceneLogItems(murl,quality='all'):
    if murl.startswith('Movies'):
        main.addDir('Search SceneLog','Movies',659,art+'/search.png')
        subpages = 5
        category = "movies"
    elif murl.startswith('TV'):
        main.addDir('Search SceneLog','TV',659,art+'/search.png')
        subpages = 5
        category = "tv-shows"
    parts = murl.split('-', 1 );
    max = subpages
    try:
        pages = parts[1].split(',', 1 );
        page = int(pages[0])
        max = int(pages[1])
        murl = parts[0]
    except:
        page = 0
    page = page * subpages;
    html = ''
    urls = []
    for n in range(subpages):
        if page + n + 1 > max: break
        urls.append('http://scnlog.eu/'+category+'/page/'+str(page+n+1)+'/')
    cached_path = os.path.join(os.path.join(main.datapath,'Temp'), filename + '_' + murl+"-"+str(page)+'.cache')
    cached = main.getFile(cached_path)
    if cached:
        xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")          
        html = cached
    else:
        html = main.batchOPENURL(urls)
        main.setFile(cached_path,html)
    hasNextPage = re.compile('<strong>&raquo;</strong>').findall(html)
    if len(hasNextPage) < subpages:
        page = None
    hasMax = re.compile('page/(\d+)/">Last &raquo;').findall(html)
    if hasMax:
        max = hasMax[0]
    if html:
        ShowSceneLogItems(html,murl,quality)
        if not page is None:
            main.addDir('Page ' + str(page/subpages+1) + ', Next Page >>>',murl + "-" + str(page/subpages+1) + "," + max,657,art+'/next2.png')
    main.GA("Movies-TV","SceneLog")
    main.VIEWS()
    
def ShowSceneLogItems(html,category,quality):
    html = main.unescapes(html)
    match = re.compile('<h1>.*?href="(.+?)".*?title="(.+?)"').findall(html)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Episodes list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Episodes Cached :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
    if match:
        for url,title in match:
            title = title.replace("."," ").replace("_"," ")
            episode = re.search('(\d+)x(\d\d+)',title, re.I)
            if(episode):
                e = str(episode.group(2))
                s = str(episode.group(1))
                if len(s)==1: s = "0" + s
                episode = "S" + s + "E" + e
                title = re.sub('(\d+)x(\d\d+)',episode,title,re.I)
            else:
                title = re.sub('(\d{4}) (\d{2}) (\d{2})','\\1.\\2.\\3',title,re.I)
            isHD = re.compile('720p|1080p').findall(title)
            q = re.search('(?i)(720p|1080p|HDTV|PDTV|WEB DL|DVDRIP|WS DSR|DSR|BDRip|WEBRiP)',title,re.I)
            title = re.sub('(?i)(720p|1080p|HDTV|PDTV|WEB DL|DVDRIP|WS DSR|DSR|BDRip|WEBRiP|x264|lol ?-).*','',title).strip("- ")
            title = re.sub('(\d{4}\.\d{2}\.\d{2})(.*)','\\1[COLOR blue]\\2[/COLOR]',title,re.I)
            title = re.sub('(S\d+E\d+.*?) (.*)','\\1 [COLOR blue]\\2[/COLOR]',title,re.I)
            if q: title += " [COLOR red]"+q.group(1)+"[/COLOR]"
            else: title += " [COLOR red]SD[/COLOR]"
            if (isHD or quality != 'HD'):
                if category=='TV':
                    main.addDirTE(title,url,656,'','','','','','')
                else:
                    main.addDirM(title,url,656,'','','','','','')
                    xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
            loadedLinks = loadedLinks + 1
            percent = (loadedLinks * 100)/totalLinks
            remaining_display = 'Episodes Cached :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
            dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
            if (dialogWait.iscanceled()):
                return False
    dialogWait.close()
    del dialogWait
    
def StartSceneLogSearch(searchCategory):
    seapath=os.path.join(main.datapath,'Search')
    if searchCategory == 'TV':
        searchHistoryFile = "SearchHistoryTv"
    else:
        searchCategory = "Movies"
        searchHistoryFile = "SearchHistory25"
    SearchFile=os.path.join(seapath,searchHistoryFile)
    if not os.path.exists(SearchFile):
        SearchSceneLog('Search',searchCategory)
    else:
        main.addDir('Search',searchCategory,660,art+'/search.png')
        main.addDir('Clear History',SearchFile,128,art+'/cleahis.png')
        thumb=art+'/link.png'
        searchis=re.compile('search="(.+?)",').findall(open(SearchFile,'r').read())
        for seahis in reversed(searchis):
            seahis=seahis.replace('%20',' ')
            main.addDir(seahis,searchCategory,660,thumb)

def superSearch(searchQuery,searchCategory):
    try:
        returnList=[]
        if searchCategory.startswith('TV'):
            cat = 5
        else:
            searchCategory = "Movies"
            cat = 4
        try:
            params = searchCategory.split('#@#', 2 );
            searchCategory = params[0]
            page = int(params[1])
            searchQuery = params[2]
        except: page = 1
        if not searchQuery: return False
        searchUrl='http://scnlog.eu/page/'+str(page)+'/?s='+searchQuery+'&cat='+str(cat)
        html = main.OPENURL(searchUrl,verbose=False)
        html = main.unescapes(html)
        match = re.compile('<h1>.*?href="(.+?)".*?title="(.+?)"').findall(html)
        for url,title in match:
            title = title.replace("."," ").replace("_"," ")
            episode = re.search('(\d+)x(\d\d+)',title, re.I)
            if(episode):
                e = str(episode.group(2))
                s = str(episode.group(1))
                if len(s)==1: s = "0" + s
                episode = "S" + s + "E" + e
                title = re.sub('(\d+)x(\d\d+)',episode,title,re.I)
            else:
                title = re.sub('(\d{4}) (\d{2}) (\d{2})','\\1.\\2.\\3',title,re.I)
            isHD = re.compile('720p|1080p').findall(title)
            q = re.search('(?i)(720p|1080p|HDTV|PDTV|WEB DL|DVDRIP|WS DSR|DSR|BDRip|WEBRiP)',title,re.I)
            title = re.sub('(?i)(720p|1080p|HDTV|PDTV|WEB DL|DVDRIP|WS DSR|DSR|BDRip|WEBRiP|x264|lol ?-).*','',title).strip("- ")
            title = re.sub('(\d{4}\.\d{2}\.\d{2})(.*)','\\1[COLOR blue]\\2[/COLOR]',title,re.I)
            title = re.sub('(S\d+E\d+.*?) (.*)','\\1 [COLOR blue]\\2[/COLOR]',title,re.I)
            if q: title += " [COLOR red]"+q.group(1)+"[/COLOR]"
            else: title += " [COLOR red]SD[/COLOR]"
            returnList.append((title,prettyName,url,'',656,True))
        return returnList
    except: return []

def SearchSceneLog(searchQuery,searchCategory):
    if searchCategory.startswith('TV'):
        cat = 5
    else:
        searchCategory = "Movies"
        cat = 4
    try:
        params = searchCategory.split('#@#', 2 );
        searchCategory = params[0]
        page = int(params[1])
        searchQuery = params[2]
    except: page = 1
    searchQuery = main.updateSearchFile(searchQuery,searchCategory,'Search')
    if not searchQuery: return False
    searchUrl='http://scnlog.eu/page/'+str(page)+'/?s='+searchQuery+'&cat='+str(cat)
    html = main.OPENURL(searchUrl)
    if html:
        hasNextPage = re.compile('<strong>&raquo;</strong>').findall(html)
        ShowSceneLogItems(html,searchCategory,'all')
        if hasNextPage:
            main.addDir('Page ' + str(page) + ', Next Page >>>',searchCategory + "#@#" + str(page+1) + '#@#' + searchQuery,660,art+'/next2.png')
    else:
        xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False)
        xbmc.executebuiltin("XBMC.Notification(Sorry,Could not connect to SceneLog,3000)") 
    main.GA("SceneLog","Search")
                    
def ListSceneLogLinks(mname,url):
    html = main.OPENURL(url)
    html = main.unescapes(html)
    if selfAddon.getSetting("hide-download-instructions") != "true":
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
    paragraphs = re.compile('<p>.*?</p>',re.I|re.DOTALL).findall(html)
    itemsAdded = 0
    from urlparse import urlparse
    for paragraph in paragraphs:
        links = re.compile('<a[\s]*?href="(.*?)"',re.I|re.DOTALL).findall(paragraph)
        if len(links) == 1: # if more than 1 links per paragraph, its probably splitted file
            for url in links:
                if not re.search('rar',url,re.I):
                    host = urlparse(url).hostname.replace('www.','').partition('.')[0]
                    if main.supportedHost(host):
                        title = mname
                        quality = re.search('(?i)(720p|1080p|HDTV|PDTV|WEB DL|DVDRIP|WS DSR|DSR|BDRip|WEBRiP)',url,re.I)
                        if quality and not quality.group(1).lower() in mname.lower() :
                            title = re.sub('\[COLOR.*?\[/COLOR\]','',title).strip()
                            title += ' [COLOR red]'+quality.group(1).upper()+'[/COLOR]'
                        host = re.sub('^(https?://)?[^/]*?([^/^.]+?)\.\w+?/.*','\\2',url).upper()
                        thumb = host.lower()
                        main.addDown2(title+' [COLOR blue]'+host+'[/COLOR]',url,658,art+'/hosts/'+thumb+".png",art+'/hosts/'+thumb+".png")
                        itemsAdded += 1
    if not itemsAdded:
        xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False)
        xbmc.executebuiltin("XBMC.Notification(Sorry,No sources found!,3000)")
#     if itemsAdded == 1:
#         xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False)
#         PlaySceneLogLink(mname+' [COLOR blue]'+host+'[/COLOR]',murl)

def PlaySceneLogLink(mname,murl):
    main.GA("SceneLog","Watched") 
    ok=True
    r = re.findall('s(\d+)e(\d\d+)',mname,re.I)
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
        stream_url = main.resolve_url(murl)
        infoLabels['title'] = main.removeColoredText(infoLabels['title'])
        infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre']}
        if not video_type is 'episode': infoL['originalTitle']=main.removeColoredText(infoLabels['metaName']) 
        # play with bookmark
        from resources.universal import playbackengine
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=infoLabels['title'],season=season, episode=episode, year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            from resources.universal import watchhistory
            wh = watchhistory.WatchHistory(addon_id)
            wh.add_item(mname+' '+'[COLOR green]SceneLog[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=infoLabels['cover_url'], fanart=infoLabels['backdrop_url'], is_folder=False)
        main.CloseAllDialogs()
        player.KeepAlive()
        return ok
    except Exception, e:
        if stream_url != False:
                main.ErrorReport(e)
        return ok
