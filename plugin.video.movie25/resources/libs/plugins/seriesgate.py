import urllib,re,string,urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art

def MAINSG():
        main.addDir('Search','sg',612,art+'/search.png')
        main.addDir('A-Z','http://seriesgate.tv/',610,art+'/az.png')
        main.addDir('Latest Episodes','http://seriesgate.me/latestepisodes/',602,art+'/latest.png')
        HOMESG()
        main.GA("Plugin","SeriesGate")
def HOMESG():
        url='http://seriesgate.tv/home1/'
        link=main.OPENURL(url)

        main.addLink('[COLOR red]Updated Tv Shows[/COLOR]','','')
        match=re.compile('href = "(.+?)" style=".+?"><img src="(.+?)"   width=".+?" height=".+?" alt="(.+?)" title = ".+?"').findall(link)
        for url,thumb,name in match[0:16]:
            main.addDirT(name,'http://seriesgate.me'+url,604,thumb,'','','','','')
        main.addLink('[COLOR red]TV SHOWS BEING WATCHED[/COLOR]','','')
        match=re.compile('href = "(.+?)" style=".+?"><img src="(.+?)"   width=".+?" height=".+?" alt="(.+?)" title = ".+?"').findall(link)
        for url,thumb,name in match[16:32]:
            main.addDirT(name,'http://seriesgate.me'+url,604,thumb,'','','','','')


            
def AtoZSG():
        main.addDir('0-9','numb',611,art+'/09.png')
        for i in string.ascii_uppercase:
                main.addDir(i,i,611,art+'/'+i.lower()+'.png')
        main.GA("SeriesGate","A-Z")
        main.VIEWSB()
        
def AllShows(murl):
        from t0mm0.common.net import Net as net
        sear = net().http_POST('http://seriesgate.tv/tvshows_ajax/', {'_number':murl,'_genre_':'', '_network_':'', '_rating_':''}).content
        match= re.compile('<a href = "(.+?)"><img src = "(.+?)" height=".+?/><div class = "_tvshow_title">(.+?)</div>').findall(sear)
        for url,thumb,name in match:
                main.addDirT(name,'http://seriesgate.me'+url,604,thumb,'','','','','')
                    

        main.GA("SeriesGate","AllShows")
def LISTEpiSG(murl):
    link=main.OPENURL(murl)
    match=re.compile('<a href="([^"]+?)"><div  class=".+?"><img class="lazy"   data-original="(.+?)" width=".+?" height=".+?"  alt=".+?" title = ".+?" /><div class=".+?"><a href=".+?">(.+?)</a> - (.+?)</span><div class=".+?"></div><span style=".+?">(.+?)</span>').findall(link)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Show list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
    for url,thumb,showname,seep,epiname in match:

        main.addPlayTE(showname.strip()+' '+seep.strip()+" "+'[COLOR blue]'+epiname+'[/COLOR]','http://seriesgate.me'+url+'searchresult/',609,thumb,'','','','','')
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if (dialogWait.iscanceled()):
                return False   
    dialogWait.close()
    del dialogWait
    main.GA("SeriesGate","Latest-list")
def LISTSeasonSG(mname,murl,thumb):
    link=main.OPENURL(murl).replace('April,','')
    match=re.compile('(?i)<li><a href="([^"]+?)">([^<]+?)</a>').findall(link)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Show list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
    for url, seaname in match:
        seaname = seaname.replace('&raquo','').strip()
        main.addPlayTE(mname+' '+seaname,'http://seriesgate.tv'+url+'more_sources/',609,str(thumb),'','','','','')
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if (dialogWait.iscanceled()):
                return False   
    dialogWait.close()
    del dialogWait
    main.GA("SeriesGate","Sea-list")
def LISTEpilistSG(mname,murl):
    link=main.OPENURL(murl)
    match=re.compile('<div class=".+?" style=".+?" >(.+?)- <span><a href = ".+?">.+?</a></span></div><div class=".+?" >(.+?)</div><div class = ".+?"></div><div style=".+?"><a href="(.+?)"><img src="(.+?)" width=".+?" height=".+?"  alt=".+?" title = "(.+?)" ></a>').findall(link)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Show list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
    for seep, airdate, url, thumb, epiname in match:
        durl = url+'searchresult/'
        mname=mname.split('Season')[0]
        main.addPlayTE(mname.strip()+" "+seep.strip()+" "+'[COLOR blue]'+epiname+'[/COLOR]',durl,609,thumb,'','','','','')
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if (dialogWait.iscanceled()):
                return False   
    dialogWait.close()
    del dialogWait
    main.GA("SeriesGate","Epi-list")
    if selfAddon.getSetting('auto-view') == 'true':
                xbmc.executebuiltin("Container.SetViewMode(%s)" % selfAddon.getSetting('episodes-view'))

