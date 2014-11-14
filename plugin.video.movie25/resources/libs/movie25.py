import urllib,re,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
MainUrl='http://www.movie25.so'
prettyName='Movie25'

def LISTMOVIES(murl,index=False):
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match = re.findall('movie_pic"><a href="([^"]+)"  target=".+?<img src="(.+?)".+?target="_self">([^<]+)</a>.+?>([^<]+)</a>.+?<br/>Views: <span>(.+?)</span>.+?(.+?)votes.*?<li class="current-rating" style="width:(\d+?)px',link)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Movie list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
    xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")
    for url,thumb,name,genre,views,votes,rating in match:
        votes=votes.replace('(','')
        name=name.replace('-','').replace('&','').replace('acute;','').strip()
        if index == 'True':
            main.addInfo(name+'[COLOR blue] Views: '+views+'[/COLOR] [COLOR red]Votes: '+votes+'[/COLOR] [COLOR green]Rating: '+rating+'/100[/COLOR]',MainUrl+url,21,thumb,genre,'')
        else:
            main.addInfo(name+'[COLOR blue] Views: '+views+'[/COLOR] [COLOR red]Votes: '+votes+'[/COLOR] [COLOR green]Rating: '+rating+'/100[/COLOR]',MainUrl+url,3,thumb,genre,'')
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if dialogWait.iscanceled(): return False   
    dialogWait.close()
    del dialogWait
    
    main.GA("None","Movie25-list")
    
    paginate=re.compile('</a><a href=\'([^<]+)\'>Next</a>').findall(link)
    if paginate:
#                 main.addDir('[COLOR red]Home[/COLOR]','',2000,art+'/home.png')
        main.addDir('[COLOR red]Enter Page #[/COLOR]',murl,207,art+'/gotopage.png',index=index)
        xurl=MainUrl+paginate[0]
        r = re.findall('>Next</a><a href=\'/.+?/(\d+)\'>Last</a>',link)
        pg= re.findall('/.+?/(\d+)',paginate[0])
        pg=int(pg[0])-1
        if r:
            main.addDir('[COLOR blue]Page '+ str(pg)+' of '+r[0]+'[/COLOR]',xurl,1,art+'/next2.png',index=index)
        else:
            main.addDir('[COLOR blue]Page '+ str(pg)+'[/COLOR]',xurl,1,art+'/next2.png',index=index)
    
    xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
    main.VIEWS()

