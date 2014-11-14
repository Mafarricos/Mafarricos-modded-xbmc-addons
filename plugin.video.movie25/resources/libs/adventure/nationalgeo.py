import urllib,urllib2,re,cookielib,os,sys
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

def NG():
    #main.addDir('National Geographic Channel','ngc','',art+'/ngccm.png')
    #main.addDir('Nat Geo Wild','ngw','',art+'/ngwcm.png')
    main.addDir('Nat Geo Animals','nga',71,art+'/nga2.png')
    main.GA("Adventure","NationalGeo")
    main.VIEWSB()

def NGDir(murl):
    if murl  =='ngc':
        main.addDir('Full Episodes','http://video.nationalgeographic.com/video/national-geographic-channel/full-episodes/',72,art+'/ngc.png')
        main.addDir('Shows','http://video.nationalgeographic.com/video/national-geographic-channel/shows/',72,art+'/ngc.png')
        main.addDir('Specials','http://video.nationalgeographic.com/video/national-geographic-channel/specials-1/',72,art+'/ngc.png')
        main.addDir('Extras','http://video.nationalgeographic.com/video/national-geographic-channel/extras/',72,art+'/ngc.png')
        main.GA("NationalGeo","NGC")
    elif murl  =='ngw':
        main.addDir('Full Episodes','http://video.nationalgeographic.com/video/nat-geo-wild/full-episodes-1/',72,art+'/ngw.png')
        main.addDir('Shows','http://video.nationalgeographic.com/video/nat-geo-wild/shows-1/',72,art+'/ngw.png')
        main.addDir('Specials','http://video.nationalgeographic.com/video/nat-geo-wild/specials-2/',72,art+'/ngw.png')
        main.addDir('Extras','http://video.nationalgeographic.com/video/nat-geo-wild/extras-1/',72,art+'/ngw.png')
        main.GA("NationalGeo","NGW")
    elif murl  =='nga':
        main.addDir('Amphibians','http://video.nationalgeographic.com/video/animals/amphibians-animals/',72,art+'/nga2.png')
        main.addDir('Birds','http://video.nationalgeographic.com/video/animals/birds-animals/',72,art+'/nga2.png')
        main.addDir('Bugs','http://video.nationalgeographic.com/video/animals/bugs-animals/',72,art+'/nga2.png')
        main.addDir('Crittercam','http://video.nationalgeographic.com/video/animals/crittercam-animals/',72,art+'/nga2.png')
        main.addDir('Fish','http://video.nationalgeographic.com/video/animals/fish-animals/',72,art+'/nga2.png')
        main.addDir('Invertebrates','http://video.nationalgeographic.com/video/animals/invertebrates-animals/',72,art+'/nga2.png')
        main.addDir('Mammals','http://video.nationalgeographic.com/video/animals/mammals-animals/',72,art+'/nga2.png')
        main.addDir('Reptiles','http://video.nationalgeographic.com/video/animals/reptiles-animals/',72,art+'/nga2.png')
        main.GA("NationalGeo","NGA")
    elif murl  =='ngk':
        main.addDir('Animals & Pets','http://video.nationalgeographic.com/video/kids/animals-pets-kids/',72,art+'/ngk.png')
        main.addDir('Cartoons & Shows','http://video.nationalgeographic.com/video/kids/cartoons-tv-movies-kids/',72,art+'/ngk.png')
        main.addDir('Explorers','http://video.nationalgeographic.com/video/kids/explorers-kids/',73,art+'/ngk.png')
        main.addDir('Forces of Nature','http://video.nationalgeographic.com/video/kids/forces-of-nature-kids/',73,art+'/ngk.png')
        main.addDir('Green','http://video.nationalgeographic.com/video/kids/green-kids/',73,art+'/ngk.png')
        main.addDir('History','http://video.nationalgeographic.com/video/kids/history-kids/',73,art+'/ngk.png')
        main.addDir('Movies & Books','http://video.nationalgeographic.com/video/kids/movies-books-kids/',73,art+'/ngk.png')
        main.addDir('My Shot Minute','http://video.nationalgeographic.com/video/kids/my-shot-minute-kids/',73,art+'/ngk.png')
        main.addDir('People & Places','http://video.nationalgeographic.com/video/kids/people-places-kids/',73,art+'/ngk.png')
        main.addDir('Science & Space','http://video.nationalgeographic.com/video/kids/science-space-kids/',73,art+'/ngk.png')
        main.addDir('Weird & Wacky','http://video.nationalgeographic.com/video/kids/weird-wacky-kids/',72,art+'/ngk.png')
        main.GA("KidZone","NGK")

def LISTNG(murl):
    MainUrl='http://video.nationalgeographic.com'
    link=main.OPENURL(murl)
    match=re.compile('<a href="(.+?)">More \xc2\xbb</a></p><h3>(.+?)\n        \n    </h3><ul class=".+?"><li><a class=".+?" href=".+?" title=".+?"><img src="(.+?)">').findall(link)
    for url, name, thumb in match:
            main.addDir(name,MainUrl+url,73,MainUrl+thumb)
    main.GA("NationalGeo","NG-Show")
        
