# -*- coding: utf-8 -*-
import urllib,re,os,sys,json
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,time
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
smalllogo=art+'/smallicon.png'


def MAIN():
    main.GA("Plugin","Dramania")
    main.addDir('Search','http://www.dubzonline.net/anime-list/',274,art+'/search.png')
    main.addDir('Movies','dramania',269,art+'/dramania.png')
    main.addDir('Dramas','dramania',273,art+'/dramania.png')

def MOVIES():
    main.addDir('All Movies','http://api.dramago.com/GetAllMovies',270,art+'/dramania.png')
    main.addDir('Popular Movies','http://api.dramago.com/GetPopularMovies',270,art+'/dramania.png')
    main.addDir('New Movies','http://api.dramago.com/GetNewMovies',270,art+'/dramania.png')

def DRAMAS():
    main.addDir('All Dramas','http://api.dramago.com/GetAllShows',270,art+'/dramania.png')
    main.addDir('Popular Dramas','http://api.dramago.com/GetPopularShows',270,art+'/dramania.png')
    main.addDir('New Dramas','http://api.dramago.com/GetNewShows',270,art+'/dramania.png')


def SEARCH():
    dialog = xbmcgui.Dialog()
    ret = dialog.select('[COLOR=FF67cc33][B]Choose A Search Type[/COLOR][/B]',['[B][COLOR=FF67cc33]TV Shows[/COLOR][/B]','[B][COLOR=FF67cc33]Movies[/COLOR][/B]'])
    if ret == -1:
        return
    if ret==0:
        murl='http://api.dramago.com/GetAllShows'
        keyb = xbmc.Keyboard('', 'Search For Shows')
    else:
        murl='http://api.dramago.com/GetAllMovies'
        keyb = xbmc.Keyboard('', 'Search For Movies')
    
    keyb.doModal()
    if (keyb.isConfirmed()):
            search = keyb.getText()
            encode=urllib.quote(search)
            link=main.OPENURL(murl)
            field=json.loads(link)
            for data in field:
                genre=str(data["genres"]).replace("u'",'').replace("'",'').replace("[",'').replace("]",'')
                if encode.lower()in(str(data["name"].encode('utf-8'))).lower():
                    if ret==0:
                        main.addDirT(str(data["name"].encode('utf-8'))+' [COLOR red]'+str(data["rating"])+'/10[/COLOR] [COLOR blue]'+str(data["released"])+'[/COLOR]','http://api.dramago.com/GetDetails/'+str(data["id"]),275,'http://www.dramago.com/images/series/big/'+str(data["id"])+'.jpg',str(data["description"].encode('utf-8')),'','',genre,'')
                    else:
                        main.addDirM(str(data["name"].encode('utf-8'))+' [COLOR red]'+str(data["rating"])+'/10[/COLOR] [COLOR blue]'+str(data["released"])+'[/COLOR]','http://api.dramago.com/GetDetails/'+str(data["id"]),271,'http://www.dramago.com/images/series/big/'+str(data["id"])+'.jpg',str(data["description"].encode('utf-8')),'','',genre,'')
    else:
        return
    main.GA("Dramania","Search")
                        
def LIST(murl):
    link=main.OPENURL(murl)
    field=json.loads(link)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Movie list is cached.')
    totalLinks = len(field)
    loadedLinks = 0
    remaining_display = 'Movies/Shows Cached :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
    xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")
    for data in field:
        genre=str(data["genres"]).replace("u'",'').replace("'",'').replace("[",'').replace("]",'')
        if 'Movies' in murl:
            try: desc=str(data["description"].encode('utf-8'))
            except: desc =' '
            main.addDirM(str(data["name"].encode('utf-8'))+' [COLOR red]'+str(round(data["rating"],2)).rstrip('0').rstrip('.')+'/10[/COLOR] [COLOR blue]'+str(data["released"])+'[/COLOR]','http://api.dramago.com/GetDetails/'+str(data["id"]),271,'http://www.dramago.com/images/series/big/'+str(data["id"])+'.jpg',desc,'','',genre,'')
        else:
            main.addDirT(str(data["name"].encode('utf-8'))+' [COLOR red]'+str(round(data["rating"],2)).rstrip('0').rstrip('.')+'/10[/COLOR] [COLOR blue]'+str(data["released"])+'[/COLOR]','http://api.dramago.com/GetDetails/'+str(data["id"]),275,'http://www.dramago.com/images/series/big/'+str(data["id"])+'.jpg',str(data["description"].encode('utf-8')),'','',genre,'')
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Movies/Episodes Cached :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if (dialogWait.iscanceled()):
            return False
    main.GA("Dramania","List")


