import urllib,re,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main
from t0mm0.common.net import Net as net
#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
smalllogo=art+'/smallicon.png'
prettyName = 'Noobroom'
    
user = selfAddon.getSetting('username')
passw = selfAddon.getSetting('password')
cookie_file = os.path.join(os.path.join(main.datapath,'Cookies'), 'noobroom.cookies')
if user == '' or passw == '':
    if os.path.exists(cookie_file):
        try: os.remove(cookie_file)
        except: pass
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=FF67cc33]MashUp[/COLOR]", "Please set your Noobroom credentials", "in Addon settings under logins tab")
    selfAddon.openSettings()
    user = selfAddon.getSetting('username')
    passw = selfAddon.getSetting('password')

def setCookie(nrDomain):
    cookieExpired = False
    if os.path.exists(cookie_file):
        try:
            cookie = open(cookie_file).read()
            if not nrDomain.replace('http://','') in cookie:
                cookieExpired = True
        except: cookieExpired = True 
    if not os.path.exists(cookie_file) or cookieExpired:
        net().http_GET(nrDomain+'/login.php')
        net().http_POST(nrDomain+'/login2.php',{'email':user,'password':passw})
        net().save_cookies(cookie_file)
    else:
        net().set_cookies(cookie_file)     
               
def GetNewUrl():
    return 'http://superchillin.com'


def NBMAIN():
    main.addDir('Search for Movies','Movies',298,art+'/search.png')
    main.addDir('A-Z','movies',300,art+'/az.png')
    main.addDir('Latest','/latest.php',57,art+'/noobroom.png')
    main.addDir('Release Date','/year.php',57,art+'/noobroom.png')
    main.addDir('IMDB Rating','/rating.php',57,art+'/noobroom.png')
    main.addDir('Genre','genre',297,art+'/genre.png')
    main.GA("Plugins","Noobroom")

def AtoZNB():
    nrDomain = GetNewUrl()
    murl=nrDomain+'/azlist.php'
    setCookie(nrDomain)
    response = net().http_GET(murl)
    link = response.content
    link = link.decode('iso-8859-1').encode('utf8')
    match = re.compile('<h1>(.+?)</h1>(.+?)<br><br><br><br>').findall(link)
    for name,url in match:
        if name == '#':
            name='09'
        main.addDir(name,url,301,art+'/'+name.lower()+'.png')
    matchz = re.compile('<h1>Z</h1>(.+?)</span>',re.DOTALL).findall(link)
    if matchz:
        url=matchz[0]
        main.addDir('Z',url,301,art+'/z.png')
    main.VIEWSB()

def AZLISTNB(murl):
    nrDomain = GetNewUrl()
    if selfAddon.getSetting("hide-download-instructions") != "true":
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'',art+'/link.png')
    match=re.compile("href='(.+?)'>(.+?)</a>").findall(murl)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Movie list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
    for url,name in match:
        name=fix_title(main.unescapes(name))
        url=nrDomain+url
        loadedLinks += 1
        name = name.decode('iso-8859-1').encode('utf8')
        main.addDown3(name,url,58,'','',loadedLinks)
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if (dialogWait.iscanceled()):
            return False    
    dialogWait.close()
    del dialogWait
    main.GA("Noobroom","List")
    main.VIEWS()

def NBGENRE():
    main.addDir('Action','/genre.php?b=10000000000000000000000000',57,art+'/act.png')
    main.addDir('Adventure','/genre.php?b=01000000000000000000000000',57,art+'/adv.png')
    main.addDir('Animation','/genre.php?b=00100000000000000000000000',57,art+'/ani.png')
    main.addDir('Biography','/genre.php?b=00010000000000000000000000',57,art+'/bio.png')
    main.addDir('Comedy','/genre.php?b=00001000000000000000000000',57,art+'/com.png')
    main.addDir('Crime','/genre.php?b=00000100000000000000000000',57,art+'/cri.png')
    main.addDir('Documentary','/genre.php?b=00000010000000000000000000',57,art+'/doc.png')
    main.addDir('Drama','/genre.php?b=00000001000000000000000000',57,art+'/dra.png')
    main.addDir('Family','/genre.php?b=00000000100000000000000000',57,art+'/fam.png')
    main.addDir('Fantasy','/genre.php?b=00000000010000000000000000',57,art+'/fant.png')
    main.addDir('History','/genre.php?b=00000000000010000000000000',57,art+'/his.png')
    main.addDir('Horror','/genre.php?b=00000000000001000000000000',57,art+'/hor.png')
    main.addDir('Music','/genre.php?b=00000000000000100000000000',57,art+'/mus.png')
    main.addDir('Musical','/genre.php?b=00000000000000010000000000',57,art+'/mucl.png')
    main.addDir('Mystery','/genre.php?b=00000000000000001000000000',57,art+'/mys.png')
    main.addDir('Romance','/genre.php?b=00000000000000000001000000',57,art+'/rom.png')
    main.addDir('Sci-Fi','/genre.php?b=00000000000000000000100000',57,art+'/sci.png')
    main.addDir('Sport','/genre.php?b=00000000000000000000010000',57,art+'/sport.png')
    main.addDir('Thriller','/genre.php?b=00000000000000000000000100',57,art+'/thr.png')
    main.addDir('War','/genre.php?b=00000000000000000000000010',57,art+'/war.png')
    main.addDir('Western','/genre.php?b=00000000000000000000000001',57,art+'/west.png')
    main.GA("Noobroom","Genre")
    main.VIEWSB()

