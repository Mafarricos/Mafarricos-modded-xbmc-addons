# -*- coding: utf-8 -*-
import urllib,urllib2,re,cookielib,urlresolver,os,sys,string
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
MainUrl='http://www.viki.com'
def VIKIMAIN():
    main.GA("Plugin","Dramania")
    main.addDir('Search','viki',485,art+'/search.png')
    main.addDir('Movies','Movies',479,art+'/intl.png')
    main.addDir('Shows','dramania',479,art+'/intl.png')
    
def VIKICAT(murl):
    if murl == 'Movies':
        main.addDir('Popular Movies','http://www.viki.com/movies/browse?sort=viewed',483,art+'/intl.png')
        main.addDir('New Movies','http://www.viki.com/movies/browse?sort=latest',483,art+'/intl.png')
        main.addDir('By Genre','genre',484,art+'/intl.png')
        main.addDir('By Country','country',484,art+'/intl.png')
    else:
        main.addDir('Popular Shows','http://www.viki.com/tv/browse?sort=viewed',480,art+'/intl.png')
        main.addDir('New Shows','http://www.viki.com/tv/browse?sort=latest',480,art+'/intl.png')
        main.addDir('By Genre','genreT',484,art+'/intl.png')
        main.addDir('By Country','countryT',484,art+'/intl.png')
    main.GA("DIRINT","Viki")

def SEARCHVIKI():
        dialog = xbmcgui.Dialog()
        ret = dialog.select('[COLOR=FF67cc33][B]Choose A Search Type[/COLOR][/B]',['[B][COLOR=FF67cc33]TV Shows[/COLOR][/B]','[B][COLOR=FF67cc33]Movies[/COLOR][/B]'])
        if ret == -1:
            return
        if ret==0:
            keyb = xbmc.Keyboard('', 'Search For Shows')
        else:
            keyb = xbmc.Keyboard('', 'Search For Movies')
        keyb.doModal()
        if (keyb.isConfirmed()):
            search = keyb.getText()
            encode=urllib.quote(search)
            if ret==0:
                surl='http://www.viki.com/search?q='+encode+'&type=series'
            else:
                surl='http://www.viki.com/search?q='+encode+'&type=film'
            html = main.OPENURL(surl)
            link=main.unescapes(html).decode('ascii', 'ignore')
            match = re.findall('(?sim)class="thumbnail pull-left"><img alt=".+?src="([^"]+)".+?<a href="([^"]+)">([^<]+)</a>.+?<p>(.+?)...',link.replace('  ',''))
            for thumb,url,name,desc in match:
                fan=re.findall('(.+?jpg)',thumb)
                if fan:
                    fanart=fan[0]
                else:
                    fanart=''
                if ret==0:
                    main.addDirT(name,MainUrl+url,481,thumb,desc,fanart,'','','')
                else:
                    main.addPlayc(name,url,482,thumb,desc,fanart,'','','')

def VIKIGENREM(murl):
    if murl == 'genre':
        html = main.OPENURL('http://www.viki.com/movies/browse')
        link=main.unescapes(html).decode('ascii', 'ignore')
        match = re.findall('(?sim)<li title=""><a class="" href="(/movies/browse.?genre=[^"]+)">([^<]+)</a></li>',link.replace('  ',''))
        for url, name in match:
            main.addDir(name,MainUrl+url,483,art+'/dramania.png')
    elif murl == 'country':
        html = main.OPENURL('http://www.viki.com/movies/browse')
        link=main.unescapes(html).decode('ascii', 'ignore')
        match = re.findall('(?sim)<li title=""><a class="" href="(/movies/browse.?country=[^"]+)">([^<]+)</a></li>',link.replace('  ',''))
        for url, name in match:
            main.addDir(name,MainUrl+url,483,art+'/dramania.png')
    elif murl == 'genreT':
        html = main.OPENURL('http://www.viki.com/tv/browse')
        link=main.unescapes(html).decode('ascii', 'ignore')
        match = re.findall('(?sim)<li title=""><a class="" href="(/tv/browse.?genre=[^"]+)">([^<]+)</a></li>',link.replace('  ',''))
        for url, name in match:
            main.addDir(name,MainUrl+url,480,art+'/dramania.png')
    elif murl == 'countryT':
        html = main.OPENURL('http://www.viki.com/tv/browse')
        link=main.unescapes(html).decode('ascii', 'ignore')
        match = re.findall('(?sim)<li title=""><a class="" href="(/tv/browse.?country=[^"]+)">([^<]+)</a></li>',link.replace('  ',''))
        for url, name in match:
            main.addDir(name,MainUrl+url,480,art+'/dramania.png')
            

