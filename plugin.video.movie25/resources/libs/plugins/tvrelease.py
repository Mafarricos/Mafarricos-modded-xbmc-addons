import urllib, urllib2,re,string,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main
from t0mm0.common.addon import Addon

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
    
art = main.art
error_logo = art+'/bigx.png'

BASEURL = 'http://www.tv-release.net/'
prettyName = 'TVRelease'

def MAINMENU():
    main.addDir('Search Tv-Release',    BASEURL+'?seacher=',           1006,art+'/tvrsearch1.png')
    main.addDir('TV 480',               BASEURL+'?cat=TV-480p',        1001,art+'/TV480.png')
    main.addDir('TV 720',               BASEURL+'?cat=TV-720p',        1001,art+'/TV720.png')
    main.addDir('TV MP4',               BASEURL+'?cat=TV-Mp4',         1001,art+'/TVmp4.png')
    main.addDir('TV Xvid',              BASEURL+'?cat=TV-XviD',        1001,art+'/TVxvid.png')
    #main.addDir('TV Packs',             BASEURL+'category/tvshows/tvpack/',       1007,art+'/TVpacks.png')
    main.addDir('TV Foreign',           BASEURL+'?cat=TV-Foreign',     1001,art+'/TVforeign.png')
    main.addDir('Movies 480',           BASEURL+'?cat=Movies-480p',    1001,art+'/Movies480.png')
    main.addDir('Movies 720',           BASEURL+'?cat=Movies-720p',    1001,art+'/Movies720.png')
    main.addDir('Movies Xvid',          BASEURL+'?cat=Movies-XviD',    1001,art+'/Moviesxvid.png')
    main.addDir('Movies Foreign',       BASEURL+'?cat=Movies-Foreign', 1001,art+'/Moviesforeign.png')
    main.addSpecial('Resolver Settings',BASEURL,                                1004,art+'/tvrresolver.png')
    main.VIEWSB()

def INDEX(url):
    types = []
    SearchType = None
    if '!' in url:
        r = url.rpartition('!')
        print r
        url = r[0]
        SearchType = r[2]
    else:
        url = url
    if 'cat=TV' in url:
        types = 'tv'
    elif 'cat=Movies' in url:
        types = 'movie'
    html = GETHTML(url)
    if html == None:
        return
    pattern = '<tr><td[^>]*?><a [^>]*?>([^<]*?)</a></td><td[^>]*?><a href=\'([^\']*?)\'[^>]*?>([^<]*?)<'
    r = re.findall(pattern, html, re.I|re.M|re.DOTALL)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until list is cached.')
    totalLinks = len(r)
    loadedLinks = 0
    remaining_display = 'Media loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
    for tag, url, name in r:
        if re.search('(?i)WEB-DL',name): tag = tag.strip() + " WEB-DL"
        if re.findall('\d{4}p', name):
            r = re.findall('(.+?)\s(\d+p)', name)
            for name, quality in r:
                tag = tag.replace('720p',quality)
                pass
        if re.findall('\ss\d+e\d+\s', name, re.I|re.DOTALL):
            r = re.findall('(.+?)\ss(\d+)e(\d+)\s', name, re.I)
            for name, season, episode in r:
                name = name+' S'+season+'E'+episode
        elif re.findall('\s\d{4}\s\d{2}\s\d{2}\s', name):
            r = re.findall('(.+?)\s(\d{4})\s(\d{2})\s(\d{2})\s',name)
            for name, year, month, day in r:
                name = name+' '+year+' '+month+' '+day
        elif re.findall('\shdtv\sx', name, re.I):
            r = re.findall('(.+?)\shdtv\sx',name, re.I)
            for name in r:
                pass
        name = re.sub('\s\s+',' ',name).strip()
        name = name+' [COLOR red]'+re.sub('(?sim)^(TV-|Movies-)(.*)','\\2',tag)+'[/COLOR]'
        if SearchType == None:
            if 'TV' in tag:
                main.addDirTE(main.CleanTitle(name),url,1003,'','','','','','')
            elif 'Movies' in tag:
                if re.findall('\s\d+\s',name):
                    r = name.rpartition('\s\d{4}\s')
                main.addDirM(main.CleanTitle(name),url,1003,'','','','','','')
        elif SearchType == 'tv' and 'TV' in tag:
            main.addDirTE(main.CleanTitle(name),url,1003,'','','','','','')
        elif SearchType == 'movie' and 'Movies' in tag:
            r = name.rpartition('\s\d{4}\s')
            main.addDirM(main.CleanTitle(name),url,1003,'','','','','','')
        
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Media loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if dialogWait.iscanceled(): break
    dialogWait.close()
    del dialogWait
    if "<div class='zmg_pn'" in html and loadedLinks >= totalLinks:
        r = re.findall("""<span class='zmg_pn_current'>(\d+?)</span>[^<]*?<span class='zmg_pn_standar'><a href="([^"]+?)">""", html, re.I|re.DOTALL|re.M)
        total = re.findall('">(\d+)</a></span>', html)
        if total: total = total[-1]
        else: total = "1"
        for current, url in r:
            name = 'Page '+current+' of '+total+' [COLOR green]Next Page >>>[/COLOR]'
            main.addDir('[COLOR green]Go to Page[/COLOR]', url+':'+total, 1002, art+'/gotopagetr.png')
            main.addDir(name, url.replace('%5C',''), 1001, art+'/nextpage.png')
    main.VIEWS()

