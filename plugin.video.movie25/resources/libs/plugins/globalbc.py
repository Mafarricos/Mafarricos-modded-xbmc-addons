import urllib,urllib2,re,cookielib,string,sys,os
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
    
def GLOBALBC():
        main.GA("Plugin","GlobalBC")
        #main.addDir('Search Global BC','gbc',170,art+'/search.png')
        main.addDir('Latest Local Video','http://globalnews.ca/bc/videos/',166,art+'/globalbc.png')
        main.addDir('Latest National Video','http://globalnews.ca/national/videos/',166,art+'/globalbc.png')
        main.addLink('[COLOR red]Programs[/COLOR]','','')
        main.addDir('BC1','bc1',169,art+'/globalbc.png')
        main.addDir('News Hour','newshour',169,art+'/globalbc.png')
        main.addDir('Noon News Hour','http://globalnews.ca/bc/videos/program/noon-news-hour-bc/',166,art+'/globalbc.png')
        main.addDir('Morning News','morningnews',169,art+'/globalbc.png')
        main.addDir('Global National','globalnat',169,art+'/globalbc.png')
        main.addDir('Global National Mandarin','http://globalnews.ca/national/videos/program/global-national-mandarin/',166,art+'/globalbc.png')
        main.addDir('16x9','16x9',169,art+'/globalbc.png')
        main.addDir('The West Block','http://globalnews.ca/national/videos/program/the-west-block/',166,art+'/globalbc.png')
        main.addDir('The Morning Show','http://globalnews.ca/national/videos/program/the-morning-show/',166,art+'/globalbc.png')

def GLOBALBCSearch():
        keyb = xbmc.Keyboard('', 'Search Global BC')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
                surl='http://globalnews.ca/national/videos/?video-search='+encode
                link=main.OPENURL(surl)
                link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                match=re.compile('<a class=".+?" href="([^<]+)" title="([^<]+)"><img src="http://en.wordpress.com/imgpress.?url=([^<]+)w=300" alt=".+?"><div><h4>([^<]+)</h4>').findall(link)
                for url, name,thumb,cat in match:
                    main.addPlayc('[COLOR red]'+cat+':[/COLOR]  '+name,thumb,167,thumb,'','','','','')

def GLOBALBCList2(murl):
        if murl=='bc1':
                main.addDir('BC1','http://globalnews.ca/bc/videos/program/bc-1/',166,art+'/globalbc.png')
                main.addDir('AM/BC','http://globalnews.ca/bc/videos/program/ambc/',166,art+'/globalbc.png')
                main.addDir('Top Story','http://globalnews.ca/bc/videos/program/bc-1+top-story-bc1/',166,art+'/globalbc.png')
        elif murl=='newshour':
                main.addDir('News Hour','http://globalnews.ca/bc/videos/program/news-hour-bc/',166,art+'/globalbc.png')
                main.addDir('Mike McCardell','http://globalnews.ca/bc/videos/program/news-hour-bc+mike-mccardell/',166,art+'/globalbc.png')
                main.addDir('Satellite Debris','http://globalnews.ca/bc/videos/program/news-hour-bc+satellite-debris/',166,art+'/globalbc.png')
                main.addDir('Health Headlines','http://globalnews.ca/bc/videos/program/news-hour-bc+health-headlines/',166,art+'/globalbc.png')
        elif murl=='morningnews':
                main.addDir('Morning News','http://globalnews.ca/bc/videos/program/morning-news-bc/',166,art+'/globalbc.png')
                main.addDir('Small Town BC','http://globalnews.ca/bc/videos/program/morning-news-bc+small-town-bc/',166,art+'/globalbc.png')
                main.addDir('Trending Now','http://globalnews.ca/bc/videos/program/morning-news-bc+trending-now/',166,art+'/globalbc.png')
        elif murl=='globalnat':
                main.addDir('Global National','http://globalnews.ca/national/videos/program/global-national/',166,art+'/globalbc.png')
                main.addDir('Everyday Hero','http://globalnews.ca/national/videos/program/global-national+everyday-hero/',166,art+'/globalbc.png')
                main.addDir('Vital Signs','http://globalnews.ca/national/videos/program/global-national+vital-signs/',166,art+'/globalbc.png')
        elif murl=='16x9':
                main.addDir('16x9','http://globalnews.ca/national/videos/program/16x9/',166,art+'/globalbc.png')
                main.addDir('Season 5','http://globalnews.ca/national/videos/program/16x9+season-5/',166,art+'/globalbc.png')
                main.addDir('Season 4','http://globalnews.ca/national/videos/program/16x9+season-4/',166,art+'/globalbc.png')
                        
        
def GLOBALBCList(murl):
        main.GA("GlobalBC","List")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<a class=".+?" href="([^<]+)" title="([^<]+)" data-vid_id=".+?"><img src="http://en.wordpress.com/imgpress.?url=([^<]+)w=300" alt=".+?"><div><h4>([^<]+)</h4>').findall(link)
        for url, name,thumb,cat in match:
            thumb=thumb.replace('jpg&','jpg')
            main.addPlayc('[COLOR red]'+cat+':[/COLOR]  '+name,thumb,167,thumb,'','','','','')


def GLOBALBCLink(mname,murl):
        main.GA("GlobalBC","Watched")
        match=re.compile('http://media.globalnews.ca/videothumbnails/(.+?)_2.+?_.+?.jpg').findall(murl)
        if len(match)==0:
                match=re.compile('http://media.globalnews.ca/videothumbnails/(.+?)_6.+?_.+?.jpg').findall(murl)
                if len(match)==0:
                    match=re.compile('http://media.globalnews.ca/videothumbnails/(.+?).jpg').findall(murl)
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        stream_url='http://globalnewsvideo.smdg.ca/'+match[0]+'.mp4'
        

        # play with bookmark
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=murl,infolabels='', watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            wh.add_item(mname+' '+'[COLOR green]GlobalBC[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=murl, fanart='', is_folder=False)
        player.KeepAlive()
        return ok
        
