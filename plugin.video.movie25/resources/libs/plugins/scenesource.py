import urllib,re,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
prettyName = 'SceneSource'

def MAINSCENE():
        main.GA("Plugin",prettyName)
        main.addDir('Search Movies & TV Shows','s',392,art+'/search.png')
        main.addDir('Movies','movies',388,art+'/scenesource.png')
        main.addDir('Tv Shows','tvshows',388,art+'/scenesource.png')
        main.VIEWSB2()

def SECSCENE(murl):
        if murl=='movies':
            main.GA(prettyName,"Movies")
            main.addDir('All Movies','http://www.scenesource.me/category/films/',389,art+'/scenesource.png')
            main.addDir('BDRip','http://www.scenesource.me/category/films/bdrip/',389,art+'/scenesource.png')
            main.addDir('BluRay','http://www.scenesource.me/category/films/bluray/',389,art+'/scenesource.png')
            main.addDir('DVDRip','http://www.scenesource.me/category/films/dvdrip/',389,art+'/scenesource.png')
            main.addDir('DVDSCR','http://www.scenesource.me/category/films/dvdscr/',389,art+'/scenesource.png')
            main.addDir('CAM','http://www.scenesource.me/category/films/cam/',389,art+'/scenesource.png')
            main.addDir('R5','http://www.scenesource.me/category/films/r5/',389,art+'/scenesource.png')
        elif murl=='tvshows':
            main.GA(prettyName,"Tv")
            main.addDir('All TV Shows','http://www.scenesource.me/category/tv/',391,art+'/scenesource.png')
            main.addDir('DVD','http://www.scenesource.me/category/tv/dvd/',389,art+'/scenesource.png')
            main.addDir('Sports','http://www.scenesource.me/category/tv/sports-tv/',391,art+'/scenesource.png')
            main.addDir('PREAIR','http://www.scenesource.me/category/tv/preair/',391,art+'/scenesource.png')
        main.VIEWSB2()

def SearchhistorySCENE():
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistory25')
        if not os.path.exists(SeaFile):
            murl='sec'
            SEARCHSCEPER(murl)
        else:
            main.addDir('Search','sec',393,art+'/search.png')
            main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
            thumb=art+'/link.png'
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                    url=seahis
                    seahis=seahis.replace('%20',' ')
                    main.addDir(seahis,url,393,thumb)
            
def superSearch(encode,type):
    try:
        returnList=[]
        if not encode: return returnList
        surl='http://www.scenesource.me/?s='+encode+'&x=0&y=0'
        link = main.OPENURL(surl,verbose=False,mobile=True)
        link=link.replace('\xc2\xa0','').replace('\n','')
        match=re.compile('<a href="([^<]+)" rel="bookmark" title=".+?>([^<]+)</a></h2>').findall(link)
        for url,name in match:
            name=main.CleanTitle(name)
            if type=='Movies' and not re.findall('\ss(\d+)e(\d+)',name,re.I) or type=='TV' and re.findall('\ss(\d+)e(\d+)',name,re.I):
                returnList.append((name,prettyName,url,'',390,False))
    
        return returnList            
    except: return []
    
def SEARCHSCENE(encode):
        main.GA(prettyName,"Search")
        if encode=='sec':
                encode = main.updateSearchFile('','Movies',searchMsg='Search For Movies or TV Shows')
                if not encode: return False
        surl='http://www.scenesource.me/?s='+encode+'&x=0&y=0'
        link=main.OPENURL(surl,mobile=True)
        i=0
        link=link.replace('\xc2\xa0','').replace('\n','')
        match=re.compile('<a href="([^<]+)" rel="bookmark" title=".+?>([^<]+)</a></h2>').findall(link)
        for url,name in match:
            name=main.CleanTitle(name)    
            if re.findall('(.+?)\ss(\d+)e(\d+)\s',name,re.I):
                main.addPlayTE(name,url,390,'','','','','','')
            else:
                main.addPlayM(name,url,390,'','','','','','')
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')

def LISTMOVIES(murl):
    main.GA(prettyName,"List")   
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\\','')
    match=re.compile('''<a href="([^<]+)" rel="bookmark" title=".+?">(.+?)</a></h2><div.+?<img.+?src="(.+?)".*?http://www.imdb.com/title/([t\d]+?)[/"']''',re.DOTALL).findall(link)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Movie list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
    xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")
    for url,name,thumb,imdb in match:
        name=main.CleanTitle(name)
        if re.findall('\ss(\d+)\s',name,re.I):
            main.addPlayT(name,url,390,thumb,'','','','','')
        else:
            main.addPlayM(name,url,390,thumb,'','','','','')
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if dialogWait.iscanceled(): break
    dialogWait.close()
    del dialogWait
    paginate = re.compile('<a class="nextpostslink"[^>]+?href="([^"]+)"').findall(link)
    if paginate and loadedLinks >= totalLinks:
        main.addDir('Next',paginate[0],389,art+'/next2.png')
    main.VIEWS()

