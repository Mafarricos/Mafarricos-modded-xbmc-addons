#-*- coding: utf-8 -*-
import urllib,urllib2,re,cookielib,string, urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,urlresolver
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
from resources.universal import playbackengine, watchhistory
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art
wh = watchhistory.WatchHistory('plugin.video.movie25')


def MAINFULLS():
        main.addDir('Search','extra',792,art+'/search.png')
        #main.addDir('A-Z','http://seriesgate.tv/',538,art+'/azex.png')
        main.addDir('Films','http://full-stream.net/films-en-vk-streaming/',787,art+'/dpstreaming.png')
        main.addDir('Films Genre','http://full-stream.net/films-en-vk-streaming/',793,art+'/dpstreaming.png')
        main.addDir('Séries Tv','http://full-stream.net/seriestv/',787,art+'/dpstreaming.png')
        main.addDir('Séries Tv VF','http://full-stream.net/seriestv/vf/',787,art+'/dpstreaming.png')
        main.addDir('Séries Tv VOSTFR','http://full-stream.net/seriestv/vostfr/',787,art+'/dpstreaming.png')
        main.GA("INT","fullstream")

def SEARCHFULLS():
        keyb = xbmc.Keyboard('', 'Search Movies & Shows')
        keyb.doModal()
        if (keyb.isConfirmed()):
            search = keyb.getText()
            encode=urllib.quote(search)
            surl='http://full-stream.net/?s='+encode
            LISTDP(surl)
            
def GENRESFULLS():
		main.addDir('HD/HQ','http://full-stream.net/films-en-vk-streaming/haute-qualite/',787,art+'/genre.png')
		main.addDir('Action','http://full-stream.net/films-en-vk-streaming/action/',787,art+'/genre.png')
		main.addDir('Aventure','http://full-stream.net/films-en-vk-streaming/aventure/',787,art+'/genre.png')
		main.addDir('Animation','http://full-stream.net/films-en-vk-streaming/animation/',787,art+'/genre.png')
		main.addDir('Arts Martiaux','http://full-stream.net/films-en-vk-streaming/arts-martiaux/',787,art+'/genre.png')
		main.addDir('Biopic','http://full-stream.net/films-en-vk-streaming/biopic/',787,art+'/genre.png')
		main.addDir('Comedie','http://full-stream.net/films-en-vk-streaming/comedie/',787,art+'/genre.png')
		main.addDir('Comedie Dramatique','http://full-stream.net/films-en-vk-streaming/comedie-dramatique/',787,art+'/genre.png')
		main.addDir('Comedie Musicale','http://full-stream.net/films-en-vk-streaming/comedie-musicale/',787,art+'/genre.png')
		main.addDir('Drame','http://full-stream.net/films-en-vk-streaming/drame/',787,art+'/genre.png')
		main.addDir('Documentaire','http://full-stream.net/films-en-vk-streaming/documentaire/',787,art+'/genre.png')
		main.addDir('Horreur','http://full-stream.net/films-en-vk-streaming/horreur/',787,art+'/genre.png')
		main.addDir('Fantastique','http://full-stream.net/films-en-vk-streaming/fantastique/',787,art+'/genre.png')
		main.addDir('Guerre','http://full-stream.net/films-en-vk-streaming/guerre/',787,art+'/genre.png')
		main.addDir('Policier','http://full-stream.net/films-en-vk-streaming/policier/',787,art+'/genre.png')
            