def LISTEPISODES(name,murl,thumb):
    link=main.OPENURL(murl)
    match=re.findall('{"id":"(.+?)","name":"(.+?)","date":"(.+?)"}',link,re.DOTALL)  
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Movie list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Movies/Episodes Cached :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
    for id,name,date in match:
        main.addDirTE(name+' [COLOR red]'+date+'[/COLOR]',id,271,thumb,'','','','','')
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Movies/Episodes Cached :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if (dialogWait.iscanceled()):
            return False
    
def LISTHOSTS(name,murl,thumb):
    name=main.removeColoredText(name)
    videobug=[]
    yourupload=[]
    video44=[]
    play44=[]
    videoweed=[]
    cheesestream=[]
    videofun=[]
    yucache=[]
    i=1
    j=1
    v=1
    p=1
    vw=1
    c=1
    vf=1
    y=1
    if 'GetDetails' in murl:
        link=main.OPENURL(murl)
        idnum=re.findall('"id":"(.+?)"',link,re.DOTALL)[0]
    else:
        idnum=murl
    link=main.OPENURL('http://api.dramago.com/GetVideos/'+idnum).replace('\/','/')
    collect=re.findall('"(.+?)"',link,re.DOTALL)
    for links in collect:
        if 'videobug' in links or 'easyvideo' in links:
            main.addDown2(name+' [COLOR blue]VideoBug Part '+str(i)+'[/COLOR]',links,272,thumb,'')
            videobug.append(('Part '+str(i),links))
            i=i+1
    if videobug:
        main.addDown2(name+' [COLOR blue]VideoBug Play All[/COLOR]',str(videobug),272,thumb,'')  
    for links in collect:
        if 'yourupload' in links:
            main.addDown2(name+' [COLOR yellow]YourUpload Part '+str(j)+'[/COLOR]',links,272,thumb,'')
            yourupload.append(('Part '+str(j),links))
            j=j+1          
    if yourupload :
        main.addDown2(name+' [COLOR yellow]YourUpload Play All[/COLOR]',str(yourupload),272,thumb,'')
    for links in collect:
        if 'video44' in links or 'video66' in links:
            main.addDown2(name+' [COLOR red]Video44 Part '+str(v)+'[/COLOR]',links,272,thumb,'')
            video44.append(('Part '+str(v),links))
            v=v+1
    if video44:
        main.addDown2(name+' [COLOR red]Video44 Play All[/COLOR]',str(video44),272,thumb,'')
    for links in collect:
        if 'play44' in links or 'play66' in links or 'playbb' in links:
            main.addDown2(name+' [COLOR green]Play44 Part '+str(p)+'[/COLOR]',links,272,thumb,'')
            play44.append(('Part '+str(p),links))
            p=p+1
    if play44:
        main.addDown2(name+' [COLOR green]Play44 Play All[/COLOR]',str(play44),272,thumb,'')
    for links in collect:
        if 'videoweed' in links:
            main.addDown2(name+' [COLOR aqua]Videoweed Part '+str(vw)+'[/COLOR]',links,272,thumb,'')
            videoweed.append(('Part '+str(vw),links))
            vw=vw+1
    if videoweed:
        main.addDown2(name+' [COLOR aqua]Videoweed Play All[/COLOR]',str(videoweed),272,thumb,'')
    for links in collect:
        if 'cheesestream' in links:
            main.addDown2(name+' [COLOR purple]Cheesestream Part '+str(c)+'[/COLOR]',links,272,thumb,'')
            cheesestream.append(('Part '+str(c),links))
            c=c+1
    if cheesestream:
        main.addDown2(name+' [COLOR purple]Cheesestream Play All[/COLOR]',str(cheesestream),272,thumb,'')
    for links in collect:
        if 'videofun' in links:
            main.addDown2(name+' [COLOR maroon]Videofun Part '+str(vf)+'[/COLOR]',links,272,thumb,'')
            videofun.append(('Part '+str(vf),links))
            vf=vf+1
    if videofun:
        main.addDown2(name+' [COLOR maroon]Videofun Play All[/COLOR]',str(videofun),272,thumb,'')
    for links in collect:
        if 'yucache' in links:
            main.addDown2(name+' [COLOR maroon]Yucache Part '+str(y)+'[/COLOR]',links,272,thumb,'')
            yucache.append(('Part '+str(y),links))
            y=y+1
    if yucache:
        main.addDown2(name+' [COLOR maroon]Yucache Play All[/COLOR]',str(yucache),272,thumb,'')