def NBSearchhistory():
    seapath=os.path.join(main.datapath,'Search')
    SeaFile=os.path.join(seapath,'SearchHistory25')
    if not os.path.exists(SeaFile):
        NBSearch('','')
    else:
        main.addDir('Search','###',299,art+'/search.png')
        main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
        thumb=art+'/link.png'
        searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
        for seahis in reversed(searchis):
            url=seahis
            seahis=seahis.replace('%20',' ')
            main.addDir(seahis,url,299,thumb)    
            
def superSearch(encode,type):
    try:
        nrDomain = GetNewUrl()
        surl=nrDomain+'/search.php?q='+encode
        setCookie(nrDomain)
        response = net().http_GET(surl)
        link = response.content
        link = link.decode('iso-8859-1').encode('utf8')
        returnList=[]
        match=re.compile("<br>(.+?) - <a[^>]+?href='(.+?)'>(.+?)</a>").findall(link)
        for year,url,name in match:
            name=fix_title(main.unescapes(name))
            try:year=year.split('</b> - ')[1]
            except:pass
            if(year=='0'):
                    year='0000'  
            url=nrDomain+url
            returnList.append((name,prettyName,url,'',58,False))
        return returnList
    except: return []

def NBSearch(mname,murl):
    if murl != '':
        encode = main.updateSearchFile(mname,'Movies','Search')
        if not encode: return False
        else:LISTSP5('/search.php?q='+encode)
    else:
        LISTSP5('/search.php?q='+murl)

def LISTSP5(xurl, retries = 1):
    try:
        nrDomain = GetNewUrl()
        murl=nrDomain+xurl
        setCookie(nrDomain)
        response = net().http_GET(murl)
    except:
        xbmc.executebuiltin("XBMC.Notification(Sorry!,Noobroom website is down,5000,"+smalllogo+")")
        return
    link = response.content
    link = link.decode('iso-8859-1').encode('utf8')
    if response.get_url() != murl or murl+'?ckattempt' in link:
        if os.path.exists(cookie_file):
            try: os.remove(cookie_file)
            except: pass
        if murl+'?ckattempt' in link:
            if retries:
                retries -= 1
                return LISTSP5('retry',retries)
        else:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Email or Password Incorrect,10000,"+smalllogo+")")
    if selfAddon.getSetting("hide-download-instructions") != "true":
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'',art+'/link.png')
    match=re.compile("<br>(.+?) - <a[^>]+?href='(.+?)'>(.+?)</a>").findall(link)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Movie list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
    for year,url,name in match:
        name=fix_title(main.unescapes(name))
        try:year=year.split('</b> - ')[1]
        except:pass
        if(year=='0'):
                year='0000'  
        url=nrDomain+url
        loadedLinks += 1
        main.addDown3(name+' [COLOR red]('+year+')[/COLOR]',url,58,'','',loadedLinks)
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if dialogWait.iscanceled(): break
    dialogWait.close()
    del dialogWait
    main.GA("Noobroom","List")
    main.VIEWS()
        
def fix_title(name):
    if name == "+1":
        name = "+1 (plus 1)"
    return name

def find_noobroom_video_url(page_url):
    import urllib2
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.71 Safari/537.36'}
    setCookie(re.sub('http://([^/]+?)/.*','\\1',page_url))
    html = net().http_GET(page_url).content
    media_id = re.compile('"file": "(.+?)"').findall(html)[0]
    fork_url = GetNewUrl() + media_id

    class MyHTTPRedirectHandler(urllib2.HTTPRedirectHandler):    
        def http_error_302(self, req, fp, code, msg, headers):
            #print headers
            self.video_url = headers['Location']
            #print self.video_url
            return urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)

        http_error_301 = http_error_303 = http_error_307 = http_error_302

    myhr = MyHTTPRedirectHandler()

    opener = urllib2.build_opener(
        urllib2.HTTPCookieProcessor(net()._cj),
        urllib2.HTTPBasicAuthHandler(),
        myhr)
    urllib2.install_opener(opener)

    req = urllib2.Request(fork_url)
    for k, v in headers.items():
        req.add_header(k, v)
    try: response = urllib2.urlopen(req)
    except: pass

    return myhr.video_url
            
def LINKSP5(mname,url):
    main.GA("Noobroom","Watched")
    ok=True
    try:
        mname  = mname.replace('[COLOR red]','').replace('[/COLOR]','')
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Opening Link,9000)")

        stream_url=find_noobroom_video_url(url)
        infoLabels =main.GETMETAT(mname,'','','')
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
            wh.add_item(mname+' '+'[COLOR=FF67cc33]Starplay[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=img, fanart='', is_folder=False)
        player.KeepAlive()
        return ok
    except Exception, e:
        main.ErrorReport(e)
        return ok