def LISTNG2(murl):
    MainUrl='http://video.nationalgeographic.com'
    link=main.OPENURL(murl)
    match2=re.compile('http://video.nationalgeographic.com/video/animals').findall(murl)
    match3=re.compile('http://video.nationalgeographic.com/video/kids').findall(murl)
    match=re.compile('<a href="(.+?)" title="(.+?)"><img src="(.+?)"></a>').findall(link)
    for url, name, thumb in match:
        name=name.replace("&#39;","'").replace('&lt;i&gt;','').replace('&lt;/i&gt;','').replace('&quot;','"').replace('&amp;quot;','"').replace('&amp;','&')
        if (len(match2)==0)and(len(match3)==0):
            main.addPlayMs(name,MainUrl+url,74,MainUrl+thumb,'','','','','')
        else:
            main.addPlayMs(name,MainUrl+url,75,MainUrl+thumb,'','','','','')
    paginate=re.compile("""\n            if ((.+?) === (.+?)) .+?\n                .+?<li><a href="(.+?)">Next &raquo;</a></li>""").findall(link)
    if (len(paginate)>0):
        for pges, pg, pgtot,purl in paginate:
            pg=pg.replace('(','')
            pgtot=pgtot.replace(')','')
            if pgtot!=pg:
                main.addDir('Page '+str(int(pg)+1),MainUrl+purl+pg+'/',73,art+'/next2.png')
    main.GA("NG-Show","List")

def LINKNG(mname,murl):
        main.GA("NatGeo-"+mname,"Watched")
        link=main.OPENURL(murl)
        ok=True
        match=re.compile('property=".+?" content="(.+?)" />\n    <meta property=".+?" content=".+?" />\n    <meta property=".+?" content=".+?" />\n    <meta property=".+?" content=".+?" />\n\n\n    \n    <meta property=".+?" content=".+?" />\n\n    \n    <meta property=".+?" content="(.+?)" />\n\n    \n\n    <meta property=".+?" content="(.+?)" ').findall(link)
        for thumb, desc, vid in match:
                video=vid
        match2=re.compile('<source src="(.+?)" type="video/mp4" />').findall(link)
        for vidurl in match2:
                link2=main.OPENURL(vidurl)
                match3=re.compile('<video src="(.+?)1800.mp4"').findall(link2)
                for hd in match3:
                        hdlink=hd
                match8=re.compile('<video src="(.+?)1800(.+?).mp4"').findall(link2)
                for hd,hd1 in match8:
                        hdlink=hd
                        print hdlink
        match4=re.compile('shows').findall(murl)
        match5=re.compile('specials').findall(murl)
        match6=re.compile('extras').findall(murl)
        match7=re.compile('nat-geo-wild').findall(murl)
        if selfAddon.getSetting("bit-natgeo") == "0":
                try:
                        stream_url = hdlink + '1800.mp4'
                except:
                        stream_url = hdlink + '1800'+hd1+'.mp4'
        elif selfAddon.getSetting("bit-natgeo") == "1":
                if (len(match4)>0)or(len(match5)>0)or(len(match6)>0)or(len(match7)>0):
                        stream_url = hdlink + '660.mp4'
                else:
                        try:
                            stream_url = hdlink + '800.mp4'
                        except:
                            stream_url = hdlink + '800'+hd1+'.mp4'
        elif selfAddon.getSetting("bit-natgeo") == "2":
                if (len(match4)>0)or(len(match5)>0)or(len(match6)>0)or(len(match7)>0):
                        stream_url = hdlink + '220.mp4'
                else:
                        try:
                            stream_url = hdlink + '300.mp4'
                        except:
                            stream_url = hdlink + '300'+hd1+'.mp4'
        elif selfAddon.getSetting("bit-natgeo") == "3":
                try:
                        stream_url = video
                except:
                        stream_url = hdlink + '300.mp4'

        infoL={ "Title": mname, "Plot": desc}
        # play with bookmark
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            wh.add_item(mname+' '+'[COLOR green]NatGeo[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
        player.KeepAlive()
        return ok
        
def LINKNG2(mname,murl):
        main.GA("NatGeo-"+mname,"Watched")
        MainUrl='http://video.nationalgeographic.com'
        link=main.OPENURL(murl)
        ok=True
        descm=re.compile("caption : .+?3E([^<]+)\u003C.+?\u003E',").findall(link)
        for desc in descm:
            desc=desc.replace('3E','').replace('\u0027',"").replace('\u0026#8212\u003B',' ').replace('\u002D',' ')
        thumbm=re.compile('poster : "http://".+?"([^<]+)",').findall(link)
        for thumb in thumbm:
            thumb=MainUrl+thumb
        vlink=re.compile("HTML5src:'(.+?)'").findall(link)
        for vidlink in vlink:
            flink=MainUrl+vidlink
            link2=main.OPENURL(flink)
            match=re.compile('http://(.+?)\n').findall(link2)
            for vlink2 in match:
                vlink2='http://'+vlink2
            if (len(match)==0):
                xbmc.executebuiltin("XBMC.Notification([B]Sorry![/B],No video link available,3000)")
            else:
                bitmatch1=re.compile('1800').findall(vlink2)
                if (len(bitmatch1)>0):
                    stream_url = vlink2
                else:
                    stream_url = vlink2
                bitmatch2=re.compile('660').findall(vlink2)
                if (len(bitmatch1)==0)and(len(bitmatch2)>0):
                    stream_url = vlink2
                else:
                    stream_url = vlink2
            
                infoL={ "Title": mname, "Plot": desc}
                # play with bookmark
                player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
                #WatchHistory
                if selfAddon.getSetting("whistory") == "true":
                    wh.add_item(mname+' '+'[COLOR green]NatGeo[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
                player.KeepAlive()
            return ok
