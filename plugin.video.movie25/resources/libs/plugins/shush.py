#-*- coding: utf-8 -*-
import urllib,re,string,urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
prettyName = 'Shush'



def MAIN(murl):
    if 'TV' in murl:
        main.addDir('Movies','MOVIES',451,art+'/shush.png')
        link=main.OPENURL('http://www.shush.se/index.php?shows')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('&raquo;','')
        match=re.compile('(?sim)class="shows"><a href="([^"]+)"><img src="([^"]+)" alt="Watch (.+?) online').findall(link)
        for url,thumb,name in match:
            main.addDirT(name.title(),'http://www.shush.se/'+url,452,thumb,'','','','','')
    else:
        main.addDir('TV','TV',451,art+'/shush.png')
        link=main.OPENURL('http://www.shush.se/index.php?movies')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('&raquo;','')
        match=re.compile('(?sim)class="shows"><a href="([^"]+)"><img src="([^"]+)" alt="([^"]+)" title=').findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")
        for url,thumb,name in match:
            main.addPlayM(name.title(),'http://www.shush.se/'+url,453,thumb,'','','','','')
            loadedLinks = loadedLinks + 1
            percent = (loadedLinks * 100)/totalLinks
            remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
            dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
            if (dialogWait.iscanceled()):
                    return False   
        dialogWait.close()
        del dialogWait

def LIST(mname,murl,thumb):
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('&raquo;','')
    match=re.compile('(?sim)<a href="([^"]+)">([^<]+)</a><br').findall(link)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Show list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
    xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")
    for url,name in match:
        main.addPlayTE(name.replace(':',''),'http://www.shush.se/'+url,453,thumb,'','','','','')
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if (dialogWait.iscanceled()):
                return False   
    dialogWait.close()
    del dialogWait
        
def getLINK(code):
    from resources.universal import GKDecrypter
    import base64
    x = GKDecrypter.decrypter(198,128)# create the object
    return x.decrypt(code,base64.urlsafe_b64decode('djRBdVhhalplRm83akFNZ1VOWkI='),'ECB').split('\0')[0];
    
def LINK(mname,murl,thumb):
        main.GA(mname,"Watched")
        ok=True
        code=re.search('proxy.link=shush*(.+?)&logo',main.OPENURL(murl))
        murl=getLINK(code.group(1).replace('*',''))
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Opening Link,5000)")
        if re.findall('(.+?)\ss(\d+)e(\d+)\s',mname,re.I) or re.findall('Season(.+?)Episode([^<]+)',mname,re.I):
                infoLabels =main.GETMETAEpiT(mname,thumb,'')
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
        try:
            stream_url = main.resolve_url(murl)
            if stream_url == False:
                  return                                                            
            infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre'], 'originaltitle': infoLabels['metaName']}
            # play with bookmark
            stream_url=stream_url.replace(' ','%20')
            from resources.universal import playbackengine
            player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=str(infoLabels['title']),season=str(season), episode=str(episode), year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
            #WatchHistory
            if selfAddon.getSetting("whistory") == "true":
                from resources.universal import  watchhistory
                wh = watchhistory.WatchHistory('plugin.video.movie25')
                wh.add_item(mname+' '+'[COLOR green]Shush[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=img, fanart=fanart, is_folder=False)
            player.KeepAlive()
            return ok
        except Exception, e:
                if stream_url != False:
                        main.ErrorReport(e)
                return ok
