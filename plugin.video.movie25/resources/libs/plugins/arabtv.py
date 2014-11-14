#-*- coding: utf-8 -*-
import urllib,re,string,urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
prettyName = '3Arabtv'
MAINURL='http://3arabtv.com'



def MAIN3arabtv():
    main.addDir('Search (بحث)','aflam',354,art+'/search.png')
    main.addDir('Movies','movies',352,art+'/3arabtv.png')
    main.addDir('Series','series',352,art+'/3arabtv.png')
    main.addDir('Shows','shows',352,art+'/3arabtv.png')
    main.addDir('Clips','clips',352,art+'/3arabtv.png')
    main.GA("Plugin","3Arabtv")
    
def CAT3arabtv(murl):
    if 'movies'in murl:
        main.addDir('All','http://3arabtv.com/movies',353,art+'/3arabtv.png')
        main.addDir('Comedy Movies','http://3arabtv.com/movies/category/comedy-channels',353,art+'/3arabtv.png')
        main.addDir('Old Movies','http://3arabtv.com/movies/category/old-movies',353,art+'/3arabtv.png')
        main.addDir('Plays','http://3arabtv.com/movies/category/plays',353,art+'/3arabtv.png')
    if 'series'in murl:
        main.addDir('All','http://3arabtv.com/series',353,art+'/3arabtv.png')
        main.addDir('Khaliji','http://3arabtv.com/series/category/khaliji-series',353,art+'/3arabtv.png')
        main.addDir('Jordanian','http://3arabtv.com/series/category/jordan-series',353,art+'/3arabtv.png')
        main.addDir('Historic','http://3arabtv.com/series/category/historic',353,art+'/3arabtv.png')
        main.addDir('Indian','http://3arabtv.com/series/category/indian-series',353,art+'/3arabtv.png')
        main.addDir('Iranian','http://3arabtv.com/series/category/iranian-series',353,art+'/3arabtv.png')
        main.addDir('Comedy','http://3arabtv.com/series/category/comedy-series',353,art+'/3arabtv.png')
        main.addDir('Turkish','http://3arabtv.com/series/category/turkish-series',353,art+'/3arabtv.png')
        main.addDir('Mexican','http://3arabtv.com/series/category/mexican-series',353,art+'/3arabtv.png')
        main.addDir('Syrian','http://3arabtv.com/series/category/syrian-series',353,art+'/3arabtv.png')
        main.addDir('Egyptian','http://3arabtv.com/series/category/egyptian-series',353,art+'/3arabtv.png')
        main.addDir('Lebanese','http://3arabtv.com/series/category/lebanese-series',353,art+'/3arabtv.png')
    if 'shows'in murl:
        main.addDir('All','http://3arabtv.com/shows',353,art+'/3arabtv.png')
        main.addDir('Documentary','http://3arabtv.com/shows/category/documentary',353,art+'/3arabtv.png')
        main.addDir('Variety','http://3arabtv.com/shows/category/television-show',353,art+'/3arabtv.png')
        main.addDir('Sport','http://3arabtv.com/shows/category/sport',353,art+'/3arabtv.png')
        main.addDir('Health','http://3arabtv.com/shows/category/health',353,art+'/3arabtv.png')
        main.addDir('Religious','http://3arabtv.com/shows/category/religious-show',353,art+'/3arabtv.png')
        main.addDir('Beauty','http://3arabtv.com/shows/category/beauty-show',353,art+'/3arabtv.png')
        main.addDir('Talk Shows','http://3arabtv.com/shows/category/talk-shows',353,art+'/3arabtv.png')
        main.addDir('Music','http://3arabtv.com/shows/category/music-shows',353,art+'/3arabtv.png')
        main.addDir('Competition','http://3arabtv.com/shows/category/competition-shows',353,art+'/3arabtv.png')
        main.addDir('Quiz','http://3arabtv.com/shows/category/quiz-shows',353,art+'/3arabtv.png')
        main.addDir('Political','http://3arabtv.com/shows/category/political',353,art+'/3arabtv.png')
        main.addDir('Comdy','http://3arabtv.com/shows/category/comdy',353,art+'/3arabtv.png')
        main.addDir('Technology','http://3arabtv.com/shows/category/technology',353,art+'/3arabtv.png')
    if 'clips'in murl:
        main.addDir('All','http://3arabtv.com/clips',353,art+'/3arabtv.png')
        main.addDir('Arabic Music','http://3arabtv.com/clips/category/arabic-music',353,art+'/3arabtv.png')
        main.addDir('Trailers','http://3arabtv.com/clips/category/trailers',353,art+'/3arabtv.png')

        
