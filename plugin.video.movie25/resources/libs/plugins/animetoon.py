# -*- coding: utf-8 -*-
import urllib,re,os,sys,json
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,time
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
smalllogo=art+'/smallicon.png'

def AZAT(sec):
    import string
    main.addDir('0-9','http://www.animetoon.tv/'+sec+'/others',376,art+'/09.png')
    for i in string.ascii_uppercase:
            main.addDir(i,'http://www.animetoon.tv/'+sec+'/'+i.lower(),376,art+'/'+i.lower()+'.png')
    main.GA("Watchseries","A-Z")
    main.VIEWSB()

def MAIN():
    main.GA("Plugin","Animania")
    main.addDir('Search','anime',385,art+'/search.png')
    main.addDir('Daily Releases','dramania',384,art+'/animetoon.png')
    main.addDir('Popular Dubbed Anime & Cartoon List','http://www.animetoon.tv/popular-list',376,art+'/animetoon.png')
    main.addDir('Dubbed Anime','dramania',375,art+'/animetoon.png')
    main.addDir('Cartoons','dramania',382,art+'/animetoon.png')
    main.addDir('Movies','dramania',380,art+'/animetoon.png')

def DUBBED():
    main.addDir('A-Z Dubbed Anime','alpha-dubbed-anime',383,art+'/animetoon.png')
    main.addDir('Popular Dubbed Anime','http://www.animetoon.tv/popular-dubbed-anime',376,art+'/animetoon.png')
    main.addDir('Newly Released Dubbed Anime','http://www.animetoon.tv/new-dubbed-anime',376,art+'/animetoon.png')
    main.addDir('Recently Added Dubbed Anime','',376,art+'/animetoon.png')
    main.addDir('Ongoing Dubbed Anime','http://www.animetoon.tv/ongoing-dubbed-anime',376,art+'/animetoon.png')
    main.addDir('Completed Dubbed Anime','http://www.animetoon.tv/completed-dubbed-anime',376,art+'/animetoon.png')
    main.addDir('Genre Dubbed Anime','dubbed-anime-genres',386,art+'/genre.png')

def MOVIES():
    main.addDir('A-Z Movies','alpha-movies',383,art+'/animetoon.png')
    main.addDir('Popular Movies','http://www.animetoon.tv/popular-movies',376,art+'/animetoon.png')
    main.addDir('Newly Released Movies','http://www.animetoon.tv/new-movies',376,art+'/animetoon.png')
    main.addDir('Recently Added Movies','http://www.animetoon.tv/recent-movies',376,art+'/animetoon.png')
    main.addDir('Genre Movies','movies-genres',386,art+'/genre.png')

def CARTOONS():
    main.addDir('A-Z Cartoon','alpha-cartoon',383,art+'/animetoon.png')
    main.addDir('Popular Cartoon','http://www.animetoon.tv/popular-cartoon',376,art+'/animetoon.png')
    main.addDir('Newly Released Cartoon','http://www.animetoon.tv/new-cartoon',376,art+'/animetoon.png')
    main.addDir('Recently Added Cartoon','http://www.animetoon.tv/recent-cartoon',376,art+'/animetoon.png')
    main.addDir('Ongoing Cartoon','http://www.animetoon.tv/ongoing-cartoon',376,art+'/animetoon.png')
    main.addDir('Completed Cartoon','http://www.animetoon.tv/completed-cartoon',376,art+'/animetoon.png')
    main.addDir('Genre Cartoon','cartoon-genres',386,art+'/genre.png')

def SEARCHAT():
        keyb = xbmc.Keyboard('', 'Search Movies & Series')
        keyb.doModal()
        if (keyb.isConfirmed()):
            search = keyb.getText()
            encode=urllib.quote(search)
            surl='http://www.animetoon.tv/toon/search?key='+encode
            LIST(surl)

def GENREAT(sec):
    link=main.OPENURL('http://www.animetoon.tv/'+sec, mobile=True)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','').replace('>Follow @GoGoAnime</a>','')
    match=re.compile('<tr><td><a href="(.+?)">(.+?)</a></td><td>(.+?)</td> </tr>',re.DOTALL).findall(link)
    for url,name,count in match:
        main.addDir(name+' [COLOR red]('+count+')[/COLOR]',url,376,art+'/genre.png')

