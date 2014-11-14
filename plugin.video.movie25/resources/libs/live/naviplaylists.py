import urllib,urllib2,re,cookielib
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)



def playlists():
        link=main.OPENURL('https://nkjtvt.googlecode.com/svn/trunk/playlistDir.xml')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('type=playlistname=Sorted by user-assigned order','').replace('name=Sorted [COLOR=FF00FF00]by user-assigned order[/COLOR]','').replace('name=Live Tv Channels Twothumb','')
        thumb="%s/art/folder.png"%selfAddon.getAddonInfo("path")
        match=re.compile('<name>(.+?)</name><link>(.+?)</link><thumbnail>.+?</thumbnail><mode>(.+?)</mode>').findall(link)
        for name,url,mode in match:
            main.addDir(name,url,int(mode),thumb)
        main.GA("Live","Playlists")

        

def playlistList(mname,murl):
        main.GA("Playlists-"+mname,"Watched")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('type=playlistname=Sorted by user-assigned order','').replace('name=Sorted [COLOR=FF00FF00]by user-assigned order[/COLOR]','').replace('name=Live Tv Channels Twothumb','')
        match=re.compile('name=(.+?)thumb=(.+?)date=.+?URL=(.+?)#').findall(link)
        for name,thumb,url in match:
                match2=re.compile('http://(.+?)URL').findall(thumb)
                if len(match2)>0:
                        thumb ='http://'+match2[0]
                url=url.replace('player=defaultrating=-1.00','').replace('%20',' ').replace('player=default','').replace(' conn=S:OK --live','').replace(' conn=S:OK','')
                match3=re.compile('rtmp').findall(url)
                match4=re.compile('timeout').findall(url)
                if len(match3)>0 and len(match4)==0:
                        url=url+' timeout=15'
                main.addLink(name,url,thumb)
        
def playlistList2(mname,murl):
        main.GA("Playlists-"+mname,"Watched")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('name=Sorted by user-assigned order','').replace('name=Sorted [COLOR=FF00FF00]by user-assigned order[/COLOR]','').replace('name=[COLOR=FFFFD700] Sky Sports Channels Live HD [/COLOR] [COLOR=FF00FFFF]','').replace('thumb=http://coloradorushrfc.org/home/wp-content/uploads/2010/11/foxsoccer_logo.jpg','')
        match=re.compile('name=(.+?)date.+?URL=(.+?)#').findall(link)
        for name,url in match[0:9]:
                url=url.replace('player=defaultrating=-1.00','')
                match3=re.compile('rtmp').findall(url)
                match4=re.compile('timeout').findall(url)
                if len(match3)>0 and len(match4)==0:
                        url=url+' timeout=15'
                main.addLink(name,url,'')
        
def playlistList3(mname,murl):
        main.GA("Playlists-"+mname,"Watched")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('type=playlistname=Sorted by user-assigned order','').replace('name=Sorted [COLOR=FF00FF00]by user-assigned order[/COLOR]','').replace('name=Live Tv Channels Twothumb','')
        match=re.compile('name=(.+?)thumb=(.+?)date=.+?URL=(.+?)#').findall(link)
        for name,thumb,url in match:
                match2=re.compile('http://(.+?)URL').findall(thumb)
                if len(match2)>0:
                        thumb ='http://'+match2[0]
                url=url.replace('player=defaultrating=-1.00','')
                match3=re.compile('rtmp').findall(url)
                match4=re.compile('timeout').findall(url)
                if len(match3)>0 and len(match4)==0:
                        url=url+' timeout=15'
                main.addLink(name,url,thumb)
        match=re.compile('name=(.+?)thumb=(.+?)URL=(.+?)#').findall(link)
        for name,thumb,url in match:
                match2=re.compile('http://(.+?)URL').findall(thumb)
                if len(match2)>0:
                        thumb ='http://'+match2[0]
                url=url.replace('player=defaultrating=-1.00','').replace('%20',' ').replace('player=default','')
                match3=re.compile('rtmp').findall(url)
                match4=re.compile('timeout').findall(url)
                if len(match3)>0 and len(match4)==0:
                        url=url+' timeout=15'
                main.addLink(name,url,thumb)
        
def playlistList4(mname,murl):
        main.GA("Playlists-"+mname,"Watched")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('type=playlistname=Sorted by user-assigned order','').replace('name=Sorted [COLOR=FF00FF00]by user-assigned order[/COLOR]','').replace('name=Live Tv Channels Twothumb','')
        match=re.compile('name=(.+?)thumb=(.+?)URL=(.+?)#').findall(link)
        for name,thumb,url in match:
                match2=re.compile('http://(.+?)URL').findall(thumb)
                if len(match2)>0:
                        thumb ='http://'+match2[0]
                url=url.replace('player=defaultrating=-1.00','').replace('%20',' ').replace('player=default','').replace(' conn=S:OK --live','').replace(' conn=S:OK','')
                match3=re.compile('rtmp').findall(url)
                match4=re.compile('timeout').findall(url)
                if len(match3)>0 and len(match4)==0:
                        url=url+' timeout=15'
                main.addLink(name,url,thumb)
        
def playlistList5(mname,murl):
        main.GA("Playlists-"+mname,"Watched")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('date=',' ').replace('\t','').replace('&nbsp;','').replace('name=Sorted by user-assigned order','').replace('name=Sorted [COLOR=FF00FF00]by user-assigned order[/COLOR]','').replace('name=[COLOR=FFFFD700] Sky Sports Channels Live HD [/COLOR] [COLOR=FF00FFFF]','').replace('thumb=http://coloradorushrfc.org/home/wp-content/uploads/2010/11/foxsoccer_logo.jpg','')
        match=re.compile('name=(.+?)URL=(.+?)#').findall(link)
        for name,url in sorted(match):
                url=url.replace('player=defaultrating=-1.00','')
                match3=re.compile('rtmp').findall(url)
                match4=re.compile('timeout').findall(url)
                if len(match3)>0 and len(match4)==0:
                        url=url+' timeout=15'
                main.addLink(name,url,'')
        

def playlistList6(mname,murl):
        main.GA("Playlists-"+mname,"Watched")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('type=playlistname=Sorted by user-assigned order','').replace('name=Sorted [COLOR=FF00FF00]by user-assigned order[/COLOR]','').replace('name=Live Tv Channels Twothumb','')
        match=re.compile('<item><titl[^>]+>([^<]+)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail></item>').findall(link)
        for name,url,thumb in sorted(match):
            main.addLink(name,url,thumb)
        

def playlistList7(mname,murl):
        main.GA("Playlists-"+mname,"Watched")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('name=Sorted by user-assigned order','').replace('name=Sorted [COLOR=FF00FF00]by user-assigned order[/COLOR]','').replace('name=[COLOR=FFFFD700] Sky Sports Channels Live HD [/COLOR] [COLOR=FF00FFFF]','').replace('thumb=http://coloradorushrfc.org/home/wp-content/uploads/2010/11/foxsoccer_logo.jpg','')
        match=re.compile('name=(.+?)date.+?URL=(.+?)#').findall(link)
        for name,url in match:
                url=url.replace('player=defaultrating=-1.00','')
                match3=re.compile('rtmp').findall(url)
                match4=re.compile('timeout').findall(url)
                if len(match3)>0 and len(match4)==0:
                        url=url+' timeout=15'
                main.addLink(name,url,'')