def SearchhistorySG():
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryTv')
        if not os.path.exists(SeaFile):
            url='sg'
            SEARCHSG(url)
        else:
            main.addDir('Search','sg',608,art+'/search.png')
            main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
            thumb=art+'/link.png'
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                    url=seahis
                    seahis=seahis.replace('%20',' ')
                    main.addDir(seahis,url,608,thumb)
            
            


def SEARCHSG(murl):
    seapath=os.path.join(main.datapath,'Search')
    SeaFile=os.path.join(seapath,'SearchHistoryTv')
    try:
        os.makedirs(seapath)
    except:
        pass
    if murl == 'sg':
        keyb = xbmc.Keyboard('', 'Search For Shows or Episodes')
        keyb.doModal()
        if (keyb.isConfirmed()):
            search = keyb.getText()
            encode=urllib.quote(search)
            surl='http://seriesgate.tv/search/indv_episodes/'+encode+'/'
            if not os.path.exists(SeaFile) and encode != '':
                open(SeaFile,'w').write('search="%s",'%encode)
            else:
                if encode != '':
                    open(SeaFile,'a').write('search="%s",'%encode)
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                continue
            if len(searchis)>=10:
                searchis.remove(searchis[0])
                os.remove(SeaFile)
                for seahis in searchis:
                    try:
                        open(SeaFile,'a').write('search="%s",'%seahis)
                    except:
                        pass
    else:
        encode = murl
        surl='http://seriesgate.tv/search/indv_episodes/'+encode+'/'    
    link = main.OPENURL(surl)
    main.addLink('[COLOR red]Shows[/COLOR]','',art+'/link.png')
    match=re.compile('src = "([^<]+)" height=".+?" width=".+?" alt=""  /></a><div class = ".+?" style=".+?"><div class = ".+?"><a href = "([^<]+)">([^<]+)</a></div><a href = ".+?">').findall(link)
    for thumb,url,name in match:
            main.addDirT(name,'http://seriesgate.tv'+url,604,thumb,'','','','','')

    main.GA("SeriesGate","Search")


def GETLINKSG(murl):
    durl= 'http://seriesgate.tv'+murl
    link=main.OPENURL(durl)
    link=link.replace('var url = "http://cdn.seriesgate.tv','')
    match=re.compile('var url = "(.+?)";').findall(link)
    for url in match:
            return url

def VIDEOLINKSSG(mname,murl,thumb):
    main.GA("SG","Watched")
    msg = xbmcgui.DialogProgress()
    msg.create('Please Wait!','')
    msg.update(0,'Collecting hosts')
    sources = []
    ok=True
    infoLabels =main.GETMETAEpiT(mname,thumb,'')
    video_type='episode'
    season=infoLabels['season']
    episode=infoLabels['episode']
    link=main.OPENURL(murl)
    img=infoLabels['cover_url']
    fanart =infoLabels['backdrop_url']
    imdb_id=infoLabels['imdb_id']
    infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','')
    match=re.compile('href="([^"]+)"><img src=".+?" /><span class="link_name_tt">([^<]+)</span>').findall(link)
    hostsmax = len(match)
    h = 0
    import urlresolver
    for url, host in sorted(match):
            host=host.replace('Visit ','')
            h += 1
            percent = (h * 100)/hostsmax
            msg.update(percent,'Collecting hosts - ' + str(percent) + '%')
            if (msg.iscanceled()): break
            hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
            sources.append(hosted_media)                
    if (len(sources)==0):
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Show doesn't have playable links,5000)")
            return
    else:
            source = urlresolver.choose_source(sources)
    msg.close()
    try:
        if not source:
            main.CloseAllDialogs()
            return
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
        stream_url = main.resolve_url(source.get_url())
        if stream_url == False: return

        infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre']}
        # play with bookmark
        from resources.universal import playbackengine
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=str(infoLabels['title']),season=str(season), episode=str(episode), year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            from resources.universal import watchhistory
            wh = watchhistory.WatchHistory('plugin.video.movie25')
            wh.add_item(mname+' '+'[COLOR green]SeriesGate[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=img, fanart=fanart, is_folder=False)
        player.KeepAlive()
        return ok
    except Exception, e:
        if stream_url != False:
                main.ErrorReport(e)
        return ok