def UFCMOVIE25():
    surl='http://www.movie25.so/search.php?key=ufc&submit='
    link=main.OPENURL(surl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.compile('<div class="movie_pic"><a href="(.+?)" target=".+?">                            <img src="(.+?)" width=".+?" height=".+?" />                            </a></div>            <div class=".+?">              <div class=".+?">                <h1><a href=".+?" target=".+?">                  (.+?)                  </a></h1>                <div class=".+?">Genre:                  <a href=".+?" target=\'.+?\'>(.+?)</a>.+?Release:.+?Views: <span>                (.+?)                </span>.+?<span id=RateCount.+?>                (.+?)                </span> votes').findall(link)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Movie list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
    for url,thumb,name,genre,views,votes in match:
        name=name.replace('-','').replace('&','').replace('acute;','').strip()
        furl= MainUrl+url
        main.addInfo(name+'('+year+')[COLOR blue] Views: '+views+'[/COLOR] [COLOR red]Votes: '+votes+'[/COLOR]',furl,3,thumb,genre,'')
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if dialogWait.iscanceled(): return False 
    dialogWait.close()
    del dialogWait
    main.addDir('[COLOR blue]Page 2[/COLOR]','http://www.movie25.so/search.php?page=2&key=ufc',9,art+'/next2.png')
    main.GA("UFC","UFC_Movie25-List")

def Searchhistory(index=False):
    seapath=os.path.join(main.datapath,'Search')
    SeaFile=os.path.join(seapath,'SearchHistory25')
    if not os.path.exists(SeaFile):
        SEARCH(index=index)
    else:
        main.addDir('Search','###',4,art+'/search.png',index=index)
        main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
        thumb=art+'/link.png'
        searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
        for seahis in reversed(searchis):
            url=seahis
            seahis=seahis.replace('%20',' ')
            main.addDir(seahis,url,4,thumb,index=index)
            
def superSearch(encode,type):
    try:
        returnList=[]
        surl=MainUrl+'/search.php?key='+encode+'&submit='
        link=main.OPENURL(surl,verbose=False)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class="movie_pic"><a href="([^"]+?)"[^>]+?>\s*?<img src="([^"]+?)"[^>]+?>.+?<a href[^>]+?>([^<]+?)</a></h1><div class=".+?">().*?Views: <span>(.+?)</span>.+?id=RateCount_.+?>(.+?)</span>.*?<li class="current-rating" style="width:(\d+?)px').findall(link)
        for url,thumb,name,genre,views,votes,rating in match:
            url= MainUrl+url
            name=name.replace('  ','')
            returnList.append((name,prettyName,url,thumb,3,True))
        return returnList
    except: return []

def SEARCH(murl = '',index=False):
    encode = main.updateSearchFile(murl,'Movies')
    if not encode: return False   
    surl=MainUrl+'/search.php?key='+encode+'&submit='
    link=main.OPENURL(surl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.compile('<div class="movie_pic"><a href="([^"]+?)"[^>]+?>\s*?<img src="([^"]+?)"[^>]+?>.+?<a href[^>]+?>([^<]+?)</a></h1><div class=".+?">().*?Views: <span>(.+?)</span>.+?id=RateCount_.+?>(.+?)</span>.*?<li class="current-rating" style="width:(\d+?)px').findall(link)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Movie list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
    xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")
    for url,thumb,name,genre,views,votes,rating in match:
        name=name.replace('-','').replace('&','').replace('acute;','')
        furl= MainUrl+url
        if index == 'True':
            main.addInfo(name+'[COLOR blue] Views: '+views+'[/COLOR] [COLOR red]Votes: '+votes+'[/COLOR] [COLOR green]Rating: '+rating+'/100[/COLOR]',furl,21,thumb,genre,'')
        else:
            main.addInfo(name+'[COLOR blue] Views: '+views+'[/COLOR] [COLOR red]Votes: '+votes+'[/COLOR] [COLOR green]Rating: '+rating+'/100[/COLOR]',furl,3,thumb,genre,'')
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if dialogWait.iscanceled(): return False 
    dialogWait.close()
    del dialogWait
    exist = re.findall("<a href='search.php.?page=.+?'>Next</a>",link)
    if exist:
        r = re.findall(""">Next</a><a href='search.php.?page=([^<]+)&key=.+?'>Last</a>""",link)
        if r:
            main.addDir('[COLOR blue]Page 1 of '+r[0]+'[/COLOR]','http://www.movie25.so/search.php?page=2&key='+encode,9,art+'/next2.png',index=index)
        else:
            main.addDir('[COLOR blue]Page 1[/COLOR]','http://www.movie25.so/search.php?page=2&key='+encode,9,art+'/next2.png',index=index)
    xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
    main.GA("None","Movie25-Search")


def ENTYEAR(index=False):
    dialog = xbmcgui.Dialog()
    d = dialog.numeric(0, 'Enter Year')
    if d:
        encode=urllib.quote(d)
        if encode < '2014' and encode > '1900':
            surl='http://www.movie25.so/search.php?year='+encode+'/'
            YEARB(surl,index=index)
        else:
            dialog = xbmcgui.Dialog()
            ret = dialog.ok('Wrong Entry', 'Must enter year in four digit format like 1999','Enrty must be between 1900 and 2014')
        
def GotoPage(url,index=False):
    link=main.OPENURL(url)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    r = re.findall('>Next</a><a href=\'/.+?/(\d+)\'>Last</a>',link)
    x = re.findall('>Next</a><a href=\'([^<]+)/.+?\'>Last</a>',link)
    dialog = xbmcgui.Dialog()
    d = dialog.numeric(0, 'Section Last Page = '+r[0])
    if d:
        pagelimit=int(r[0])
        if int(d) <= pagelimit:
            encode=urllib.quote(d)
            surl=MainUrl+x[0]+'/'+encode
            LISTMOVIES(surl,index=index)
        else:
            dialog = xbmcgui.Dialog()
            ret = dialog.ok('Wrong Entry', 'The page number you entered does not exist.',' This sections page limit is '+str(pagelimit) )
    else:
        xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False)
        return False

def GotoPageB(url,index=False):
    link=main.OPENURL(url)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    r = re.findall('>Next</a><a href=\'search.php.?page=(.+?)&year=.+?\'>Last</a>',link)
    dialog = xbmcgui.Dialog()
    d = dialog.numeric(0, 'Section Last Page = '+r[0])
    if d:
        pagelimit=int(r[0])
        if int(d) <= pagelimit:
            encode=urllib.quote(d)
            year  = url.split('year=')
            url  = url.split('year=')
            url  = url[0].split('page=')
            surl=url[0]+'page='+encode+'&year='+year[1]
            NEXTPAGE(surl,index=index)
        else:
            dialog = xbmcgui.Dialog()
            ret = dialog.ok('Wrong Entry', 'The page number you entered does not exist.',' This sections page limit is '+str(pagelimit) )
    else:
        xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False)
        return False

def YEARB(murl,index=False):
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.compile('<div class="movie_pic"><a href="(.+?)" target=".+?">    <img src="(.+?)" width=".+?" height=".+?" />.+?<a href=".+?" target=".+?">(.+?)</a></h1><div class=".+?">Genre:  <a href=".+?" target=\'.+?\'>(.+?)</a>.+?Release:.+?<br/>Views: <span>(.+?)</span>.+?id=RateCount_.+?>(.+?)</span> votes.*?<li class="current-rating" style="width:(\d+?)px').findall(link)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Movie list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
    for url,thumb,name,genre,views,votes,rating in match:
        name=name.replace('-','').replace('&','').replace('acute;','')
        furl= 'http://movie25.com/'+url
        if index == 'True':
            main.addInfo(name+'[COLOR blue] Views: '+views+'[/COLOR] [COLOR red]Votes: '+votes+'[/COLOR] [COLOR green]Rating: '+rating+'/100[/COLOR]',furl,21,thumb,genre,'')
        else:
            main.addInfo(name+'[COLOR blue] Views: '+views+'[/COLOR] [COLOR red]Votes: '+votes+'[/COLOR] [COLOR green]Rating: '+rating+'/100[/COLOR]',furl,3,thumb,genre,'')
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if dialogWait.iscanceled(): return False 
    dialogWait.close()
    del dialogWait
    ye = murl[38:45]
    r = re.findall("Next</a><a href='search.php.?page=([^<]+)&year=.+?'>Last</a>",link)
    if r:
        main.addDir('[COLOR red]Enter Page #[/COLOR]',murl,208,art+'/gotopage.png',index=index)
        main.addDir('[COLOR blue]Page 1 of '+r[0]+'[/COLOR]','http://www.movie25.so/search.php?page=2&year='+str(ye),9,art+'/next2.png',index=index)    
    else:
        main.addDir('[COLOR blue]Page 1[/COLOR]','http://www.movie25.so/search.php?page=2&year='+str(ye),9,art+'/next2.png',index=index)
    
    xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
    main.VIEWS()
        
def NEXTPAGE(murl,index=False):
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.compile('<div class="movie_pic"><a href="(.+?)" target=".+?">    <img src="(.+?)" width=".+?" height=".+?" />.+?<a href=".+?" target=".+?">(.+?)</a></h1><div class=".+?">Genre:  <a href=".+?" target=\'.+?\'>(.+?)</a>.+?Release:.+?<br/>Views: <span>(.+?)</span>.+?id=RateCount_.+?>(.+?)</span> votes.*?<li class="current-rating" style="width:(\d+?)px').findall(link)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Movie list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
    for url,thumb,name,genre,views,votes,rating in match:
        name=name.replace('-','').replace('&','').replace('acute;','')
        furl= MainUrl+url
        if index == 'True':
            main.addInfo(name+'[COLOR blue] Views: '+views+'[/COLOR] [COLOR red]Votes: '+votes+'[/COLOR] [COLOR green]Rating: '+rating+'/100[/COLOR]',furl,21,thumb,genre,'')
        else:
            main.addInfo(name+'[COLOR blue] Views: '+views+'[/COLOR] [COLOR red]Votes: '+votes+'[/COLOR] [COLOR green]Rating: '+rating+'/100[/COLOR]',furl,3,thumb,genre,'')
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if dialogWait.iscanceled(): return False
    dialogWait.close()
    del dialogWait
    
    matchx=re.compile('http://www.movie25.so/search.php.+?page=(.+?)&year=(.+?)').findall(murl)
    if len(matchx)>0:
        durl = murl + '/'
        paginate=re.compile('http://www.movie25.so/search.php.+?page=(.+?)&year=(.+?)/').findall(durl)
        for page, yearb in paginate:
            pgs = int(page)+1
            jurl='http://www.movie25.so/search.php?page='+str(pgs)+'&year='+str(yearb)
#                 main.addDir('[COLOR red]Home[/COLOR]','',0,art+'/home.png')
        r = re.findall("Next</a><a href='search.php.?page=([^<]+)&year=.+?'>Last</a>",link)
        if r:
            main.addDir('[COLOR red]Enter Page #[/COLOR]',murl,208,art+'/gotopage.png',index=index)
            main.addDir('[COLOR blue]Page '+str(page)+' of '+r[0]+'[/COLOR]',jurl,9,art+'/next2.png',index=index)
        else:
            main.addDir('[COLOR blue]Page '+str(page)+'[/COLOR]',jurl,9,art+'/next2.png',index=index)
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
        main.VIEWS()                
    else:
        durl = murl + '/'
        paginate=re.compile('http://www.movie25.so/search.php.+?page=(.+?)&key=(.+?)/').findall(durl)
        for page, search in paginate:
            pgs = int(page)+1
            jurl='http://www.movie25.so/search.php?page='+str(pgs)+'&key='+str(search)
#                 main.addDir('[COLOR red]Home[/COLOR]','',0,art+'/home.png')
        r = re.findall(""">Next</a><a href='search.php.?page=([^<]+)&key=.+?'>Last</a>""",link)
        if r:
            main.addDir('[COLOR blue]Page '+str(page)+' of '+r[0]+'[/COLOR]',jurl,9,art+'/next2.png',index=index)
        else:
            main.addDir('[COLOR blue]Page '+str(page)+'[/COLOR]',jurl,9,art+'/next2.png',index=index)

def VIDEOLINKS(name,url):
    link=main.OPENURL(url)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\\','')
    qual = re.compile('<h1 >Links - Quality\s*?([^\s]+?)\s*?</h1>').findall(link)
    quality = str(qual)
    quality = quality.replace("'","")
    name  = name.split('[COLOR blue]')[0]
    import collections
    all=re.compile('<li class="link_name">\s*?([^<^\s]+?)\s*?</li>.+?<li class=".+?"><span><a href="([^"]+?)"').findall(link)
    all_coll = collections.defaultdict(list)
    for d in all: all_coll[d[0]].append(d[1])
    all_coll = all_coll.items()
    sortorder = "putlocker,sockshare,billionuploads,hugefiles,mightyupload,movreel,lemuploads,180upload,megarelease,filenuke,flashx,gorillavid,bayfiles,veehd,vidto,epicshare,2gbhosting,alldebrid,allmyvideos,castamp,cheesestream,clicktoview,crunchyroll,cyberlocker,daclips,dailymotion,divxstage,donevideo,ecostream,entroupload,facebook,filebox,hostingbulk,hostingcup,jumbofiles,limevideo,movdivx,movpod,movshare,movzap,muchshare,nolimitvideo,nosvideo,novamov,nowvideo,ovfile,play44_net,played,playwire,premiumize_me,primeshare,promptfile,purevid,rapidvideo,realdebrid,rpnet,seeon,sharefiles,sharerepo,sharesix,skyload,stagevu,stream2k,streamcloud,thefile,tubeplus,tunepk,ufliq,upbulk,uploadc,uploadcrazynet,veoh,vidbull,vidcrazynet,video44,videobb,videofun,videotanker,videoweed,videozed,videozer,vidhog,vidpe,vidplay,vidstream,vidup_org,vidx,vidxden,vidzur,vimeo,vureel,watchfreeinhd,xvidstage,yourupload,youtube,youwatch,zalaa,zooupload,zshare,"
    sortorder = ','.join((sortorder.split(',')[::-1]))
    all_coll = sorted(all_coll, key=lambda word: sortorder.find(word[0].lower())*-1)
    for host,urls in all_coll:
        if host.lower() in sortorder:
            host = host.strip()
            main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+" [COLOR blue]"+host.upper()+"[/COLOR]",str(urls),11,art+'/hosts/'+host+'.png',art+'/hosts/'+host+'.png')

