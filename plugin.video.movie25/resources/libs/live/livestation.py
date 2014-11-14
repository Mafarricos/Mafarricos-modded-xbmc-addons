import urllib,urllib2,re,cookielib,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art
from resources.universal import watchhistory
    
wh = watchhistory.WatchHistory('plugin.video.movie25')

def LivestationList(murl):
        main.GA("Live","Livestation")
        link=main.OPENURL('http://www.livestation.com/en/channels')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('''<a href="([^"]+?)" class=".+?" data-action=".+?<img alt=".+?" itemprop=".+?" src="([^"]+?)" title="([^"]+?)" /></a>(.+?)<div id='channel_description'><p>([^<]+?)</p></div>''').findall(link)
        for url,thumb,name,data,desc in sorted(match):
                if 'language_selector' in url:
                        main.addPlayL(name,data,118,thumb,'','','','','',secName='Livestation News',secIcon=art+'/livestation.png')
                else:
                    url='http://www.livestation.com'+url
                    main.addPlayL(name,url,118,thumb,'','','','','',secName='Livestation News',secIcon=art+'/livestation.png')
                       
                       


def LivestationLink(mname,murl,thumb):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match= re.compile('ipadUrl: "([^"]+?)",').findall(link)
        if match:
                LivestationLink2(mname,match[0],thumb)
            
def LivestationLink2(mname,murl,thumb):
        main.GA("Livestation-"+mname,"Watched")
        ok=True
        namelist=[]
        urllist=[]
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        if 'class="ga_track"' in murl:                
                match= re.findall('<a href="([^"]+?)" class="ga_track" data-action="([^"]+?)"',murl)
                for url,name in match:
                        url='http://www.livestation.com'+url
                        namelist.append(name)
                        urllist.append(url)
                dialog = xbmcgui.Dialog()
                answer =dialog.select("Pick A Language", namelist)
                if answer != -1:
                        murl=urllist[int(answer)]
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match= re.compile('ipadUrl: "([^"]+?)",').findall(link)
        if match:
                stream_url =match[0].replace('b_,264,528,828,','b_528')
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Playing Link,1000)")
        
        listitem = xbmcgui.ListItem(thumbnailImage=thumb)
        infoL={'Title': mname, 'Genre': 'Live'} 
        from resources.universal import playbackengine
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='movie', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams='',imdb_id='')

        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
                wh.add_item(mname+' '+'[COLOR green]Livestation[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
        return ok
