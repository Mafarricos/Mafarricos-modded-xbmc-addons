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

def DISC(murl):
        link=main.OPENURL(murl)
        link=main.unescapes(link)
        match= re.compile('<a href="([^<]+)" class="event-click-tracking" data-track-rule="module" data-module-name="shows-carousel".+?<img class=".+?" src=".+?" data-original="(.+?)" width=".+?alt="(.+?)" title=".+?" />').findall(link)
        for url,thumb,name in sorted(match):
            thumb=thumb.replace(' ','%20')
            print thumb
            main.addDir(name,'http://dsc.discovery.com'+url,64,thumb)
        main.GA("Adventure","Discovery")
        main.VIEWSB()

def ANIP(murl):
        link=main.OPENURL(murl)
        link=main.unescapes(link)
        match= re.compile('<a href="([^<]+)" class="event-click-tracking" data-track-rule="module" data-module-name="shows-carousel".+?<img class=".+?" src=".+?" data-original="(.+?)" width=".+?alt="(.+?)" title=".+?" />').findall(link)
        for url,thumb,name in sorted(match):
            thumb=thumb.replace(' ','%20')
            main.addDir(name,'http://animal.discovery.com'+url,64,thumb)
        main.GA("Adventure","AnimalPlanet")
        main.VIEWSB()
        
def MILIT(murl):
        main.addDir('AIR ACES','aa',90,'http://viewersguide.ca/wp-content/uploads/2013/01/air-aces-ss-280x200.png')
        link=main.OPENURL(murl)
        link=main.unescapes(link)
        match= re.compile('<a href="([^<]+)" class="event-click-tracking" data-track-rule="module" data-module-name="shows-carousel".+?<img class=".+?" src=".+?" data-original="(.+?)" width=".+?alt="(.+?)" title=".+?" />').findall(link)
        for url,thumb,name in sorted(match):
            thumb=thumb.replace(' ','%20')
            main.addDir(name,'http://military.discovery.com'+url,64,thumb)
        main.GA("Adventure","Military")
        main.VIEWSB()

def SCI(murl):
        link=main.OPENURL(murl)
        link=main.unescapes(link)
        match= re.compile('<a href="([^<]+)" class="event-click-tracking" data-track-rule="module" data-module-name="shows-carousel".+?<img class=".+?" src=".+?" data-original="(.+?)" width=".+?alt="(.+?)" title=".+?" />').findall(link)
        for url,thumb,name in sorted(match):
            thumb=thumb.replace(' ','%20')
            main.addDir(name,'http://science.discovery.com'+url,64,thumb)
        main.GA("Adventure","Science")
        main.VIEWSB()

def VELO(murl):
        link=main.OPENURL(murl)
        link=main.unescapes(link)
        match= re.compile('<a href="([^<]+)" class="event-click-tracking" data-track-rule="module" data-module-name="shows-carousel".+?<img class=".+?" src=".+?" data-original="(.+?)" width=".+?alt="(.+?)" title=".+?" />').findall(link)
        for url,thumb,name in sorted(match):
            thumb=thumb.replace(' ','%20')
            main.addDir(name,'http://velocity.discovery.com'+url,64,thumb)
        main.GA("Adventure","Velocity")
        main.VIEWSB()

