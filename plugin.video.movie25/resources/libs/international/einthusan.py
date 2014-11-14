import urllib,urllib2,re,cookielib,urlresolver,os,sys,string
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
MainUrl = "http://www.einthusan.com"
MainMovie = "http://www.einthusan.com/movies/"


def MAINFULLS():
        #main.addDir('Search','extra',822,art+'/search.png')
        main.addDir('Tamil','http://www.einthusan.com/index.php?lang=tamil',39,art+'/intl.png')
        main.addDir('Hindi','http://www.einthusan.com/index.php?lang=hindi',39,art+'/intl.png')
        main.addDir('Telugu','http://www.einthusan.com/index.php?lang=telugu',39,art+'/intl.png')
        main.addDir('Malayalam','http://www.einthusan.com/index.php?lang=malayalam',39,art+'/intl.png')
        main.GA("INT","einthusan")
        
def DIRINT(url):
        langID=re.findall('lang=([^<]+)',url)[0]
        main.addDir('Search','http://www.einthusan.com/movies/index.php?lang='+langID+'&organize',419,art+'/search.png')
        main.addDir('A-Z Movies','http://www.einthusan.com/movies/index.php?lang='+langID+'&organize=Alphabetical&filtered=C&org_type=Alphabetical',40,art+'/az2.png')
        main.addDir('Movies Recently Posted','http://www.einthusan.com/movies/index.php?lang='+langID+'&organize=Activity&filtered=RecentlyPosted&org_type=Activity',42,art+'/latest2.png')
        main.addDir('Movies Recently Viewed','http://www.einthusan.com/movies/index.php?lang='+langID+'&organize=Activity&filtered=RecentlyViewed&org_type=Activity',42,art+'/view2.png')
        main.addDir('A-Z bluray','http://www.einthusan.com/bluray/index.php?lang='+langID+'&organize=Alphabetical&filtered=C&org_type=Alphabetical',41,art+'/az2.png')
        main.addDir('Bluray Recently Posted','http://www.einthusan.com/bluray/index.php?lang='+langID+'&organize=Activity&filtered=RecentlyPosted&org_type=Activity',42,art+'/latest2.png')
        main.addDir('Bluray Recently Viewed','http://www.einthusan.com/bluray/index.php?lang='+langID+'&organize=Activity&filtered=RecentlyViewed&org_type=Activity',42,art+'/view2.png')
        main.GA("DIRINT","einthusan")
        
def AZMOVIES(url):
        langID=re.findall('lang=(.+?)&',url)[0]
        main.addDir('0-9','http://www.einthusan.com/movies/index.php?lang='+langID+'&organize=Alphabetical&filtered=Numerical&org_type=Alphabetical',42,art+'/09.png')
        for i in string.ascii_uppercase:
                main.addDir(i,'http://www.einthusan.com/movies/index.php?lang='+langID+'&organize=Alphabetical&filtered='+i+'&org_type=Alphabetical',42,art+'/'+i.lower()+'.png')
        main.GA("einthusan","A-Z Movies")
        main.VIEWSB()
        
def AZBLURAY(url):
        langID=re.findall('lang=(.+?)&',url)[0]
        main.addDir('0-9','http://www.einthusan.com/bluray/index.php?lang='+langID+'&organize=Alphabetical&filtered=Numerical&org_type=Alphabetical',42,art+'/09.png')
        for i in string.ascii_uppercase:
                main.addDir(i,'http://www.einthusan.com/bluray/index.php?lang='+langID+'&organize=Alphabetical&filtered='+i+'&org_type=Alphabetical',42,art+'/'+i.lower()+'.png')
        main.GA("einthusan","A-Z Bluray")
        main.VIEWSB()
        
def LISTINT(murl):
        html = main.OPENURL(murl)
        link=main.unescapes(html)
        match = re.compile('<a class="movie-cover-wrapper" href="(.+?)"><img src="(.+?)" alt="(.+?)"').findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for url,thumb,name in match:
                url=url.replace('../movies/','')
                thumb=thumb.replace('../movies/','')
                name = name.replace('movie online','').replace('tamil','').replace('hindi','').replace('telugu','').replace('malayalam','')
                main.addPlayM(name,MainMovie+url,38,MainMovie+thumb,'','','','','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        paginate = re.compile('<a class="numerical-nav-selected" href=".+?">.+?</a><a href="([^<]+)">.+?</a>').findall(link)
        if len(paginate)>0:
                if 'movies' in murl:
                    main.addDir('[COLOR blue]Next Page >>>[/COLOR]',MainUrl+'/movies/index.php'+paginate[0],42,art+'/next2.png')
                else:
                    main.addDir('[COLOR blue]Next Page >>>[/COLOR]',MainUrl+'/bluray/index.php'+paginate[0],42,art+'/next2.png')
        main.GA("einthusian","List")

def SEARCHEIN(url):
        keyb = xbmc.Keyboard('', 'Search Movies')
        keyb.doModal()
        if (keyb.isConfirmed()):
            search = keyb.getText()
            encode=urllib.quote(search)
            langID=re.findall('lang=(.+?)&',url)[0]
            surl='http://www.einthusan.com/movies/index.php?lang='+langID+'&search='+encode
            link=main.OPENURL(surl)
            match = re.compile('<a class="movie-cover-wrapper" href="(.+?)"><img src="(.+?)" alt="(.+?)"').findall(link)
            for url,thumb,name in match:
                url=url.replace('../movies/','')
                thumb=thumb.replace('../movies/','')
                name = name.replace('movie online','').replace('tamil','').replace('hindi','').replace('telugu','').replace('malayalam','')
                main.addPlayM(name,MainMovie+url,38,MainMovie+thumb,'','','','','')

def LINKINT(mname,url):
        main.GA("Einthusan","Watched")
        ok=True
        MainUrl = "http://www.einthusan.com/movies/"
        link=main.OPENURL(url)
        try:
                match = re.compile("{ 'file': '([^']+)'").findall(link)
                thumb = re.compile('<img src="(../images.+?)"').findall(link)
                thumb=thumb[0].replace('../','http://www.einthusan.com/')
                infoLabels =main.GETMETAT(mname,'','',thumb)
                video_type='movie'
                season=''
                episode=''
                img=infoLabels['cover_url']
                fanart =infoLabels['backdrop_url']
                imdb_id=infoLabels['imdb_id']
                infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }
                desc=' '
                for stream_url in match:
                        continue
        
                infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre']}
                # play with bookmark
                player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=infoLabels['title'],season=season, episode=episode, year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
                #WatchHistory
                if selfAddon.getSetting("whistory") == "true":
                    wh.add_item(mname+' '+'[COLOR green]Einthusan[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=MainUrl+thumb, fanart='', is_folder=False)
                player.KeepAlive()
                return ok
        except Exception, e:
                if stream_url != False:
                    main.ErrorReport(e)
                return ok