def LISTPOP():
    link=main.OPENURL('http://www.animetoon.tv/updates', mobile=True)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','').replace('>Follow @GoGoAnime</a>','')
    match=re.compile('<tr><td><div><a href="(.+?)">(.+?)</a></div><ul>.+?</ul></td><td><img src="(.+?)" alt="(.+?)" /></td><td>(.+?)</td></tr>',re.DOTALL).findall(link)
    for url,name,thumb,type,date in match:
        if 'Movie' in type:
            main.addDirMs(name+' [COLOR red]('+date+')[/COLOR] [COLOR blue]'+type+'[/COLOR]',url,381,thumb,'','','','','')
        else:
            main.addDirMs(name+' [COLOR red]('+date+')[/COLOR] [COLOR blue]'+type+'[/COLOR]',url,377,thumb,'NA','','',thumb,'')

def LIST(murl):
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('&raquo;','').replace('&rarr;','').replace('  ','')
    match=re.compile("""<a href="([^<]+)"><img src="(.+?)".+?<h3><a href=".+?">(.+?)</a></h3><div><span class="type_indic">(.+?)</span>.+?<div class="descr">(.+?).?<a.+?Released:</span><span class="bold">(.+?)</span>.+?Rating:</span><span class="bold">(.+?)</span>""",re.DOTALL).findall(link)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Movie list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Movies/Shows Cached :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
    xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")
    for url,thumb,name,type,desc,year,rate in match:
        if 'Movie' in type:
            main.addDirMs(name+' [COLOR red]('+year+') [/COLOR][COLOR blue]'+rate+'[/COLOR] [COLOR tan]'+type+'[/COLOR]',url,381,thumb,desc,'','','','')
        else:
            main.addDirMs(name+' [COLOR red]('+year+') [/COLOR][COLOR blue]'+rate+'[/COLOR] [COLOR tan]'+type+'[/COLOR]',url,377,thumb,desc,'','',thumb,'')
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Movies/Episodes Cached :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if (dialogWait.iscanceled()):
            return False
    paginate = re.compile('''<a href="([^<]+)">Next</a>''').findall(link)
    if len(paginate)>0:
        main.addDir('Next',paginate[0],376,art+'/next2.png')   
    main.GA("Animania","List")

def GETMOVIE(mname,murl,thumb):
    link=main.OPENURL(murl, mobile=True)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','').replace('>Follow @GoGoAnime</a>','')
    match=re.compile('<h2>Videos:</h2><ul><li><a href="([^<]+)">.+?</a>',re.DOTALL).findall(link)
    LISTHOSTS(mname,match[0],thumb)

def LISTEPI(mname,murl,pic,desc,thumb):
    link=main.OPENURL(murl, mobile=True)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','').replace('>Follow @GoGoAnime</a>','')
    match=re.compile('<li><a href="([^<]+)">(.+?)</a>.+?<span class="right_text">(.+?)</span>',re.DOTALL).findall(link)
    for url,name,date in match:
        main.addDirMs(name+' [COLOR red]('+date+')[/COLOR]',url,378,thumb,desc,'','','','')
    paginate = re.compile('''<a href="([^<]+)">Next</a>''').findall(link)
    if len(paginate)>0:
        main.addDirc('Next',paginate[0],377,art+'/next2.png',desc,'','',thumb,'')