def LISTDISC(mname,murl):
        thumbList=[]
        dsc=re.findall('dsc.discovery',murl)
        if dsc:
            turl='http://dsc.discovery.com'
        mil=re.findall('military.discovery',murl)
        if mil:
            turl='http://military.discovery.com'
        sci=re.findall('science.discovery',murl)
        if sci:
            turl='http://science.discovery.com'
        velo=re.findall('velocity.discovery',murl)
        if velo:
            turl='http://velocity.discovery.com'
        ap=re.findall('animal.discovery',murl)
        if ap:
            turl='http://animal.discovery.com'
        linka=main.OPENURL(murl)
        r=re.findall('uri="/services/taxonomy/(.+?)/">',linka)
        nurl=turl+'/services/taxonomy/'+r[0]+'/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video'
        link=main.OPENURL(nurl)
        Thumb=re.compile('<img src="(.+?)" />').findall(link)
        for thumb in Thumb:
                thumbList.append(thumb)
         
        match=re.compile('<a href="(.+?)" class=".+?" data-track-rule=".+?"  data-module-name=".+?" data-module-location=".+?" data-link-position=".+?" data-track-more=".+?">(.+?)</a></h4>\n                        \n                        <p>(.+?)</p>\n ').findall(link)
        if len(match)==0:
                match=re.compile('<a href="(.+?)" class=".+?" data-track-rule=".+?"  data-module-name=".+?" data-module-location=".+?" data-link-position=".+?" data-track-more=".+?">(.+?)</a></h4>\n                        <p class="clip-count-all">(.+?)</p>\n').findall(link)
                i=0
                for url, name, view in match:
                        url=url.replace('http://animal.discovery.com','').replace('http://military.discovery.com','').replace('http://science.discovery.com','').replace('http://velocity.discovery.com','').replace('http://dsc.discovery.com','')
                        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                        Full=re.compile('<img src="([^<]+)" />[^<]+>Full Episode</span>').findall(link)
                        Full=re.compile('<span class="full-episode-flag">Full Episode</span>.+?<a href="(.+?)" class=".+?" data-track-rule=".+?"').findall(link)
                        if Full:
                            for ind in Full:
                                if ind == url:
                                        name= name + '  [COLOR red]Full Episode[/COLOR]'
                        name=name.replace('&#39;',"'").replace('&quot;','"').replace('&amp;',"&")
                        main.addPlayMs(name+'  [COLOR blue]'+view+'[/COLOR]',turl+url,65,thumbList[i],'','','','','')
                        i=i+1
        else:
                i=0
                for url, name, types in match:
                        url=url.replace('http://animal.discovery.com','').replace('http://military.discovery.com','').replace('http://science.discovery.com','').replace('http://velocity.discovery.com','').replace('http://dsc.discovery.com','')
                
                        name=name.replace('&#39;',"'").replace('&quot;','"').replace('&amp;',"&")
                        main.addPlayMs(name+'  [COLOR blue]'+types+'[/COLOR]',turl+url,65,thumbList[i],'','','','','')
                        i=i+1
        main.GA("Discovery",mname+"-list")

