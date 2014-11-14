import urllib,urllib2,re,cookielib,sys,os,urlresolver
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main
from t0mm0.common.net import Net
from t0mm0.common.addon import Addon
net = Net()
from urlresolver import common

#Mash Up - by Mash2k3 2012.


from resources.universal import playbackengine, watchhistory
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art
    
wh = watchhistory.WatchHistory('plugin.video.movie25')



def Mplaylists(murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        r=re.findall('<poster>(.+?)</poster>',link)
        if r:
                vip=r[0]
        else:
                vip='Unknown'
        f=re.findall('<fanart>(.+?)</fanart>',link)
        if f:
                fan=f[0]
        else:
                fan=art+'/fanart2.jpg'
        match=re.compile('<name>(.+?)</name><link>(.+?)</link><thumbnail>(.+?)</thumbnail><date>(.+?)</date>').findall(link)
        for name,url,thumb,date in match:
            main.addDirc(name+' [COLOR red] Updated '+date+'[/COLOR]',url,246,thumb,'',fan,'','','')
        info=re.findall('<info><message>(.+?)</message><thumbnail>(.+?)</thumbnail></info>',link)
        if info:
            for msg,pic in info:
                main.addLink(msg,'',pic)
        popup=re.compile('<popup><name>([^<]+)</name.+?popImage>([^<]+)</popImage.+?thumbnail>([^<]+)</thumbnail></popup>').findall(link)
        for name,image,thumb in popup:
                main.addPlayc(name,image,244,thumb,'','','','','')
        main.GA("Ondemand",vip+"-Directory")


def MList(mname,murl):
        mname  = mname.split('[C')[0]
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        r=re.findall('<poster>(.+?)</poster>',link)
        if r:
                vip=r[0]
        else:
                vip='Unknown'
        f=re.findall('<fanart>(.+?)</fanart>',link)
        if f:
                fan=f[0]
        else:
                fan=art+'/fanart2.jpg'
        info=re.findall('<info><message>(.+?)</message><thumbnail>(.+?)</thumbnail></info>',link)
        if info:
            for msg,pic in info:
                main.addLink(msg,'',pic)
        popup=re.compile('<popup><name>([^<]+)</name.+?popImage>([^<]+)</popImage.+?thumbnail>([^<]+)</thumbnail></popup>').findall(link)
        for name,image,thumb in popup:
                main.addPlayc(name,image,244,thumb,'','','','','')
                
        directory=re.compile('<dir><name>([^<]+)</name.+?link>([^<]+)</link.+?thumbnail>([^<]+)</thumbnail></dir>').findall(link)
        for name,url,thumb in directory:
                main.addDir(name,url,246,thumb)
        match=re.compile('<subchannel><name>(.+?)</name.+?fanart>(.+?)</fanart.+?thumbnail>(.+?)</thumbnail.+?link>(.+?)</link></subchannel>').findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for name,fan,thumb,url in match:
                main.addDown4(name+' [COLOR blue]'+vip+'[/COLOR]',url,247,thumb,'',fan,'','','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False
        dialogWait.close()
        del dialogWait
        main.GA(vip+"-Directory",vip+"-Playlist")

def MLink(mname,suburl,thumb):
        main.GA(mname,"Watched")
        i=1
        namelist=[]
        urllist=[]
        ok=True
        infoLabels =main.GETMETAT(mname,'','','')
        video_type='movie'
        season=''
        episode=''
        img=infoLabels['cover_url']
        fanart =infoLabels['backdrop_url']
        imdb_id=infoLabels['imdb_id']
        infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }
        suburl=main.unescapes(suburl)
        match=re.compile('<sublink>(.+?)</sublink><host>(.+?)</host>').findall(suburl)
        for url,host in match:
                namelist.append(host.upper())        
                urllist.append(url)         
        dialog = xbmcgui.Dialog()
        answer =dialog.select("Pick Host", namelist)
        if answer != -1:
                murl=urllist[int(answer)]
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Opening Link,5000)")
        else:
              return  
        try:
            xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
            stream_url = main.resolve_url(murl)
            if(stream_url == False):
                    return
            infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre']}
            # play with bookmark
            player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=str(infoLabels['title']),season=str(season), episode=str(episode), year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
            #WatchHistory
            if selfAddon.getSetting("whistory") == "true":
                wh.add_item(mname+' '+'[COLOR green]VIPlaylist[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=img, fanart=fanart, is_folder=False)
            player.KeepAlive()
            return ok
        except Exception, e:
            if stream_url != False:
                    main.ErrorReport(e)
            return ok

