import urllib,re,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
prettyName = 'Sceper'

def MAINSCEPER():
        main.GA("Plugin","Sceper")
        main.addDir('Search Movies & TV Shows','s',543,art+'/search.png')
        main.addDir('Movies','movies',540,art+'/sceperm.png')
        main.addDir('Tv Shows','tvshows',540,art+'/scepert.png')
        main.VIEWSB2()
def MORTSCEPER(murl):
        if murl=='movies':
            main.GA("Sceper","Movies")
            main.addDir('All Movies','http://sceper.ws/home/category/movies',541,art+'/sceperm.png')
            main.addDir('Cartoons','http://sceper.ws/home/category/movies/cartoons',541,art+'/sceperm.png')
            main.addDir('Foreign Movies','http://sceper.ws/home/category/movies/movies-foreign',541,art+'/sceperm.png')
            main.addDir('HDTV 720p Movies','http://sceper.ws/home/category/movies/movies-hdtv-720p',541,art+'/sceperm.png')
            main.addDir('BluRay Rip Movies (BDRC,BDRip,BRRip)','http://sceper.ws/home/category/movies/movies-bluray-rip',541,art+'/sceperm.png')
            main.addDir('HDDVD Rip Movies','http://sceper.ws/home/category/movies/movies-hddvd-rip',541,art+'/sceperm.png')
            main.addDir('DVD Rip Movies','http://sceper.ws/home/category/movies/movies-dvd-rip',541,art+'/sceperm.png')
            main.addDir('DVD Screener Movies','http://sceper.ws/home/category/movies/movies-screener/movies-screener-dvd',531,art+'/sceperm.png')
            main.addDir('R5 Movies','http://sceper.ws/home/category/movies/movies-r5',541,art+'/sceperm.png')
        elif murl=='tvshows':
            main.GA("Sceper","Tv")
            main.addDir('All TV Shows','http://sceper.ws/home/category/tv-shows',545,art+'/scepert.png')
            main.addDir('Anime/Cartoon TV Shows','http://sceper.ws/home/category/tv-shows/animes',545,art+'/scepert.png')
            main.addDir('HDTV 720p TV Shows','http://sceper.ws/home/category/tv-shows/tv-shows-x264',545,art+'/scepert.png')
            main.addDir('Documentary TV Shows','http://sceper.ws/home/category/tv-shows/documentaries',545,art+'/scepert.png')
        main.VIEWSB2()
        
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
        
    isHD = re.compile('(?i)720p?|1080p?').findall(quality)
    if isHD:
        quality = quality.split(isHD[0])[0].strip("- ")
    else:
        quality = re.sub('(?i)(HDTV|PDTV|WEB DL|DVDRIP|WS DSR|DSR|HDRIP|BDRip|DVDR|WEBRiP|DVDscr|DVDSCR|BRRIP|R5|R6|480p|x264|lol ?-).*','',quality).strip("- ")
    if 'webdl' in quality and isHD: isHD[0] += " WEB-DL"
    if 'dvdrip' in quality and not isHD: isHD = [("DVDRip")]
    title = re.sub('(\d{4}\.\d{2}\.\d{2})(.*)','\\1[COLOR blue]\\2[/COLOR]',title)
    title = re.sub('([sS]\d+[eE]\d+).?([eE]\d+)','\\1.\\2',title)
    title = re.sub('([sS]\d+[eE]\d+.*?) (.*)','\\1 [COLOR blue]\\2[/COLOR]',title)
    if not isHD: isHD = [("SD")]
    if isHD:
        quality += " [COLOR red]"+isHD[0].strip()+"[/COLOR]"
    return quality.strip()
            
def LISTSCEPER(name,murl):
    main.GA("Sceper","List")
    link=main.OPENURL(murl, timeout = 10,cookie="sceper")
    if "setCookie(" in link:
        import time
        from cookielib import Cookie
        cookieList = []
        t = time.time() + 259200
        c = Cookie(version=False, name='hasVisitedSite', value='Yes', port=None, port_specified=False, domain='', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=t, discard=True, comment=None, comment_url=None, rest={}, rfc2109=False)
        cookieList.append(c)
        link=main.OPENURL(murl, timeout = 10,cookie="sceper",setCookie=cookieList)
    i=0
    audiolist=[]
    desclist=[]
    genrelist=[]
    link=link.replace('\xc2\xa0','').replace('\n','')
    audio=re.compile('>Audio:</.+?>([^<]+?)<').findall(link)
    if len(audio)>0:
        for aud in audio:
            audiolist.append(aud)
    else:
        audiolist.append('Audio Unknown')
    descr=re.compile('>Release Description</div><p>([^<]+?)</p>').findall(link)
    if len(descr)>0:
        for desc in descr:
            desc=desc.replace('</span><span style="font-family: arial"> ','').replace('<span style="color: #ff0000;">','').replace('</span>','')
            desclist.append(desc)
    else:
        desclist.append('Description Unavailable')
    genre=re.compile('>Genre:</span>([^<]+?)<br').findall(link)
    if len(genre)>0:
        for gen in genre:
            gen=gen.replace('</span><span style="font-family: arial"> ','').replace('<span style="color: #ff0000;">','').replace('</span>','')
            genrelist.append(gen)
    else:
        genrelist.append('Genre Unknown')
    match=re.compile('<a href="([^<]+)">([^<]+)</a></h2>\t\t<div class="[^"]+?">\t\t\t\t<div class="[^"]+?">Release Info</div><p><a href="([^"]+?)"').findall(link)
    if match:
        main.addDir('Search','s',543,art+'/search.png')
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Movie list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
    for url,name,thumb in match:
        
        if len(audiolist)<8:
            audiolist.append('Audio Unknown')
        if len(desclist)<8:
            desclist.append('Description Unavailable')
        if len(genrelist)<8:
            genrelist.append('Genre Unknown')
        sname=name
        data=re.findall('([^<]+)\s\(?(\d{4})\)?\s([^<]+)',sname)
        for title,date,quality in data:
            sname = processTitle(title,quality)
            name=title+' ('+date+') '+sname
        main.addPlayM(name.strip()+' [COLOR blue]'+audiolist[i].strip()+'[/COLOR]',url,544,thumb,desclist[i],'','',genrelist[i],'')
        i=i+1
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if dialogWait.iscanceled(): break
    dialogWait.close()
    del dialogWait
    paginate = re.compile('<a class="nextpostslink" rel="next" href="([^"]+)">').findall(link)
    if paginate and loadedLinks >= totalLinks:
        main.addDir('Next',paginate[0],541,art+'/next2.png')
    main.VIEWS()

