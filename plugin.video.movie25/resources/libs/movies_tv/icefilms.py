import urllib,re,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
IceURL='http://www.icefilms.info'
prettyName='IceFilms'

def AtoZICE(type,index=False):
    import string
    main.addDir('0-9','/'+type+'/a-z/1',282,art+'/09.png',index=index)
    for i in string.ascii_uppercase:
        main.addDir(i,'/'+type+'/a-z/'+i,282,art+'/'+i.lower()+'.png',index=index)
    main.VIEWSB()
    
def ICEMAIN():
    main.addDir('TV','TV',288,art+'/icefilms.png')
    main.addDir('Movies','Movies',295,art+'/icefilms.png')
    
def ICEMOVIEMAIN(index=False):
    main.addDir('Search for Movies','Movies',286,art+'/search.png',index=index)
    main.addDir('A-Z','movies',292,art+'/az.png',index=index)
    main.addDir('Highly Rated','/movies/rating/1',282,art+'/icefilms.png',index=index)
    main.addDir('Popular Movies','/movies/popular/1',282,art+'/icefilms.png',index=index)
    main.addDir('Latest Released','/movies/release/1',282,art+'/icefilms.png',index=index)
    main.addDir('Latest Added','/movies/added/1',282,art+'/icefilms.png',index=index)
    main.addDir('Genre','movies',293,art+'/genre.png',index=index)
    main.GA("IceFilms","Movie")
    main.VIEWSB2()

def ICETVMAIN(index=False):
    main.addDir('Search for TV Shows','TV',286,art+'/search.png',index=index)
    main.addDir('A-Z','tv',292,art+'/az.png',index=index)
    main.addDir('Latest Releases','TV',291,art+'/icefilms.png',index=index)
    main.addDir('Highly Rated','/tv/rating/1',282,art+'/icefilms.png',index=index)
    main.addDir('Popular Shows','/tv/popular/1',282,art+'/icefilms.png',index=index)
    main.addDir('Latest Released','/tv/release/1',282,art+'/icefilms.png',index=index)
    main.addDir('Latest Added','/tv/added/1',282,art+'/icefilms.png',index=index)
    main.addDir('Genre','tv',293,art+'/genre.png',index=index)
    main.GA("IceFilms","TV")
    main.VIEWSB2()

def ICEGENRE(type,index=False):
    main.addDir('Action','/'+type+'/popular/action',282,art+'/act.png',index=index)
    main.addDir('Animation','/'+type+'/popular/animation',282,art+'/anim.png',index=index)
    main.addDir('Comedy','/'+type+'/popular/comedy',282,art+'/com.png',index=index)
    main.addDir('Documentary','/'+type+'/popular/documentary',282,art+'/doc.png',index=index)
    main.addDir('Drama','/'+type+'/popular/drama',282,art+'/dra.png',index=index)
    main.addDir('Family','/'+type+'/popular/family',282,art+'/fam.png',index=index)
    main.addDir('Horror','/'+type+'/popular/horror',282,art+'/hor.png',index=index)
    main.addDir('Romance','/'+type+'/popular/romance',282,art+'/rom.png',index=index)
    main.addDir('Sci-Fi','/'+type+'/popular/sci-fi',282,art+'/sci.png',index=index)
    main.addDir('Thriller','/'+type+'/popular/thriller',282,art+'/thr.png',index=index)

def ICETODAY(murl,index=False):
    link = main.OPENURL(IceURL)
    link = cleanHex(link)
    latest = re.compile('<h1>Latest Releases</h1>(.+?)<h1>',re.DOTALL).findall(link)
    if latest:
        main.addDir('Search for TV Shows','TV',286,art+'/search.png')
        match=re.compile('<a href=(/ip[^>]+?)>([^<]+?)</a>(.*?)<li>',re.DOTALL).findall(latest[0])
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Episode list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")
        for url,title,hd in match:
            if re.search('\d+x\d+',title):
                title = re.sub('(.*)\(\d{4}\)\s*$','\\1',title).strip()
                title = re.sub('(\d+x\d+)\s(.*)','\\1 [COLOR blue]\\2[/COLOR]',title)
                title = re.sub(' \[COLOR blue\](& \d+x\d+ )',' \\1[COLOR blue]',title)
                title = title.replace('[COLOR blue][/COLOR]','').strip()
                if hd: title += " [COLOR red]HD[/COLOR]"
                if index == 'True':
                    main.addDirTE(title,url,21,'','','','','','')
                else:
                    main.addDirTE(title,url,283,'','','','','','')
                loadedLinks += 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if dialogWait.iscanceled(): return False    
        dialogWait.close()
        del dialogWait

