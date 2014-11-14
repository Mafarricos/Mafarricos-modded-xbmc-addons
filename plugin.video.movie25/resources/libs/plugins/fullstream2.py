#-*- coding: utf-8 -*-
import urllib,urllib2,re,cookielib,string, urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
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
        main.addDir('Search','extra',799,art+'/search.png')
        #main.addDir('A-Z','http://seriesgate.tv/',538,art+'/azex.png')
        main.addDir('Films','http://full-streaming.org/films/',795,art+'/dpstreaming.png')
        main.addDir('Films Genre','http://full-streaming.org/films/',800,art+'/dpstreaming.png')
        main.addDir('Films Qualité','http://full-streaming.org/films/',801,art+'/dpstreaming.png')
        main.addDir('Séries Tv','http://full-streaming.org/series/',795,art+'/dpstreaming.png')
        main.addDir('Séries Tv VF','http://full-streaming.org/series-fr/',795,art+'/dpstreaming.png')
        main.addDir('Séries Tv VOSTFR','http://full-streaming.org/series-vostfr/',795,art+'/dpstreaming.png')
        main.GA("INT","fullstream2")

def SEARCHFULLS():
        keyb = xbmc.Keyboard('', 'Search Movies & Shows')
        keyb.doModal()
        if (keyb.isConfirmed()):
            search = keyb.getText()
            encode=urllib.quote(search)
            surl='http://full-streaming.org/xfsearch/'+encode+'/'
            LISTFULLS(surl)
            
            
def GENRESFULLS():
		main.addDir('Action','http://full-streaming.org/action/',795,art+'/genre.png')
		main.addDir('Animation','http://full-streaming.org/animation/',795,art+'/genre.png')
		main.addDir('Arts Martiaux','http://full-streaming.org/arts-martiaux/',795,art+'/genre.png')
                main.addDir('Aventure','http://full-streaming.org/aventure/',795,art+'/genre.png')
                main.addDir('Biopic','http://full-streaming.org/biopic/',795,art+'/genre.png')
		main.addDir('Comedie','http://full-streaming.org/comedie/',795,art+'/genre.png')
		main.addDir('Comedie Dramatique','http://full-streaming.org/comedie-dramatique/',795,art+'/genre.png')
		main.addDir('Comedie Musicale','http://full-streaming.org/comedie-musicale/',795,art+'/genre.png')
                main.addDir('Documentaire','http://full-streaming.org/documentaire/',795,art+'/genre.png')        
		main.addDir('Drame','http://full-streaming.org/drame/',795,art+'/genre.png')
                main.addDir('Epouvante-horreur','http://full-streaming.org/epouvante-horreur/',795,art+'/genre.png')
                main.addDir('Erotique','http://full-streaming.org/erotique/',795,art+'/genre.png')
                main.addDir('Espionnage','http://full-streaming.org/espionnage/',795,art+'/genre.png')
                main.addDir('Famille','http://full-streaming.org/famille/',795,art+'/genre.png')
		main.addDir('Fantastique','http://full-streaming.org/fantastique/',795,art+'/genre.png')
		main.addDir('Guerre','http://full-streaming.org/guerre/',795,art+'/genre.png')
                main.addDir('Historique','http://full-streaming.org/historique/',795,art+'/genre.png')
                main.addDir('Musical','http://full-streaming.org/musical/',795,art+'/genre.png')
		main.addDir('Policier','http://full-streaming.org/policier/',795,art+'/genre.png')
                main.addDir('Peplum','http://full-streaming.org/peplum/',795,art+'/genre.png')
                main.addDir('Romance','http://full-streaming.org/romance/',795,art+'/genre.png')
                main.addDir('Science-Fiction','http://full-streaming.org/science-fiction/',795,art+'/genre.png')
                main.addDir('Spectacle','http://full-streaming.org/spectacle/',795,art+'/genre.png')
                main.addDir('Thriller','http://full-streaming.org/thriller/',795,art+'/genre.png')
                main.addDir('Western','http://full-streaming.org/western/',795,art+'/genre.png')
                main.addDir('Divers','http://full-streaming.org/divers/',795,art+'/genre.png')
                
def QLTFULLS():
		main.addDir('HD','http://full-streaming.org/hd/',795,art+'/genre.png')
		main.addDir('BdRip-DvdRip','http://full-streaming.org/bdrip-dvdrip/',795,art+'/genre.png')
		main.addDir('DvdScr-R5','http://full-streaming.org/dvdscr-r5/',795,art+'/genre.png')
                main.addDir('Ts-Cam','http://full-streaming.org/ts-cam/',795,art+'/genre.png')
            
def LISTFULLS(murl):
        link=main.OPENURL2(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('class="movie movie-block"><img src="([^<]+)" alt=".+?" title="([^<]+)"/>.+?<h2 onclick="window.location.href=\'([^<]+)\'">',re.DOTALL).findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for thumb,name,url in match:
                name=name.replace("<span style='color: #ff0000'>",'').replace('</span>','')
                if '/series-tv/' in murl or 'saison' in url:
                    main.addDirT(name,url,798,thumb,'','','','','')
                else:
                    main.addDirM(name,url,796,thumb,'','','','','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        paginate = re.compile('''<div class="navigation".+? <span.+? <a href="(.+?)">''').findall(link)
        if len(paginate)>0:
                main.addDir('[COLOR blue]Next Page >>>[/COLOR]',paginate[0],795,art+'/next2.png')
                
        main.GA("Fullstream2","List")

def LISTEPISODE(mname,url):
    link=main.OPENURL(url)
    link=link.replace('\r','').replace('\n','').replace('\t','')
    link=main.unescapes(link)
    if selfAddon.getSetting("hide-download-instructions") != "true":
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
    match=re.compile('<dd><a href="([^<]+)" class="zoombox.+?" title="([^<]+)">',re.DOTALL).findall(link)
    for url,name in match:
        hostn=re.compile("http://(.+?)/.+?").findall(url)
        for hname in hostn:
            host=hname.replace('www.','').replace('embed.','').replace('.es','').replace('.in','').replace('.sx','').replace('.net','').replace('.com','').replace('.to','').replace('.org','').replace('.ch','').replace('.eu','').replace('.ES','')
            host=host.split('.')[0]
        if main.supportedHost(host):
            mname=main.removeColoredText(mname)
            main.addDown2(name+' [COLOR blue]'+host.upper()+' [/COLOR]',url,797,art+'/hosts/'+host.lower()+".png",art+'/hosts/'+host.lower()+".png") 


def LINKLIST(mname,url):
    link=main.OPENURL(url)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('<iframe src="//www.facebook.com/plugins/likebox.php','').replace('<iframe src="http://creative.rev2pub.com','')
    link=main.unescapes(link)
    if selfAddon.getSetting("hide-download-instructions") != "true":
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
    match=re.compile('<center><iframe.+?src="(.+?)".+?',re.DOTALL | re.IGNORECASE).findall(link)
    #main.ErrorReport(match)
    for url in match:
        hostn=re.compile("http://(.+?)/.+?").findall(url)
        for hname in hostn:
            host=hname.replace('www.','').replace('embed.','').replace('.es','').replace('.in','').replace('.sx','').replace('.net','').replace('.com','').replace('.to','').replace('.org','').replace('.ch','').replace('.eu','').replace('.ES','')
            host=host.split('.')[0]
        if main.supportedHost(host):
            mname=main.removeColoredText(mname)
            main.addDown2(mname+' [COLOR blue]'+host.upper()+' [/COLOR]',url,797,art+'/hosts/'+host.lower()+".png",art+'/hosts/'+host.lower()+".png") 


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
