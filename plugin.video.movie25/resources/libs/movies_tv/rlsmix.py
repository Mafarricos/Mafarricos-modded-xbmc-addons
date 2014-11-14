# -*- coding: utf-8 -*-
import urllib,re,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
smalllogo=art+'/smallicon.png'
filename = main.getFileName(__file__)
prettyName = 'Rlsmix'

user = selfAddon.getSetting('rlsusername')
passw = selfAddon.getSetting('rlspassword')
filters = ''
if selfAddon.getSetting('ddtv_pdtv') == 'true': filters += 'pdtv,'
if selfAddon.getSetting('ddtv_dsr') == 'true': filters += 'dsr,'
if selfAddon.getSetting('ddtv_hdtv480p') == 'true': filters += 'hdtv,'
if selfAddon.getSetting('ddtv_hdtv720p') == 'true': filters += 'realhd,'
if selfAddon.getSetting('ddtv_dvdrip') == 'true': filters += 'dvdrip,'
if selfAddon.getSetting('ddtv_webdl720p') == 'true': filters += 'webdl,'
if selfAddon.getSetting('ddtv_webdl1080p') == 'true': filters += 'webdl1080p,'
filters = filters.strip(',')
if user == '' or passw == '':
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=FF67cc33]MashUp[/COLOR]", "Please set your Rlsmix credentials", "in Addon settings under logins tab.", "For credentials register @ http://directdownload.tv/.")
    selfAddon.openSettings()
    user = selfAddon.getSetting('rlsusername')
    passw = selfAddon.getSetting('rlspassword')

def ListDirectDownloadTVItems(startpage):
    subpages = 3
    main.addDir('Search Rlsmix','rlsmix',136,art+'/search.png')
    mytag = '#my'
    if re.search(mytag +'$',startpage):
        startpage = startpage.replace(mytag,'')
        myshows = '/myshows/true'
    else: 
        mytag = ''
        myshows = ''
    if 'TV' in startpage:
        startpage = 0
    try: page = int(startpage)
    except: page = 0
    urls = []
    for n in range(subpages):
        urls.append('http://directdownload.tv/index/search/keyword//qualities/'+filters+'/from/'+str(page)+myshows+'/search')
        page += 20
    cached_path = os.path.join(os.path.join(main.datapath,'Temp'), filename + '_' + str(startpage)+mytag+'.cache')
    cached = main.getFile(cached_path)
    count = 0
    if cached:
        count = ShowDirectDownloadTVItems('',cached)
    else: 
        setCookie()
        html = getBatchUrl(urls)
        count = ShowDirectDownloadTVItems(html,cached_path=cached_path)
        if not count and myshows:
            xbmcplugin.endOfDirectory(int(sys.argv[1]),False,False)
            xbmc.executebuiltin("XBMC.Notification(You are not following any shows!,Add shows on directdownload.tv,5000,"+smalllogo+")")
    strpage = str((int(startpage))/(20*subpages)+1)
    if count == subpages * 20:
        main.addDir('Page ' + strpage + ' [COLOR blue]Next Page >>>[/COLOR]',str(page)+mytag,61,art+'/next2.png')
    main.GA("TV","DirectDownloadTV")
         
def setCookie():
    from t0mm0.common.net import Net as net
    cookie_file = os.path.join(os.path.join(main.datapath,'Cookies'), 'directdownload.cookies')
    cookieExpired = False
    if os.path.exists(cookie_file):
        try:
            cookie = open(cookie_file).read()
            expire = re.search('expires="(.*?)"',cookie, re.I)
            if expire:
                expire = str(expire.group(1))
                import time
                if time.time() > time.mktime(time.strptime(expire, '%Y-%m-%d %H:%M:%SZ')):
                   cookieExpired = True
        except: cookieExpired = True 
    if not os.path.exists(cookie_file) or cookieExpired:
        log_in = net().http_POST('http://directdownload.tv',{'username':user,'password':passw,'Login':'Login'}).content
        if "alert('Invalid login or password.')" in log_in:
                xbmcplugin.endOfDirectory(int(sys.argv[1]),False,False)
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Username or Password Incorrect,10000,"+smalllogo+")")
                return
        net().save_cookies(cookie_file)
    else:
        net().set_cookies(cookie_file)
        