def LISTHOSTERS(name,url):
    html = GETHTML(url)
    if html == None: return
    if selfAddon.getSetting("hide-download-instructions") != "true":
            main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
    r = re.findall(r'class="td_cols"><a target=\'_blank\'.+?href=\'(.+?)\'>',html, re.M|re.DOTALL)
    try:
        t = re.findall(r'rel="nofollow">((?!.*\.rar).*)</a>', html, re.I)
        r = r+t
    except: pass
    if len(r) == 0:
        addon.show_ok_dialog(['No Playable Streams Found,','It Might Be That They Are Still Being Uploaded,',
                              'Or They Are Unstreamable Archive Files'],'MashUP: TV-Release')
        xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False)
        return
    from urlparse import urlparse
    for url in r:
        url = url.replace("180upload.nl","180upload.com")
        host = urlparse(url).hostname.replace('www.','').partition('.')[0]
        if main.supportedHost(host):
            main.addDown2(name.strip()+" [COLOR blue]"+host.upper()+"[/COLOR]",url,1005,art+'/hosts/'+host+'.png',art+'/hosts/'+host+'.png')
            
def superSearch(encode,type):
    try:
        if type == 'Movies': cat = 'Movies-XviD,Movies-720p,Movies-480p,Movies-Foreign,Movies-DVDR,'
        else: cat = 'TV-XviD,TV-Mp4,TV-720p,TV-480p,TV-Foreign,'
        surl ='http://tv-release.net/?s='+encode+'&cat='+cat
        returnList=[]
        link=main.OPENURL(surl,verbose=False)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        pattern = '<tr><td[^>]*?><a [^>]*?>([^<]*?)</a></td><td[^>]*?><a href=\'([^\']*?)\'[^>]*?>([^<]*?)<'
        r = re.findall(pattern, link, re.I|re.M|re.DOTALL)
        for tag, url, name in r:
            if re.search('(?i)WEB-DL',name): tag = tag.strip() + " WEB-DL"
            if re.findall('\d+p\s', name):
                r = re.findall('(.+?)\s(\d+p)\s', name)
                for name, quality in r:
                    tag = tag.replace('720p',quality)
                    pass
            if re.findall('\ss\d+e\d+\s', name, re.I|re.DOTALL):
                r = re.findall('(.+?)\ss(\d+)e(\d+)\s', name, re.I)
                for name, season, episode in r:
                    name = name+' S'+season+'E'+episode
            elif re.findall('\s\d{4}\s\d{2}\s\d{2}\s', name):
                r = re.findall('(.+?)\s(\d{4})\s(\d{2})\s(\d{2})\s',name)
                for name, year, month, day in r:
                    name = name+' '+year+' '+month+' '+day
            elif re.findall('\shdtv\sx', name, re.I):
                r = re.findall('(.+?)\shdtv\sx',name, re.I)
                for name in r:
                    pass
            name = name+' [COLOR red]'+re.sub('(?sim)^(TV-|Movies-)(.*)','\\2',tag)+'[/COLOR]'
            returnList.append((main.CleanTitle(name),prettyName,url,'',1003,True))
        return returnList
    except: return []