def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))

def LISTICE(murl,index=False):
    link = main.OPENURL(IceURL+murl)
    link = cleanHex(link)
    if '/tv/'in murl:
        match=re.compile('<a name=i id=(\d+)></a><img class=star><a href=(/tv[^<]+?)>([^<]+?)</a>(.)*?<br>',re.DOTALL).findall(link)
        main.GA("TV","IceFilms")
    else:    
        main.addDir('Search for Movies','Movies',286,art+'/search.png')
        match=re.compile('<a name=i id=(\d+)></a><img class=star><a href=(/ip[^>]+?)>([^<]+?)</a>(.)*?<br>',re.DOTALL).findall(link)
        main.GA("HD","IceFilms")
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Movie/Show list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Movies/Shows loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
    xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")
    for imdb,url,title,hd in match:
        if hd: title += ' [COLOR red]HD[/COLOR]'
        title = re.sub('\s\s+',' ',title)
        if '/tv/'in murl:
            main.addDirT(title.strip(),IceURL+url,289,'','','','','','',index=index)
        else:
            if index == 'True':
                main.addDirM(title.strip(),IceURL+url,21,'','','','','','',imdb)
            else:
                main.addDirM(title.strip(),IceURL+url,283,'','','','','','',imdb)
        loadedLinks += 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Movies/Shows loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if dialogWait.iscanceled(): break   
    dialogWait.close()
    del dialogWait
    main.VIEWS()
    
def ICESEASONS(name,url,index=False):
    link = main.OPENURL(url)
    link = cleanHex(link)
    name = re.sub('(.*)\(\d{4}\)\s*$','\\1',name).strip(" :-")
    seasons = re.compile('(?sim)<h3><a [^>]*?></a>([^<]*?)<(.*?)(?=<h3|div)').findall(link)
    if not re.search('<h3><a [^>]*?></a>(\d+)', link): seasons = reversed(seasons)
    for season,data in seasons:
        episodes = re.compile('<a href=(/ip[^>]+?)>([^<]+?)</a>(.)*?<br>',re.DOTALL).findall(data)
        if not re.search('<h3><a [^>]*?></a>(\d+)', link): episodes = list(reversed(episodes))
        main.addDir(name+' '+season.strip(),urllib.quote(str(episodes)),290,'','',index=index)

def ICEEPISODES(name,url,index=False):
    name = re.sub('(.*)\(\d{4}\)\s*$','\\1',name).strip(" :-")
    name = re.sub('(.*)\d{4}$','\\1',name).strip(" :-")
    name = name.partition('Season')[0].strip()
    episodes = eval(urllib.unquote(url))
    totalLinks = len(episodes)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Episode list is cached.')
    loadedLinks = 0
    remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
    xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")
    for url,title,hd in episodes:
        title = re.sub('(\d+x\d+)\s(.*)','\\1 [COLOR blue]\\2[/COLOR]',title)
        title = re.sub(' \[COLOR blue\](& \d+x\d+ )',' \\1[COLOR blue]',title)
        title = title.replace('[COLOR blue][/COLOR]','').strip()
        if hd: title += " [COLOR red]HD[/COLOR]"
        if index == 'True':
            main.addDirTE(name+' '+title,IceURL+url,21,'','','','','','')
        else:
            main.addDirTE(name+' '+title,IceURL+url,283,'','','','','','')
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if (dialogWait.iscanceled()):
            return False    
    dialogWait.close()
    del dialogWait
    main.GA("Episodes","IceFilms")

