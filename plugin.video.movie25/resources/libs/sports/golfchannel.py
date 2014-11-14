import urllib,urllib2,re,sys
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



def MAIN():
        main.GA("Sports","GolfChannel")
        main.addDir('Full Episodes','http://www.golfchannel.com/tv/?WOtab=#watchOnlineTab',218,art+'/golfchannel.png')
        main.addDir('Featured Videos','http://www.golfchannel.com/search/?&q=&submitSearch=+&mediatype=Video',221,art+'/golfchannel.png')

def LIST(murl):
        main.GA("GolfChannel","List")
        link=main.OPENURL(murl)
        link=main.unescapes(link)
        match = re.compile('<div class="field-content"><a href=".+?"><img typeof="foaf:Image" src="([^<]+)" width=".+?" height=".+?" /></a></div>  </div>    <div class=".+?<a href=".+?">(.+?)</a></span>  </div>    <div class=".+?<div class="field-content">(.+?)</div>  </div>    <div class=".+?<li class="views-row views-row-1 views-row-odd views-row-first">(.+?)<div class="clearfix"></div>',re.DOTALL).findall(link)
        for thumb, name,desc,url in match:
            thumb=thumb.replace(' ','%20')
            main.addDirc(name,url,219,thumb,desc,'','','','')

def LIST3(murl):
        link=main.OPENURL(murl)
        link=main.unescapes(link)
        match = re.compile("""<a title="([^<]+)" target="" rel=".+? href="(.+?)"><img src=".+?onerror=".+?altVideoThumbnail.?this, '(.+?)'.?"></a>.+?<p class="ez-desc">(.+?)</p>""").findall(link)
        for name,url,thumb,desc in match:
            thumb=thumb.replace(' ','%20')
            main.addPlayMs(name,url,220,thumb,desc,'','','','')
        paginate = re.compile("""href="javascript:window.location='(.+?)';" class=".+?">Next</a><a title=".+?" rel=".+?" onclick=".+?""").findall(link)
        if len(paginate)>0:
            paginates=main.unescapes(paginate[0])
            main.addDir('Next',paginates,221,art+'/next2.png')

             


def LIST2(mname,murl,thumb,desc):
        main.GA("GolfChannel","List")
        match = re.compile('<a href="([^<]+)">([^<]+)</a>').findall(murl)
        for url,name in match:
            main.addPlayMs(mname+" [COLOR red]"+name+"[/COLOR]",'http://www.golfchannel.com'+url,220,thumb,'','','','','')


def LINK(mname,murl,thumb):
        
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Playing Video,4000)")
        ok= True
        link=main.OPENURL(murl)
        link=main.unescapes(link)
        r = re.findall('<iframe id="tp-global-player" src="(.+?)"',link)
        if r:
            print r
            try: 
                    link=main.OPENURL(r[0])
                    z = re.findall('tp:releaseUrl="(.+?)"',link)
                    link2=main.OPENURL(z[0])
                    link3=main.unescapes(link2)
                    try:
                            match = re.findall('<video src="(.+?)"',link3)
                            descs=re.findall('abstract="(.+?)"',link3)
                            if descs:
                                    desc=descs[0]
                            else:
                                    desc=''
                            vid=match[2]
                    except:
                            match = re.findall('<video src="(.+?)".+?title=.+?abstract="(.+?)"',link3)
                            for vurl,desc in match:
                                    vid=vurl
                    if 'flv' in vid:
                            vid='rtmp://cp74847.edgefcs.net/ondemand/'+vid
                    stream_url=vid
                    infoL={ "Title": mname, "Plot": desc}
                    # play with bookmark
                    player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
                    #WatchHistory
                    main.GA("GolfChannel","Watched")
                    if selfAddon.getSetting("whistory") == "true":
                        wh.add_item(mname+' '+'[COLOR green]GolfChannel[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
                    player.KeepAlive()
                    return ok
            except:
                    xbmc.executebuiltin("XBMC.Notification(Sorry!,No Link Found,3000)")
                    link3=''
            
        else:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,No Link Found,3000)")
        return ok
