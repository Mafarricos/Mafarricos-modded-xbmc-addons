#-*- coding: utf-8 -*-
import urllib,re,string,urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
prettyName = 'Aflam1'
MAINURL='http://www.aflam1.com'

def aflamOPENURL(url):
    fp = urllib.urlopen(url)
    return fp.read()

def MAINAFLAM():
    main.addDir('Search (بحث)','aflam',342,art+'/search.png')
    main.addDir('Home (الرئيسية)','http://www.aflam1.com/',336,art+'/aflam1.png')
    main.addDir('Egyptian Series (مسلسلات مصرية)','http://www.aflam1.com/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa-%d9%85%d8%b5%d8%b1%d9%8a%d8%a9/',339,art+'/aflam1.png')
    main.addDir('Syria Series (مسلسلات سورية)','http://www.aflam1.com/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa-%d8%b3%d9%88%d8%b1%d9%8a%d8%a9/',339,art+'/aflam1.png')
    main.addDir('Turkish Series (مسلسلات تركية)','http://www.aflam1.com/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa-%d8%aa%d8%b1%d9%83%d9%8a%d8%a9/',339,art+'/aflam1.png')
    main.addDir('Series foreign (مسلسلات أجنبية)','http://www.aflam1.com/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa-%d8%a3%d8%ac%d9%86%d8%a8%d9%8a%d8%a9/',339,art+'/aflam1.png')
    main.addDir('Movies (أفلام)','http://www.aflam1.com/%d8%a3%d9%81%d9%84%d8%a7%d9%85/%d8%a3%d9%81%d9%84%d8%a7%d9%85-%d8%a3%d8%ac%d9%86%d8%a8%d9%8a%d8%a9/',341,art+'/aflam1.png')
    main.addDir('Egyptian New Movies (أفلام مصرية جديدة)','http://www.aflam1.com/%d8%a3%d9%81%d9%84%d8%a7%d9%85/%d8%a3%d9%81%d9%84%d8%a7%d9%85-%d9%85%d8%b5%d8%b1%d9%8a%d8%a9-%d8%ac%d8%af%d9%8a%d8%af%d8%a9/',341,art+'/aflam1.png')
    main.addDir('Films Ancient Egyptian (أفلام مصرية قديمة)','http://www.aflam1.com/%d8%a3%d9%81%d9%84%d8%a7%d9%85/%d8%a3%d9%81%d9%84%d8%a7%d9%85-%d9%85%d8%b5%d8%b1%d9%8a%d8%a9-%d9%82%d8%af%d9%8a%d9%85%d8%a9/',341,art+'/aflam1.png')
    main.GA("Plugin","Aflam1")

def SEARCHAFLAM():
        keyb = xbmc.Keyboard('', 'Search Movies & Shows')
        keyb.doModal()
        if (keyb.isConfirmed()):
            search = keyb.getText()
            encode=urllib.quote(search)
            surl='http://www.aflam1.com/?s='+encode
            link=aflamOPENURL(surl)
            link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('&raquo;','')
            
            match=re.compile("""<a href="([^"]+)" rel=".+?<img width=.+?src="([^"]+)" class=".+?alt="([^"]+)" />""",re.DOTALL).findall(link)
            for url,thumb,name in match:
                if '%d8%a3%d9%81%d9%84%d8%a7%d9%85'in url:
                    main.addPlayM(name,url,338,thumb,'','','','','')
                else:
                    main.addDir(name,url,337,thumb)

def SERIESAFLAM(murl):
    link=aflamOPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('&raquo;','')
    match=re.compile("""<a href="([^"]+)"><img src="([^"]+)" class=".+?alt="([^"]+)" />""",re.DOTALL).findall(link)
    for url,thumb,name in match:
        name=name+'  '
        main.addDir(name,url,337,thumb)
    paginate = re.compile('''<a class="nextpostslink" href="([^"]+)">»</a>''').findall(link)
    if len(paginate)>0:
        main.addDir('Next',paginate[0],339,art+'/next2.png')

def MOVIESAFLAM(murl):
    link=aflamOPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('&raquo;','')
    match=re.compile("""<a href="([^<]+)"><b>(.+?)</b></a>([^<]+)""",re.DOTALL).findall(link)
    for url,name,count in match:
        count=count.replace('  ','')
        name=name+'  '
        main.addDir('[COLOR red]'+count+'[/COLOR]'+name,url,341,art+'/aflam1.png')