def GroupedHosts(name,url,thumb):
    if selfAddon.getSetting("hide-download-instructions") != "true":
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
    urls = eval(url)
    for url in urls:
        main.addDown2(name,MainUrl+url,5,thumb,thumb)
        
def resolveM25URL(url):
    html=main.OPENURL(url)
    match = re.search("location\.href='(.+?)'",html)
    if match: return match.group(1)
    return

def PLAY(name,murl):
    main.GA("Movie25-Movie","Watched")
    ok=True
    hname=name
    name  = name.split('[COLOR blue]')[0]
    name  = name.split('[COLOR red]')[0]
    infoLabels = main.GETMETAT(name,'','','')
    murl = resolveM25URL(murl)
    if not murl: return False
    video_type='movie'
    season=''
    episode=''
    img=infoLabels['cover_url']
    fanart =infoLabels['backdrop_url']
    imdb_id=infoLabels['imdb_id']
    infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }

    try:
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
        stream_url = main.resolve_url(murl)

        infoL={'Title': infoLabels['metaName'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre']}
        # play with bookmark
        from resources.universal import playbackengine
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=str(infoLabels['title']),season=str(season), episode=str(episode), year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            from resources.universal import watchhistory
            wh = watchhistory.WatchHistory('plugin.video.movie25')
            wh.add_item(hname+' '+'[COLOR green]Movie25[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=img, fanart=fanart, is_folder=False)
        player.KeepAlive()
        return ok
    except Exception, e:
        if stream_url != False:
                main.ErrorReport(e)
        return ok

def PLAYB(name,murl):
    main.GA("Movie25-Movie","Watched")
    ok=True
    hname=name
    name  = name.split('[COLOR blue]')[0]
    name  = name.split('[COLOR red]')[0]
    infoLabels = main.GETMETAT(name,'','','')
    video_type='movie'
    season=''
    episode=''
    img=infoLabels['cover_url']
    fanart =infoLabels['backdrop_url']
    imdb_id=infoLabels['imdb_id']
    infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }

    try:
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
        stream_url = main.resolve_url(murl)

        infoL={'Title': infoLabels['metaName'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre']}
        # play with bookmark
        from resources.universal import playbackengine
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=str(infoLabels['title']),season=str(season), episode=str(episode), year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            from resources.universal import watchhistory
            wh = watchhistory.WatchHistory('plugin.video.movie25')
            wh.add_item(hname+' '+'[COLOR green]Movie25[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=img, fanart=fanart, is_folder=False)
        player.KeepAlive()
        return ok
    except Exception, e:
        if stream_url != False:
                main.ErrorReport(e)
        return ok
