#-*- coding: utf-8 -*-
import urllib,re,string,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
prettyName = 'Yify'
subpages = 4

def MAIN():
    main.addDir('Search','extra',424,art+'/search.png')
    main.addDir('Releases','http://yify.tv/files/releases/',422,art+'/new.png')
    main.addDir('Last Added','http://yify.tv/files/movies/',422,art+'/latest.png')
    main.addDir('Popular','http://yify.tv/popular/',422,art+'/view.png')
    main.addDir('IMDB Rating','http://yify.tv/files/movies/?meta_key=imdbRating&orderby=meta_value&order=desc',422,art+'/vote.png')
    main.addDir('Genre','genre',426,art+'/genre.png')
    main.addDir('Year','year',426,art+'/year.png')
    main.addDir('Language','lang',426,art+'/intl.png')
    main.GA("Plugin","Yify")

def LIST(murl,subp = False):
    global subpages
    if subp: subpages = subp
    parts = murl.partition('%%%')
    murl = parts[0]
    page = re.search('(?i)page\/(\d+?)\/',murl)
    if page: page = int(page.group(1))
    else: page = 1
    max = page * subpages
    if parts[-1]:
        parts = parts[-1].partition('$$$')
        max = int(parts[0])
        if parts[-1]: subpages = int(parts[-1])
    urls = []
    for n in range(subpages):
        if page + n > max: break
        if re.search('[^\d]\/$',murl): urls.append(murl + 'page/'+str(page + n) + '/')
        elif re.search('movies\/\?',murl): urls.append(murl.replace('movies/?', 'movies/page/'+str(page + n) + '/?'))
        else: urls.append(re.sub('page\/\d+?\/', 'page/'+str(page + n) + '/',murl))
    link=main.batchOPENURL(urls).replace('\\/','/')
    link=link.replace('\r','').replace('\n','').replace('\t','')
    match=re.compile('{"ID":.+?,"title":"(.*?)","link":"(.*?)","post_content":"(.*?)","image":"(.*?)","slidercap":"(.*?)","year":"(.*?)","genre":"(.*?)","director":".+?}',re.DOTALL).findall(link)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Movie list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
    xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")
    for name,url,desc,thumb,fan,year,genre in match:
        main.addPlayM(name+' [COLOR red]('+year+')[/COLOR]',url,423,thumb,desc,fan,'',genre,year)
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if dialogWait.iscanceled(): break
    dialogWait.close()
    del dialogWait
    paginate = re.compile('''<a class="nextpostslink" href="([^<]+)">.+?</a>''',re.DOTALL).findall(link)
    if len(paginate) == subpages and loadedLinks >= totalLinks:
        last = re.search('(?i)<a class="last" href="[^"]+?/page/(\d+)/[^"]*?">Last',link)
        if last: last = int(last.group(1))
        else:
            last = re.findall('(?i)<a class="page larger" href="[^"]+?/page/(\d+)/[^"]*?">',link)
            if last: last = int(last[-1])
            else: last = page + subpages
        main.addDir('[COLOR red]Enter Page #[/COLOR]',paginate[0]+'%%%'+str(subpages),427,art+'/gotopage.png')
        main.addDir('Page ' + str(page/subpages+1) + ' [COLOR blue]Next Page >>>[/COLOR]',re.sub('page\/\d+?\/', 'page/'+str(page+subpages)+'/',paginate[0])+'%%%'+str(last)+'$$$'+str(subpages),422,art+'/next2.png')     
    main.GA("Yify","List")
    main.VIEWS()

def GotoPage(url):
    parts = url.partition('%%%')
    url = parts[0]
    page = re.search('(?i)page\/(\d+?)\/',url)
    if page: page = int(page.group(1))
    else: page = 1
    try: subp = int(parts[-1])
    except: subp = 1
    link=main.OPENURL(url)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    last = re.search('(?i)<a class="last" href="[^"]+?/page/(\d+)/[^"]*?">Last',link)
    if last: last = int(last.group(1))
    else:
        last = re.findall('(?i)<a class="page larger" href="[^"]+?/page/(\d+)/[^"]*?">',link)
        if last: last = int(last[-1])
        else: last = page
    dialog = xbmcgui.Dialog()
    pagelimit=((last+subp-1)/subp)
    d = dialog.numeric(0, 'Section Last Page = '+str(pagelimit))
    if d:
        if int(d) <= pagelimit:
            d = 1 + (int(d) - 1) * subp 
            surl = re.sub('page\/\d+?\/', 'page/'+str(d) + '/',url)
            LIST(surl+'%%%'+str(last))
        else:
            dialog = xbmcgui.Dialog()
            ret = dialog.ok('Wrong Entry', 'The page number you entered does not exist.',' This sections page limit is '+str(pagelimit) )
    else:
        xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False)
        return False