def LISTFULLS(murl):
        link=main.OPENURL2(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('full-stream-view-hover"><img src="(.+?)" alt="(.+?)".+?<h2><a href="(.+?)">.+?</a></h2>',re.DOTALL).findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for thumb,name,url in match:
                name=name.replace("<span style='color: #ff0000'>",'').replace('</span>','')
                if '/series-tv/' in murl or 'saison' in url:
                    main.addDirT(name,url,790,thumb,'','','','','')
                else:
                    main.addDirM(name,url,788,thumb,'','','','','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        paginate = re.compile('''<div class="navigation".+? <span.+? <a href="(.+?)">''').findall(link)
        #xbmc.log(msg='-------------------'+str(match)+str(len(paginate)), level=xbmc.LOGDEBUG)
        if len(paginate)>0:
                main.addDir('Next',paginate[0],787,art+'/next2.png')
                
        main.GA("Fullstream","List")

def LISTEPISODE(mname,url):
    link=main.OPENURL(url)
    link=link.replace('\r','').replace('\n','').replace('\t','')
    link=main.unescapes(link)
    if selfAddon.getSetting("hide-download-instructions") != "true":
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
    match=re.compile('<a href="([^<]+)" title="([^<]+)" target=".+?" class="ilink sinactive">',re.DOTALL).findall(link)
    for url,name in match:
        hostn=re.compile("http://(.+?)/.+?").findall(url)
        xbmc.log(msg='-------------------'+str(hostn), level=xbmc.LOGDEBUG)
        for hname in hostn:
            host=hname.replace('www.','').replace('embed.','').replace('.es','').replace('.in','').replace('.sx','').replace('.net','').replace('.com','').replace('.to','').replace('.org','').replace('.ch','').replace('.eu','').replace('.ES','')
            host=host.split('.')[0]
        if main.supportedHost(host):
            mname=main.removeColoredText(mname)
            main.addDown2(name+' [COLOR blue]'+host.upper()+' [/COLOR]',url,789,art+'/hosts/'+host.lower()+".png",art+'/hosts/'+host.lower()+".png") 


def LINKLIST(mname,url):
    link=main.OPENURL(url)
    link=link.replace('\r','').replace('\n','').replace('\t','')
    link=main.unescapes(link)
    if selfAddon.getSetting("hide-download-instructions") != "true":
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
    match=re.compile('<iframe src="(.+?)"',re.DOTALL).findall(link)
    #xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving"+str(match)+" Link)")
    #xbmc.log(msg='-------------------'+str(match)+str(len(match)), level=xbmc.LOGDEBUG)
    for url in match:
        hostn=re.compile("http://(.+?)/.+?").findall(url)
        for hname in hostn:
            host=hname.replace('www.','').replace('embed.','').replace('.es','').replace('.in','').replace('.sx','').replace('.net','').replace('.com','').replace('.to','').replace('.org','').replace('.ch','').replace('.eu','').replace('.ES','')
            host=host.split('.')[0]
        #if main.supportedHost(host):
            mname=main.removeColoredText(mname)
            main.addDown2(mname+' [COLOR blue]'+host.upper()+' [/COLOR]',url,789,art+'/hosts/'+host.lower()+".png",art+'/hosts/'+host.lower()+".png") 


def LINKLIST2(mname,url):
    if selfAddon.getSetting("hide-download-instructions") != "true":
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
    match=re.compile('href="(.+?)" target="_blank">(.+?)</a>',re.DOTALL).findall(url)
    for url,host in match:
        if main.supportedHost(host):
            mname=main.removeColoredText(mname)
            main.addDown2(mname+' [COLOR blue]'+host.upper()+' [/COLOR]',url,789,art+'/hosts/'+host.lower()+".png",art+'/hosts/'+host.lower()+".png") 


def LINKFULLS(name,murl):
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
        main.GA("fullstream","Watched")
        stream_url = False
        ok=True
        r = re.findall('Season(.+?)Episode([^<]+)',name)
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
        stream_url = main.resolve_url(murl)
        try:
                    listitem = xbmcgui.ListItem(thumbnailImage=img)
                    listitem.setInfo('video', {'Title': name, 'Year': ''} )         
                
                    infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre']}
                    # play with bookmark
                    player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=infoLabels['title'],season=season, episode=episode, year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
                    #WatchHistory
                    if selfAddon.getSetting("whistory") == "true":
                        wh.add_item(name+' '+'[COLOR green]Peliculaspepito[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=img, fanart='', is_folder=False)
                    player.KeepAlive()
                    return ok
        except Exception, e:
                    if stream_url != False:
                        main.ErrorReport(e)
                    return ok