def LISTTV(murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\\','')
        match=re.compile("""<a href="([^<]+)" rel="bookmark" title=".+?">(.+?)</a></h2><div class="cat meta">.+?<img.+?src=([^<]+jpg|gif|jpeg|png)""",re.DOTALL).findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Show list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for url,name,thumb in match:
            name=main.CleanTitle(name)
            thumb=thumb.replace('"','').replace(",",'')
            main.addPlayTE(name,url,390,thumb,'','','','','')
            loadedLinks = loadedLinks + 1
            percent = (loadedLinks * 100)/totalLinks
            remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
            dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
            if (dialogWait.iscanceled()):
                    return False
        dialogWait.close()
        del dialogWait
        paginate = re.compile('<a class="nextpostslink" [^>]*?href="([^"]+)"').findall(link)
        if len(paginate)>0:
            main.addDir('Next',paginate[0],391,art+'/next2.png')

def VIDEOLINKSSCENE(mname,murl,thumb):
        main.GA(prettyName,"Watched")
        msg = xbmcgui.DialogProgress()
        msg.create('Please Wait!','')
        msg.update(0,'Collecting hosts')
        link=main.OPENURL(murl)
        sources=[]
        titles=[]
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        paragraphs = re.compile('(?sim)<p.*?</p>').findall(link)
        match = []
        for paragraph in paragraphs:
            domains = re.compile('<a href="https?://([^"]+?)/[^"]+(?!jpg|gif|jpeg|png)" rel="nofollow">htt').findall(paragraph)
            urls = re.compile('<a href="([^"]+)(?!jpg|gif|jpeg|png)" rel="nofollow">htt').findall(paragraph)
            for d in domains:
                if domains.count(d) > 1:
                    while d in domains:
                        index = domains.index(d)
                        domains.pop(index)
                        urls.pop(index)
            match += urls
        hostsmax = len(match)
        h = 0
        from urlparse import urlparse
        for url in match:
            h += 1
            percent = (h * 100)/hostsmax
            msg.update(percent,'Collecting hosts - ' + str(percent) + '%')
            if msg.iscanceled(): break
            vlink=re.compile('rar|part\d+?(\.html)?$|/folder/').findall(url)
            if len(vlink)==0:
                url = re.sub('(?i)\.html$','',url)
                filename = re.compile('(?i)/([^/]*?\..{3,4})$').findall(url)
                if filename: filename = " [" + filename[0] + "]"
                else: filename = ""
                firstword = mname.partition(' ')[0]
                if re.search('(?i)'+mname.partition(' ')[0],url):
                    if re.search('(?i)1080p?',mname):
                        if not re.search('(?i)1080p?',url): continue 
                    if re.search('(?i)720p',mname):
                        if not re.search('(?i)720p?',url): continue 
                if re.search('(?i)lumfile.com|freakshare.com',url):
                    if not re.search('(?i)'+mname.partition(' ')[0],url): continue
                if re.search('(?i)1080p?',mname):
                    if re.search('(?i)720p|dvdrip|480p/|xvid',url): continue
                if re.search('(?i)720p?',mname):
                    if re.search('(?i)1080p?|dvdrip|480p|xvid',url): continue
                if re.search('(?i)xvid|480p',mname) or not re.search('(?i)1080p?|720p?',mname):
                    if re.search('(?i)1080p?|720p?',url): continue
#                 url = url.replace('ul.to','uploaded.net')
                host = urlparse(url).hostname.replace('www.','').partition('.')[0]
                hostname = host
                host = host.upper()
                quality = url
                match3=re.compile('(?i)(720p?|1080p?)').findall(quality)
                if match3 and not 'p' in match3[0]: match3[0] += 'p'
                match4=re.compile('mp4').findall(url)
                if len(match3)>0:
                    host =host+' [COLOR red]'+match3[0]+'[/COLOR]'
                elif len(match4)>0:
                    host =host+' [COLOR green]SD MP4[/COLOR]'
                else:
                    host =host+' [COLOR blue]SD[/COLOR]'
                if main.supportedHost(hostname):
                    titles.append( host + filename )
                    sources.append(url)
        msg.close()
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Could not find a playable link,3000)")
                return
        else:
                dialog = xbmcgui.Dialog()
                index = dialog.select('Choose your stream', titles)
                if index != -1: 
                    source = sources[index]
                else: source = None
        try:
                if not source:
                    main.CloseAllDialogs()
                    return
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,5000)")
                stream_url = main.resolve_url(source)
                if(stream_url == False):
                    return
                
                if re.findall('(.+?)\ss(\d+)e(\d+)\s',mname,re.I):
                    mname=mname.split('&')[0]
                    infoLabels =main.GETMETAEpiT(mname,thumb,'')
                    video_type='episode'
                    season=infoLabels['season']
                    episode=infoLabels['episode']
                else:
                    infoLabels =main.GETMETAT(mname,'','',thumb)
                    video_type='movie'
                    season=''
                    episode=''
                img=infoLabels['cover_url']
                fanart =infoLabels['backdrop_url']
                imdb_id=infoLabels['imdb_id']
                infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }
                
                infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre']}
                if not video_type is 'episode': infoL['originalTitle']=main.removeColoredText(infoLabels['metaName'])
                # play with bookmark
                from resources.universal import playbackengine
                player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=str(infoLabels['title']),season=str(season), episode=str(episode), year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
                #WatchHistory
                if selfAddon.getSetting("whistory") == "true":
                    from resources.universal import watchhistory
                    wh = watchhistory.WatchHistory(addon_id)
                    wh.add_item(mname+' '+'[COLOR green]'+prettyName+'[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=img, fanart=fanart, is_folder=False)
                player.KeepAlive()
                return ok
        except Exception, e:
                if stream_url != False:
                        main.ErrorReport(e)
                return ok