def LINKDISC(name,url):
        from resources.universal import playbackengine
        idlist1=[]
        idlist2=[]
        idlist3=[]
        qualitylist=[]
        ETitleList=[]
        thumbList=[]
        plotList=[]
        main.GA("Discovery","Watched")
        MainUrl= 'http://dsc.discovery.com'
        xbmc.executebuiltin("XBMC.Notification([B]Please Wait![/B],Playing Link,10000)")
        link=main.OPENURL(url)
        ok=True
        Title=re.compile('"name": "(.+?)",').findall(link)
        if Title:
            for title in Title:
                title=title.replace('3E','').replace('\u0027',"").replace('\u0026#8212\u003B',' ').replace('\u002D',' ')
                mtitle = title
        else:
            mtitle=name
        Thumb=re.compile('"thumbnailURL": "(.+?)",').findall(link)
        for thumb in Thumb:
            thumbList.append(thumb)
        Plot=re.compile('"videoCaption": "(.+?)",').findall(link)
        for plot in Plot:
            plotList.append(plot)
        ETitle=re.compile('"episodeTitle": "(.+?)",').findall(link)
        for etitle in ETitle:
            etitle=etitle.replace('3E','').replace('\u0027',"").replace('\u0026#8212\u003B',' ').replace('\u002D',' ')
            ETitleList.append(etitle)
        Full=re.findall('full episode',name,re.I)
        if Full:
            match2=re.compile('"m3u8": "http://discidevflash-f.akamaihd.net/i/digmed/(.+?).mp4.csmil/master.m3u8"').findall(link)
            main.GA("Discovery-"+name,"Watching")
            final='http://discidevflash-f.akamaihd.net/i/digmed/'+match2[0]+'.mp4.csmil/master.m3u8'
            # play with bookmark           
            player = playbackengine.PlayWithoutQueueSupport(final, 'plugin.video.movie25', video_type='', title=name,season='', episode='', year='', watch_percent=0.85, watchedCallbackwithParams=main.WatchedCallback, img=thumbList[0], infolabels={'Title':name,'Plot': plotList[0]})
            
            #WatchHistory
            if selfAddon.getSetting("whistory") == "true":
                wh.add_item(name+' '+'[COLOR green]Discovery[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumbList[0], fanart='', is_folder=False)

            player.KeepAlive()
            return ok
        else:
            match=re.compile('"m3u8": "http://discidevflash-f.akamaihd.net/i/digmed/hdnet/(.+?)/(.+?)/(.+?)-(.+?).mp4').findall(link)
            for id1, id2, id3, quality in match:
                idlist1.append(id1)
                idlist2.append(id2)
                idlist3.append(id3)
                qualitylist.append(quality)
            i=0
            main.GA("Discovery-"+mtitle,"Watching")
            player=None
            for i in range(len(match)):
                    match1=re.compile('3500k').findall(qualitylist[i])
                    match2=re.compile('1500k').findall(qualitylist[i])
                    if selfAddon.getSetting("bit-disc") == "0":
                        if (len(match1)>0):
                            final= 'http://discidevflash-f.akamaihd.net/digmed/hdnet/'+idlist1[i]+'/'+idlist2[i]+'/'+idlist3[i]+'-3500k.mp4?seek=5'
                        elif (len(match1)==0) and (len(match2)>0):
                            final= 'http://discidevflash-f.akamaihd.net/digmed/hdnet/'+idlist1[i]+'/'+idlist2[i]+'/'+idlist3[i]+'-1500k.mp4?seek=5'
                        else:
                            final= 'http://discidevflash-f.akamaihd.net/digmed/hdnet/'+idlist1[i]+'/'+idlist2[i]+'/'+idlist3[i]+'-600k.mp4?seek=5'    
                    elif selfAddon.getSetting("bit-disc") == "1":
                        if (len(match2)>0):
                            final= 'http://discidevflash-f.akamaihd.net/digmed/hdnet/'+idlist1[i]+'/'+idlist2[i]+'/'+idlist3[i]+'-1500k.mp4?seek=5'
                        else:
                            final= 'http://discidevflash-f.akamaihd.net/digmed/hdnet/'+idlist1[i]+'/'+idlist2[i]+'/'+idlist3[i]+'-600k.mp4?seek=5'
                    else:
                            final= 'http://discidevflash-f.akamaihd.net/digmed/hdnet/'+idlist1[i]+'/'+idlist2[i]+'/'+idlist3[i]+'-600k.mp4?seek=5'
                    match2=re.compile('1500k').findall(quality)
                    tot = i + 1
                    # play with bookmark
                    if i==0:    
                        player = playbackengine.PlayWithoutQueueSupport(final, 'plugin.video.movie25', video_type='', title=ETitleList[i],season='', episode='', year='', watch_percent=0.85, watchedCallbackwithParams=main.WatchedCallback, img=thumbList[i], infolabels={'Title':'[COLOR blue]'+ETitleList[i]+'[/COLOR]','Plot': plotList[i],'Genre': '[B]Clip '+str(tot)+'/'+str(len(match))+' on playlist[/B]        '+mtitle})
                    else:
                        playbackengine.AddToPL(ETitleList[i], final, img=thumbList[i], infolabels={'Title':'[COLOR blue]'+ETitleList[i]+'[/COLOR]','Plot': plotList[i],'Genre': '[B]Clip '+str(tot)+'/'+str(len(match))+' on playlist[/B]        '+mtitle})
                    i=i+1
      
            

            xbmc.Player().pause()
            if idlist3[0][0:7]==idlist3[1][0:7]:
                xbmc.executebuiltin("XBMC.Notification([B]Attention![/B],"+str(len(match))+" Clips loaded to playlist,10000)")
            elif idlist3[0][6:13]==idlist3[1][6:13]:
                xbmc.executebuiltin("XBMC.Notification([B]Attention![/B],"+str(len(match))+" Clips loaded to playlist,10000)")
            elif idlist3[1][6:13]==idlist3[2][6:13]:
                xbmc.executebuiltin("XBMC.Notification([B]Attention![/B],"+str(len(match))+" Clips loaded to playlist,10000)")
            else:
                xbmc.executebuiltin("XBMC.Notification([B]Attention![/B],Related clips loaded to playlist,10000)")
            #WatchHistory
            if selfAddon.getSetting("whistory") == "true":
                wh.add_item(name+' '+'[COLOR green]Discovery[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumbList[0], fanart='', is_folder=False)

            player.KeepAlive()
            return ok
        