def getUrl(url, q = False):
    from t0mm0.common.net import Net as net
    content = net().http_GET(url).content
    if q: q.put(content)
    return content

def getBatchUrl(urls):
    import threading
    try:
        import Queue as queue
    except ImportError:
        import queue
    max = len(urls)
    results = []
    for url in urls: 
        q = queue.Queue()
        threading.Thread(target=getUrl, args=(url,q)).start()
        results.append(q)
    content = ''
    for n in range(max):
        content += results[n].get()
    return content

def processTitle(title,quality):
    title = title.replace("."," ").replace("_"," ")
    episode = re.search('(\d+)[xX](\d\d+)',title)
    if(episode):
        e = str(episode.group(2))
        s = str(episode.group(1))
        if len(s)==1: s = "0" + s
        episode = "S" + s + "E" + e
        title = re.sub('(\d+)[xX](\d\d+)',episode,title)
    else:
        title = re.sub('(\d{4}) (\d{2}) (\d{2})','\\1.\\2.\\3',title)
        
    isHD = re.compile('(?i)720p?|1080p?').findall(title)
    if isHD:
        title = title.split(isHD[0])[0].strip("- ")
    else:
        title = re.sub('(?i)(HDTV|PDTV|WEB DL|DVDRIP|WS DSR|DSR|BDRip|WEBRiP|x264|lol ?-).*','',title).strip("- ")
    if 'webdl' in quality and isHD: isHD[0] += " WEB-DL"
    if 'dvdrip' in quality and not isHD: isHD = [("DVDRip")]
    title = re.sub('(\d{4}\.\d{2}\.\d{2})(.*)','\\1[COLOR blue]\\2[/COLOR]',title)
    title = re.sub('([sS]\d+[eE]\d+).?([eE]\d+)','\\1.\\2',title)
    title = re.sub('([sS]\d+[eE]\d+.*?) (.*)','\\1 [COLOR blue]\\2[/COLOR]',title)
    if not isHD: isHD = [("SD")]
    if isHD:
        title += " [COLOR red]"+isHD[0].strip()+"[/COLOR]"
    return title

def ShowDirectDownloadTVItems(html, cached=False, cached_path=False):
    html=main.unescapes(html)
    if cached: 
        match = eval(cached)
    else:
        match=re.compile('{"release":"([^"]+?)","when":.+?,"size":".+?","links":(.+?),"idtvs".+?"quality":"([^"]+?)".+?}').findall(html)
        if cached_path and match:
            main.setFile(cached_path,str(match))
    totalLinks = len(match)
    if totalLinks:
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Show list is cached.')
        loadedLinks = 0
        remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")
        for title,url,quality in match:
            title = processTitle(title,quality)
            url=url.replace('\/','/')
            if isArchive(url): title = '[B][Archived][/B] ' + title
            main.addDirTE(title,url,62,'','','','','','')
            loadedLinks += 1
            percent = (loadedLinks * 100)/totalLinks
            remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
            dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
            if dialogWait.iscanceled(): return loadedLinks
        dialogWait.close()
        del dialogWait
    return totalLinks

def isArchive(url):
    match2=re.compile('{"url":"[^"]+?","hostname":"([^"]+?)"}').findall(url)
    prev = '_'
    hostlist = ''
    for host in match2:
        if (host == prev and not host in hostlist ):
            url = re.sub('\{[^\}]+?"'+host+'"\},?','',url)
            hostlist += host
        prev = host
    return (url == '[]')

def ListDirectDownloadTVLinks(mname,url):
    ok=True
    if selfAddon.getSetting("hide-download-instructions") != "true":
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
    match=re.compile('{"url":"([^"]+?)","hostname":"([^"]+?)"}').findall(url)
    prev = ''
    archived = ''
    for url,host in match:
        if (host == prev and not host in archived ):
            archived += host
        prev = host
    h = 0
    for url,host in match:
        thumb=host.lower()
        urlExceptions = re.compile('rar').findall(url)
        if not (urlExceptions or host in archived) and main.supportedHost(host):
            h += 1
            main.addDown2(mname+' [COLOR blue]'+host.upper()+'[/COLOR]',url,210,art+"/hosts/"+thumb+".png",art+"/hosts/"+thumb+".png")     
    if not h:
        xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False)
        xbmc.executebuiltin("XBMC.Notification(Sorry,No Playable Links Found,2000)")
        
