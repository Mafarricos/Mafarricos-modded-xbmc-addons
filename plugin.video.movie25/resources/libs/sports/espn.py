import urllib,urllib2,re,cookielib,string, urlparse,os,sys
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

def ESPN():
        main.addDir('NFL','2459789',45,art+'/espn.png')
        main.addDir('NBA','2459788',45,art+'/espn.png')
        main.addDir('WNBA','3414465',45,art+'/espn.png')
        main.addDir('NCAA Basketball','2459792',45,art+'/espn.png')
        main.addDir('NCAA Football','2564308',45,art+'/espn.png')
        main.addDir('SOCCER','2731137',45,art+'/espn.png')
        main.addDir('TENNIS','2491545',45,art+'/espn.png')
        main.addDir('MLB','2521705',45,art+'/espn.png')
        main.addDir('MMA','2881270',45,art+'/espn.png')
        main.addDir('BOXING','2491554',45,art+'/espn.png')
        main.addDir('NHL','2459791',45,art+'/espn.png')
        main.addDir('GOLF','2630020',45,art+'/espn.png')
        main.addDir('NASCAR','2492290',45,art+'/espn.png')
        main.addDir('RACING','2755879',45,art+'/espn.png')
        main.addDir('OUTDOORS','2872804',45,art+'/espn.png')
        main.GA("Sports","ESPN")

def ESPNList(murl):
        
        if 'http://espn.go.com/video/' in murl:
                lurl=murl
                xurl=re.findall('(.+?)&pageNum=',murl)[0]
        else:
                lurl='http://espn.go.com/video/format/libraryPlaylist?categoryid='+murl
                xurl='http://espn.go.com/video/format/libraryPlaylist?categoryid='+murl
        link=main.OPENURL(lurl)
        match=re.compile('<a href="([^<]+)"><img src="(.+?)".+?></a><h5>(.+?)</h5>',re.DOTALL).findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Sports list is loaded.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Videos loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Loading....[/B]',remaining_display)
        for url,thumb,name in match:
                main.addPlayMs(name,url,46,thumb,'','','','','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Videos loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Loading....[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        match=re.compile('class="page-numbers">(\d+) of (\d+)</div>',re.DOTALL).findall(link)
        for p1,p2 in match:
                continue
        if p1 != p2:
                purl=xurl+ "&pageNum=" + str(int(p1)) + "&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index"
                main.addDir('[COLOR blue]Next[/COLOR]   Page '+p1+' of '+p2,purl,45,art+'/next2.png')
        main.GA("ESPN","ESPN-List")

def ESPNLink(mname,murl,thumb,desc):
        main.GA("ESPN-List","Watched")
        ok=True
        link=main.OPENURL(murl)
        match=re.compile('"thumbnailURL": "http://a.espncdn.com/combiner/i.?img=/media/motion(.+?).jpg',re.DOTALL).findall(link)[0]
        print match
        playpath = match + "_" + selfAddon.getSetting("espn-qua") + ".mp4"
	#url = 'rtmp://svod.espn.go.com/motion'
        stream_url = 'rtmp://svod.espn.go.com/motion'+playpath
        infoL={ "Title": mname, "Plot": desc}
        # play with bookmark
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            wh.add_item(mname+' '+'[COLOR green]Espn[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
        player.KeepAlive()
        return ok
