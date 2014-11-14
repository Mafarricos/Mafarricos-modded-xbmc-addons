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

def CastalbaList(murl):
        try:
            urllist=['http://castalba.tv/channels/p=1','http://castalba.tv/channels/p=2']
        except:
            urllist=['http://castalba.tv/channels/p=1','http://castalba.tv/channels/p=2']
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until channel list is loaded.')
        totalLinks = len(urllist)
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Loading.....[/B]',remaining_display)
        for durl in urllist:
                link=main.OPENURL(durl)
                link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                match=re.compile('<li><div class=".+?"><a href=".+?"><img src="(.+?)" alt=""/><.+?><a href=".+?class=".+?" href="(.+?)">(.+?)</a></h4>.+?<a href=".+?" class=".+?">(.+?)</a></p></li>').findall(link)
                for thumb,url,name,section in match:
                    if name != 'Playboy TV':
                        url=url.replace('..','')
                        thumb=thumb.replace('..','')
                        main.addPlayL(name+'   [COLOR red]'+section+'[/COLOR]','http://castalba.tv'+url,123,'http://castalba.tv'+thumb,'','','','','',secName='Castalba',secIcon=art+'/castalba.png')

                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Loading.....[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        main.GA("Castalba","List")

def CastalbaLink(mname,murl,thumb):
        main.GA("Castalba","Watched")
        link=main.OPENURL(murl)
        ok=True
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<script type="text/javascript"> id="(.+?)"; ew="(.+?)"; eh="(.+?)";</script>').findall(link)
        for fid,wid,hei in match:
            pageUrl='http://castalba.tv/embed.php?cid='+fid+'&wh='+wid+'&ht='+hei
        link2=main.OPENURL(pageUrl)
        rtmp=re.compile("'streamer\': \'(.+?)\',").findall(link2)
        swfUrl=re.compile('flashplayer\': "(.+?)"').findall(link2)
        playPath=re.compile("'file\': \'(.+?)\'").findall(link2)
        stream_url= rtmp[0] + ' playpath=' + playPath[0] + ' swfUrl=' + swfUrl[0] + ' live=true timeout=15 swfVfy=true pageUrl=' + pageUrl
        listitem = xbmcgui.ListItem(mname, thumbnailImage=thumb)
        infoL={'Title': mname, 'Genre': 'Live'} 
        from resources.universal import playbackengine
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='movie', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams='',imdb_id='')

        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            wh.add_item(mname+' '+'[COLOR green]Castalba[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
        return ok