def LISTHOSTS(name,murl,thumb):
    name=main.removeColoredText(name)
    collect=[]
    videobug=[]
    yourupload=[]
    video44=[]
    play44=[]
    videoweed=[]
    cheesestream=[]
    videofun=[]
    byzoo=[]
    yucache=[]
    i=1
    j=1
    v=1
    p=1
    vw=1
    c=1
    vf=1
    b=1
    y=1

    link=main.OPENURL(murl).replace('\/','/').replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace(' class="selected"','').replace('&rarr;','')
    """parts=re.compile('<li><a href="(http://www.animetoon.tv/.+?/\d-\d+).+?>(Part.+?)</a>').findall(link)
    print len(parts)
    if part_pages:
        for url,pname in part_pages:
            match=re.compile('</ul></div><div><.+?src="(.+?)"').findall(main.OPENURL(url))
            for url in match:
                collect.append(url)"""
    try:
        count=1
        match=re.findall('<div><iframe src="(.+?)"',link,re.I)
        for url in match:
            parts=re.compile('<li><a href="http://www.animetoon.tv/.+?/'+str(count)+'-([^<]+)">Part(.+?)</a>').findall(link)
            if len(parts)>1:
                for item,num in parts:
                    furl=url.replace('part_1','part_'+str(item))
                    collect.append(furl)
            else:
                collect.append(url)
            count=count+1
    
    except: pass
    for links in collect:
        if 'byzoo' in links:
            main.addDown2(name+' [COLOR tan]Byzoo Part '+str(b)+'[/COLOR]',links,379,thumb,'')
            byzoo.append(('Part '+str(b),links))
            b=b+1
    if byzoo and len(byzoo)>1:
        main.addDown2(name+' [COLOR tan]Byzoo Play All[/COLOR]',str(byzoo),379,thumb,'')  
    for links in collect:
        if 'videobug' in links or 'easyvideo' in links:
            main.addDown2(name+' [COLOR blue]VideoBug Part '+str(i)+'[/COLOR]',links,379,thumb,'')
            videobug.append(('Part '+str(i),links))
            i=i+1
    if videobug and len(videobug)>1:
        main.addDown2(name+' [COLOR blue]VideoBug Play All[/COLOR]',str(videobug),379,thumb,'')  
    for links in collect:
        if 'yourupload' in links:
            main.addDown2(name+' [COLOR yellow]YourUpload Part '+str(j)+'[/COLOR]',links,379,thumb,'')
            yourupload.append(('Part '+str(j),links))
            j=j+1          
    if yourupload and len(yourupload)>1:
        main.addDown2(name+' [COLOR yellow]YourUpload Play All[/COLOR]',str(yourupload),379,thumb,'')
    for links in collect:
        if 'video44' in links or 'video66' in links:
            main.addDown2(name+' [COLOR red]Video44 Part '+str(v)+'[/COLOR]',links,379,thumb,'')
            video44.append(('Part '+str(v),links))
            v=v+1
    if video44 and len(video44)>1:
        main.addDown2(name+' [COLOR red]Video44 Play All[/COLOR]',str(video44),379,thumb,'')
    for links in collect:
        if 'play44' in links or 'play66' in links or 'playbb' in links:
            main.addDown2(name+' [COLOR green]Play44 Part '+str(p)+'[/COLOR]',links,379,thumb,'')
            play44.append(('Part '+str(p),links))
            p=p+1
    if play44 and len(play44)>1:
        main.addDown2(name+' [COLOR green]Play44 Play All[/COLOR]',str(play44),379,thumb,'')
    for links in collect:
        if 'videoweed' in links:
            main.addDown2(name+' [COLOR aqua]Videoweed Part '+str(vw)+'[/COLOR]',links,379,thumb,'')
            videoweed.append(('Part '+str(vw),links))
            vw=vw+1
    if videoweed and len(videoweed)>1:
        main.addDown2(name+' [COLOR aqua]Videoweed Play All[/COLOR]',str(videoweed),379,thumb,'')
    for links in collect:
        if 'cheesestream' in links:
            main.addDown2(name+' [COLOR purple]Cheesestream Part '+str(c)+'[/COLOR]',links,379,thumb,'')
            cheesestream.append(('Part '+str(c),links))
            c=c+1
    if cheesestream and len(cheesestream)>1:
        main.addDown2(name+' [COLOR purple]Cheesestream Play All[/COLOR]',str(cheesestream),379,thumb,'')
    for links in collect:
        if 'videofun' in links:
            main.addDown2(name+' [COLOR maroon]Videofun Part '+str(vf)+'[/COLOR]',links,379,thumb,'')
            videofun.append(('Part '+str(vf),links))
            vf=vf+1
    if videofun and len(videofun)>1:
        main.addDown2(name+' [COLOR maroon]Videofun Play All[/COLOR]',str(videofun),379,thumb,'')
    for links in collect:
        if 'yucache' in links:
            main.addDown2(name+' [COLOR maroon]Yucache Part '+str(y)+'[/COLOR]',links,379,thumb,'')
            yucache.append(('Part '+str(y),links))
            y=y+1
    if yucache:
        main.addDown2(name+' [COLOR maroon]Yucache Play All[/COLOR]',str(yucache),379,thumb,'')




def getLink(links):
        if 'byzoo' in links:
            link=main.OPENURL(links)
            try:match=re.compile("playlist:.+?url: '(.+?)',",re.DOTALL).findall(link)[0]
            except:match=re.compile('file: "(.+?)",',re.DOTALL).findall(link)[0]
            match=urllib.unquote_plus(match)
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
            try:match=re.compile("""'fit'},.+?{url: "([^<]+)", autoPlay""",re.DOTALL).findall(link)[0]
            except:pass
            match=urllib.unquote_plus(match)
        if 'yucache' in links:
            link=main.OPENURL(links)
            try:match=re.compile("""'<source src="([^"]+)" />';""",re.DOTALL).findall(link)[0]
            except:pass
            match=urllib.unquote_plus(match)
        return match

def PLAY(mname,murl,thumb):

        main.GA("Animania","Watched") 
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
