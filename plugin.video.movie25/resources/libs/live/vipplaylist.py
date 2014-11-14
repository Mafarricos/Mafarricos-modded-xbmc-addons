import urllib,urllib2,re,cookielib,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art




def VIPplaylists(murl):
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
        match=re.compile('<notify><new>(.+?)</new><message1>(.+?)</message1><message2>(.+?)</message2><message3>(.+?)</message3><old>(.+?)</old></notify>').findall(link)
        if len(match)>0:
            for new,mes1,mes2,mes3,old in match: continue
            if new != ' ':
                new=vip+new
                runonce=os.path.join(main.datapath,'RunOnce')
                notified=os.path.join(runonce,str(new))
                if not os.path.exists(notified):
                    open(notified,'w').write('version="%s",'%new)
                    dialog = xbmcgui.Dialog()
                    ok=dialog.ok('[B]'+vip+' Announcement![/B]', str(mes1) ,str(mes2),str(mes3))
                if old != ' ':
                    old=vip+old
                    notified=os.path.join(runonce,str(old))
                    if  os.path.exists(notified):
                        os.remove(notified)
            else: print 'No Messages'
        else: print 'Github Link Down'
        match3=re.compile('<name>([^<]+)</name><link>([^<]+)</link><thumbnail>([^<]+)</thumbnail><mode>([^<]+)</mode>').findall(link)
        for name,url,thumb,mode in match3:
                if re.findall('http',thumb):
                        thumbs=thumb
                else:
                        thumbs=art+'/'+thumb+'.png'
                main.addDir(name,url,int(mode),thumbs)
        match=re.compile('<name>([^<]+)</name><link>([^<]+)</link><thumbnail>([^<]+)</thumbnail><date>([^<]+)</date>').findall(link)
        for name,url,thumb,date in match:
            main.addDirc(name+' [COLOR red] Updated '+date+'[/COLOR]',url,182,thumb,'',fan,'','','')
        info=re.findall('<info><message>(.+?)</message><thumbnail>(.+?)</thumbnail></info>',link)
        if info:
            for msg,pic in info:
                main.addLink(msg,'',pic)
        popup=re.compile('<popup><name>([^<]+)</name.+?popImage>([^<]+)</popImage.+?thumbnail>([^<]+)</thumbnail></popup>').findall(link)
        for name,image,thumb in popup:
                main.addPlayc(name,image,244,thumb,'','','','','')
        main.GA("Live",vip+"-Playlists")


def VIPList(mname,murl):
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
                main.addDir(name,url,182,thumb)
        match=re.compile('<title>([^<]+)</title.+?link>(.+?)</link.+?thumbnail>([^<]+)</thumbnail>').findall(link)
        for name,url,thumb in sorted(match):
            main.addPlayL(name+' [COLOR blue]'+vip+'[/COLOR]',url,183,thumb,'',fan,'','','',secName=vip,secIcon=art+'/'+vip.lower()+'.png')
        main.GA(vip+"-Playlists",mname)

def VIPLink(mname,murl,thumb):
        main.GA(mname,"Watched")
        ok=True
        namelist=[]
        urllist=[]
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        if '.f4m'in murl:
                from resources.universal import F4mProxy
                player=F4mProxy.f4mProxyHelper()
                proxy=None
                use_proxy_for_chunks=False
                player.playF4mLink(murl, mname, proxy, use_proxy_for_chunks,'',thumb)
                if selfAddon.getSetting("whistory") == "true":
                    from resources.universal import watchhistory
                    wh = watchhistory.WatchHistory('plugin.video.movie25')
                    wh.add_item(mname+' '+'[COLOR green]Live[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
        else:
                if '</regex>'in murl: 
                        murl=main.doRegex(murl)
                match=re.compile('<sublink>(.+?)</sublink>').findall(murl)
                if match:
                        i=1
                        for url in match:
                                name= 'Link '+str(i)
                                namelist.append(name)        
                                urllist.append(url)
                                i=i+1
                        dialog = xbmcgui.Dialog()
                        answer =dialog.select("Pick A Link", namelist)
                        if answer != -1:
                                murl=urllist[int(answer)]
                                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Opening Link,5000)")
                        else:
                              return
                
                stream_url = murl
                listitem = xbmcgui.ListItem(thumbnailImage=thumb)
                listitem.setInfo('video', {'Title': mname, 'Genre': 'Live'} )
                
                playlist.add(stream_url,listitem)
                xbmcPlayer = xbmc.Player()
                xbmcPlayer.play(playlist)        #WatchHistory
                if selfAddon.getSetting("whistory") == "true":
                    from resources.universal import watchhistory
                    wh = watchhistory.WatchHistory('plugin.video.movie25')
                    wh.add_item(mname+' '+'[COLOR green]Live[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
        return ok
