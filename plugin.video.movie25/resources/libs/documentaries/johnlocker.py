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
MAINURL='http://johnlocker.com'

def MAINJL():
        main.addDir('Search','extra',323,art+'/search.png')
        main.addDir('LATEST VIDEOS','http://johnlocker.com/home/main',319,art+'/johnlocker.png')
        main.addDir('MOST VIEWED','http://johnlocker.com/home/main',319,art+'/johnlocker.png')
        main.addDir('HIGHEST RATED','http://johnlocker.com/home/main',319,art+'/johnlocker.png')
        main.addDir('FEATURED','http://johnlocker.com/home/main',319,art+'/johnlocker.png')
        main.addDir('CATEGORIES','johnlocker',322,art+'/johnlocker.png')
        main.GA("Documentary","John Locker")

def CATJL():
    main.addDir('Conspiracy','http://johnlocker.com/component/seyret/category/videos/1',321,art+'/johnlocker.png')
    main.addDir('World History','http://johnlocker.com/component/seyret/category/videos/4',321,art+'/johnlocker.png')
    main.addDir('US History','http://johnlocker.com/component/seyret/category/videos/3',321,art+'/johnlocker.png')
    main.addDir('Music','http://johnlocker.com/component/seyret/category/videos/5',321,art+'/johnlocker.png')
    main.addDir('Nature','http://johnlocker.com/component/seyret/category/videos/6',321,art+'/johnlocker.png')
    main.addDir('Political','http://johnlocker.com/component/seyret/category/videos/7',321,art+'/johnlocker.png')
    main.addDir('Religon','http://johnlocker.com/component/seyret/category/videos/8',321,art+'/johnlocker.png')
    main.addDir('Science','http://johnlocker.com/component/seyret/category/videos/9',321,art+'/johnlocker.png')
    main.addDir('Society','http://johnlocker.com/component/seyret/category/videos/10',321,art+'/johnlocker.png')
    main.addDir('Sports','http://johnlocker.com/component/seyret/category/videos/14',321,art+'/johnlocker.png')
    main.addDir('War','http://johnlocker.com/component/seyret/category/videos/12',321,art+'/johnlocker.png')
    main.addDir('Weird','http://johnlocker.com/component/seyret/category/videos/13',321,art+'/johnlocker.png')

def SEARCHJL():
        keyb = xbmc.Keyboard('', 'Search John Locker')
        keyb.doModal()
        if (keyb.isConfirmed()):
            search = keyb.getText()
            encode=urllib.quote(search)
            surl='http://johnlocker.com/home/search/qs?qssearchkey='+encode+'&option=com_seyret&view=search&task=qs'
            LISTJL2('SEARCH',surl)

def LISTJL(mname,murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\xc2\xa0','')
        if mname=='LATEST VIDEOS' or 'lvpage' in murl:
            match=re.compile('<!-- START OF LATEST VIDEOS-->(.+?)<!-- END OF LATEST VIDEOS-->',re.DOTALL).findall(link)[0]
        if mname=='MOST VIEWED' or 'mvvpage' in murl:
            match=re.compile('<!-- START OF MOST VIEWED VIDEOS-->(.+?)<!-- END OF MOST VIEVED VIDEOS-->',re.DOTALL).findall(link)[0]
        if mname=='HIGHEST RATED' or 'hrvpage' in murl:
            match=re.compile('<!-- START OF HIGHEST RATED VIDEOS-->(.+?)<!-- END OF HIGHEST RATED VIDEOS-->',re.DOTALL).findall(link)[0]
        if mname=='FEATURED' or 'fvpage' in murl:
            match=re.compile('<!-- START OF FEATURED VIDEOS-->(.+?)<!-- END OF FEATURED VIDEOS-->',re.DOTALL).findall(link)[0]
            match2=re.compile('style="font-weight:bold;">([^<]+).+?<a href="([^<]+)"><img class=".+?" src="(.+?)" alt=(.+?)',re.DOTALL).findall(match)
        else:
            match2=re.compile('style="font-weight:bold;">([^<]+).+?<a href="([^<]+)"><img class=".+?" src="(.+?)" title="(.+?)"',re.DOTALL).findall(match)           
        for name,url,thumb,desc in match2:
            main.addPlayMs(name,url,320,thumb,desc,'','','','')
        paginate = re.compile('href="([^<]+)">Next</a>').findall(match)
        if len(paginate)>0:
                main.addDir('Next',MAINURL+paginate[0],319,art+'/next2.png')               
        main.GA("John Locker","List")
        
def LISTJL2(mname,murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\xc2\xa0','')
        if 'SEARCH' in mname or 'searchkey' in murl:
            match2=re.compile('style="font-weight:bold;">([^<]+).+?<a href="([^<]+)"><img class=".+?" src="(.+?)" alt=(.+?)',re.DOTALL).findall(link)
        else:
            match2=re.compile('style="font-weight:bold;">([^<]+).+?<a href="([^<]+)"><img class=".+?" src="(.+?)" title="(.+?)"',re.DOTALL).findall(link)
            if len(match2)==0:
                match2=re.compile('style="font-weight:bold;">([^<]+).+?<a href="([^<]+)"><img class=".+?" src="(.+?)" alt=(.+?)',re.DOTALL).findall(link)               
        for name,url,thumb,desc in match2:
            main.addPlayMs(name,url,320,thumb,desc,'','','','')
        paginate = re.compile('href="([^<]+)">Next</a>').findall(link)
        if len(paginate)>0:
                main.addDir('Next',MAINURL+paginate[0],321,art+'/next2.png')
        main.GA("John Locker","List")


def LINKJL(name,murl,thumb,desc):
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
        main.GA("John Locker","Watched")
        stream_url = False
        ok=True
        link=main.OPENURL(murl)
        try:
            match=re.compile("'file':               '(.+?)',",re.DOTALL).findall(link)[0]
            stream_url = main.resolve_url(match)
        except:xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Removed or Dead,3000)")
        
        try:
                    listitem = xbmcgui.ListItem(thumbnailImage=thumb)
                    listitem.setInfo('video', {'Title': name, 'Year': ''} )         
                
                    infoL={'Title': name, 'Plot': desc, 'Genre': ''}
                    # play with bookmark
                    player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=name,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
                    #WatchHistory
                    if selfAddon.getSetting("whistory") == "true":
                        wh.add_item(name+' '+'[COLOR green]John Locker[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infoL, img=thumb, fanart='', is_folder=False)
                    player.KeepAlive()
                    return ok
        except Exception, e:
                    if stream_url != False:
                        main.ErrorReport(e)
                    return ok
