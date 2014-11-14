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

def MAINOTV():
        main.addDir("A Dog's Life",'http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/g3Or2UhUY9_m/',361,art+'/myoutdoortv.png')
        main.addDir('Adirondack Trails','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/u4NgTD1BIE0x/',361,art+'/myoutdoortv.png')
        main.addDir('Alaskan Wilderness Family','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/VQLhXqAX3n1Z/',361,art+'/myoutdoortv.png')
        main.addDir('Arctic Cat Outdoors','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/c4kV9xKQW1sh/',361,art+'/myoutdoortv.png')
        main.addDir('Australian Fishing Championships','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/ycI5sgZ6vraB/',361,art+'/myoutdoortv.png')
        main.addDir("Babe Winkelman's Good Fishing",'http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/jXTpQeI9maTP/',361,art+'/myoutdoortv.png')
        main.addDir('Backwoods Life','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/pWbVbZjmjrtF/',361,art+'/myoutdoortv.png')
        main.addDir('Between the Banks','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/pssHGpIVQIQi/',361,art+'/myoutdoortv.png')
        main.addDir("Bob Redfern's Outdoor Magazine",'http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/r98R5jFbMLLf/',361,art+'/myoutdoortv.png')
        main.addDir("Cabela's Outfitter Journal",'http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/lA19UVpNoKoc/',361,art+'/myoutdoortv.png')
        main.addDir("Cabela's Memories in the Field",'http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/E4YINEMBEZQj/',361,art+'/myoutdoortv.png')
        main.addDir("Cabela's Ultimate Adventures",'http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/hSHZQg0y3uKU/',361,art+'/myoutdoortv.png')
        main.addDir('Ducks, Dogs, and Decoys','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/Cj6OKDHAxcY0/',361,art+'/myoutdoortv.png')
        main.addDir('Gator Trax Outdoors','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/kwQx53U1g0hn/',361,art+'/myoutdoortv.png')
        main.addDir('High Country TV','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/I47FGARbPisB/',361,art+'/myoutdoortv.png')
        main.addDir('Indiana Outdoor Adventures','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/dNQ5xo5icQRh/',361,art+'/myoutdoortv.png')
        main.addDir('Jeep Outdoors','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/zTwvm4Z7FVB3/',361,art+'/myoutdoortv.png')
        main.addDir("Jim Duckworth's Fishing Adventures",'http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/hjG3sk3KSMum/',361,art+'/myoutdoortv.png')
        main.addDir('Jimmy Houston Outdoors','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/Qd2SJ3VK9A4d/',361,art+'/myoutdoortv.png')
        main.addDir('Living on the Wildside','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/QZ29eDqzDFIj/',361,art+'/myoutdoortv.png')
        main.addDir('Living Outdoors','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/1mZrKxEl8mir/',361,art+'/myoutdoortv.png')
        main.addDir("Mike Avery's Outdoor Magazine",'http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/kK_0Xhn6jvLX/',361,art+'/myoutdoortv.png')
        main.addDir('National Wild Turkey Federation','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/EZ1uFBJ51WY2/',361,art+'/myoutdoortv.png')
        main.addDir('Remington Country TV','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/jTAbgblRwWHU/',361,art+'/myoutdoortv.png')
        main.addDir('Scott Martin Challenge','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/hnRmy8KPkZjL/',361,art+'/myoutdoortv.png')
        main.addDir('Shooting USA','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/zzBvTR8eH5a3/',361,art+'/myoutdoortv.png')
        main.addDir("Sportsman's Adventures",'http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/N_fzoOymr0Ud/',361,art+'/myoutdoortv.png')
        main.addDir('The Carolina Outdoorsman Show','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/sA2HrQEiQZZV/',361,art+'/myoutdoortv.png')
        main.addDir('Ultimate Catch','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/N58gKpiZKsOY/',361,art+'/myoutdoortv.png')

def OC():
        main.addDir('All Videos','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/swTdEQGW9CKd',51,art+'/OC.png')
        main.addDir('Hunting','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/swTdEQGW9CKd?byCategories=Outdoor%20Channel/Hunting',51,art+'/OC.png')
        main.addDir('Fishing','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/swTdEQGW9CKd?byCategories=Outdoor%20Channel/Fishing',51,art+'/OC.png')
        main.addDir('Shooting','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/swTdEQGW9CKd?byCategories=Outdoor%20Channel/Shooting',51,art+'/OC.png')
        main.addDir('Off Road','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/swTdEQGW9CKd?byCategories=Outdoor%20Channel/Off-Road',51,art+'/OC.png')
        main.addDir('Adventure','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/swTdEQGW9CKd?byCategories=Outdoor%20Channel/Adventure',51,art+'/OC.png')
        main.addDir('Conservation','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/swTdEQGW9CKd?byCategories=Outdoor%20Channel/Conservation',51,art+'/OC.png')
        main.GA("Sports","OutChannel")

def OCList(murl):
        link=main.OPENURL(murl)
        match=re.compile('<item>.+?<title>([^<]+)</title><description>(.+?)</description>.+?<plrelease:url>(.+?)</plrelease:url>.+?<plmedia:defaultThumbnailUrl>(.+?)</plmedia:defaultThumbnailUrl>',re.DOTALL).findall(link)
        for name,desc,url,thumb in match:
                main.addPlayMs(name,url,52,thumb,desc,'','','','')
        main.GA("Sports","OC-List")

def OTVList(murl):
        link=main.OPENURL(murl)
        match=re.compile('<item>.+?<title>([^<]+)</title><description>(.+?)</description>.+?url="(.+?)".+?<plmedia:defaultThumbnailUrl>(.+?)</plmedia:defaultThumbnailUrl>',re.DOTALL).findall(link)
        for name,desc,url,thumb in match:
                main.addPlayMs(name,url,52,thumb,desc,'','','','')
        main.GA("Sports","OC-List")

def OCLink(mname,url,thumb,desc):
        main.GA("OC-List","Watched")
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Opening Link,5000)")
        link=main.OPENURL(url)
        ok=True
        match=re.compile('<video src="(.+?)"',re.DOTALL).findall(link)
        for video in match[0:1]:
                print video
                if 'http' not  in video:
                        stream_url = 'http://media.outdoorchannel.com/'+video
                else:
                        stream_url = video
        infoL={ "Title": mname, "Plot": desc}
        # play with bookmark
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            wh.add_item(mname+' '+'[COLOR green]Outdoor[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
        player.KeepAlive()
        return ok
