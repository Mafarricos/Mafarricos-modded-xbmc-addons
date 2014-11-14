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

def DISJR():
        main.GA("KidZone","DisneyJR")
        main.addDir('All Videos','http://disneyjunior.com/_grill/json/video?r=1-1&l=31&o=0',109,art+'/disjr.png')
        main.addDir('By Character','charac',108,art+'/disjr.png')

def DISJRList(murl):
        main.GA("DisneyJR","Category")
        if murl=='music':
            url ='http://disney.go.com/disneyjunior/data/tilePack?id=1815108&maxAmount=240'
            link=main.OPENURL(url)
            match = re.compile('<a href="(.+?)" ping=".+?"/>\n\t\t<img src="(.+?)" />\n\t\t<text class="title"><(.+?)>').findall(link)
            for url,thumb, name in match:
                name=name.replace('![CDATA[',' ').replace(']]',' ')
                main.addPlayMs(name,url,110,thumb,'','','','','')

        elif murl=='full':
            url ='http://disney.go.com/disneyjunior/data/tilePack?id=1815106&maxAmount=240'
            link=main.OPENURL(url)
            match = re.compile('<a href="(.+?)" ping=".+?"/>\n\t\t<img src="(.+?)" />\n\t\t<text class="title"><(.+?)>').findall(link)
            for url,thumb, name in match:
                sname = re.compile('http://disney.go.com/disneyjunior/(.+?)/.+?').findall(url)
                if sname:
                    sname = sname[0]
                    sname=sname.replace('-',' ')
                    sname=sname.upper()
                else:
                    sname=''
                name=name.replace('![CDATA[',' ').replace(']]',' ')
                
                main.addPlayMs(sname+'  [COLOR red]"'+name+'"[/COLOR]',url,110,thumb,'','','','','')

        elif murl=='short':
            url ='http://disney.go.com/disneyjunior/data/tilePack?id=1815107&maxAmount=240'
            link=main.OPENURL(url)
            match = re.compile('<a href="(.+?)" ping=".+?"/>\n\t\t<img src="(.+?)" />\n\t\t<text class="title"><(.+?)>').findall(link)
            for url,thumb, name in match:
                sname = re.compile('http://disney.go.com/disneyjunior/(.+?)/.+?/.+?').findall(url)
                sname = sname[0]
                sname=sname.replace('-',' ')
                name=name.replace('![CDATA[',' ').replace(']]',' ')
                sname=sname.upper()
                main.addPlayMs(sname+'  [COLOR red]"'+name+'"[/COLOR]',url,110,thumb,'','','','','')

        elif murl=='charac':
            url ='http://disneyjunior.com/'
            link=main.OPENURL(url)
            match = re.compile('{"type":"show","id":".+?","slug":".+?","href":"(.+?)","title":"(.+?)","logo":".+?","thumb":"(.+?)","icon"').findall(link)
            for url,name,thumb in match:
                if 'http' in url:
                        url=url
                else:
                        url='http://disneyjunior.com/_grill/json'+url+'/video?r=1-1&l=31&o=0'
                main.addDir(name,url,109,thumb)
        
def DISJRList2(murl):
            main.GA("DisneyJR","DisJR-list")
            link=main.OPENURL(murl)
            match = re.compile('{"duration":".+?","duration_sec".+?"duration_iso":".+?"id":".+?","slug":".+?","href":"(.+?)","title":"(.+?)","thumb":"(.+?)","description":"(.+?)","vType":"(.+?)",.+?}').findall(link)
            for url, name,thumb,desc,vtype in match:
                main.addPlayMs('[COLOR red]'+name+'[/COLOR] [COLOR yellow]"'+vtype+'"[/COLOR]',url,110,thumb,desc,'','','','')
            if len(match)==25 or len(match)==31:
                paginate=re.compile('(.+?)/video.?r=1-1&l=31&o=([^\&]+)').findall(murl)
                for url, page in paginate:
                        i=int(page)+24
                        url=url.replace('json','more')
                        purl=url+'/video?r=1-1&l=31&o='+str(i)
                        main.addDir('[COLOR blue]Next[/COLOR]',purl,109,art+'/next2.png')

def DISJRLink(mname,murl,thumb):
        main.GA("DisJR-list","Watched")
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        if 'http' not in murl:
                murl='http://disneyjunior.com'+murl
        link=main.OPENURL(murl)
        stream_url = 'rtmp://videodolimgfs.fplive.net/videodolimg'
        video = re.compile('{"bitrate":.+?,"format":"mp4","url":"mp4:(.+?)","id".+?}').findall(link)
        if video:
                if selfAddon.getSetting("disj-qua") == "0":
                                        vid=video[len(video)-1]
                elif selfAddon.getSetting("disj-qua") == "1":
                                        vid=video[len(video)-5]
                elif selfAddon.getSetting("disj-qua") == "2":
                                        vid=video[0]
                stream_url=stream_url+'/'+vid
                
        else:
                video = re.compile('{"bitrate":.+?,"format":"applehttp","url":"(.+?)","id":.+?}').findall(link)
                if selfAddon.getSetting("disj-qua") == "0":
                                        vid=video[len(video)-1]
                elif selfAddon.getSetting("disj-qua") == "1":
                                        vid=video[len(video)-5]
                elif selfAddon.getSetting("disj-qua") == "2":
                                        vid=video[0]
                stream_url=vid
        
        listitem = xbmcgui.ListItem(mname,thumbnailImage=thumb)

        # play with bookmark
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels='', watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            wh.add_item(mname+' '+'[COLOR green]Disney jr[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
        player.KeepAlive()
        return ok