def SEARCHarabtv():
        keyb = xbmc.Keyboard('', 'Search Movies & Shows')
        keyb.doModal()
        if (keyb.isConfirmed()):
            search = keyb.getText()
            encode=urllib.quote(search)
            surl='http://3arabtv.com/search?radio=All&s='+encode+'&submit-search=Search'
            LIST3arabtv(surl)

def LIST3arabtv(murl):
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('&raquo;','').replace('&rarr;','')
    match=re.compile("""><img src="([^<]+)".+?<a href="([^<]+)">([^<]+)</a></span>""",re.DOTALL).findall(link)
    for thumb,url,name in match:
        thumb=thumb.split('"')[0]
        if 'http' not in thumb:
            thumb=MAINURL+thumb
        thumb=thumb.replace(' ','')
        if 'Episodes' in name or 'Shows' in name:
            name2=re.compile('href="'+url+'">'+name+'</a></span>.+?><a href=".+?">([^<]+)</a>',re.DOTALL).findall(link)
            if name2:
                name2=name2[0]
            else:
                name2=''
            main.addDir('[COLOR red]'+name+'[/COLOR] '+name2,MAINURL+url,356,thumb)
        else:
            if 'Clips' in name or 'Movies' in name:
                name2=re.compile('href="'+url+'">'+name+'</a></span>.+?><a href=".+?">([^<]+)</a>',re.DOTALL).findall(link)
                if name2:
                    name2=name2[0]
                else:
                    name2=''
                main.addPlayc('[COLOR red]'+name+'[/COLOR] '+name2,MAINURL+url,355,thumb,'','','','','')
            else:
                main.addPlayc(name,MAINURL+url,355,thumb,'','','','','')

    paginate = re.compile('''<a class="page" href="([^<]+)">Next''').findall(link)
    if len(paginate)>0:
        main.addDir('Next',MAINURL+paginate[0],353,art+'/next2.png')                
    main.GA("3Arabtv","List")



def LIST3arabtvEPI(murl,thumb):
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('&raquo;','').replace('&rarr;','')
    match=re.compile("""<h5><a href="([^<]+)">([^<]+)</a></h5>""",re.DOTALL).findall(link)
    for url,name in match:
        main.addPlayc(name,MAINURL+url,355,thumb,'','','','','')


def resolveVID(murl):
    murl=murl.split('"')[0]
    murl=main.unescapes(murl)
    link=main.OPENURL(murl)
    match=re.compile('"http://www.youtube.com/v/([^<]+)"',re.DOTALL).findall(link)
    if match:
        vlink=main.resolve_url('http://www.youtube.com/v/'+match[0])
    match2=re.compile('mediaId=([^<]+)&&defaultQuality',re.DOTALL).findall(link)
    if match2:
        link2=main.OPENURL('http://hadynz-shahid.appspot.com/scrape?m='+match2[0])
        vlinks=re.compile('{"Quality":"(.+?)","URL":"(.+?)"}',re.DOTALL).findall(link2)
        for qua,links in vlinks:
            if '720' in qua:
                vlink=links   
            else:
                vlink=links
    return vlink

def LINKS3arabtv(mname,murl,thumb):
    main.GA("3Arabtv","Watched")
    xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,5000)")
    link=main.OPENURL(murl)
    ok=True
    match=re.compile('<iframe id="playerframe" src="([^<]+)"',re.DOTALL).findall(link)
    if match:
        stream_url=resolveVID(MAINURL+match[0].replace('/inter.php?u=',''))
    else:
         return
    try:
        if stream_url == False: return                                                            
        infoL={'Title': mname, 'Plot': '', 'Genre': '', 'originaltitle': mname}
        # play with bookmark
        stream_url=stream_url.replace(' ','%20')
        from resources.universal import playbackengine
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            from resources.universal import watchhistory
            wh = watchhistory.WatchHistory(addon_id)
            wh.add_item(mname+' '+'[COLOR green]3Arabtv[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
        player.KeepAlive()
        return True
    except Exception, e:
        if stream_url != False: main.ErrorReport(e)
        return False