def resolveIceLink(params):
    from t0mm0.common.net import Net as net
    ajax_url = IceURL + '/membersonly/components/com_iceplayer/video.phpAjaxResp.php'
    headers = {'Content-type':'application/x-www-form-urlencoded'}
    s_params=re.search('<t>([^<]+?)</t><sec>([^<]+?)</sec><id>([^<]+?)</id>',params)
    params = {}
    params['sec'] = s_params.group(2)
    params['t']=s_params.group(1)
    params['id']=s_params.group(3)
    import random
    source_params = {'iqs': '','url': '', 'cap': '' }
    source_params['m'] = random.randrange(100, 300) * -1
    source_params['s'] = random.randrange(5, 50)
    source_params.update(params)
    ajax_content = net().http_POST(ajax_url, source_params, headers).content
    return urllib.unquote(re.search('url=(.*)', ajax_content).group(1))

def GetHostsName(url):
    print "ddds "+str(url)
    #murl = eval(urllib.unquote(url))
    url=resolveIceLink(url)
    host_list = {"2shared.com":"2shared","180upload.com":"180upload","vidhog.com":"vidhog","sharebees.com": "sharebees","movreel.com":"movreel",
            "billionuploads.com": "billionuploads","epicshare.net": "epicshare","megarelease.org": "megarelease","lemuploads.com": "lemuploads",
            "hugefiles.net": "hugefiles","entroupload.com": "entroupload","donevideo.com":"donevideo","vidplay.net":"vidplay","megafiles.se":"megafiles"}
     
    hoster = re.search('https?://[www\.]*([^/]+)/', url)
    if hoster:
        hoster=hoster.group(1)
        for s, r in host_list.items():
            hoster = hoster.replace(s, r)
        hoster = re.sub(r"<!--.+?-->", "", hoster)
        return hoster,url
def LISTLINKS(mname,murl):
    mname = re.sub('\[COLOR red\].*?\[/COLOR\]','',mname).strip()
    url = '/membersonly/components/com_iceplayer/video.php?h=331&w=719&vid='
    id = re.compile('v=(\d+)').findall(murl)[0]
    url += id + '&img='
    content = main.OPENURL(IceURL+url, verbose=False)
    source_args = {}
    source_args['sec'] = re.search('f\.lastChild\.value="([^"]+?)",a', content).group(1)
    source_args['t'] = re.search('"&t=([^"]+)",', content).group(1)
    sec = re.search('f\.lastChild\.value="([^"]+?)",a', content).group(1)
    t = re.search('"&t=([^"]+)",', content).group(1)
    for quality, links in re.findall('<div class=ripdiv><b>([^<]+?)</b><p>(.+?)<p></div>', content):
        if 'DVD' in quality: quality = 'SD'
        elif 'HD' in quality: quality = 'HD'
        for id, text in re.findall('''<a[^>]+?go\(([^\)]+?)\)'>Source #\d+: (.+?)</a>''', links):
            
            source_params = source_args
            source_params['id'] = id
            s_params='<t>'+t+'</t><sec>'+sec+'</sec><id>'+id+'</id>'
            host=re.sub('<.*?>','',text,re.I|re.DOTALL).strip()
            #host=GetHostsName(source_params)
            thumb = host.lower()
            main.addDown2(mname+' [COLOR red]'+quality+'[/COLOR]'+' [COLOR blue]'+host.upper()+'[/COLOR]',s_params,284,art+'/hosts/'+thumb+".png",art+'/hosts/'+thumb+".png")
            
def StartIceFilmsSearch(type='Movies',index=False):
    searchpath=os.path.join(main.datapath,'Search')
    if type == 'Movies': SearchFile=os.path.join(searchpath,'SearchHistory25')
    else: SearchFile=os.path.join(searchpath,'SearchHistoryTv')
    if not os.path.exists(SearchFile):
        SearchIceFilms(type=type)
    else:
        main.addDir('Search','###',287,art+'/search.png',type)
        main.addDir('Clear History',SearchFile,128,art+'/cleahis.png')
        thumb=art+'/link.png'
        searchitems=re.compile('search="(.+?)",').findall(open(SearchFile,'r').read())
        for searchitem in reversed(searchitems):
            searchitem=searchitem.replace('%20',' ')
            main.addDir(searchitem,searchitem,287,thumb,type,index=index)
            
