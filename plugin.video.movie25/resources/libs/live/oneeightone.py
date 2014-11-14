import urllib,urllib2,re,cookielib,string
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from t0mm0.common.addon import Addon
import datetime
import time
import os
from resources.libs import main

ADDON=xbmcaddon.Addon(id='plugin.video.movie25')
art = main.art




def MAINFM():
        main.GA("Live","181fm")
        if xbmc.Player().isPlayingAudio():
                main.addPlayc('[COLOR red]Download Current Track Playing[/COLOR]','dummy', 213 ,art+"hubmusic.png",'','','','','')
                main.addPlayc('[COLOR red]Search Current Artist Playing[/COLOR]','dummy', 214,art+"hubmusic2.png",'','','','','')

        link=main.OPENURL('http://www.181.fm/channellistmini.php')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match = re.compile('700"><br>(.+?)</font></td>(.+?)</table>').findall(link)
        for name,url in match:
            name=name.replace('/','&')
            thumb=name.replace(' ','%20')
            main.addDir(name,url,192,art+'/'+thumb+".png")
    

def LISTFM(mname,murl):
        main.GA("181fm","List")
        if xbmc.Player().isPlayingAudio():
                main.addPlayc('[COLOR red]Download Current Track Playing[/COLOR]','dummy', 213 ,art+"hubmusic.png",'','','','','')
                main.addPlayc('[COLOR red]Search Current Artist Playing[/COLOR]','dummy', 214,art+"hubmusic2.png",'','','','','')
        image=mname.replace(' ','%20')
        thumb=art+'/'+"%s.png"%(image)
        match = re.compile('<a STYLE="text-decoration:none" href="(.+?)" class="left_link">(.+?)</a></font></td>').findall(murl)
        for url,name in match:
            main.addPlayL(name,url,193,thumb,'','','','','')


def LINKFM(name,url):
        main.GA("181fm-"+name,"Watched")
        link=main.OPENURL(url)
        source = re.compile('<REF HREF="(.+?)"/>').findall(link)
        for stream_url in source:
                match = re.compile('relay').findall(stream_url)
                print match
                if len(match)>0:
                        stream=stream_url
                else:
                        stream=stream_url
        pl = xbmc.PlayList(xbmc.PLAYLIST_MUSIC)
        pl.clear()    
        pl.add(stream)
        xbmc.Player().play(pl)
        xbmc.executebuiltin("Container.Refresh")

