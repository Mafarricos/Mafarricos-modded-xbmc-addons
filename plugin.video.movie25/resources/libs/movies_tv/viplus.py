import urllib,urllib2,re,cookielib,sys,os,urlresolver,cookielib
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main, debridroutines
from t0mm0.common.net import Net as net
from t0mm0.common.addon import Addon
from urlresolver import common

#Mash Up - by Mash2k3 2012.


from resources.universal import playbackengine, watchhistory
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art
smalllogo = xbmc.translatePath('special://home/addons/plugin.video.movie25/resources/art/smallicon.png')
elogo = xbmc.translatePath('special://home/addons/plugin.video.movie25/resources/art/bigx.png')
refererTXT = xbmc.translatePath('special://home/addons/plugin.video.movie25/resources/message/referer.txt')    
wh = watchhistory.WatchHistory('plugin.video.movie25')

datapath = addon.get_profile()
cookie_path = os.path.join(datapath, 'cookies')
cookie_jar = os.path.join(cookie_path, "cookiejar.lwp")
try:
    os.makedirs(cookie_path)
except:
    pass



def VIP(murl):
        debriduser = selfAddon.getSetting('hmvusername')
        debridpass = selfAddon.getSetting('hmvpassword')
        if debriduser == '' and debridpass == '':
                dialog = xbmcgui.Dialog()
                dialog.ok("[COLOR=FF67cc33]MashUp[/COLOR]", "Please set your VIP++ credentials", "in Addon settings under logins tab")
                selfAddon.openSettings()
        else:

                 try:
                     rd = debridroutines.RealDebrid(cookie_jar, debriduser, debridpass)
                     if rd.Login():
                        xbmc.executebuiltin("XBMC.Notification(VIP++,Account login successful.,3000,"+smalllogo+")")
                        durl=re.findall('<vip>(.+?)</vip>',murl)[0]
                        link=main.OPENURL(durl)
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
                        match=re.compile('<item><name>([^<]+)</name.+?link>([^<]+)</link.+?thumbnail>([^<]+)</thumbnail.+?username>([^<]+)</username></item>').findall(link)
                        for name,url,thumb,user in match:
                            if debriduser == user or debriduser == 'mash2k3' or debriduser == 'hackermil':
                                main.addDirc(name+' [COLOR red] '+user+'[/COLOR]',url,261,thumb,'',fan,'','','')
                        info=re.findall('<info><message>(.+?)</message><thumbnail>(.+?)</thumbnail></info>',link)
                        if info:
                            for msg,pic in info:
                                main.addLink(msg,'',pic)
                        popup=re.compile('<popup><name>([^<]+)</name.+?popImage>([^<]+)</popImage.+?thumbnail>([^<]+)</thumbnail></popup>').findall(link)
                        for name,image,thumb in popup:
                                main.addPlayc(name,image,244,thumb,'',fan,'','','')
                        main.GA("Vip++",vip+"-Directory")
                     else:
                        xbmc.executebuiltin("XBMC.Notification(VIP++,Login failed.,3000,"+smalllogo+")")
                        print 'VIP++ Account: login failed'
                 except Exception, e:
                        print '**** VIP++ Error: %s' % e
                        dialog = xbmcgui.Dialog()
                        dialog.ok('VIP++ Login Failed','Failed to connect with Website.','Please check your internet connection.')
                        pass
                
        
def VIPList(murl):
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
                main.addPlayc(name,image,244,thumb,'',fan,'','','')
                
        directory=re.compile('<dir><name>([^<]+)</name.+?link>([^<]+)</link.+?thumbnail>([^<]+)</thumbnail></dir>').findall(link)
        for name,url,thumb in directory:
                main.addDirb(name,url,261,thumb,fan)
        
        match=re.compile('<title>([^<]+)</title.+?link>(.+?)</link.+?thumbnail>([^<]+)</thumbnail>').findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for name,url,thumb in match:
                if '</sublink>' in url:
                        main.addDown4(name+' [COLOR blue]'+vip+'[/COLOR]',url,262,thumb,'',fan,'','','')
                else:
                        main.addDown4(name+' [COLOR blue]'+vip+'[/COLOR]',url,263,thumb,'',fan,'','','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        main.GA(vip+"-Directory",vip+"-Playlist")
        
def subLink(mname,suburl):
        match=re.compile('<sublink>(.+?)</sublink>').findall(suburl)
        for url in match:
                match6=re.compile('http://(.+?)/.+?').findall(url)
                for url2 in match6:
                        host = url2.replace('www.','').replace('.in','').replace('.net','').replace('.com','').replace('.to','').replace('.org','').replace('.ch','')
                        if re.findall('\d+.\d+.\d+.\d+',host):
                            host='Static Link'
                        main.addDown2(mname+' [COLOR red]'+host.upper()+'[/COLOR]',url,263,art+'/hosts/'+host.lower()+'.png',art+'/hosts/'+host.lower()+'.png')


def Get_video(murl):
        debriduser = selfAddon.getSetting('hmvusername')
        debridpass = selfAddon.getSetting('hmvpassword')
        rd = debridroutines.RealDebrid(cookie_jar, debriduser, debridpass)
        if rd.Login():
            download_details = rd.Resolve(murl)
            link = download_details['download_link']
            if not link:
                dialog = xbmcgui.Dialog()
                dialog.ok('VIP++','Error occurred attempting to stream the file.',download_details['message'])
                return None
            else:
                print 'VIP++ Link resolved: %s ' % link
                return link
def valid_host(host):
        hoster = re.findall('https?://[www\.]*([^/]+)/', host)
        url = 'http://real-debrid.com/lib/api/hosters.php'
        allhosts = main.OPENURL(url)
        if hoster[0] in allhosts:
            return True
        else:
            return False

def MLink(mname,murl,thumb):
        main.GA(mname,"Watched")
        ok=True
        stream_url = False
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Opening Link,5000)")
        infoLabels =main.GETMETAT(mname,'','','')
        video_type='movie'
        season=''
        episode=''
        img=infoLabels['cover_url']
        fanart =infoLabels['backdrop_url']
        imdb_id=infoLabels['imdb_id']
        infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }
        try:
            linktype=valid_host(murl)
            if linktype== True:
                stream_url = Get_video(murl)
            else:
                stream_url = main.resolve_url(murl)
            if stream_url == False:
                  return                                                            
            infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre'], 'originaltitle': infoLabels['metaName']}
            # play with bookmark
            stream_url=stream_url.replace(' ','%20')
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

