#-*- coding: utf-8 -*-
import urllib,re,string,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
prettyName = 'Catiii.tv'


def MAIN():
    main.addDir('Search','extra',438,art+'/search.png')
    main.addDir('South Korean','http://www.catiii.tv/category/watch-south-korean-movies-dramas-online/page/1/',435,art+'/catiii.png')
    main.addDir('Chinese','http://www.catiii.tv/category/watch-chinese-movies-dramas-online/page/1/',435,art+'/catiii.png')
    main.addDir('Japanese','http://www.catiii.tv/category/watch-japanese-movies-dramas-online/page/1/',435,art+'/catiii.png')
    main.addDir('Hongkong','http://www.catiii.tv/category/watch-hongkong-movies-dramas-online/page/1/',435,art+'/catiii.png')
    main.addDir('Thai','http://www.catiii.tv/category/other-countries/watch-thai-movies-dramas-online/page/1/',435,art+'/catiii.png')
    main.addDir('Taiwanese','http://www.catiii.tv/category/other-countries/watch-taiwanese-movies-dramas-online/page/1/',435,art+'/catiii.png')
    main.addDir('Filipino','http://www.catiii.tv/category/other-countries/watch-filipino-movies-dramas-online/page/1/',435,art+'/catiii.png')
    
    main.GA("INT",prettyName)


def LIST(murl):
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('  ','')
    match=re.compile('(?sim)<img src="([^"]+?)" alt="([^"]+?)" /></div>.+?<a href="([^"]+?)"><span>views</span>(.+?)</a>').findall(link)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Movie list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
    xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")
    for thumb,name,url,views in match:
        main.addPlayM(name+' [COLOR red]('+views+')[/COLOR]',url,436,thumb,'','','','','')
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if dialogWait.iscanceled(): break
    dialogWait.close()
    del dialogWait
    paginate = re.compile('Total Pages: (.+?)</li>',re.DOTALL).findall(link)
    if paginate:
        paginate=paginate[0]
        main.addDir('[COLOR red]Enter Page #[/COLOR]',murl,437,art+'/gotopage.png')
        page = re.compile('/page/(\d+)/',re.DOTALL).findall(murl)[0]
        nextpage=int(page)+1
        finalpage=re.sub('page/\d+?/', 'page/'+str(nextpage) + '/',murl)
        main.addDir('Page ' + str(page) + ' [COLOR blue]Next Page >>>[/COLOR]',finalpage,435,art+'/next2.png')     
    main.GA(prettyName,"List")
    main.VIEWS()


def SEARCH(encode):
    main.GA(prettyName,"Search")
    encode = main.updateSearchFile('','Movies',searchMsg='Search For Movies')
    if not encode: return False
    surl='http://www.catiii.tv/?s='+encode
    LIST(surl)

def GotoPage(url):
    link=main.OPENURL(url)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    r = re.compile('Total Pages: (.+?)</li>',re.DOTALL).findall(link)
    dialog = xbmcgui.Dialog()
    d = dialog.numeric(0, 'Section Last Page = '+r[0])
    if d:
        pagelimit=int(r[0])
        if int(d) <= pagelimit:
            encode=urllib.quote(d)
            surl=re.sub('page/\d+?/', 'page/'+str(encode) + '/',url)
            LIST(surl)
        else:
            dialog = xbmcgui.Dialog()
            ret = dialog.ok('Wrong Entry', 'The page number you entered does not exist.',' This sections page limit is '+str(pagelimit) )
    else:
        xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False)
        return False


def getlink(murl):
    if 'http' in murl:
        link=main.OPENURL(murl)
        key=re.findall('(?sim)vkey=(.+?)&',link)
        if key:
            murl=key[0]
    videurl='http://www.pinit.tv/player/vConfig_embed_new.php?vkey='+murl
    link=main.OPENURL(videurl)
    flv=re.findall('(?sim)<location>([^<]+?)</location>',link)
    srt=re.findall('(?sim)<jwplayer:captions.file>([^<]+?)</jwplayer:captions.file>',link)
    if srt:
        srt=srt[0]
    else:
        srt=''
    return flv[0],srt

def LINK(name,murl,thumb):
    xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,5000)")
    main.GA(prettyName,"Watched")
    stream_url = False
    ok=True
    infoLabels =main.GETMETAT(name,'','',thumb)
    video_type='movie'
    season=''
    episode=''
    img=infoLabels['cover_url']
    fanart =infoLabels['backdrop_url']
    imdb_id=infoLabels['imdb_id']
    infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }
    link=main.OPENURL(murl)
    
    keys=re.findall('(?sim)vkey=(.+?)&',link)
    
    if keys:
        vurl='http://www.pinit.tv/embedplayer.php?width=620&height=465&vkey='+keys[0]+'&autoplay=true&subtitles='
        link=main.OPENURL(vurl)
        key=re.findall('href="(rtmp://[^"]+?)">Play',link)
        stream_url = key[0]
        id=re.findall('rtmp://.+?/pinit/(\d+)_.+?.mp4',key[0])[0]
    else:
        urllist=[]
        epiList=[]
        match=re.findall('(?sim)<a href="([^"]+?)" target="_blank">([^<]+?)</a>',link)
        for url,epi in match:
            urllist.append(url)
            epiList.append(epi)
        dialog = xbmcgui.Dialog()
        ret = dialog.select('[COLOR=FF67cc33][B]Select Episode[/COLOR][/B]',epiList)
        if ret == -1:
            return
        link2=main.OPENURL(urllist[ret])
        key=re.findall('href="(rtmp[^"]+?)">Play',link2)
        
        stream_url = key[0]
        id=re.findall('rtmp://.+?/pinit/(\d+)_.+?.mp4',key[0])[0]
        name=epiList[ret]
    try:
        infoL={'Title': name, 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre'], 'originaltitle': infoLabels['metaName']}
        # play with bookmark
        from resources.universal import playbackengine
        if stream_url: main.CloseAllDialogs()
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=infoLabels['title'],season=season, episode=episode, year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
        player.setSubtitles('http://www.pinit.tv/subs/'+id+'.srt')
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            from resources.universal import watchhistory
            wh = watchhistory.WatchHistory(addon_id)
            wh.add_item(name+' '+'[COLOR green]'+prettyName+'[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=img, fanart='', is_folder=False)
        player.KeepAlive()
        return ok
    except Exception, e:
        if stream_url != False:
            main.ErrorReport(e)
        return ok