def SortBy(murl):
    if 'genre' in murl:
        main.addDir('Action','http://yify.tv/genre/action/',422,art+'/folder.png')
        main.addDir('Adventure','http://yify.tv/genre/adventure/',422,art+'/folder.png')
        main.addDir('Animation','http://yify.tv/genre/animation/',422,art+'/folder.png')
        main.addDir('Comedy','http://yify.tv/genre/comedy/',422,art+'/folder.png')
        main.addDir('Crime','http://yify.tv/genre/crime/',422,art+'/folder.png')
        main.addDir('Drama','http://yify.tv/genre/drama/',422,art+'/folder.png')
        main.addDir('Fantasy','http://yify.tv/genre/fantasy/',422,art+'/folder.png')
        main.addDir('Horror','http://yify.tv/genre/horror/',422,art+'/folder.png')
        main.addDir('Biography','http://yify.tv/genre/biography/',422,art+'/folder.png')
        main.addDir('Thriller','http://yify.tv/genre/thriller/',422,art+'/folder.png')
        main.addDir('Documentary','http://yify.tv/genre/documentary/',422,art+'/folder.png')
        main.addDir('Family','http://yify.tv/genre/family/',422,art+'/folder.png')
        main.addDir('History','http://yify.tv/genre/history/',422,art+'/folder.png')
        main.addDir('Music','http://yify.tv/genre/music/',422,art+'/folder.png')
        main.addDir('Mistery','http://yify.tv/genre/mistery/',422,art+'/folder.png')
        main.addDir('Romance','http://yify.tv/genre/romance/',422,art+'/folder.png')
        main.addDir('Sci-Fi','http://yify.tv/genre/sci-fi/',422,art+'/folder.png')
        main.addDir('Sport','http://yify.tv/genre/sport/',422,art+'/folder.png')
        main.addDir('War','http://yify.tv/genre/war/',422,art+'/folder.png')
        main.addDir('Western','http://yify.tv/genre/western/',422,art+'/folder.png')
        main.addDir('Short','http://yify.tv/genre/short/',422,art+'/folder.png')
        main.addDir('Film-Noir','http://yify.tv/genre/film-noir/',422,art+'/folder.png')
    if 'lang' in murl:
        main.addDir('Arabic','http://yify.tv/languages/arabic/',422,art+'/folder.png')
        main.addDir('Bulgarian','http://yify.tv/languages/bulgarian/',422,art+'/folder.png')
        main.addDir('Chinese','http://yify.tv/languages/chinese/',422,art+'/folder.png')
        main.addDir('Croatian','http://yify.tv/languages/croatian/',422,art+'/folder.png')
        main.addDir('Dutch','http://yify.tv/languages/dutch/',422,art+'/folder.png')
        main.addDir('English','http://yify.tv/languages/english/',422,art+'/folder.png')
        main.addDir('Finnish','http://yify.tv/languages/finnish/',422,art+'/folder.png')
        main.addDir('French','http://yify.tv/languages/french/',422,art+'/folder.png')
        main.addDir('German','http://yify.tv/languages/german/',422,art+'/folder.png')
        main.addDir('Greek','http://yify.tv/languages/greek/',422,art+'/folder.png')
        main.addDir('Hebrew','http://yify.tv/languages/hebrew/',422,art+'/folder.png')
        main.addDir('Hindi','http://yify.tv/languages/hindi/',422,art+'/folder.png')
        main.addDir('Hungarian','http://yify.tv/languages/hungarian/',422,art+'/folder.png')
        main.addDir('Icelandic','http://yify.tv/languages/icelandic/',422,art+'/folder.png')
        main.addDir('Italian','http://yify.tv/languages/italian/',422,art+'/folder.png')
        main.addDir('Japanese','http://yify.tv/languages/japanese/',422,art+'/folder.png')
        main.addDir('Korean','http://yify.tv/languages/korean/',422,art+'/folder.png')
        main.addDir('Norwegian','http://yify.tv/languages/norwegian/',422,art+'/folder.png')
        main.addDir('Persian','http://yify.tv/languages/persian/',422,art+'/folder.png')
        main.addDir('Polish','http://yify.tv/languages/polish/',422,art+'/folder.png')
        main.addDir('Portuguese','http://yify.tv/languages/portuguese/',422,art+'/folder.png')
        main.addDir('Punjabi','http://yify.tv/languages/punjabi/',422,art+'/folder.png')
        main.addDir('Romanian','http://yify.tv/languages/romanian/',422,art+'/folder.png')
        main.addDir('Russian','http://yify.tv/languages/russian/',422,art+'/folder.png')
        main.addDir('Spanish','http://yify.tv/languages/spanish/',422,art+'/folder.png')
        main.addDir('Swedish','http://yify.tv/languages/swedish/',422,art+'/folder.png')
        main.addDir('Turkish','http://yify.tv/languages/turkish/',422,art+'/folder.png')
    if 'year' in murl:
        main.addDir('2013','http://yify.tv/years/2013/',422,art+'/folder.png')
        main.addDir('2012 ','http://yify.tv/years/2012/',422,art+'/folder.png')
        main.addDir('2011','http://yify.tv/years/2011/',422,art+'/folder.png')
        main.addDir('2010 ','http://yify.tv/years/2010/',422,art+'/folder.png')
        main.addDir('2009 ','http://yify.tv/years/2009/',422,art+'/folder.png')
        main.addDir('2008','http://yify.tv/years/2008/',422,art+'/folder.png')
        main.addDir('2007 ','http://yify.tv/years/2007/',422,art+'/folder.png')
        main.addDir('2006 ','http://yify.tv/years/2006/',422,art+'/folder.png')
        main.addDir('2005','http://yify.tv/years/2005/',422,art+'/folder.png')
        main.addDir('Enter Year','com',428,art+'/enteryear.png')