def SEARCHhistory():
    dialog = xbmcgui.Dialog()
    ret = dialog.select('[B]Choose A Search Type[/B]',['[B]TV Shows[/B]','[B]Movies[/B]'])
    if ret == -1:
        xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False)
    if ret == 0:
        searchType = 'tv'
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryTv')
        if not os.path.exists(SeaFile):
            SEARCH(searchType)
        else:
            main.addDir('Search',searchType,1008,art+'/search.png')
            main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
            thumb=art+'/link.png'
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                    url=seahis
                    seahis=seahis.replace('%20',' ')
                    url = 'http://tv-release.net/?s='+url+'&cat=TV-XviD,TV-Mp4,TV-720p,TV-480p,TV-Foreign,'
                    main.addDir(seahis,url,1001,thumb)
    if ret == 1:
        searchType = 'movie'
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistory25')
        if not os.path.exists(SeaFile):
            SEARCH(searchType)
        else:
            main.addDir('Search',searchType,1008,art+'/search.png')
            main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
            thumb=art+'/link.png'
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                    url=seahis
                    seahis=seahis.replace('%20',' ')
                    url = 'http://tv-release.net/?s='+url+'&cat=Movies-XviD,Movies-720p,Movies-480p,Movies-Foreign,Movies-DVDR,'
                    main.addDir(seahis,url,1001,thumb)

def SEARCH(murl):
    if murl == 'tv':
        encode = main.updateSearchFile(murl,'TV',defaultValue=murl,searchMsg='Search For Shows or Episodes')
        if not encode: return False   
        url = 'http://tv-release.net/?s='+encode+'&cat=TV-XviD,TV-Mp4,TV-720p,TV-480p,TV-Foreign,'
        INDEX(url)
    elif murl=='movie':
        encode = main.updateSearchFile(murl,'Movies',defaultValue=murl,searchMsg='Search For Movies')
        if not encode: return False   
        url = 'http://tv-release.net/?s='+encode+'&cat=Movies-XviD,Movies-720p,Movies-480p,Movies-Foreign,Movies-DVDR,'
        INDEX(url)

def TVPACKS(url):
    html = GETHTML(url)
    if html == None:
        return
    pattern = '(?sim)Tv/Pack</a></span>.+?<a href="([^"]+?)"><b><font size="2px">([^<]+?)<'
    r = re.findall(pattern,html)
    for url, name in r:
        main.addDir(name, url, 1001,'')
        
def GOTOP(url):
    default = url
    r = url.rpartition(':')
    url = re.findall('^(.+page=)\d+(.*)$',r[0])
    total = r[2]
    keyboard = xbmcgui.Dialog().numeric(0, '[B][I]Goto Page Number[/B][/I]')
    if not keyboard: 
        xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False)
        return False
    if int(keyboard) > int(total) or keyboard == '0':
        addon.show_ok_dialog(['Please Do Not Enter a Page Number bigger than',''+total+', Enter A Number Between 1 and '+total+'',
                              ''], 'MashUP: TV-Release')
        GOTOP(default)
    url = url[0][0]+keyboard+str(url[0][1])
    INDEX(url)
        
def PLAYMEDIA(name,url):
    ok = True
    r = re.findall(r'(.+?)\[COLOR', name)
    name = r[0]
    r=re.findall('Season(.+?)Episode([^<]+)',name)
    if r:
        infoLabels =main.GETMETAEpiT(name,'','')
        video_type='episode'
        season=infoLabels['season']
        episode=infoLabels['episode']
    else:
        infoLabels =main.GETMETAT(name,'','','')
        video_type='movie'
        season=''
        episode=''
    img=infoLabels['cover_url']
    fanart =infoLabels['backdrop_url']
    imdb_id=infoLabels['imdb_id']
    infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }
    try:
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
        stream_url = main.resolve_url(url)
        infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre']}
        # play with bookmark
        from resources.universal import playbackengine
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=str(infoLabels['title']),season=str(season), episode=str(episode), year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            from resources.universal import watchhistory
            wh = watchhistory.WatchHistory(addon_id)
            wh.add_item(name+' '+'[COLOR=FF67cc33]TvRelease[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=str(img), fanart=str(fanart), is_folder=False)
        player.KeepAlive()
        return ok
    except:
        return ok

def GETHTML(url):
    try:
        h = main.OPENURL(url.replace(' ','%20'))
        if '<h2>Under Maintenance</h2>' in h:
            addon.show_ok_dialog(['[COLOR=FF67cc33][B]TV-Release is Down For Maintenance,[/COLOR][/B]',
                                  '[COLOR=FF67cc33][B]Please Try Again Later[/COLOR][/B]',''],'MashUP: TV-Release')
            xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False)
            return
        return h
    except urllib2.URLError, e:
        addon.show_small_popup('MashUP: Tv-Release','TV-Release Web Site Failed To Respond, Check Log For Details', 9000, error_logo)
        addon.log_notice(str(e))
        xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False)
        return
