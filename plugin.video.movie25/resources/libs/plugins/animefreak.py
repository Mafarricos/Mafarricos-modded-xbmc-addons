# -*- coding: cp1252 -*-
import urllib,urllib2,re,cookielib,string, urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,urlresolver
from t0mm0.common.net import Net as net
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
from resources.universal import playbackengine, watchhistory
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art

wh = watchhistory.WatchHistory('plugin.video.movie25')

def AtoZ():
        main.addDir('#','http://www.animefreak.tv/book',629,art+'/09.png')
        for i in string.ascii_uppercase:
            main.addDir(i,'http://www.animefreak.tv/book',629,art+'/'+i.lower()+'.png')
        main.GA("Tvshows","A-ZTV")
        main.VIEWSB()

def MAIN():
        main.GA("Plugin","AnimeFreak")
        main.addDir('Search','http://www.animefreak.tv',638,art+'/search.png')
        main.addDir('A-Z','http://www.animefreak.tv',628,art+'/AZ.png')
        main.addDir('Genre','http://www.animefreak.tv/browse',634,art+'/genre.png')
        main.addDir('Popular Anime','http://www.animefreak.tv/watch/popular-animes',637,art+'/animefreak.png')
        main.addDir('Latest Episodes','http://www.animefreak.tv/tracker',632,art+'/animefreak.png')
        main.addDir('Latest Anime','http://www.animefreak.tv/latest',633,art+'/animefreak.png')


