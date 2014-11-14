import urllib,re,os,sys
import xbmc,xbmcgui,xbmcaddon,xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art

def LISTSP3(murl):
    subpages = 3
    if murl == 'HD':
        page = 1
        max = subpages
    else:
        try:
            pages = murl.split(',', 1 );
            page = int(pages[0])
            max = int(pages[1])
        except:
            page = 1
    url='http://rls1click.com/category/movies/1080p/'
    urls = []
    for n in range(subpages):
        if page+n == 1:
            urls.append(url)
        else:
            urls.append(url+"page/"+str(page+n)+"/")
        if page+n == max: break
    page = page + subpages - 1
    link=main.batchOPENURL(urls)
    if re.compile('"maxPages":"(\d+?)"').findall(link):
        max = int(re.compile('"maxPages":"(\d+?)"').findall(link)[0])
#     link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('&#38;','&')
    match=re.compile('(?sim)<h1 class="post-title"><a href="([^"]+?)">([^<]+?)<.*?<img[^>]+?src="([^"]+?)"').findall(link)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Movie list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
    for url, title, thumb  in match:
        url = url.decode('utf-8').encode('ascii', 'ignore')
        main.addPlayM(title,url,408,thumb,'','','','','')
        loadedLinks = loadedLinks + 1
        try:
            percent = (loadedLinks * 100)/totalLinks
        except: percent = 100
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if dialogWait.iscanceled(): break
    if page < max and loadedLinks >= totalLinks:
        main.addDir('Page ' + str(page/subpages) + ' [COLOR blue]Next Page >>>[/COLOR]',str(page+1)+','+str(max),407,art+'/next2.png')
    dialogWait.close()
    del dialogWait
    main.GA("HD-TV","Rls1Click")
    main.VIEWS()
        
def LINKSP3(mname,murl):
    main.GA("Rls1Click","Watched")
    msg = xbmcgui.DialogProgress()
    msg.create('Please Wait!','')
    msg.update(0,'Collecting hosts')
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('&#38;','&')
    sources=[]
    titles=[]
    urls=[]
    ok=True
    paragraphs=re.compile('(?sim)<strong>1-Click</strong>.*?<strong>1GB Links</strong>').findall(link)
    for paragraph in paragraphs:
        urls = re.compile('href="(https?://[^<^\]^"]+)"').findall(paragraph)
#         match=re.compile('<a href="([^<]+)">htt').findall(link)
#     match = match1 + match
    print urls
    hostsmax = len(urls)
    h = 0
    from urlparse import urlparse
    for url in urls:
        h += 1
        percent = (h * 100)/hostsmax
        msg.update(percent,'Collecting hosts - ' + str(percent) + '%')
        if msg.iscanceled(): break
        if '1fichier' in url:
            host = '1fichier'
        else:
            host = urlparse(url).hostname.replace('www.','').partition('.')[0]
        hostname = host
        host = host.upper()
        if main.supportedHost(hostname):
            titles.append(host + ' [COLOR red]1080P[/COLOR]')
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
        
        infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre'], 'originaltitle': infoLabels['metaName']}
        if not video_type is 'episode': infoL['originalTitle']=main.removeColoredText(infoLabels['metaName'])
        # play with bookmark
        from resources.universal import playbackengine
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=str(infoLabels['title']),season=str(season), episode=str(episode), year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            from resources.universal import watchhistory
            wh = watchhistory.WatchHistory('plugin.video.movie25')
            wh.add_item(mname+' '+'[COLOR green]DL4Free[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=img, fanart=fanart, is_folder=False)
        player.KeepAlive()
        return ok
    except Exception, e:
        if stream_url != False:
            main.ErrorReport(e)
        return ok
