import urllib,urllib2,re,cookielib,urlresolver,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
from resources.universal import playbackengine, watchhistory
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art
    
wh = watchhistory.WatchHistory('plugin.video.movie25')
def YOUKIDS():
    main.addDir('Sesame Street','sesamestreet',47,art+'/youkids.png')
    main.addDir('Yo Gabba Gabba!','yogabbagabba',47,art+'/youkids.png')
    main.addDir('Baby Tv','BabyTVChannel',47,art+'/youkids.png')
    main.addDir('Houston Zoo','houstonzoo',47,art+'/youkids.png')
    main.addDir('Simple Kids Crafts','simplekidscrafts',47,art+'/youkids.png')
    main.addDir('Cartoon Network','cartoonnetwork',47,art+'/youkids.png')
    main.addDir('Muppets Studio','MuppetsStudio',47,art+'/youkids.png')
    main.addDir('Word World PBS','WordWorldPBS',47,art+'/youkids.png')
    main.addDir('Big Red Hat Kids','bigredhatkids',47,art+'/youkids.png')
    main.addDir('Baby Einstein','TerrapinStation5',47,art+'/youkids.png')
    main.addDir('Activity Village','activityv',47,art+'/youkids.png')
    main.addDir('Hoopla Kids','hooplakidz',47,art+'/youkids.png')
    main.addDir('4KidsTV','4KidsTV',47,art+'/youkids.png')
    main.addDir('School House Rock Kids','MrRiggyRiggs',47,art+'/youkids.png')
    main.addDir('Arthur','MsArthurTV',47,art+'/youkids.png')
    main.addDir('POCOYO','pocoyotv',47,art+'/youkids.png')
    main.addDir('Disney jr','disneyjunior',47,art+'/youkids.png')
    main.addDir('Mickey Mouse','MickeyMouseCartoon',47,art+'/youkids.png')
    main.addDir('Tom and Jerry','TheTomEJerryShow',47,art+'/youkids.png')
    main.addDir('Dora','TheDoraTheExplorerHD',47,art+'/youkids.png')
    main.addDir('SpongeBob','Spongebob4Children',47,art+'/youkids.png')
    main.addDir('Curious George','ngk',47,art+'/youkids.png')
    main.addDir('Kids Camp','kidscamp',47,art+'/youkids.png')
    main.addDir('Timon and Pumbaa','timonandpumbaa1',47,art+'/youkids.png')
    main.addDir('Dragon Tales','DejectedDragon',47,art+'/youkids.png')
    main.addDir('Aladdin','aladdinvids',47,art+'/youkids.png')
    main.GA("KidZone","YoutubeKids")
    main.VIEWSB()

def YOUList(mname,durl):
        if 'gdata' in durl:
                murl=durl
        else:
                murl='http://gdata.youtube.com/feeds/api/users/'+durl+'/uploads?start-index=1&max-results=50'
        link=main.OPENURL(murl)
        match=re.compile("http\://www.youtube.com/watch\?v\=([^\&]+)\&.+?<media\:descriptio[^>]+>([^<]+)</media\:description>.+?<media\:thumbnail url='([^']+)'.+?<media:title type='plain'>(.+?)/media:title>").findall(link)
        for url,desc,thumb,name in match:
                name=name.replace('<','')
                main.addPlayMs(name,url,48,thumb,desc,'','','','')
        if len(match) >=49:   
            paginate=re.compile('http://gdata.youtube.com/feeds/api/users/(.+?)/uploads.?start-index=(.+?)&max-results=50').findall(murl)
            for id, page in paginate:
                i=int(page)+50
                purl='http://gdata.youtube.com/feeds/api/users/'+id+'/uploads?start-index='+str(i)+'&max-results=50'
                main.addDir('[COLOR blue]Next[/COLOR]',purl,47,art+'/next2.png')
        main.GA(mname,"Youtube-List")

def YOULink(mname,url,thumb):
        ok=True
        main.GA("Youtube-List","Watched")
        url = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+url+"&hd=1"
        stream_url = url
        # play with bookmark
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels='', watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            wh.add_item(mname+' '+'[COLOR green]YoutubeChannel[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
        player.KeepAlive()
        return ok
