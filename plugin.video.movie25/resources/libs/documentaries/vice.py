import urllib,urllib2,re,cookielib,string, urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,urlresolver
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art   




def Vice(murl):
    main.GA("Documentary","Vice")
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.compile('<a class=".+?" href="(.+?)"><img width=".+?" height=".+?" src="(.+?)" /></a>    <h2><a href=".+?">(.+?)</a></h2>    <p>(.+?)</p>').findall(link)
    for url,thumb,name,desc in match:
        url='http://www.vice.com'+url
        main.addDirc(name,url,105,thumb,desc,'','','','')

def ViceList(murl):
    main.GA("Vice","Vice-list")
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','')
    match=re.compile('''<a data-id=".+?" href="([^"]+)" onClick=".+?"><div class="media"><img src="(.+?)" alt="">.+?</p><h3>(.+?)</h3>''').findall(link)
    for url,thumb,name in match:
        url='http://www.vice.com'+url
        main.addPlayMs(name,url,106,thumb,'','','','','')

def ViceLink(mname,murl,thumb2):
    main.GA("Vice","Watched")
    xbmc.executebuiltin("XBMC.Notification(Please Wait!,Playing Link,5000)")
    link=main.OPENURL(murl)
    ok=True
    desci=re.compile('<meta name="description" content="(.+?)" />').findall(link)
    if len(desci)>0:
        desc=desci[0]
    else:
        desc=''
    thumbi=re.compile('<meta property="og:image" content="(.+?)" />').findall(link)
    if len(thumbi)>0:
        thumb=thumbi[0]
    else:
        thumb=''
    match=re.compile('content="http://player.ooyala.com/player.swf.?embedCode=(.+?)&').findall(link)
    if len(match)>0:

        durl='http://player.ooyala.com/player/ipad/'+match[0]+'.m3u8'
        link2=main.OPENURL(durl)
        match=re.compile('http://(.+?).m3u8').findall(link2)
        for n in match:
            print n
        if len(match)==0:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Played,5000)")
        else:
            if selfAddon.getSetting("vice-qua") == "0":
                try:
                    stream_url = 'http://'+match[4]+'.m3u8'
                except:
                    stream_url = 'http://'+match[3]+'.m3u8'
            elif selfAddon.getSetting("vice-qua") == "1":
                try:
                    stream_url = 'http://'+match[1]+'.m3u8'
                except:
                    stream_url = 'http://'+match[3]+'.m3u8'
            else:
                    stream_url = durl
                
            infoL={ "Title": mname, "Plot": desc}
            # play with bookmark
            from resources.universal import playbackengine, watchhistory
            wh = watchhistory.WatchHistory('plugin.video.movie25')
            player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
            #WatchHistory
            if selfAddon.getSetting("whistory") == "true":
                wh.add_item(mname+' '+'[COLOR green]Vice[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
            player.KeepAlive()
            return ok
    
    match2=re.compile('content="http://www.youtube.com/v/(.+?)" />').findall(link)
    if len(match2)>0:
        url='http://www.youtube.com/watch?v='+match2[0]
        
        listitem = xbmcgui.ListItem(mname)
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
        stream_url = main.resolve_url(str(url))
        if(stream_url == False):
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
            return
        
        # play with bookmark
        from resources.universal import playbackengine, watchhistory
        wh = watchhistory.WatchHistory('plugin.video.movie25')
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels='', watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            wh.add_item(mname+' '+'[COLOR green]Vice[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb2, fanart='', is_folder=False)
        player.KeepAlive()
        return ok
