import urllib,re,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art

def LISTSP4(murl):
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Movie list is cached.')
    urllist=main.batchOPENURL(('http://oneclickmoviez.com/category/bluray/','http://oneclickmoviez.com/category/bluray/page/2/',
                               'http://oneclickmoviez.com/category/bluray/page/3/','http://oneclickmoviez.com/category/bluray/page/4/',
                               'http://oneclickmoviez.com/category/bluray/page/5/'))
    if urllist:
        match=re.compile('href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h2>\n</div>\n<div class="cover">\n<div class="entry">\n\t\t\t\t\t<p style="text-align: center;"><img class="alignnone" title="poster" src="(.+?)" ').findall(urllist)
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for url,name, thumb in match:
            main.addDirM(name,url,56,thumb,'','','','','')
            loadedLinks = loadedLinks + 1
            percent = (loadedLinks * 100)/totalLinks
            remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
            dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
            if (dialogWait.iscanceled()):
                return False    
    dialogWait.close()
    del dialogWait
    main.GA("HD","Oneclickmoviez")

def getlink(content):
    match=re.compile("Lbjs.TargetUrl = '([^']+?)'").findall(content)
    for url in match:
        return url
    return "rar"

def LINKSP4(mname,murl):
    html = main.OPENURL(murl)
    html = html.replace('href="http://oneclickmoviez.com/dws/MEGA','')
    if selfAddon.getSetting("hide-download-instructions") != "true":
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
    match=re.compile('<a rel="nofollow" href="([^"]+?)"[^>]*?>([^<]+?)</a>\s*?\(Single\)<',re.DOTALL).findall(html)
    if match:
        urls = []
        exlude = "(BAYFILES|RYUSHARE)"
        for url, host in match:
            if not re.search(exlude,host):
                urls.append(url)
        if urls:
            contents = main.batchOPENURL(urls, merge=False)
        i = 0
        for url, host in match:
            if not re.search('(?i)'+exlude,host):
                thumb = host.lower()
                thumb = thumb.replace('www.','').replace('.in','').replace('.net','').replace('.com','').replace('.to','').replace('.org','').replace('.ch','')
                vlink = getlink(contents[i])
                i += 1
                archive = re.compile('rar').findall(vlink)
                if not archive:
                    import urlresolver
                    hosted_media = urlresolver.HostedMediaFile(url=vlink, title=host)
                    match2=re.compile("{'url': '(.+?)', 'host': '(.+?)', 'media_id': '.+?'}").findall(str(hosted_media))
                    for murl,name in match2:
                            main.addDown2(mname+' [COLOR blue]'+host+'[/COLOR]',murl,211,art+'/hosts/'+thumb+".png",art+'/hosts/'+thumb+".png")
        
def LINKSP4B(mname,murl):
    main.GA("Oneclickmovies","Watched")
    ok=True
    infoLabels =main.GETMETAT(mname,'','','')
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
        infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre']}
        # play with bookmark
        from resources.universal import playbackengine
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=str(infoLabels['title']),season=str(season), episode=str(episode), year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            from resources.universal import watchhistory
            wh = watchhistory.WatchHistory('plugin.video.movie25')
            wh.add_item(mname+' '+'[COLOR green]OneclickMoviez[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=img, fanart=fanart, is_folder=False)
        player.KeepAlive()
        return ok
    except Exception, e:
        if stream_url != False:
                main.ErrorReport(e)
        return ok