def getLink(links):
        if 'videobug' in links or 'easyvideo' in links:
            link=main.OPENURL(links)
            try:match=re.compile("playlist:.+?url: '(.+?)',",re.DOTALL).findall(link)[0]
            except:match=re.compile('file: "(.+?)",',re.DOTALL).findall(link)[0]
            match=urllib.unquote_plus(match)
        if 'yourupload' in links:
            link=main.OPENURL(links)
            try:
                match=re.compile('<meta property="og.+?video" content="(.+?)"/>',re.DOTALL).findall(link)
                if len(match)!=0:
                    match=urllib.unquote_plus(match[0])
            except:pass
        if 'video44' in links or 'video66' in links:
            link=main.OPENURL(links)
            try:match=re.compile("playlist:.+?url: '(.+?)',",re.DOTALL).findall(link)[0]
            except:match=re.compile('file: "(.+?)"',re.DOTALL).findall(link)[0]
            match=urllib.unquote_plus(match)
        if 'play44' in links or 'play66' in links or 'playbb' in links:
            link=main.OPENURL(links)
            try:match=re.compile("playlist:.+?url: '(.+?)',",re.DOTALL).findall(link)[0]
            except:match=re.compile('file: "(.+?)"',re.DOTALL).findall(link)[0]
            match=urllib.unquote_plus(match)
        if 'videoweed' in links:
            try:stream_url = main.resolve_url(links)
            except:pass
            match=urllib.unquote_plus(stream_url)
        if 'cheesestream' in links:
            link=main.OPENURL(links)
            try:match=re.compile('<meta property="og:video" content="(.+?)"/>',re.DOTALL).findall(link)[0]
            except:pass
            match=urllib.unquote_plus(match)
        if 'videofun' in links:
            link=main.OPENURL(links)
            try:match=re.compile("""'fit'},.+?{url: "([^"]+)", autoPlay""",re.DOTALL).findall(link)[0]
            except:pass
            match=urllib.unquote_plus(match)
        if 'yucache' in links:
            link=main.OPENURL(links)
            try:match=re.compile("""'<source src="([^"]+)" />';""",re.DOTALL).findall(link)[0]
            except:pass
            match=urllib.unquote_plus(match)
        return match
    

def PLAY(mname,murl,thumb):

        main.GA("Dramania","Watched") 
        ok=True
        
        r = re.findall('(.+?)\ss(\d+)e(\d+)\s',mname,re.I)
        if r:
            infoLabels =main.GETMETAEpiT(mname,'','')
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
        try :
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre']}
                if not video_type is 'episode': infoL['originalTitle']=main.removeColoredText(infoLabels['metaName'])
                from resources.universal import playbackengine
                
                if "'," in murl:
                    mname=main.removeColoredText(mname)
                    pl=xbmc.PlayList(1);pl.clear()
                    playlist = sorted(list(set(eval(murl))), key=lambda playlist: playlist[0])
                    for xname,link in playlist:
                        pl.add(getLink(link),xbmcgui.ListItem(mname+' '+xname,thumbnailImage=img))
                    xbmc.Player().play(pl)
                    while xbmc.Player().isPlaying():
                        xbmc.sleep(2500)
                else:
                    stream_url = getLink(murl)
                    # play with bookmark
                    player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=infoLabels['title'],season=season, episode=episode, year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
                    #WatchHistory
                    if selfAddon.getSetting("whistory") == "true":
                        from resources.universal import watchhistory
                        wh = watchhistory.WatchHistory(addon_id)
                        wh.add_item(mname+' '+'[COLOR green]Dramania[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=infoLabels['cover_url'], fanart=infoLabels['backdrop_url'], is_folder=False)
                    player.KeepAlive()
                    return ok
        except Exception, e:
                if stream_url != False:
                        main.ErrorReport(e)
                return ok