def ENTYEAR():
    dialog = xbmcgui.Dialog()
    d = dialog.numeric(0, 'Enter Year')
    if d:
        encode=urllib.quote(d)
        if encode < '2014' and encode > '1900':
            surl='http://yify.tv/years/'+encode+'/'
            LIST(surl,1)
        else:
            dialog = xbmcgui.Dialog()
            ret = dialog.ok('Wrong Entry', 'Must enter year in four digit format like 1999','Enrty must be between 1900 and 2014')
    

def Searchhistory():
    seapath=os.path.join(main.datapath,'Search')
    SeaFile=os.path.join(seapath,'SearchHistory25')
    if not os.path.exists(SeaFile):
        murl='sec'
        SEARCH(murl)
    else:
        main.addDir('Search','sec',425,art+'/search.png')
        main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
        thumb=art+'/link.png'
        searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
        for seahis in reversed(searchis):
            url=seahis
            seahis=seahis.replace('%20',' ')
            main.addDir(seahis,url,425,thumb)
            
def superSearch(encode,type):
    try:
        returnList=[]
        surl='http://yify.tv/?s='+encode
        link = main.OPENURL(surl,verbose=False).replace('\\/','/')
        link=link.replace('\r','').replace('\n','').replace('\t','')
        match=re.compile('{"ID":.+?,"title":"(.*?)","link":"(.*?)","post_content":".*?","image":"(.*?)","slidercap":".*?","year":"(.*?)","genre":".*?","director":".+?}',re.DOTALL).findall(link)
        for title,url,thumb,year in match:
            returnList.append((title.strip() + " (" + year + ")",prettyName,url,thumb,423,False))
        return returnList            
    except: return []
    
def SEARCH(encode):
    main.GA("Yify","Search")
    encode = main.updateSearchFile(encode,'Movies','sec','Search For Movies')
    if not encode: return False
    surl='http://yify.tv/?s='+encode
    LIST(surl,1)

def LINK(name,murl,thumb):
    xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,5000)")
    main.GA("Yify","Watched")
    stream_url = False
    ok=True
    infoLabels =main.GETMETAT(name,'','',thumb)
    video_type='movie'
    season=''
    episode=''
    img=infoLabels['cover_url']
    fanart =infoLabels['backdrop_url']
    imdb_id=infoLabels['imdb_id']
    infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }  
    stream_url = main.resolve_url(murl)
    try:
        infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre'], 'originaltitle': infoLabels['metaName']}
        # play with bookmark
        from resources.universal import playbackengine
        if stream_url: main.CloseAllDialogs()
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=infoLabels['title'],season=season, episode=episode, year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            from resources.universal import watchhistory
            wh = watchhistory.WatchHistory(addon_id)
            wh.add_item(name+' '+'[COLOR green]Yify[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=img, fanart='', is_folder=False)
        player.KeepAlive()
        return ok
    except Exception, e:
        if stream_url != False:
            main.ErrorReport(e)
        return ok