def SEARCH():
        keyb = xbmc.Keyboard('', 'Search Anime')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
                surl='http://www.animefreak.tv/search/node/'+encode
        link=main.OPENURL(surl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match= re.compile('<dt class="title".+?a href="(.+?)">(.+?)</a.+?dt>').findall(link)
        for url,name in match:
                r = re.findall('Episode',name)
                if not r:
                        main.addDirT(name,url,626,'','','','','','')
                else:
                        main.addDirT(name,url,630,'','','','','','')

def GENRE(murl):
        link=main.OPENURL(murl)
        link=main.unescapes(link)
        match = re.compile('<input type="checkbox" name="taxonomy.+?" id=".+?" value=".+?"   class="form-checkbox" /> (.+?)</label>').findall(link)
        for name in match:
                uname=name
                uname=uname.replace(' ','-')
                if uname == 'Slice-of-Life':
                        uname='slice-life'
                main.addDir(name,'http://www.animefreak.tv/category/genre/'+uname.lower(),635,'')

def GENRELIST(murl):
        link=main.OPENURL(murl)
        link=main.unescapes(link)
        match = re.compile('<h2 class="nodeTitle">.+?<a href="(.+?)".+?src="(.+?)" alt="(.+?)" />').findall(link)
        for url, thumb,name in match:
                main.addDirT(name,'http://www.animefreak.tv/'+url,626,thumb,'','','','','')
        paginate = re.compile("""<li class="pager-next"><a href="(.+?)" title=".+?" class="active">.+?</a></li>""").findall(link)
        if len(paginate)>0:
            paginates=paginate[0]
            main.addDir('Next','http://www.animefreak.tv/'+paginates,635,art+'/next2.png')
        

def AZLIST(mname,murl):
        if mname=='#':
            link=main.OPENURL(murl)
            link=main.unescapes(link)
            match = re.compile('<li><a href="([^<]+)">(.+?)</a></li>').findall(link)
            for url, name in match[0:10]:
                main.addDirT(name,'http://www.animefreak.tv/'+url,626,'','','','','','')
        else:
            link=main.OPENURL(murl)
            link=main.unescapes(link)
            match = re.compile('<li><a href="([^<]+)">(.+?)</a></li>').findall(link)
            for url, name in match:
                if name[0]==mname or name[0]==mname.lower():
                    main.addDirT(name,'http://www.animefreak.tv/'+url,626,'','','','','','')
            
def LATESTE(mname,murl):
        link=main.OPENURL(murl)
        link=main.unescapes(link)
        match = re.compile('<td class=".+?<a href="(.+?)">(.+?)</a>          </td>').findall(link)
        for url, name in match:
                main.addDirT(name,'http://www.animefreak.tv/'+url,630,'','','','','','')
        paginate = re.compile("""<li class="pager-next last"><a href="(.+?)" class="active">.+?</a></li>""").findall(link)
        if len(paginate)>0:
            paginates=paginate[0]
            main.addDir('Next','http://www.animefreak.tv/'+paginates,632,art+'/next2.png')

def LATESTA(mname,murl):
        link=main.OPENURL(murl)
        link=main.unescapes(link)
        match = re.compile('<td class=".+?<a href="(.+?)">(.+?)</a>          </td>').findall(link)
        for url, name in match:
                main.addDirT(name,'http://www.animefreak.tv/'+url,626,'','','','','','')
        paginate = re.compile("""<li class="pager-next last"><a href="(.+?)" class="active">.+?</a></li>""").findall(link)
        if len(paginate)>0:
            paginates=paginate[0]
            main.addDir('Next','http://www.animefreak.tv/'+paginates,633,art+'/next2.png')        

def LISTPOP(murl):
        link=main.OPENURL(murl)
        link=main.unescapes(link)
        match = re.compile('<div><span><img alt=".+?" src="(.+?)" /></span></div>            </td>            <td .+?>            <h2><a href="(.+?)"><strong>(.+?)</strong></a></h2>').findall(link)
        for thumb,url, name in match:
                main.addDirT(name,url,626,thumb,'','','','','')
                
def LIST(mname,murl):
        link=main.OPENURL(murl)
        link=main.unescapes(link)
        match = re.compile('<li class="leaf.+?<a href="([^<]+)">(.+?)</a></li>').findall(link)
        thumbs = re.compile('</p><p><img align="left".+?src="(.+?)".+?>').findall(link)
        if thumbs:
            thumb=thumbs[0]
        else:
            thumb=''
        descs = re.compile('<h2><span style=".+?"><strong>.+?</strong></span></h2><blockquote><p>(.+?)</p>').findall(link)
        if descs:
            desc=descs[0]
        else:
            desc=''
        for url, name in match:
                main.addDirT(name,'http://www.animefreak.tv/'+url,630,thumb,desc,'','','','')


def LIST2(mname,murl,thumb,desc):
        main.GA("AnimeFreak","List")
        link=main.OPENURL(murl)
        link=main.unescapes(link)
        match = re.compile("""onClick="javascript:loadParts.?\'(.+?)', \'\'.?" class="multi">(.+?)</a>""").findall(link)
        
        if len(match)==0:
            match = re.compile('<iframe .+?src="(.+?)".+?/iframe>').findall(link)
            for url in match:
                host=re.compile("http://(.+?).?/.+?").findall(url)
                for hname in host:
                        name=hname.replace('www.','').replace('embed.','').replace('.co','').replace('.t','').replace('.e','')
                main.addPlayc(mname+' [COLOR red]'+name+'[/COLOR]',url,627,thumb,desc,'','','','')
        else:
            for url, name in match:
                    match2 = re.compile('<iframe(.+?)/iframe>').findall(url)
                    if len(match2)>=2:
                            for url in match2:
                                match = re.compile('src="(.+?)"').findall(url)
                                if len(match)==0:
                                    match = re.compile("src='(.+?)'").findall(url)
                                for url in match:
                                        host=re.compile("http://(.+?).?/.+?").findall(url)
                                        for hname in host:
                                                name=hname.replace('www.','').replace('embed.','').replace('.co','').replace('.t','').replace('.e','')
                                                main.addPlayc(mname+' [COLOR red]'+name+'[/COLOR]',url,627,thumb,desc,'','','','')
                    
                    main.addPlayc(mname+' [COLOR red]'+name+'[/COLOR]',url,627,thumb,desc,'','','','')

def NovaWeed(murl):
        link=main.OPENURL(murl)
        link=main.unescapes(link)
        vw = re.compile('flashvars.advURL="(.+?)";').findall(link)
        vid_url=vw[0]
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
        return main.resolve_url(vid_url)

def Upload2(murl):
        link=main.OPENURL(murl)
        link=main.unescapes(link)
        vw = re.compile("1&video=(.+?)&rating").findall(link)
        if vw:
                stream_url = vw[0]
        else:
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Removed,4000)")
                stream_url =''
        return stream_url

def Sapo(murl):
        match=re.compile('/play\?file=([^\&]+)').findall(murl)
        newlink='http://videos.sapo.pt/playhtml?file=' + match[0]
        link=main.OPENURL(newlink)
        link=main.unescapes(link)
        link = ''.join(link.splitlines()).replace('\'','"')
        match1=re.compile('showEmbedHTML\("swfplayer", (.+?), "(.+?)"\);').findall(link)
        for time,token in match1:
                stream_url = match[0]+"?player=EXTERNO&time="+time+"&token="+token;
        return stream_url