def LISTSCEPER2(name,murl):
        link=main.OPENURL(murl, timeout = 10)
        link=link.replace('\xc2\xa0','').replace('\n','')
        match=re.compile('<a href="([^<]+)">([^<]+)</a></h2>\t\t<div class=".+?<img.+?src="([^"]+?)"').findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Show list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for url,name,thumb in match:
            name=main.CleanTitle(name)
            main.addPlayTE(name,url,544,thumb,'','','','','')
            loadedLinks = loadedLinks + 1
            percent = (loadedLinks * 100)/totalLinks
            remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
            dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
            if (dialogWait.iscanceled()):
                    return False
        dialogWait.close()
        del dialogWait
        paginate = re.compile('<a class="nextpostslink" rel="next" href="([^"]+)">').findall(link)
        if len(paginate)>0:
            main.addDir('Next',paginate[0],545,art+'/next2.png')

def SearchhistorySCEPER():
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistory25')
        if not os.path.exists(SeaFile):
            SEARCHSCEPER()
        else:
            main.addDir('Search','###',542,art+'/search.png')
            main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
            thumb=art+'/link.png'
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                    url=seahis
                    seahis=seahis.replace('%20',' ')
                    main.addDir(seahis,url,542,thumb)
            
def superSearch(encode,type):
    try:
        returnList=[]
        if not encode: return returnList
        surl='http://sceper.ws/search/'+encode+'/'
        link = main.OPENURL(surl,verbose=False)
        link=link.replace('\xc2\xa0','').replace('\n','')
        match=re.compile('<a href="([^<]+)">([^<]+)</a></h2>').findall(link)
        for url,name in match:
            name=main.CleanTitle(name)
            if type=='Movies' and not re.findall('(.+?)\ss(\d+)e(\d+)',name,re.I) or type=='TV' and re.findall('(.+?)\ss(\d+)e(\d+)',name,re.I):
                returnList.append((name,prettyName,url,'',544,False))
        return returnList
    except: return []            
        
def SEARCHSCEPER(murl = ''):
        main.GA("Sceper","Search")
        encode = main.updateSearchFile(murl,'Movies',searchMsg='Search For Movies or TV Shows')
        if not encode: return False   
        surl='http://sceper.ws/search/'+encode+'/'
        link=main.OPENURL(surl,cookie="sceper")
        i=0
        link=link.replace('\xc2\xa0','').replace('\n','')
        match=re.compile('<a href="([^<]+)">([^<]+)</a></h2>').findall(link)
        for url,name in match:
            name=main.CleanTitle(name)
            if re.findall('(.+?)\ss(\d+)e(\d+)\s',name,re.I):
                main.addPlayTE(name,url,544,'','','','','','')
            else:
                main.addPlayM(name,url,544,'','','','','','')
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
        

def VIDEOLINKSSCEPER(mname,murl,thumb):
        main.GA("Sceper","Watched")
        msg = xbmcgui.DialogProgress()
        msg.create('Please Wait!','')
        msg.update(0,'Collecting hosts')
        link=main.OPENURL(murl, cookie="sceper")
        sources=[]
        titles=[]
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        match0=re.compile('(?sim)<div class="meta">Download Links</div>.*?</div>').findall(link)
        match1 = []
        match2 = []
        if match0:
            match2=re.compile('(?sim)<p.*?</p>').findall(match0[0])
            for paragraph in reversed(match2):
                match1 +=re.compile('<a href="([^"]+?)"').findall(paragraph)
        match = []
        paragraphs = re.compile('(?sim)<p.*?</p>').findall(link)
        for paragraph in paragraphs:
            domains = re.compile('<a href="https?://([^"]+?)/[^"]+(?!jpg|gif|jpeg|png)">htt').findall(paragraph)
            urls = re.compile('<a href="([^"]+)(?!jpg|gif|jpeg|png)">htt').findall(paragraph)
            for d in domains:
                if domains.count(d) > 1:
                    while d in domains:
                        index = domains.index(d)
                        domains.pop(index)
                        urls.pop(index)
            match += urls
#         match=re.compile('<a href="([^<]+)">htt').findall(link)
        match = match1 + match
        mainlinks = len(match1)
        numpar = len(match2)
        hostsmax = len(match)
        h = 0
        from urlparse import urlparse
        for url in match:
            url = url.strip()
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
                if h <= mainlinks and numpar == 1: quality = mname
                else: quality = url
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
                    titles.append(host + filename)
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
                    wh = watchhistory.WatchHistory('plugin.video.movie25')
                    wh.add_item(mname+' '+'[COLOR green]Sceper[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=img, fanart=fanart, is_folder=False)
                player.KeepAlive()
                return ok
        except Exception, e:
                if stream_url != False:
                        main.ErrorReport(e)
                return ok
