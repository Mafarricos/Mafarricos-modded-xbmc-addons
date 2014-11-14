import urllib,urllib2,re,cookielib,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
def DESISTREAMS():
        main.GA("Live","Desistreams")
        main.addDir('Sports','sports',130,art+'/desistream.png')
        main.addDir('English Channels','english',130,art+'/desistream.png')
        main.addDir('Indian Channels','indian',130,art+'/desistream.png')
        main.addDir('Pakistani Channels','pakistani',130,art+'/desistream.png')
        main.addDir('Bangladeshi Channels','bangladeshi',130,art+'/desistream.png')

def DESISTREAMSList(murl):
        link=main.OPENURL('http://www.desistreams.tv/')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        if murl=='sports':
                main.GA("Desi-Sport","Watched")
                link=main.OPENURL('https://nkjtvt.googlecode.com/svn/trunk/Desi/desiSports.xml')
                link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                match=re.compile('<item><titl[^>]+>([^<]+)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail></item>').findall(link)
                for name,url,thumb in sorted(match):
                    main.addLink(name,url,thumb)
        elif murl=='english':
                main.GA("Desi-English","Watched")
                link=main.OPENURL('https://nkjtvt.googlecode.com/svn/trunk/Desi/desiEnglish.xml')
                link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                match=re.compile('<item><titl[^>]+>([^<]+)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail></item>').findall(link)
                for name,url,thumb in sorted(match):
                    main.addLink(name,url,thumb)
        elif murl=='indian':
                main.GA("Desi-Indian","Watched")
                link=main.OPENURL('https://nkjtvt.googlecode.com/svn/trunk/Desi/desihind.xml')
                link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                match=re.compile('<item><titl[^>]+>([^<]+)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail></item>').findall(link)
                for name,url,thumb in sorted(match):
                    main.addLink(name,url,thumb)
        elif murl=='pakistani':
                main.GA("Desi-Pakistani","Watched")
                link=main.OPENURL('https://nkjtvt.googlecode.com/svn/trunk/Desi/desipak.xml')
                link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                match=re.compile('<item><titl[^>]+>([^<]+)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail></item>').findall(link)
                for name,url,thumb in sorted(match):
                    main.addLink(name,url,thumb)
        elif murl=='bangladeshi':
                main.GA("Desi-Bangla","Watched")
                link=main.OPENURL('https://nkjtvt.googlecode.com/svn/trunk/Desi/desibang.xml')
                link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                match=re.compile('<item><titl[^>]+>([^<]+)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail></item>').findall(link)
                for name,url,thumb in sorted(match):
                    main.addLink(name,url,thumb)

def DESISTREAMSLink(mname,murl):
        link=main.OPENURL(murl)
        main.GA("Desi-Indian","Watched")
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        ok=True
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<script type=\'text/javascript\'> width=(.+?), height=(.+?), channel=\'(.+?)\', g=\'.+?\';</script><script type=\'text/javascript\' src=\'(.+?)\'>').findall(link)
        for wid,hei,fid,streamer in match[0:1]:
                continue
        if len(match)==0:
            match=re.compile('<script type=\'text/javascript\'>fid=\'(.+?)\'; v_width=(.+?); v_height=(.+?);</script><script type=\'text/javascript\' src=\'(.+?)\'>').findall(link)
            for fid,wid,hei,streamer in match[0:1]:
                continue
        livecaster = re.compile("livecaster").findall(streamer)
        if len(livecaster)>0:
            pageUrl='http://www.livecaster.tv/embed.php?u='+fid+'&vw='+wid+'&vh='+hei
            if mname=='Live Footy' or mname=='PTV Sports'or mname=='Ten Sports':
                if fid=='ptvsportsss1':
                    fid='onlineptvsports'
                    stream_url ='rtmp://cdn.livecaster.tv/broadcast playpath='+fid+' swfUrl=http://www.livecaster.tv/player/player.swf pageUrl='+pageUrl
                elif fid=='TenSportsLive':
                    fid='1155200'
                    stream_url ='rtmp://cdn.livecaster.tv/broadcast playpath='+fid+' swfUrl=http://www.livecaster.tv/player/player.swf pageUrl='+pageUrl
            else:
                if fid =='Geosuper':
                    fid='13246540114814'
                elif fid=='ten_sports9':
                    fid='ten_sports9.stream'
                elif fid=='wwe2':
                    fid='wwe2.stream'
                stream_url ='rtmp://cdn.livecaster.tv/stream playpath='+fid+' swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl='+pageUrl
            
        ukcast = re.compile("ukcast").findall(streamer)
        if len(ukcast)>0:
            pageUrl='http://www.ukcast.tv/embed.php?u='+fid+'&vw='+wid+'&vh='+hei
            if mname=='PTV Sports 2'or mname=='JSC Sports +2':
                stream_url ='rtmp://live.ukcast.tv/broadcast playpath='+fid+' swfUrl=http://www.ukcast.tv/player/player.swf pageUrl='+pageUrl
            else:
                if fid=='espnukk':
                    fid='espn_uk'
                stream_url ='rtmp://live.ukcast.tv/broadcast playpath='+fid+'.stream swfUrl=http://www.ukcast.tv/player/player.swf pageUrl='+pageUrl
        listitem = xbmcgui.ListItem(mname)
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        return ok
