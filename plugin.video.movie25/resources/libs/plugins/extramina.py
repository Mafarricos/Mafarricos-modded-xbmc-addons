#-*- coding: utf-8 -*-
import urllib,re,string,urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
prettyName = 'Watching Now'

def MAINEXTRA():
        main.addDir('Search','extra',535,art+'/search.png')
        #main.addDir('A-Z','http://seriesgate.tv/',538,art+'/azex.png')
        main.addDir('Latest Releases','http://www.watching-now.com/',532,art+'/latest.png')
        main.addDir('Popular','http://www.watching-now.com/search/label/Popular',532,art+'/view.png')
        main.addDir('Featured','http://www.watching-now.com/search/label/Featured',532,art+'/feat.png')
        main.addDir('In Theaters','http://www.watching-now.com/search/label/In-Theaters',532,art+'/watchingnow.png')
        main.addDir('2013','http://www.watching-now.com/search/label/2013',532,art+'/year.png')
        main.addDir('MMA','http://www.watching-now.com/search/label/MMA',532,art+'/mma.png')
        main.addDir('Stand-Up Comedy','http://www.watching-now.com/search/label/Stand-Up%20Comedy',532,art+'/com.png')
        main.addDir('Genre','http://www.extraminamovies.in/',533,art+'/genre.png')
        main.GA("Plugin","Watching Now")
        main.VIEWSB()
        
