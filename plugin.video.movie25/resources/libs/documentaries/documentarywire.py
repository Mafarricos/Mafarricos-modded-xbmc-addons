import urllib,urllib2,re,cookielib,urlresolver,os,sys
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

def MAIN():
        main.GA("Documantary","DocumentaryWire")
        main.addDir('Search','s12dnm',229,art+'/search.png')
        main.addDir('Categories','http://www.documentarywire.com',230,art+'/docwire.png')
        main.addDir('Recently Added','http://www.documentarywire.com/browse?orderby=date',227,art+'/docwire.png')
        main.addDir('Popular','http://www.documentarywire.com/browse?orderby=views',227,art+'/docwire.png')
        main.addDir('Most Liked','http://www.documentarywire.com/browse?orderby=likes',227,art+'/docwire.png')
        main.addDir('Controversial','http://www.documentarywire.com/browse?orderby=comments',227,art+'/docwire.png')

def SEARCH(murl):
        if murl=='s12dnm':
            keyb = xbmc.Keyboard('', 'Search Documentaries')
            keyb.doModal()
            if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
                surl='http://www.documentarywire.com/?s='+encode
        else:
            surl=murl
        link=main.OPENURL(surl)
        link=main.unescapes(link)
        match=re.compile('<a class=".+?" data-id=".+?" title="(.+?)" href="(.+?)"><span class=".+?"><img src="(.+?)" alt=".+?" />.+?<p class="desc">(.+?)</p>').findall(link)
        for name,url,thumb,desc in match:
                main.addPlayMs(name,url,228,thumb,desc,'','','','')
        paginate=re.compile("""'extend'>...</span><a href=\'(.+?)\' class="next">Next.+?</a>""").findall(link)
        if (len(paginate)==0):
            paginate=re.compile("""<div class='wp-pagenavi'>.+?class='page larger'>[^\&]+</a><a href=\'([^\&]+)\' class="next">Next.+?</a>""").findall(link)
        if (len(paginate)>0):
            for purl in paginate:
                main.addDir('[COLOR blue]Next[/COLOR]',purl,229,art+'/next2.png')

def CATLIST(murl):
        link=main.OPENURL(murl)
        link=main.unescapes(link)
        match=re.compile('<li class="cat-item cat-item.+?"><a href="(.+?)" title=".+?">(.+?)</a>(.+?)</li>').findall(link)
        for url,name,numb in match:
                main.addDir(name,url,227,art+'/docwire.png')


def LIST(murl):
        main.GA("DocumentaryWire","List")
        link=main.OPENURL(murl)
        link=main.unescapes(link)
        r = re.findall("""<div class="loop-content switchable-view grid-small" data-view="grid-small">(.+?)<div class=\'wp-pagenavi\'>""",link)
        if r:
            match=re.compile('<div class="thumb"><a class=".+?" data-id=".+?" title="(.+?)" href="(.+?)"><span class=".+?"><img src="(.+?)" alt=".+?" />.+?<p class="desc">(.+?)</p>').findall(r[0])
        else:
            match=re.compile('<div class="thumb"><a class=".+?" data-id=".+?" title="(.+?)" href="(.+?)"><span class=".+?"><img src="(.+?)" alt=".+?" />.+?<p class="desc">(.+?)</p>').findall(link)
        for name,url,thumb,desc in match:
                main.addPlayMs(name,url,228,thumb,desc,'','','','')
        paginate=re.compile("""'extend'>...</span><a href=\'(.+?)\' class="next">Next.+?</a>""").findall(link)
        if (len(paginate)==0):
            paginate=re.compile("""<div class='wp-pagenavi'>.+?class='page larger'>[^\&]+</a><a href=\'([^\&]+)\' class="next">Next.+?</a>""").findall(link)
        if (len(paginate)>0):
            for purl in paginate:
                main.addDir('[COLOR blue]Next[/COLOR]',purl,227,art+'/next2.png')


def LINK(mname,murl,thumb,desc):
        link=main.OPENURL(murl)
        link=main.unescapes(link)
        ok=True
        try:
            match=re.compile('src="http://www.youtube.com/embed/(.+?).?autoplay=1&cc_load_policy=0.+?"').findall(link)
            if match:
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Opening Link,3000)")
                stream_url = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+match[0]+"&hd=1"
            match2=re.compile('src="http://player.vimeo.com/video/(.+?)"').findall(link)
            if match2:
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                stream_url = main.resolve_url(str('http://vimeo.com/'+match2[0]))
                if(stream_url == False):
                    xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                    return
            infoL={'Title': mname, 'Plot': desc}
            # play with bookmark
            player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
            #WatchHistory
            if selfAddon.getSetting("whistory") == "true":
                wh.add_item(mname+' '+'[COLOR green]Doc-Wire[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
            player.KeepAlive()
            return ok
        except Exception, e:
            if stream_url != False:
                    main.ErrorReport(e)
            else:
                    xbmc.executebuiltin("XBMC.Notification(Sorry!,Link deleted Or unplayable,5000)")
            return ok
        main.GA("DocumentaryWire","Watched")