def LISTMov(murl):
    link=aflamOPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('&raquo;','')
    match=re.compile("""<a href="([^"]+)"><img src="([^"]+)" class=".+?alt="([^"]+)" />""",re.DOTALL).findall(link)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Movie list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
    for url,thumb,name in match:
        name=main.unescapes(name)
        main.addPlayM(name,url,338,thumb,'','','','','')
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if (dialogWait.iscanceled()):
            return False   
    dialogWait.close()
    del dialogWait
    paginate = re.compile('''<a class="nextpostslink" href="([^"]+)">»</a>''').findall(link)
    if len(paginate)>0:
        main.addDir('Next',paginate[0],341,art+'/next2.png')
                
    main.GA("Aflam1","List")

def LISTProg(murl):
    link=aflamOPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('&raquo;','')
    match=re.compile("""<a href="([^"]+)"><img src="([^"]+)" class=".+?alt="([^"]+)" /></a>""",re.DOTALL).findall(link)
    for url,thumb,name in match:
        main.addDir(name,url,337,thumb)

    paginate = re.compile('''<a class="xo-pagarrow" href="([^<]+)"><u></u>''').findall(link)
    if len(paginate)>0:
        main.addDir('Next',MAINURL+paginate[0],336,art+'/next2.png')
                
    main.GA("Aflam1","List")


def LISTEPI(mname,murl,thumb):
    link=aflamOPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('&raquo;','')
    match=re.compile("""<li>([^<]+)<span dir="ltr"><a href="([^"]+)" onClick=".+?">([^<]+)</a></span>""",re.DOTALL).findall(link)
    for num,url,name in match:
        main.addPlayc(num+' '+name,url,338,thumb,'','','','','')


def get_mailru(url):
    from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
    import cookielib
    link=main.OPENURL(url)
    match=re.compile('videoSrc = "(.+?)",',re.DOTALL).findall(link)
    cj = cookielib.CookieJar()
    opener = build_opener(HTTPCookieProcessor(cj), HTTPHandler())
    req = Request(url)
    f = opener.open(req)
    html = f.read()
    for cookie in cj:
        cookie=str(cookie)

    rcookie=cookie.replace('<Cookie ','').replace(' for .video.mail.ru/>','')

    vlink=match[0]+'|Cookie='+rcookie
    return vlink
    

def LINKSAFLAM(mname,murl,thumb):
    main.GA("Aflam1","Watched")
    if 'car-auto' not in murl:
        link=aflamOPENURL(murl)
        match=re.compile('<a class="btn default large text-right" href="(.+?)"',re.DOTALL).findall(link)
        if match:
            murl=match[0]
            murl=murl.replace(' ','')
    xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,5000)")
    print murl
    link=aflamOPENURL(murl)
    ok=True
    infoLabels =main.GETMETAT(mname,'','',thumb)
    video_type='movie'
    season=''
    episode=''
    img=infoLabels['cover_url']
    fanart =infoLabels['backdrop_url']
    imdb_id=infoLabels['imdb_id']
    infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }
        
    match=re.compile("""<div id="Layer2".+?<iframe src='(.+?)'""",re.DOTALL).findall(link)
    if not match:
        match=re.compile('<div id="Layer2".+?<iframe src="(.+?)"',re.DOTALL).findall(link)
    if 'mail.ru' in match[0]:
        stream_url=get_mailru(match[0])
    else:
        stream_url = main.resolve_url(match[0])
        
    try:
        if stream_url == False: return                                                            
        infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre'], 'originaltitle': infoLabels['metaName']}
        # play with bookmark
        stream_url=stream_url.replace(' ','%20')
        from resources.universal import playbackengine
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=str(infoLabels['title']),season=str(season), episode=str(episode), year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            from resources.universal import watchhistory
            wh = watchhistory.WatchHistory(addon_id)
            wh.add_item(mname+' '+'[COLOR green]Aflam1[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=img, fanart=fanart, is_folder=False)
        player.KeepAlive()
        return True
    except Exception, e:
        if stream_url != False: main.ErrorReport(e)
        return False