def LISTEXrecent(murl):     
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\xc2\xa0','')
        match=re.compile("""<h3 class='post-title entry-title'><a href='([^<]+)'>(.+?)</a>.+?src="(.+?)".+?""",re.DOTALL).findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for url, name,thumb in match:
                main.addPlayM(name,url,536,thumb,'','','','','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        paginate = re.compile("<a class='blog-pager-older-link' href='(.+?)' id='.+?' title='Next Movie Page'>Next Page.+?</a>").findall(link)
        if len(paginate)>0 and len(match) == 20:
                main.addDir('Next',paginate[0],532,art+'/next2.png')
                
        main.GA("Watching Now","Recent")

def LISTEXgenre(murl):     
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\xc2\xa0','')
        match=re.compile('<a itemprop="url" href="(.+?)" rel=".+?" title="Permanent Link to (.+?)"><img itemprop="thumbnailUrl" alt=".+?" class="smallposter" src="(.+?)"></a>.+?<span itemprop="description">(.+?)</span>').findall(link)
        if len(match)==0:
                match = re.compile('<h1 class="post-title"><a href="([^<]+)" rel=".+?" title=".+?">([^<]+)</a></h1><img style=.+? src="(.+?)">(.+?)<div').findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for url, name, thumb,desc in match:
                main.addPlayM(name,url,536,thumb,desc,'','','','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        paginate = re.compile("<a href='([^<]+)' class='nextpostslink'>�</a>").findall(link)
        if len(paginate)>0:
                main.addDir('Next',paginate[0],531,art+'/next2.png')
        main.GA("Watching Now","Recent")

def GENREEXTRA(murl):
        main.addDir('Action','http://www.watching-now.com/search/label/Action',532,art+'/act.png')
        main.addDir('Adventure','http://www.watching-now.com/search/label/Adventure',532,art+'/adv.png')
        main.addDir('Animation','http://www.watching-now.com/search/label/Animation',532,art+'/ani.png')
        main.addDir('Biography','http://www.watching-now.com/search/label/Biography',532,art+'/bio.png')
        main.addDir('Bollywood','http://www.watching-now.com/search/label/Bollywood',532,art+'/bollyw.png')
        main.addDir('Comedy','http://www.watching-now.com/search/label/Comedy',532,art+'/com.png')
        main.addDir('Crime','http://www.watching-now.com/search/label/Crime',532,art+'/cri.png')
        main.addDir('Documentary','http://www.watching-now.com/search/label/Documentary',532,art+'/doc.png')
        main.addDir('Drama','http://www.watching-now.com/search/label/Drama',532,art+'/dra.png')
        main.addDir('Family','http://www.watching-now.com/search/label/Family',532,art+'/fam.png')
        main.addDir('Fantasy','http://www.watching-now.com/search/label/Fantasy',532,art+'/fant.png')
        main.addDir('History','http://www.watching-now.com/search/label/History',532,art+'/his.png')        
        main.addDir('Horror','http://www.watching-now.com/search/label/Horror',532,art+'/hor.png')
        main.addDir('Music','http://www.watching-now.com/search/label/Music',532,art+'/mus.png')
        main.addDir('Mystery','http://www.watching-now.com/search/label/Mystery',532,art+'/mys.png')
        main.addDir('Romance','http://www.watching-now.com/search/label/Romance',532,art+'/rom.png')
        main.addDir('Sci-Fi','http://www.watching-now.com/search/label/Sci-Fi',532,art+'/sci.png')
        main.addDir('Sport','http://www.watching-now.com/search/label/Sports',532,art+'/spo.png')
        main.addDir('Thriller','http://www.watching-now.com/search/label/Thriller',532,art+'/thr.png')
        main.addDir('War','http://www.watching-now.com/search/label/War',532,art+'/war.png')
        main.addDir('Western','http://www.watching-now.com/search/label/Western',532,art+'/west.png')
        main.GA("Watching Now","Genre")
        main.VIEWSB()

def AtoZEXTRA():
        main.addDir('#','http://www.extraminamovies.in/list-of-movies/?pgno=293#char_22',531,art+'/pound.png')
        main.addDir('0-9','http://www.extraminamovies.in/list-of-movies/?pgno=1#char_31',531,art+'/09.png')
        main.addDir('A','http://www.extraminamovies.in/list-of-movies/?pgno=6#char_41',531,art+'/A.png')
        main.addDir('B','http://www.extraminamovies.in/list-of-movies/?pgno=24#char_42',531,art+'/B.png')
        main.addDir('C','http://www.extraminamovies.in/list-of-movies/?pgno=44#char_43',531,art+'/C.png')
        main.addDir('D','http://www.extraminamovies.in/list-of-movies/?pgno=60#char_44',531,art+'/D.png')
        main.addDir('E','http://www.extraminamovies.in/list-of-movies/?pgno=75#char_45',531,art+'/E.png')
        main.addDir('F','http://www.extraminamovies.in/list-of-movies/?pgno=81#char_46',531,art+'/F.png')
        main.addDir('G','http://www.extraminamovies.in/list-of-movies/?pgno=92#char_47',531,art+'/G.png')
        main.addDir('H','http://www.extraminamovies.in/list-of-movies/?pgno=99#char_48',531,art+'/H.png')
        main.addDir('I','http://www.extraminamovies.in/list-of-movies/?pgno=112#char_49',531,art+'/I.png')
        main.addDir('J','http://www.extraminamovies.in/list-of-movies/?pgno=120#char_4a',531,art+'/J.png')
        main.addDir('K','http://www.extraminamovies.in/list-of-movies/?pgno=125#char_4b',531,art+'/K.png')
        main.addDir('L','http://www.extraminamovies.in/list-of-movies/?pgno=130#char_4c',531,art+'/L.png')
        main.addDir('M','http://www.extraminamovies.in/list-of-movies/?pgno=141#char_4d',531,art+'/M.png')
        main.addDir('N','http://www.extraminamovies.in/list-of-movies/?pgno=156#char_4e',531,art+'/N.png')
        main.addDir('O','http://www.extraminamovies.in/list-of-movies/?pgno=162#char_4f',531,art+'/O.png')
        main.addDir('P','http://www.extraminamovies.in/list-of-movies/?pgno=166#char_50',531,art+'/P.png')
        main.addDir('Q','http://www.extraminamovies.in/list-of-movies/?pgno=177#char_51',531,art+'/Q.png')
        main.addDir('R','http://www.extraminamovies.in/list-of-movies/?pgno=178#char_52',531,art+'/R.png')
        main.addDir('S','http://www.extraminamovies.in/list-of-movies/?pgno=188#char_53',531,art+'/S.png')
        main.addDir('T','http://www.extraminamovies.in/list-of-movies/?pgno=214#char_54',531,art+'/T.png')
        main.addDir('U','http://www.extraminamovies.in/list-of-movies/?pgno=273#char_55',531,art+'/U.png')
        main.addDir('V','http://www.extraminamovies.in/list-of-movies/?pgno=278#char_56',531,art+'/V.png')
        main.addDir('W','http://www.extraminamovies.in/list-of-movies/?pgno=279#char_57',531,art+'/W.png')
        main.addDir('X','http://www.extraminamovies.in/list-of-movies/?pgno=289#char_58',531,art+'/X.png')
        main.addDir('Y','http://www.extraminamovies.in/list-of-movies/?pgno=289#char_59',531,art+'/Y.png')
        main.addDir('Z','http://www.extraminamovies.in/list-of-movies/?pgno=291#char_5a',531,art+'/Z.png')
        main.GA("Watching Now","AZ")
        main.VIEWSB()
        


def SearchhistoryEXTRA():
    seapath=os.path.join(main.datapath,'Search')
    SeaFile=os.path.join(seapath,'SearchHistory25')
    if not os.path.exists(SeaFile):
        url='extra'
        SEARCHEXTRA(url)
    else:
        main.addDir('Search','extra',534,art+'/search.png')
        main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
        thumb=art+'/link.png'
        searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
        for seahis in reversed(searchis):
            url=seahis
            seahis=seahis.replace('%20',' ')
            main.addDir(seahis,url,534,thumb)
            
def superSearch(encode,type):
    try:
        returnList=[]
        surl='http://www.watching-now.com/search?q='+encode+'&x=-911&y=-656'
        link=main.OPENURL(surl,verbose=False)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile("""<h3 class='post-title entry-title'><a href='([^<]+)'>(.+?)</a>.+?src="(.+?)".+?""",re.DOTALL).findall(link)
        for url, name,thumb in match:
            returnList.append((name,prettyName,url,thumb,536,True))
        return returnList
    except: return []       
        
def SEARCHEXTRA(murl):
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistory25')
        try:
            os.makedirs(seapath)
        except:
            pass
        if murl == 'extra':
            keyb = xbmc.Keyboard('', 'Search Movies')
            keyb.doModal()
            if (keyb.isConfirmed()):
                    search = keyb.getText()
                    encode=urllib.quote(search)
                    surl='http://www.watching-now.com/search?q='+encode+'&x=-911&y=-656'
                    if not os.path.exists(SeaFile) and encode != '':
                        open(SeaFile,'w').write('search="%s",'%encode)
                    else:
                        if encode != '':
                            open(SeaFile,'a').write('search="%s",'%encode)
                    searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
                    for seahis in reversed(searchis):
                        continue
                    if len(searchis)>=10:
                        searchis.remove(searchis[0])
                        os.remove(SeaFile)
                        for seahis in searchis:
                            try:
                                open(SeaFile,'a').write('search="%s",'%seahis)
                            except:
                                pass
        else:
                encode = murl
                surl='http://www.watching-now.com/search?q='+encode+'&x=-911&y=-656'
        link=main.OPENURL(surl)
        link=link.replace('\xc2\xa0','').replace('\n','')
        match=re.compile("""<h3 class='post-title entry-title'><a href='([^<]+)'>(.+?)</a>.+?src="(.+?)".+?""",re.DOTALL).findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for url, name, thumb in match:
            main.addPlayM(name,url,536,thumb,'','','','','')
            loadedLinks = loadedLinks + 1
            percent = (loadedLinks * 100)/totalLinks
            remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
            dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
            if (dialogWait.iscanceled()):
                    return False   
        dialogWait.close()
        del dialogWait
        main.GA("Watching Now","Search")


def getlink(murl,url):
    print "openurl = " + url
    import urllib2
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    req.add_header('Referer', murl)
    req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
    conn = urllib2.urlopen(req)
    link = conn.read()
    conn.close()
    return link

def VIDEOLINKSEXTRA(mname,murl,thumb,desc):
        main.GA("Watching Now","Watched")
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Collecting hosts,5000)")
        sources = []
        link=main.OPENURL(murl)
        ok=True
        infoLabels =main.GETMETAT(mname,'','',thumb)
        video_type='movie'
        season=''
        episode=''
        img=infoLabels['cover_url']
        fanart =infoLabels['backdrop_url']
        imdb_id=infoLabels['imdb_id']
        infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }
        
        match=re.compile('<strong><a href="(.+?)" target=".+?">(.+?)</a>',re.DOTALL).findall(link)
        import urlresolver
        for url, host in match:
                link2=getlink(murl,url)
                xurl=re.findall('var click_url = "(.+?)";',link2)[0]
                hosted_media = urlresolver.HostedMediaFile(url=xurl, title=host)
                sources.append(hosted_media)        
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Show doesn't have playable links,5000)")
      
        else:
                source = urlresolver.choose_source(sources)
        try:
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                stream_url = main.resolve_url(source.get_url())
                if(stream_url == False):
                    return
                
                infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre']}
                # play with bookmark
                from resources.universal import playbackengine
                player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=str(infoLabels['title']),season=str(season), episode=str(episode), year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
                #WatchHistory
                if selfAddon.getSetting("whistory") == "true":
                    from resources.universal import watchhistory
                    wh = watchhistory.WatchHistory(addon_id)
                    wh.add_item(mname+' '+'[COLOR green]Watching Now[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=img, fanart='', is_folder=False)
                player.KeepAlive()
                return ok
        except Exception, e:
                if stream_url != False:
                        main.ErrorReport(e)
                return ok
