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


def MAINVD():
        main.addDir('Search','extra',334,art+'/search.png')
        main.addDir('Vidéo à la une','http://video-documentaire.com/',332,art+'/feat.png')
        link=main.OPENURL('http://video-documentaire.com/')
        link=link.replace('\r','').replace('\n','').replace('\t','')
        match=re.compile('<a href="([^<]+)" >(.+?)</a>.+?<img.+?src="(.+?)"',re.DOTALL).findall(link)
        for url,name,thumb in match: 
            main.addDir(name,url,332,thumb)
        main.GA("Documentary","Video Documentaire")

def SEARCHVD():
        keyb = xbmc.Keyboard('', 'Search Video Documentaire')
        keyb.doModal()
        if (keyb.isConfirmed()):
            search = keyb.getText()
            encode=urllib.quote(search)
            surl='http://video-documentaire.com/videoscategory/animaux/?s='+encode+'&x=-1081&y=-167'
            link=main.OPENURL(surl)
            link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\xc2\xa0','')
            match=re.compile('<a class="widget-title" href="([^<]+)"><img src="(.+?)" alt="(.+?)" title=".+?<p>(.+?)</p>',re.DOTALL).findall(link)           
            for url,thumb,name,desc in match:
                main.addPlayMs(name,url,333,thumb,desc,'','','','')

def LISTVD(murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\xc2\xa0','')
        match=re.compile('<a class="video_thumb".+?src="(.+?)".+?<span class="time"> (.+?) </span>.+?<p class="title"><a href="([^<]+)" rel=".+?" title="([^<]+)">.+?<p>(.+?)</p>',re.DOTALL).findall(link)           
        for thumb,dur,url,name,desc in match:
            main.addPlayMs(name+' [COLOR red]('+dur+')[/COLOR]',url,333,thumb,desc,'','','','')
        paginate = re.compile('href="([^<]+)" >Next</a>',re.DOTALL).findall(link)
        if len(paginate)>0:
                main.addDir('Next',paginate[0],332,art+'/next2.png')               
        main.GA("Video Documentaire","List")


def LINKVD(name,murl,thumb):
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
        main.GA("Video Documentaire","Watched")
        stream_url = False
        ok=True
        link=main.OPENURL(murl)
        try:
            match=re.compile('''<iframe.+?src="(.+?)".+?</iframe>''',re.DOTALL).findall(link)[0]
            if 'http:' not in match:
                match='http:'+match
            stream_url = main.resolve_url(match.replace('?rel=0',''))
        except:xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Removed or Dead,3000)")
        
        try:
                    listitem = xbmcgui.ListItem(thumbnailImage=thumb)
                    listitem.setInfo('video', {'Title': name, 'Year': ''} )         
                
                    infoL={'Title': name, 'Plot': '', 'Genre': ''}
                    # play with bookmark
                    player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=name,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
                    #WatchHistory
                    if selfAddon.getSetting("whistory") == "true":
                        wh.add_item(name+' '+'[COLOR green]Video Documentaire[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infoL, img=thumb, fanart='', is_folder=False)
                    player.KeepAlive()
                    return ok
        except Exception, e:
                    if stream_url != False:
                        main.ErrorReport(e)
                    return ok
