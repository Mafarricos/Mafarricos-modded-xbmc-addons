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


def MAINDP():
        main.addDir('Search','extra',317,art+'/search.png')
        #main.addDir('A-Z','http://seriesgate.tv/',538,art+'/azex.png')
        main.addDir('Films','http://dpstreaming.org/category/films/',312,art+'/dpstreaming.png')
        main.addDir('Séries Tv','http://dpstreaming.org/category/series-tv/',312,art+'/dpstreaming.png')
        main.addDir('Mangas','http://dpstreaming.org/category/mangas/',312,art+'/dpstreaming.png')
        main.GA("INT","DpStreaming")

def SEARCHDP():
        keyb = xbmc.Keyboard('', 'Search Movies & Shows')
        keyb.doModal()
        if (keyb.isConfirmed()):
            search = keyb.getText()
            encode=urllib.quote(search)
            surl='http://dpstreaming.org/?s='+encode
            LISTDP(surl)
            
def LISTDP(murl):
        link=main.OPENURL2(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\xc2\xa0','')
        match=re.compile("""height=".+?" src="(.+?)".+?<h2><a href="(.+?)" rel=".+?" title=".+?">(.+?)</a></h2>""",re.DOTALL).findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for thumb,url, name in match:
                name=name.replace("<span style='color: #ff0000'>",'').replace('</span>','')
                if '/series-tv/' in murl or 'saison' in url:
                    main.addDirT(name,url,315,thumb,'','','','','')
                else:
                    main.addDirM(name,url,313,thumb,'','','','','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        paginate = re.compile("<a href='(.+?)' class='nextpostslink'>").findall(link)
        if len(paginate)>0 and len(match) == 12:
                main.addDir('Next',paginate[0],312,art+'/next2.png')
                
        main.GA("DpStreaming","List")

def LISTEPISODE(mname,murl):
        link=main.OPENURL2(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\xc2\xa0','')
        match=re.compile("""<p style="text-align: center;">([^<]+)<a (.+?)</p>""",re.DOTALL).findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for name,url in match:
                mname=mname.split('[')[0]
                mname=mname.replace('&-','').replace('-','').replace('Saison','Season')
                main.addDirTE(mname+''+name.replace('Épisode','Episode'),url,316,'','','','','','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait

def LINKLIST(mname,url):
    link=main.OPENURL2(url)
    link=link.replace('<iframe src="http://ads.affbuzzads.com','')
    link=main.unescapes(link)
    if selfAddon.getSetting("hide-download-instructions") != "true":
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
    match=re.compile('<iframe src="(.+?)" frameborder',re.DOTALL).findall(link)
    for url in match:
        hostn=re.compile("http://(.+?)/.+?").findall(url)
        for hname in hostn:
            host=hname.replace('www.','').replace('embed.','').replace('.es','').replace('.in','').replace('.sx','').replace('.net','').replace('.com','').replace('.to','').replace('.org','').replace('.ch','').replace('.eu','').replace('.ES','')
            host=host.split('.')[0]
        if main.supportedHost(host):
            mname=main.removeColoredText(mname)
            main.addDown2(mname+' [COLOR blue]'+host.upper()+' [/COLOR]',url,314,art+'/hosts/'+host.lower()+".png",art+'/hosts/'+host.lower()+".png") 


def LINKLIST2(mname,url):
    if selfAddon.getSetting("hide-download-instructions") != "true":
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
    match=re.compile('href="(.+?)" target="_blank">(.+?)</a>',re.DOTALL).findall(url)
    for url,host in match:
        if main.supportedHost(host):
            mname=main.removeColoredText(mname)
            main.addDown2(mname+' [COLOR blue]'+host.upper()+' [/COLOR]',url,314,art+'/hosts/'+host.lower()+".png",art+'/hosts/'+host.lower()+".png") 


def LINKDP(name,murl):
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
        main.GA("DpStreaming","Watched")
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
