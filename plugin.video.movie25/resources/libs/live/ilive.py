import urllib,urllib2,re,cookielib,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art





def iLive():
        
        main.addDir('All','all',120,art+'/ilive.png')
        main.addDir('All [English]','allenglish',120,art+'/ilive.png')
        main.addDir('General','general',120,art+'/ilive.png')
        main.addDir('Entertainment','entertainment',120,art+'/ilive.png')
        main.addDir('Entertainment [English]','entertainmentenglish',120,art+'/ilive.png')
        main.addDir('Sports','sports',120,art+'/ilive.png')
        main.addDir('Sports [English]','sportsenglish',120,art+'/ilive.png')
        main.addDir('News','news',120,art+'/ilive.png')
        main.addDir('Music','music',120,art+'/ilive.png')
        main.addDir('Animation','animation',120,art+'/ilive.png')
        main.GA("Live","iLive")
        
def iLiveList(murl):
        if murl=='general':
            try:
                urllist=['http://www.ilive.to/channels/General','http://www.ilive.to/channels/General?p=2']
            except:
                urllist=['http://www.ilive.to/channels/General']
        if murl=='entertainment':
            try:
                urllist=['http://www.ilive.to/channels/Entertainment','http://www.ilive.to/channels/Entertainment?p=2','http://www.ilive.to/channels/Entertainment?p=3','http://www.ilive.to/channels/Entertainment?p=4','http://www.ilive.to/channels/Entertainment?p=5','http://www.ilive.to/channels/Entertainment?p=6']
            except:
                urllist=['http://www.ilive.to/channels/Entertainment','http://www.ilive.to/channels/Entertainment?p=2','http://www.ilive.to/channels/Entertainment?p=3','http://www.ilive.to/channels/Entertainment?p=4','http://www.ilive.to/channels/Entertainment?p=5']
        if murl=='sports':
            try:
                urllist=['http://www.ilive.to/channels/Sport','http://www.ilive.to/channels/Sport?p=2','http://www.ilive.to/channels/Sport?p=3','http://www.ilive.to/channels/Sport?p=4']
            except:
                urllist=['http://www.ilive.to/channels/Sport','http://www.ilive.to/channels/Sport?p=2','http://www.ilive.to/channels/Sport?p=3']
        if murl=='news':
            try:
                urllist=['http://www.ilive.to/channels/News']
            except:
                urllist=['http://www.ilive.to/channels/News']
        if murl=='music':
            try:
                urllist=['http://www.ilive.to/channels/Music']
            except:
                urllist=['http://www.ilive.to/channels/Music']
        if murl=='animation':
            try:
                urllist=['http://www.ilive.to/channels/Animation']
            except:
                urllist=['http://www.ilive.to/channels/Animation']
        if murl=='all':
            try:
                urllist=['http://www.ilive.to/channels','http://www.ilive.to/channels?p=2','http://www.ilive.to/channels?p=3','http://www.ilive.to/channels?p=4','http://www.ilive.to/channels?p=5','http://www.ilive.to/channels?p=6','http://www.ilive.to/channels?p=7','http://www.ilive.to/channels?p=8','http://www.ilive.to/channels?p=9','http://www.ilive.to/channels?p=10','http://www.ilive.to/channels?p=11','http://www.ilive.to/channels?p=12','http://www.ilive.to/channels?p=13','http://www.ilive.to/channels?p=14','http://www.ilive.to/channels?p=15','http://www.ilive.to/channels?p=16']
            except:
                urllist=['http://www.ilive.to/channels','http://www.ilive.to/channels?p=2','http://www.ilive.to/channels?p=3','http://www.ilive.to/channels?p=4','http://www.ilive.to/channels?p=5','http://www.ilive.to/channels?p=6','http://www.ilive.to/channels?p=7','http://www.ilive.to/channels?p=8','http://www.ilive.to/channels?p=9','http://www.ilive.to/channels?p=10']
        if murl=='allenglish':
            try:
                urllist=['http://www.ilive.to/channels?lang=1','http://www.ilive.to/channels?lang=1&p=2','http://www.ilive.to/channels?lang=1&p=3','http://www.ilive.to/channels?lang=1&p=4','http://www.ilive.to/channels?lang=1&p=5','http://www.ilive.to/channels?lang=1&p=6','http://www.ilive.to/channels?lang=1&p=7','http://www.ilive.to/channels?lang=1&p=8','http://www.ilive.to/channels?lang=1&p=9','http://www.ilive.to/channels?lang=1&p=10']
            except:
                urllist=['http://www.ilive.to/channels?lang=1','http://www.ilive.to/channels?lang=1&p=2','http://www.ilive.to/channels?lang=1&p=3','http://www.ilive.to/channels?lang=1&p=4','http://www.ilive.to/channels?lang=1&p=5','http://www.ilive.to/channels?lang=1&p=6','http://www.ilive.to/channels?lang=1&p=7','http://www.ilive.to/channels?lang=1&p=8','http://www.ilive.to/channels?lang=1&p=9']
        if murl=='entertainmentenglish':
            try:
                urllist=['http://www.ilive.to/channels/Entertainment?lang=1','http://www.ilive.to/channels/Entertainment?lang=1&p=2','http://www.ilive.to/channels/Entertainment?lang=1&p=3','http://www.ilive.to/channels/Entertainment?lang=1&p=4','http://www.ilive.to/channels/Entertainment?lang=1&p=5','http://www.ilive.to/channels/Entertainment?lang=1&p=6']
            except:
                urllist=['http://www.ilive.to/channels/Entertainment?lang=1','http://www.ilive.to/channels/Entertainment?lang=1&p=2','http://www.ilive.to/channels/Entertainment?lang=1&p=3','http://www.ilive.to/channels/Entertainment?lang=1&p=4','http://www.ilive.to/channels/Entertainment?lang=1&p=5']
        if murl=='sportsenglish':
            try:
                urllist=['http://www.ilive.to/channels/Sport?lang=1','http://www.ilive.to/channels/Sport?lang=1&p=2']
            except:
                urllist=['http://www.ilive.to/channels/Sport?lang=1']
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until channel list is loaded.')
        totalLinks = len(urllist)
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Loading.....[/B]',remaining_display)
        for durl in urllist:
                link=main.OPENURL(durl)
                link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','')
                match=re.compile('src=".+?" alt=".+?<img width=".+?" height=".+?" src="([^<]+)" alt=".+?</noscript></a><a href="(.+?)"><strong>(.*?)</strong></a><br/>').findall(link)
                for thumb,url,name in match:
                        if 'venus' not in name.lower() and '+16' not in name.lower() and '+18' not in name.lower() and 'hongkong' not in name.lower() and   'playboy' not in name.lower() and   'sex' not in name.lower() and   'girls' not in name.lower() and   'fuck' not in name.lower() and   'hardcore' not in name.lower() and   'softcore' not in name.lower() and   'pussy' not in name.lower() and   'dick' not in name.lower() and   'anal' not in name.lower() and   'cum' not in name.lower() and   'blowjob' not in name.lower() and   'adult' not in name.lower() and   '18+' not in name.lower() and  '16+' not in name.lower():
                                main.addPlayL(name,url,121,thumb,'','','','','',secName='iLive',secIcon=art+'/ilive.png')
                
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Loading.....[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        main.GA("iLive","List") 

def getToken(url):
        from t0mm0.common.net import Net
        net = Net()
        html = net.http_GET(url).content
        token_url = re.compile('\$.getJSON\("(.+?)",').findall(html)[0]

        import datetime
        time_now=datetime.datetime.now()
        import time
        epoch=time.mktime(time_now.timetuple())+(time_now.microsecond/1000000.)
        epoch_str = str('%f' % epoch)
        epoch_str = epoch_str.replace('.','')
        epoch_str = epoch_str[:-3]

        token_url = token_url + '&_=' + epoch_str
        token = re.compile('":"(.+?)"').findall(net.http_GET(token_url+'&_='+str(epoch), headers={'Referer':url}).content)[0]
        return token

def iLiveLink(mname,murl,thumb):
        main.GA("iLive","Watched")
        stream_url=False
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Opening Stream,3000)")
        link=main.OPENURL(murl)
        ok=True
        if link:
                playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                playlist.clear()
                link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace("\/",'/')
                rtmp=re.compile('''streamer: "([^"]+?)"''').findall(link)
                app=rtmp[0].split('?xs=')
                playpath=re.compile('''file: "([^"]+?).flv"''').findall(link)
                token=getToken(murl)
                stream_url =rtmp[0]+' app=edge/?xs='+app[1]+' playpath='+playpath[0]+' swfUrl=http://cdn.ilive.to/player/player_ilive_2.swf pageUrl=http://www.ilive.to/ live=true timeout=10 token='+token
                listitem = xbmcgui.ListItem(thumbnailImage=thumb)
                infoL={'Title': mname, 'Genre': 'Live'} 
                from resources.universal import playbackengine
                player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='movie', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams='',imdb_id='')

                #WatchHistory
                if selfAddon.getSetting("whistory") == "true":
                    from resources.universal import watchhistory
                    wh = watchhistory.WatchHistory('plugin.video.movie25')
                    wh.add_item(mname+' '+'[COLOR green]iLive[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
                return ok
