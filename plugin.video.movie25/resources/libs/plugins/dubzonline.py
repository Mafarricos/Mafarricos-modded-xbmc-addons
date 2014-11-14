import urllib,urllib2,re,cookielib,string, urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,urlresolver
from t0mm0.common.net import Net as net
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
from resources.universal import playbackengine, watchhistory
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art
    
wh = watchhistory.WatchHistory('plugin.video.movie25')

def MAINdz():
        main.GA("Plugin","dubzonline")
        main.addDir('A-Z','http://www.dubzonline.co/dubbed-anime/',614,art+'/AZ.png')
        main.addLink('[COLOR red]Recently Added Episodes[/COLOR]','year','')
        link=main.OPENURL('http://www.dubzonline.co/')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('<li><a href="/anime-list/" ><span>Anime List</span></a></li>','').replace('<li><a href="/contact-us/" ><span>Contact Us</span></a></li>','').replace('<li><a href="/" class="active"><span>Home</span></a></li>','')
        bits = re.compile('<h3 class="widget-title">Recently Added Episodes</h3>(.+?)</aside>').findall(link)
        match = re.compile('<li><a href="([^"]+)">([^<]+)</a></li>').findall(bits[0])
        for url,name in match:
                main.addPlayT(name,url,617,'','','','','','')

def latestLIST(murl):
        link=main.OPENURL('http://www.dubzonline.co/')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('<li><a href="/anime-list/" ><span>Anime List</span></a></li>','').replace('<li><a href="/contact-us/" ><span>Contact Us</span></a></li>','').replace('<li><a href="/" class="active"><span>Home</span></a></li>','')
        if murl=='lseries':
                match = re.compile('<li><a href="([^"]+)">(.+?)</a></li>').findall(link)
                for url, name in match:
                            main.addDir(name,'http://www.dubzonline.co/'+url,616,'')

        if murl=='lepi':
                match = re.compile('<li><a href="([^"]+)" title=".+?" >(.+?)</a> </li>').findall(link)
                for url, name in match:
                            main.addPlay(name,url,617,'')
       
def AtoZdz():
        main.addDir('0-9','http://www.dubzonline.co/dubbed-anime/',615,art+'/09.png')
        for i in string.ascii_uppercase:
            main.addDir(i,'http://www.dubzonline.co/dubbed-anime/',615,art+'/'+i.lower()+'.png')
        main.GA("Tvshows","A-ZTV")
        main.VIEWSB()

def AZLIST(mname,murl):
        link=main.OPENURL('http://www.dubzonline.co/dubbed-anime/')+main.OPENURL('http://www.dubzonline.co/dubbed-anime/')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match = re.compile('<li><a href="([^"]+)">(.+?)</a></li>').findall(link)
        for url, name in match:
            if name[0]==mname or name[0]==mname.lower():
                    main.addDirT(name,url,616,'','','','','','')

def EPILIST(murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        descs=re.compile('<img src=".+?" width=".+?" height=".+?" alt=".+?" align=".+?" style=".+?"/>(.+?)</p>').findall(link)
        if len(descs)>0:
                desc=descs[0]
        else:
                desc=''
        thumbs=re.compile('<img src="(.+?)" width=".+?" height=".+?" alt=".+?" align=".+?" style=".+?"/>').findall(link)
        if len(thumbs)>0:
                thumb=thumbs[0]
        else:
                thumb=''
        match = re.compile('href="([^<]+)" title="(.+?)">.+?</a></td>').findall(link)
        for url, name in match:
                    main.addPlayc(name,url,617,thumb,desc,'','','','')

def LINK(mname,murl):
        main.GA("dubzonline-"+mname,"Watched")
        sources = []
        ok=True

        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match = re.compile('''(?sim)Source.+?</b></span><iframe.+?src="(http://.+?)"''').findall(link)
        for url in match:
                match2=re.compile('http://(.+?)/.+?').findall(url)
                for host in match2:
                    host = host.replace('www.','')
                    if host =='firedrive.com' or host =='sockshare.com':
                                url=url.replace('embed','file')
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)      
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Show doesn't have playable links,5000)")
      
        else:
                source = urlresolver.choose_source(sources)
        try:
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                stream_url = main.resolve_url(source.get_url())
                if(stream_url == False):
                    return

                # play with bookmark
                player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img='',infolabels='', watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
                #WatchHistory
                if selfAddon.getSetting("whistory") == "true":
                    wh.add_item(mname+' '+'[COLOR green]Dubzonline[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img='', fanart='', is_folder=False)
                player.KeepAlive()
                return ok
        except Exception, e:
                if stream_url != False:
                        main.ErrorReport(e)
                return ok