def LISTVIKIT(murl):
        html = main.OPENURL(murl)
        link=main.unescapes(html).decode('ascii', 'ignore')
        match = re.findall('(?sim)class="thumbnail pull-left"><img alt=".+?src="([^"]+)".+?<a href="([^"]+)">([^<]+)</a>.+?<p>(.+?)...',link.replace('  ',''))
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Shows loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for thumb,url,name,desc in match:
                fan=re.findall('(.+?jpg)',thumb)
                if fan:
                    fanart=fan[0]
                else:
                    fanart=''
                main.addDirT(name,MainUrl+url,481,thumb,desc,fanart,'','','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        paginate = re.compile("(?sim)<a class='page-link' rel='next' href='([^']+)'>Next &rarr;</a>").findall(link)
        if len(paginate)>0:
                main.addDir('[COLOR blue]Next Page >>>[/COLOR]',MainUrl+paginate[0],480,art+'/next2.png')
        main.GA("Viki","List")

def LISTVIKIM(murl):
        html = main.OPENURL(murl)
        link=main.unescapes(html).decode('ascii', 'ignore')
        match = re.findall('(?sim)class="thumbnail pull-left"><img alt=".+?src="([^"]+)".+?<a href="([^"]+)">([^<]+)</a>.+?<p>(.+?)...',link.replace('  ',''))
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for thumb,url,name,desc in match:
                fan=re.findall('(.+?jpg)',thumb)
                if fan:
                    fanart=fan[0]
                else:
                    fanart=''
                main.addPlayc(name,url,482,thumb,desc,fanart,'','','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        paginate = re.compile("(?sim)<a class='page-link' rel='next' href='([^']+)'>Next &rarr;</a>").findall(link)
        if len(paginate)>0:
                main.addDir('[COLOR blue]Next Page >>>[/COLOR]',MainUrl+paginate[0],483,art+'/next2.png')
        main.GA("Viki","List")

def LISTVIKIEPI(murl):
        html = main.OPENURL(murl)
        link=main.unescapes(html).decode('ascii', 'ignore')
        match = re.findall('(?sim) pull-left"><img alt=".+?data-real="([^"]+)".+?itemprop="name"><a href="([^"]+)">([^<]+)</a></h4>',link.replace('  ',''))
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for thumb,url,name in match:
                main.addPlayc(name,url,482,thumb,'','','','','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait

def LINKINT(mname,url,thumb):
        main.GA("Viki","Watched")
        ok=True
        id = re.findall("(?sim)/videos/(\d+v)",url)[0]
        link=main.OPENURL('http://www.viki.com/player5_fragment/'+id)
        try:
            stream_url = re.findall('(?sim)<source type="video/mp4" src="([^"]+)">',link)[0]
            subs = re.findall('(?sim)<track src="([^"]+)"',link)[0]
            infoL={'Title': mname, 'Plot': '', 'Genre':''}
            # play with bookmark
            player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
            player.setSubtitles(subs)
            #WatchHistory
            if selfAddon.getSetting("whistory") == "true":
                wh.add_item(mname+' '+'[COLOR green]Viki[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
            player.KeepAlive()
            return ok
        except Exception, e:
            if stream_url != False:
                main.ErrorReport(e)
            return ok