def LINK(mname,murl,thumb,desc):
        
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        link=main.unescapes(murl)
        match = re.compile('src="(.+?)"').findall(link)
        if len(match)==0:
            match = re.compile("src='(.+?)'").findall(link)
            if len(match)==0:
                r = re.findall('animefreak',murl)
                if r:
                        link=main.OPENURL(murl)
                        link=main.unescapes(link)
                        match = re.compile('src="http://www.animefreak.tv/sites/default/files/af/misc/player.swf.?file=(.+?)"').findall(link)
                        print 'HH1 '+match[0]
                        s = re.findall('http://.+?/(.+?).mp4.?(.+?)e=([^\&]+)',match[0])
                        for p1,p2,p3 in s:
                                p1=p1.replace('+','%20')
                                stream_url='http://78.152.42.214/'+p1+'.mp4?'+p2+'e='+p3

                nv = re.findall('novamov',murl)
                if nv:
                                stream_url = NovaWeed(murl)
                v = re.findall('videoweed',murl)
                if v:
                                stream_url = NovaWeed(murl)

                m = re.findall('mp4upload',murl)
                if m:
                                link=main.OPENURL(murl)
                                link=main.unescapes(link)
                                vw = re.compile("'file': '(.+?)',").findall(link)
                                stream_url = vw[0]

                vb = re.findall('videobam',murl)
                if vb:
                                link=main.OPENURL(murl)
                                link=main.unescapes(link)
                                vw = re.compile("low: '(.+?)'").findall(link)
                                if len(vw)==0:
                                        vw = re.compile("high: '(.+?)'").findall(link)
                                stream_url = vw[0]
                u2 = re.findall('upload2',murl)
                if u2:        
                         stream_url = Upload2(murl)
                sp = re.findall('sapo',murl)
                if sp:
                        stream_url=Sapo(murl)

                af = re.findall('.mp4',murl)
                if len(af)>0 and len(r)==0 and len(m)==0 and len(vb)==0 and len(u2)==0 and len(sp)==0: 
                                murl=murl.replace("'","").replace("+","%20")
                                print "hh q "+murl
                                stream_url=murl
            else:
                nv = re.findall('novamov',match[0])
                if nv:
                                stream_url = NovaWeed(match[0])
                v = re.findall('videoweed',match[0])
                if v:
                                stream_url = NovaWeed(match[0])

                m = re.findall('mp4upload',match[0])
                if m:
                                link=main.OPENURL(match[0])
                                link=main.unescapes(link)
                                vw = re.compile("'file': '(.+?)',").findall(link)
                                stream_url = vw[0]

                vb = re.findall('videobam',match[0])
                if vb:
                                link=main.OPENURL(match[0])
                                link=main.unescapes(link)
                                vw = re.compile("low: '(.+?)'").findall(link)
                                if len(vw)==0:
                                        vw = re.compile("high: '(.+?)'").findall(link)
                                stream_url = vw[0]
                u2 = re.findall('upload2',match[0])
                if u2:
                        stream_url = Upload2(match[0])
                sp = re.findall('sapo',match[0])
                if sp:
                        stream_url=Sapo(match[0])
                      
        else:
                r = re.findall('animefreak',match[0])
                if r:
                        link=main.OPENURL(match[0])
                        link=main.unescapes(link)
                        match = re.compile('src="http://www.animefreak.tv/sites/default/files/af/misc/player.swf.?file=(.+?)"').findall(link)
                        print 'HH2 '+match[0]
                        s = re.findall('http://.+?/(.+?).mp4.?(.+?)e=([^\&]+)',match[0])
                        for p1,p2,p3 in s:
                                p1=p1.replace('+','%20')
                                stream_url='http://78.152.42.214/'+p1+'.mp4?'+p2+'e='+p3
                        
                nv = re.findall('novamov',match[0])
                if nv:
                                stream_url = NovaWeed(match[0])
                v = re.findall('videoweed',match[0])
                if v:
                                stream_url = NovaWeed(match[0])

                m = re.findall('mp4upload',match[0])
                if m:
                                link=main.OPENURL(match[0])
                                link=main.unescapes(link)
                                vw = re.compile("'file': '(.+?)',").findall(link)
                                stream_url = vw[0]

                vb = re.findall('videobam',match[0])
                if vb:
                                link=main.OPENURL(match[0])
                                link=main.unescapes(link)
                                vw = re.compile("low: '(.+?)'").findall(link)
                                if len(vw)==0:
                                        vw = re.compile("high: '(.+?)'").findall(link)
                                stream_url = vw[0]
                u2 = re.findall('upload2',match[0])
                if u2:
                        stream_url = Upload2(match[0])
                        
                sp = re.findall('sapo',match[0])
                if sp:
                        stream_url=Sapo(match[0])
                        

        infoL={'Title': mname, 'Plot': desc, 'Genre': 'Anime'} 
        

        # play with bookmark
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
        #WatchHistory
        main.GA("AnimeFreak","Watched")
        if selfAddon.getSetting("whistory") == "true":
            wh.add_item(mname+' '+'[COLOR green]AFTv[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
        player.KeepAlive()
        return ok
            
