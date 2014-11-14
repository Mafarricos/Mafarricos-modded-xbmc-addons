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


def TSNDIR():
        main.addDir('Featured','http://m.tsn.ca/home?p_p_id=feed_WAR_xlmagic_INSTANCE_C4iW&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=getPage&p_p_cacheability=cacheLevelPage&p_p_col_id=column-1&p_p_col_pos=6&p_p_col_count=9&_feed_WAR_xlmagic_INSTANCE_C4iW_page=0&_feed_WAR_xlmagic_INSTANCE_C4iW_portrait=false',97,art+'/tsn.png')
        main.addDir('NHL','http://m.tsn.ca/nhl?p_p_id=feed_WAR_xlmagic_INSTANCE_75Sw&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=getPage&p_p_cacheability=cacheLevelPage&p_p_col_id=column-1&p_p_col_pos=2&p_p_col_count=3&_feed_WAR_xlmagic_INSTANCE_75Sw_page=0&_feed_WAR_xlmagic_INSTANCE_75Sw_portrait=false',97,art+'/tsn.png')
        main.addDir('NFL','http://m.tsn.ca/nfl?p_p_id=feed_WAR_xlmagic_INSTANCE_u0tU&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=getPage&p_p_cacheability=cacheLevelPage&p_p_col_id=column-1&p_p_col_pos=2&p_p_col_count=3&_feed_WAR_xlmagic_INSTANCE_u0tU_page=0&_feed_WAR_xlmagic_INSTANCE_u0tU_portrait=false',97,art+'/tsn.png')
        #main.addDir('NBA','nba',97,art+'/tsn.png')
        main.addDir('CFL','http://m.tsn.ca/cfl?p_p_id=feed_WAR_xlmagic_INSTANCE_8WBz&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=getPage&p_p_cacheability=cacheLevelPage&p_p_col_id=column-1&p_p_col_pos=2&p_p_col_count=3&_feed_WAR_xlmagic_INSTANCE_8WBz_page=0&_feed_WAR_xlmagic_INSTANCE_8WBz_portrait=false',97,art+'/tsn.png')
        main.addDir('MLB','http://m.tsn.ca/mlb?p_p_id=feed_WAR_xlmagic_INSTANCE_5wRo&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=getPage&p_p_cacheability=cacheLevelPage&p_p_col_id=column-1&p_p_col_pos=2&p_p_col_count=3&_feed_WAR_xlmagic_INSTANCE_5wRo_page=0&_feed_WAR_xlmagic_INSTANCE_5wRo_portrait=false',97,art+'/tsn.png')
        main.GA("Sports","TSN")
        

def TSNLIST(murl):
        main.GA("TSN","TSN-list")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','')
        match=re.compile('''href="([^"]+)"><span class="tileText"><span class="overlay"><img src="([^"]+)" style=.+?/><img class="videoOverlay" src=".+?" /></span><span class=".+?" style=".+?">([^<]+)</span></span>''').findall(link)
        for url,thumb,name in match:
            url=main.REDIRECT(url)    
            main.addPlayMs(name,url,98,thumb,'','','','','')
        paginate=re.compile('_page=(\d+)&_',re.DOTALL).findall(murl)
        if paginate:
                purl=int(paginate[0])+ 1
                xurl=re.sub('_page=(\d+)&_','_page='+str(purl)+'&_',murl)
                main.addDir('[COLOR blue]Next[/COLOR]',xurl,97,art+'/next2.png')

def TSNLINK(mname,murl,thumb):
        #got help from TSN plugin by TEEFER
        main.GA("TSN-list","Watched")
        ok=True
        link=main.OPENURL(murl)
        m3u8 = re.compile('"(http[^"]+m3u8)"').findall(link)[0]
        link2=main.OPENURL(m3u8)
        stream = re.compile("(http.+?)Adaptive").findall(link2)[0]
        if len(stream)==0:
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Playable Only in Canada,5000)")
        else:
            if selfAddon.getSetting("tsn-qua") == "0":
                        stream_url = stream+'Adaptive_08.mp4.m3u8'
            elif selfAddon.getSetting("tsn-qua") == "1":
                        stream_url = stream+'Adaptive_05.mp4.m3u8'
            elif selfAddon.getSetting("tsn-qua") == "2":
                        stream_url = stream+'Adaptive_01.mp4.m3u8'
            # play with bookmark
            player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels='', watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
            #WatchHistory
            if selfAddon.getSetting("whistory") == "true":
                    wh.add_item(mname+' '+'[COLOR green]TSN[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
            player.KeepAlive()
            return ok