def StartDirectDownloadTVSearch():
    searchpath=os.path.join(main.datapath,'Search')
    SearchFile=os.path.join(searchpath,'SearchHistoryTv')
    if not os.path.exists(SearchFile):
        SearchDirectDownloadTV()
    else:
        main.addDir('Search','###',137,art+'/search.png')
        main.addDir('Clear History',SearchFile,128,art+'/cleahis.png')
        thumb=art+'/link.png'
        searchitems=re.compile('search="(.+?)",').findall(open(SearchFile,'r').read())
        for searchitem in reversed(searchitems):
            searchitem=searchitem.replace('%20',' ')
            main.addDir(searchitem,searchitem,137,thumb)

def superSearch(searchQuery,type):
    try:
        returnList=[]
        setCookie()
        try:
            params = searchQuery.split('#@#', 1 )
            page = int(params[1])
            searchQuery = params[0]
        except: page = 0
        searchQuery = main.updateSearchFile(searchQuery,'TV')
        if not searchQuery: return False   
        searchUrl='http://directdownload.tv/index/search/keyword/'+searchQuery+'/qualities/pdtv,dsr,hdtv,realhd,dvdrip,webdl,webdl1080p/from/'+str(page)+'/search'
        from t0mm0.common.net import Net as net
        html = net().http_GET(searchUrl).content
        match=re.compile('{"release":"([^"]+?)","when":.+?,"size":".+?","links":(.+?),"idtvs".+?"quality":"([^"]+?)".+?}').findall(html)
        for title,url,quality in match:
            name = processTitle(title,quality)
            if isArchive(url): name = '[B][Archived][/B] ' + name
            url=url.replace('\/','/')
            if '[Archived]' not in name:
                returnList.append((name,prettyName,url,'',62,True))
        return returnList
    except: return []
            
def SearchDirectDownloadTV(searchQuery = ''):
    setCookie()
    try:
        params = searchQuery.split('#@#', 1 )
        page = int(params[1])
        searchQuery = params[0]
    except: page = 0
    searchQuery = main.updateSearchFile(searchQuery,'TV')
    if not searchQuery: return False   
    searchUrl='http://directdownload.tv/index/search/keyword/'+searchQuery+'/qualities/pdtv,dsr,hdtv,realhd,dvdrip,webdl,webdl1080p/from/'+str(page)+'/search'
    from t0mm0.common.net import Net as net
    html = net().http_GET(searchUrl).content
    if html:
        totalLinks = ShowDirectDownloadTVItems(html)
        if not totalLinks:
            xbmc.executebuiltin("XBMC.Notification(DirectDownloadTV,No Results Found,3000)") 
            return False
        if page == 0: strpage = "1"
        else: strpage = str(page/20+1)
        page += 20
        if not totalLinks % 20:
            main.addDir('Page ' + strpage + ' [COLOR blue]Next Page >>>[/COLOR]',searchQuery + '#@#' + str(page),137,art+'/next2.png')
    else:
        xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False)
        xbmc.executebuiltin("XBMC.Notification(Sorry,Could not connect to DirectDownloadTV,3000)") 
    main.GA("DirectDownloadTV","Search")

def PlayDirectDownloadTVLink(mname,murl):
    main.GA("DirectDownloadTV","Watched")
    ok=True
    infoLabels =main.GETMETAEpiT(mname,'','')
    video_type='episode'
    season=infoLabels['season']
    episode=infoLabels['episode']
    img=infoLabels['cover_url']
    fanart =infoLabels['backdrop_url']
    imdb_id=infoLabels['imdb_id']
    infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }
    try:
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
        stream_url = main.resolve_url(murl)
        
        infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre'], 'originaltitle': infoLabels['metaName']}
        # play with bookmark
        from resources.universal import playbackengine
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=infoLabels['title'],season=str(season), episode=(episode), year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
        if stream_url: main.CloseAllDialogs()
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            from resources.universal import  watchhistory
            wh = watchhistory.WatchHistory('plugin.video.movie25')
            wh.add_item(mname+' '+'[COLOR green]Rlsmix[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=img, fanart=fanart, is_folder=False)
        player.KeepAlive()
        return ok
    except Exception, e:
        if stream_url != False:
                main.ErrorReport(e)
        return ok
