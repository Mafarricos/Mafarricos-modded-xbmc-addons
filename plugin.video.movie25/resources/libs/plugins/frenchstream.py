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



def MAINFS():
    main.addDir('Rechercher un film','extra',372,art+'/search.png')
    main.addDir('Nouveautes','http://frenchstream.org/',368,art+'/new.png')
    main.addDir('Les plus vues','http://frenchstream.org/les-plus-vus',368,art+'/view.png')
    main.addDir('Les plus commentés','http://frenchstream.org/les-plus-commentees',368,art+'/popu.png')
    main.addDir('Les mieux notés','http://frenchstream.org/',368,art+'/vote.png')
    main.addDir('Films Par Genre','http://frenchstream.org/films-par-genre',371,art+'/genre.png')
    main.GA("Plugin","SokroStream")

def GENREFS(murl):
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','')
    match=re.compile('<a title=".+?" href="(.+?)">(.+?)</a> <span class="mctagmap_count">(.+?)</span>',re.DOTALL).findall(link)
    for url,genre,count in match:
        main.addDir(genre+' '+count,url,368,art+'/genre.png')
            
def LISTFS(murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','')
        match=re.compile('class="moviefilm"><a href="([^<]+)">.+?<img src="(.+?)" alt="(.+?)" height=".+?<small>(.+?)</small>',re.DOTALL).findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for url,thumb,name,views in match:
                views=views.replace(' ',',').replace('Vues',' Vues')
                main.addDirM(name+' [COLOR red]'+views+'[/COLOR]',url,369,thumb,'','','','','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        #paginate = re.compile("<a href='([^<]+)' class='nextpostslink'>",re.DOTALL).findall(link)
        paginate = re.compile('''<a class="page larger" href="(.+?)">''').findall(link)
        if len(paginate)>0:
                main.addDir('Next',paginate[0],368,art+'/next2.png')     
        main.GA("SokroStream","List")


def SearchhistoryFS():
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistory25')
        if not os.path.exists(SeaFile):
            url='extra'
            SEARCHEXTRA(url)
        else:
            main.addDir('Search','extra',330,art+'/search.png')
            main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
            thumb=art+'/link.png'
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                    url=seahis
                    seahis=seahis.replace('%20',' ')
                    main.addDir(seahis,url,330,thumb)
            
            
        
def SEARCHFS(murl):
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistory25')
        try:
            os.makedirs(seapath)
        except:
            pass
        if murl == 'extra':
            keyb = xbmc.Keyboard('', 'Search Movies')
            keyb.doModal()
            if (keyb.isConfirmed()):
                    search = keyb.getText()
                    encode=urllib.quote(search)
                    surl='http://frenchstream.org/?s='+encode
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
                surl='http://frenchstream.org/?s='+encode
        link=main.OPENURL(surl)
        link=link.replace('\r','').replace('\n','').replace('\t','')
        match=re.compile('class="moviefilm"><a href="([^<]+)">.+?<img src="(.+?)" alt="(.+?)" height=".+?<small>(.+?)</small>',re.DOTALL).findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for url,thumb,name,views in match:
            views=views.replace(' ',',').replace('Vues',' Vues')
            main.addDirM(name+' [COLOR red]'+views+'[/COLOR]',url,369,thumb,'','','','','')
            loadedLinks = loadedLinks + 1
            percent = (loadedLinks * 100)/totalLinks
            remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
            dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
            if (dialogWait.iscanceled()):
                    return False   
        dialogWait.close()
        del dialogWait
        main.GA("SokroStream","Search")

def LINKLISTFS(mname,url):
    link=main.OPENURL(url)
    link=link.replace('\r','').replace('\n','').replace('\t','')
    if selfAddon.getSetting("hide-download-instructions") != "true":
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
    match=re.compile('<p><!--baslik:.+?--><br /><IFRAME SRC="(.+?)"',re.I).findall(link)
    if match:
        host=re.compile("http://(.+?)/.+?").findall(match[0])
        host=host[0].replace('www.','')
        host=host.split('.')[0]
        if 'mail.ru' in match[0]:
            host='mailru'
        if main.supportedHost(host):
            main.addDown2(mname+' [COLOR blue]'+host.upper()+' [/COLOR]',match[0],370,art+'/hosts/'+host.lower()+".png",art+'/hosts/'+host.lower()+".png")
    match=re.compile('<a href="([^<]+)"><span>(.+?)</span></a>',re.DOTALL).findall(link)
    for url,host in match:
        if main.supportedHost(host):
            main.addDown2(mname+' [COLOR blue]'+host.upper()+' [/COLOR]',url,370,art+'/hosts/'+host.lower()+".png",art+'/hosts/'+host.lower()+".png") 


def GetLink(url):
    link=main.OPENURL(url)
    link=link.replace('\r','').replace('\n','').replace('\t','')
    match=re.compile('<IFRAME SRC="([^"]+)"',re.I).findall(link)
    return match[0]

def LINKFS(name,murl):
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,5000)")
        main.GA("SokroStream","Watched")
        stream_url = False
        ok=True
        infoLabels =main.GETMETAT(name,'','','')
        video_type='movie'
        season=''
        episode=''
        img=infoLabels['cover_url']
        fanart =infoLabels['backdrop_url']
        imdb_id=infoLabels['imdb_id']
        infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }  
        if 'frenchstream'in murl:
            murl=GetLink(murl)
        stream_url = main.resolve_url(murl)
        print stream_url
        try:
                    listitem = xbmcgui.ListItem(thumbnailImage=img)
                    listitem.setInfo('video', {'Title': name, 'Year': ''} )         
                
                    infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre']}
                    # play with bookmark
                    player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=infoLabels['title'],season=season, episode=episode, year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
                    #WatchHistory
                    if selfAddon.getSetting("whistory") == "true":
                        wh.add_item(name+' '+'[COLOR green]SokroStream[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=img, fanart='', is_folder=False)
                    player.KeepAlive()
                    return ok
        except Exception, e:
                    if stream_url != False:
                        main.ErrorReport(e)
                    return ok