def superSearch(encode,type):
    try:
        returnList=[]
        epi = re.search('(?i)s(\d+?)e(\d+?)$',encode)
        if epi:
            epistring = encode.rpartition('%20')[2].upper()
            e = int(epi.group(2))
            s = int(epi.group(1))
            if len(str(e)) == 1:
                e='0'+str(e)
            encodewithoutepi = urllib.quote(re.sub('(?i)(\ss(\d+)e(\d+))|(Season(.+?)Episode)|(\d+)x(\d+)','',urllib.unquote(encode)).strip())
            encode=encodewithoutepi+' '+str(s)+'x'+str(e)
        if type == 'Movies' or epi:
            site = 'site:http://icefilms.info/ip'
        else: site = 'site:http://icefilms.info/tv/series'
        results = main.SearchGoogle(urllib.unquote(encode), site)
        for res in results:
            t = res.title.encode('utf8')
            u = res.url.encode('utf8')
            if type == 'TV':
                if epi:
                    t = re.sub('(.*\)).*','\\1',t)
                    returnList.append((t.strip(" -"),prettyName,u,'',283,True))
                else:
                    t = t.rpartition('Episode List')[0]
                    returnList.append((t.strip(" -"),prettyName,u,'',289,True))
            else:
                if not re.search('(?i)\s\d+x\d+',t) and (re.search('(?i)links',t) or re.search('\.\.\.$',t)):
                    t = re.sub('(.*\)).*','\\1',t)
                    returnList.append((t.strip(" -"),prettyName,u,'',283,True))
        return returnList
    except: return []

 
def SearchIceFilms(searchQuery = '',type='Movies',index=False):
    searchQuery = main.updateSearchFile(searchQuery,type)
    if not searchQuery: return False   
    if type == 'Movies':
        site = 'site:http://icefilms.info/ip'
    else: site = 'site:http://icefilms.info/tv/series'
    results = main.SearchGoogle(urllib.unquote(searchQuery), site)
    r = 0
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Movie list is cached.')
    totalLinks = len(results)
    remaining_display = 'Movies loaded :: [B]'+str(r)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
    xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")
    if results:
        for res in results:
            t = res.title.encode('utf8')
            u = res.url.encode('utf8')
            if type == 'TV':
                t = t.rpartition('Episode List')[0]
                main.addDirT(t.strip(" -"),u,289,'','','','','','',index=index)
                r += 1
            else:
                if not re.search('(?i)\s\d+x\d+',t) and (re.search('(?i)links',t) or re.search('\.\.\.$',t)):
                    t = re.sub('(.*\)).*','\\1',t)
                    if index == 'True':
                        main.addDirM(t.strip(),u,21,'','','','','','')
                    else:
                        main.addDirM(t.strip(),u,283,'','','','','','')
                    r += 1
                else: 
                    if totalLinks > 1: totalLinks -= 1
            percent = (r * 100)/totalLinks
            remaining_display = 'Movies loaded :: [B]'+str(r)+' / '+str(totalLinks)+'[/B].'
            dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
            if dialogWait.iscanceled(): return False  
    if not r:
        xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False)
        xbmc.executebuiltin("XBMC.Notification(Sorry,No results found,3000)")
        return False 
    main.GA("IceFilms","Search")
               

   
def PLAYLINK(mname,murl):
    name=main.removeColoredText(mname)
    main.GA("IceFilms","Watched")
    ok=True
    infoLabels =main.GETMETAT(mname,'','','')
    video_type='movie'
    season=''
    episode=''
    img=infoLabels['cover_url']
    fanart =infoLabels['backdrop_url']
    imdb_id=infoLabels['imdb_id']
    murl=resolveIceLink(murl)
    infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }
    try:
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
        stream_url = main.resolve_url(murl)
        infoL={'Title': name, 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre']}
        # play with bookmark
        from resources.universal import playbackengine
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=name,season=str(season), episode=str(episode), year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            from resources.universal import watchhistory
            wh = watchhistory.WatchHistory('plugin.video.movie25')
            wh.add_item(mname+' '+'[COLOR green]IceFilms[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=img, fanart=fanart, is_folder=False)
        player.KeepAlive()
        return ok
    except Exception, e:
        if stream_url != False:
                main.ErrorReport(e)
        return ok
