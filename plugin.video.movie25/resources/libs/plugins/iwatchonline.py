import urllib,urllib2,re,string,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
prettyName = 'iWatchOnline'

def AtoZiWATCHtv(index=False):
    main.addDir('0-9','http://www.iwatchonline.to/tv-show?startwith=09&p=0',589,art+'/09.png',index=index)
    for i in string.ascii_uppercase:
            main.addDir(i,'http://www.iwatchonline.to/tv-show?startwith='+i.lower()+'&p=0',589,art+'/'+i.lower()+'.png',index=index)
    main.GA("Tvshows","A-ZTV")
    main.VIEWSB()

def AtoZiWATCHm(index=False):
    main.addDir('0-9','http://www.iwatchonline.to/movies?startwith=09&p=0',587,art+'/09.png',index=index)
    for i in string.ascii_uppercase:
            main.addDir(i,'http://www.iwatchonline.to/movies?startwith='+i.lower()+'&p=0',587,art+'/'+i.lower()+'.png',index=index)
    main.GA("Movies","A-ZM")
    main.VIEWSB()

def iWatchMAIN():
    main.addDir('Movies','http://www.iwatchonline.org/',586,art+'/iwatchm.png')
    main.addDir('Tv Shows','http://www.iwatchonline.org/',585,art+'/iwatcht.png')
    main.addDir('Todays Episodes','http://www.iwatchonline.to/tv-schedule',592,art+'/iwatcht.png')
    main.GA("Plugin","iWatchonline")
    main.VIEWSB2()
        
def iWatchMOVIES(index=False):
    main.addDir('Search Movies','http://www.iwatchonline.to',644,art+'/search.png',index=index)
    main.addDir('A-Z','http://www.iwatchonline.to',595,art+'/az.png',index=index)
    main.addDir('Popular','http://www.iwatchonline.to/movies?sort=popular&p=0',587,art+'/view2.png',index=index)
    main.addDir('Latest Added','http://www.iwatchonline.to/movies?sort=latest&p=0',587,art+'/latest2.png',index=index)
    main.addDir('Featured Movies','http://www.iwatchonline.to/movies?sort=featured&p=0',587,art+'/feat2.png',index=index)
    main.addDir('Latest HD Movies','http://www.iwatchonline.to/movies?quality=hd&sort=latest&p=0',587,art+'/new2.png',index=index)
    main.addDir('Genre','http://www.iwatchonline.to',596,art+'/genre2.png',index=index)
    main.addDir('By Year','http://www.iwatchonline.so/',652,art+'/year2.png',index=index)
    main.GA("iWatchonline","Movies")
    main.VIEWSB2()

def iWatchTV(index=False):
    main.addDir('Search TV Shows','http://www.iwatchonline.to',642,art+'/search.png',index=index)
    main.addDir('A-Z','http://www.iwatchonline.to',593,art+'/az.png',index=index)
    main.addDir('Todays Episodes','http://www.iwatchonline.to/tv-schedule',592,art+'/iwatcht.png',index=index)
    main.addDir('Featured Shows','http://www.iwatchonline.to/tv-show?sort=featured&p=0',589,art+'/iwatcht.png',index=index)
    main.addDir('Popular Shows','http://www.iwatchonline.to/tv-show?sort=popular&p=0',589,art+'/iwatcht.png',index=index)
    main.addDir('Latest Additions','http://www.iwatchonline.to/tv-show?sort=latest&p=0',589,art+'/iwatcht.png',index=index)
    main.addDir('Genre','http://www.iwatchonline.to',594,art+'/genre.png',index=index)
    main.GA("iWatchonline","Tvshows")
    main.VIEWSB2()

def SearchhistoryTV(index=False):
    seapath=os.path.join(main.datapath,'Search')
    SeaFile=os.path.join(seapath,'SearchHistoryTv')
    if not os.path.exists(SeaFile):
        SEARCHTV()
    else:
        main.addDir('Search TV Shows','###',643,art+'/search.png',index=index)
        main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
        thumb=art+'/link.png'
        searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
        for seahis in reversed(searchis):
            seahis=seahis.replace('%20',' ')
            url=seahis
            main.addDir(seahis,url,643,thumb,index=index)
            
def superSearch(encode,type):
    try:
        if type=='Movies': type='m'
        else: type='t'
        returnList=[]
        search_url = 'http://www.iwatchonline.to/search'
        from t0mm0.common.net import Net as net
        encodewithoutepi = urllib.quote(re.sub('(?i)(\ss(\d+)e(\d+))|(Season(.+?)Episode)|(\d+)x(\d+)','',urllib.unquote(encode)).strip())
        search_content = net().http_POST(search_url, { 'searchquery' : encodewithoutepi, 'searchin' : type} ).content.encode('utf-8')
        r = re.findall('(?s)<table(.+?)</table>',search_content)
        r=main.unescapes(r[0])
        epi = re.search('(?i)s(\d+?)e(\d+?)$',encode)
        if epi:
            epistring = encode.rpartition('%20')[2].upper()

        match=re.compile('<img.+?src=\"(.+?)\".+?<a.+?href=\"(.+?)\">(.+?)</a>').findall(r)
        for thumb,url,name in match:
            if type=='m':
                returnList.append((name,prettyName,url,thumb,588,True))
            else:
                if epi:
                    url = url.replace('/tv-shows/','/episode/')+'-'+epistring.lower()
                    name=re.sub('(\d{4})','',name.replace(' (','').replace(')',''))
                    returnList.append((name + ' ' + epistring,prettyName,url,thumb,588,True))
                else:

                    returnList.append((name,prettyName,url,thumb,590,True))
        return returnList
    except: return []

def SEARCHTV(murl = '',index=False):
    encode = main.updateSearchFile(murl,'TV')
    if not encode: return False   
    search_url = 'http://www.iwatchonline.to/search'
    from t0mm0.common.net import Net as net
    search_content = net().http_POST(search_url, { 'searchquery' : encode, 'searchin' : 't'} ).content.encode('utf-8')
    r = re.findall('(?s)<table(.+?)</table>',search_content)
    r=main.unescapes(r[0])
    match=re.compile('<img[^>]+?src="([^"]+?)\".+?<a[^>]+?href="([^"]+?)">([^<]+?)</a>').findall(r)
    for thumb,url,name in match:
        main.addDirT(name,url,590,thumb,'','','','','',index=index)
    main.GA("iWatchonline","Search")

def SearchhistoryM(index=False):
    seapath=os.path.join(main.datapath,'Search')
    SeaFile=os.path.join(seapath,'SearchHistory25')
    if not os.path.exists(SeaFile):
        SEARCHM('')
    else:
        main.addDir('Search Movies','###',645,art+'/search.png',index=index)
        main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
        thumb=art+'/link.png'
        searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
        for seahis in reversed(searchis):
            seahis=seahis.replace('%20',' ')
            url=seahis
            main.addDir(seahis,url,645,thumb,index=index)

def SEARCHM(murl,index=False):
    encode = main.updateSearchFile(murl,'Movies')
    if not encode: return False   
    search_url = 'http://www.iwatchonline.to/search'
    from t0mm0.common.net import Net as net
    search_content = net().http_POST(search_url, { 'searchquery' : encode, 'searchin' : 'm'} ).content.encode('utf-8')
    r = re.findall('(?s)<table(.+?)</table>',search_content)
    r=main.unescapes(r[0])
    match=re.compile('<img.+?src=\"(.+?)\".+?<a.+?href=\"(.+?)\">(.+?)</a>').findall(r)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Movie list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
    xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")
    for thumb,url,name in match:
        if index == 'True':
            main.addDirM(name,url,21,thumb,'','','','','')
        else:
            main.addDirM(name,url,588,thumb,'','','','','')
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if dialogWait.iscanceled(): return False   
    dialogWait.close()
    del dialogWait
    main.GA("iWatchonline","Search")

def ENTYEAR(index=False):
    dialog = xbmcgui.Dialog()
    d = dialog.numeric(0, 'Enter Year')
    if d:
        encode=urllib.quote(d)
        if encode < '2014' and encode > '1900':
             surl='http://www.iwatchonline.to/movies?year='+encode+'&p=0'
             iWatchLISTMOVIES(surl,index=index)
        else:
            dialog = xbmcgui.Dialog()
            ret = dialog.ok('Wrong Entry', 'Must enter year in four digit format like 1999','Enrty must be between 1900 and 2014')

def GotoPage(url,index=False):
    dialog = xbmcgui.Dialog()
    r=re.findall('http://www.iwatchonline.to/movies(.+?)&p=.+?',url)
    d = dialog.numeric(0, 'Please Enter Page number.')
    if d:
        temp=int(d)-1
        page= int(temp)*25
        encode=str(page)
        url='http://www.iwatchonline.to/movies'+r[0]
        surl=url+'&p='+encode
        iWatchLISTMOVIES(surl,index=index)
    else:
        dialog = xbmcgui.Dialog()
        xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False)
        return False
        
def iWatchGenreTV(index=False):
    link=main.OPENURL('http://www.iwatchonline.to/tv-show')
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.compile('<li.+?a href=".?gener=([^<]+)">(.+?)</a>.+?/li>').findall(link)
    for url,genre in match:
        genre=genre.replace('  ','')
        if not 'Adult' in genre:
            main.addDir(genre,'http://www.iwatchonline.to/tv-show?sort=popular&gener='+url+'&p=0',589,art+'/folder.png',index=index)
    main.GA("Tvshows","GenreT")
    
def iWatchGenreM(index=False):
    link=main.OPENURL('http://www.iwatchonline.to/movies')
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.compile('<li.+?a href=".?gener=([^<]+)">(.+?)</a>.+?/li>').findall(link)
    for url,genre in match:
        genre=genre.replace('  ','')
        if not 'Adult' in genre:
            main.addDir(genre,'http://www.iwatchonline.to/movies?sort=popular&gener='+url+'&p=0',587,art+'/folder.png',index=index)
    main.GA("Movies","GenreM")     
               
def iWatchYearM(index=False):
    main.addDir('2013','http://www.iwatchonline.to/movies?year=2013&p=0',587,art+'/year.png',index=index)
    main.addDir('2012','http://www.iwatchonline.to/movies?year=2012&p=0',587,art+'/2012.png',index=index)
    main.addDir('2011','http://www.iwatchonline.to/movies?year=2011&p=0',587,art+'/2011.png',index=index)
    main.addDir('2010','http://www.iwatchonline.to/movies?year=2010&p=0',587,art+'/2010.png',index=index)
    main.addDir('2009','http://www.iwatchonline.to/movies?year=2009&p=0',587,art+'/2009.png',index=index)
    main.addDir('2008','http://www.iwatchonline.to/movies?year=2008&p=0',587,art+'/2008.png',index=index)
    main.addDir('2007','http://www.iwatchonline.to/movies?year=2007&p=0',587,art+'/2007.png',index=index)
    main.addDir('2006','http://www.iwatchonline.to/movies?year=2006&p=0',587,art+'/2006.png',index=index)
    main.addDir('2005','http://www.iwatchonline.to/movies?year=2005&p=0',587,art+'/2005.png',index=index)
    main.addDir('2004','http://www.iwatchonline.to/movies?year=2004&p=0',587,art+'/2004.png',index=index)
    main.addDir('2003','http://www.iwatchonline.to/movies?year=2003&p=0',587,art+'/2003.png',index=index)
    main.addDir('Enter Year','iwatchonline',653,art+'/enteryear.png',index=index)

def iWatchLISTMOVIES(murl,index=False):
    main.GA("Movies","List")   
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    videos = re.search('<ul class="thumbnails">(.+?)</ul>', link)
    if videos:
        videos = videos.group(1)
        match=re.compile('<li.+?<a.+?href=\"(.+?)\".+?<img.+?src=\"(.+?)\".+?<div class=\"title.+?>(.+?)<div').findall(videos)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")
        for url,thumb,name in match:
            if index == 'True':
                main.addDirIWO(name,url,21,thumb,'','','','','')
            else:
                main.addDirIWO(name,url,588,thumb,'','','','','')
            loadedLinks = loadedLinks + 1
            percent = (loadedLinks * 100)/totalLinks
            remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
            dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
            if (dialogWait.iscanceled()): break 
        dialogWait.close()
        del dialogWait
        if len(match)==25 and loadedLinks == 25:
            print "poooooooooooooop"+murl
            paginate=re.compile('(http://.+?&)p=(\d+)').findall(murl)
            for purl,page in paginate:
                i=int(page)+25
                pg=(int(page)/25)+2
    #                 if pg >2:
    #                     main.addDir('[COLOR red]Home[/COLOR]','',2000,art+'/home.png')
                main.addDir('[COLOR red]Enter Page #[/COLOR]',murl,654,art+'/gotopage.png',index=index)
                main.addDir('[COLOR blue]Page '+ str(pg)+'[/COLOR]',purl+'p='+str(i),587,art+'/next2.png',index=index)
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
        main.VIEWS()

def iWatchToday(murl,index=False):
    main.GA("Tvshows","TodaysList")
    link=main.OPENURL(murl)
    daysback = 2
    for x in range(0, daysback):
        match = re.findall(r"</i></a> <a href='(.*?)'" , link)
        if(match):
                link = link + main.OPENURL("http://www.iwatchonline.to/tv-schedule" + match[x])
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    link  = re.sub('>\s*','>',link)
    link  = re.sub('\s*<','<',link)
    match=re.compile('<img src="([^"]+?)"[^<]+?<br /><a href="([^"]+?)">(.+?)</a></td><td.+?>([^<]+?)</td><td.+?>([^<]+?)</td>.*?>(\d{,2}) Link\(s\)', re.M).findall(link)
    dialogWait = xbmcgui.DialogProgress()
    ret = dialogWait.create('Please wait until Show list is cached.')
    totalLinks = len(match)
    loadedLinks = 0
    remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
    dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
    xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")
    for thumb,url,name,episea,epiname,active in match:
        if(active == '0'):
            totalLinks -= 1
            continue
        name=name.strip()
        thumb=thumb.strip()
        url=url.strip()
        episea=episea.strip()
        epiname=epiname.strip()
        if index == 'True':
            name=re.sub('(\d{4})','',name.replace(' (','').replace(')',''))
            main.addDirTE(name+' '+episea+' [COLOR blue]'+epiname+'[/COLOR]',url,21,thumb,'','','','','')
        else:
            main.addDirTE(name+' '+episea+' [COLOR blue]'+epiname+'[/COLOR]',url,588,thumb,'','','','','')
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
        if (dialogWait.iscanceled()):
                return False   
    dialogWait.close()
    del dialogWait

def iWatchLISTSHOWS(murl,index=False):
    main.GA("Tvshows","List")
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    videos = re.search('<ul class="thumbnails">(.+?)</ul>', link)
    if videos:
        videos = videos.group(1)
        match=re.compile('<li.+?<a[^>]+?href=\"([^"]+?)\".+?<img[^>]+?src=\"([^"]+?)\".+?<div class=\"title[^>]+?>([^>]+?)<div').findall(videos)
        for url,thumb,name in match:
            main.addDirT(name,url,590,thumb,'','','','','',index=index)
        if len(match)==25:
            paginate=re.compile('([^<]+)&p=([^<]+)').findall(murl)
            for purl,page in paginate:
                i=int(page)+25
                main.addDir('[COLOR blue]Next[/COLOR]',purl+'&p='+str(i),589,art+'/next2.png',index=index)
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
        main.VIEWS()

def iWatchSeason(name,murl,thumb,index=False):
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.compile('<h5><i.+?</i>.*?(.+?)</h5>').findall(link)
    for season in match:
        main.addDir(name.strip()+' '+season.strip(),murl,591,thumb,'',index=index)

def GET_HTML(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3')
    response = urllib2.urlopen(req)
    link = response.read()
    response.close()
    link = link.replace('\\','')
    return link

def _decode_callback(matches):
    id = matches.group(1)
    try: return unichr(int(id))
    except: return id

def decode(data):
    return re.sub("&#(\d+)(;|(?=\s))", _decode_callback, data).strip()

def PANEL_REPLACER(content):
    panel_exists = True
    panel_id = 0
    while panel_exists == True:
        panel_name = "panel-id." + str(panel_id)
        panel_search_pattern = "(?s)\"" + panel_name + "\"\:\[\{(.+?)\}\]"
        panel_data = re.search(panel_search_pattern, content)
        if panel_data:
            panel_data = panel_data.group(1)
            content = re.sub("begin " + panel_name, "-->" + panel_data + "<!--", content)
            content = re.sub(panel_search_pattern, "panel used", content)
            panel_id = panel_id + 1
        else:
            panel_exists = False
    content = main.unescapes(content)
    content = re.sub("\\\"", "\"", content)
    from resources.universal import _common as univ_common
    content = univ_common.str_conv(decode(content))
    return content

def iWatchEpisode(mname,murl,index=False):
    seanum  = mname.split('Season ')[1]
    tv_content=main.OPENURL(murl)
    link = PANEL_REPLACER(tv_content)
    descs=re.compile('<meta name="description" content="(.+?)">').findall(link)
    if len(descs)>0: desc=descs[0]
    else: desc=''
    thumbs=re.compile('<div class="movie-cover span2"><img src="(.+?)" alt=".+?" class=".+?" />').findall(link)
    if len(thumbs)>0: thumb=thumbs[0]
    else: thumb=''
    episodes = re.search('(?sim)season'+seanum+'(.+?)</table>', link)
    if episodes:
        episodes = episodes.group(1)
        match=re.compile('<a[^>]+?href=\"([^"]+?)\".+?</i>([^<]+?)</a>.+?<td>([^<]+?)</td>').findall(episodes)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Show list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for url,epi,name in match:
            mname=mname.replace('(','').replace(')','')
            mname = re.sub(" \d{4}", "", mname)
            sea=re.compile('s'+str(seanum)).findall(url)
            if len(sea)>0:
                if index == 'True':
                    main.addDirTE(mname.strip()+' '+epi.strip()+' [COLOR blue]'+name.strip()+'[/COLOR]',url,21,thumb,desc,'','','','')
                else:
                    main.addDirTE(mname.strip()+' '+epi.strip()+' [COLOR blue]'+name.strip()+'[/COLOR]',url,588,thumb,desc,'','','','')
            loadedLinks = loadedLinks + 1
            percent = (loadedLinks * 100)/totalLinks
            remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
            dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
            if (dialogWait.iscanceled()):
                    return False   
        dialogWait.close()
        del dialogWait
        if selfAddon.getSetting('auto-view') == 'true':
                xbmc.executebuiltin("Container.SetViewMode(%s)" % selfAddon.getSetting('episodes-view'))

def GetUrl(url):
    link=main.OPENURL(url)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.compile('<iframe.+?src=\"(.+?)\"').findall(link)
    link=match[0]
    return link

def iWatchLINK(mname,url):      
    link=main.OPENURL(url)
    movie_content = main.unescapes(link)
    movie_content = re.sub("\\\"", "\"", movie_content)
    movie_content=movie_content.replace('\'','')  
    from resources.universal import _common as univ_common
    link2 = univ_common.str_conv(decode(movie_content))
    if selfAddon.getSetting("hide-download-instructions") != "true":
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
    links = re.search('<tbody>(.+?)</tbody>', link2)
    
    if links:
        links = links.group(1).replace('  ','')
        #print links         href="([^"]+?)" target="_blank" rel="nofollow"><img src=".+?>([^<]+?)</td><td><img src=".+?</td><td>.+?</td><td>([^<]+?)</td>
        match=re.compile('href="([^"]+?)" target="_blank" rel="nofollow"><img src=".+?>([^<]+?)</td><td><img src=".+?</td><td>.+?</td><td>([^<]+?)</td>', re.DOTALL).findall(links)
        for url, name, qua in match:
            name=name.replace(' ','')
            if name[0:1]=='.':
                name=name[1:]
            name=name.split('.')[0]
            if main.supportedHost(name.lower()):
                main.addDown2(mname+' [COLOR red]('+qua+')[/COLOR]'+' [COLOR blue]'+name.upper()+'[/COLOR]',url,649,art+'/hosts/'+name.lower()+'.png',art+'/hosts/'+name.lower()+'.png')

def iWatchLINKB(mname,url):
    main.GA("iWatchonline","Watched")
    ok=True
    hname=mname
    xbmc.executebuiltin("XBMC.Notification(Please Wait!,Opening Link,3000)")
    mname=mname.split('   [COLOR red]')[0]
    r = re.findall('Season(.+?)Episode([^<]+)',mname)
    if r:
        infoLabels =main.GETMETAEpiT(mname,'','')
        video_type='episode'
        season=infoLabels['season']
        episode=infoLabels['episode']
    else:
        infoLabels =main.GETMETAT(mname,'','','')
        video_type='movie'
        season=''
        episode=''
    img=infoLabels['cover_url']
    fanart =infoLabels['backdrop_url']
    imdb_id=infoLabels['imdb_id']
    infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }
    link=main.OPENURL(url)
    link=main.unescapes(link)
    match=re.compile('<(?:iframe|pagespeed_iframe).+?src=\"(.+?)\"').findall(link)
    try :
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
        stream_url = main.resolve_url(match[0])
        if stream_url == False: return
            
        infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre'],'originalTitle': main.removeColoredText(infoLabels['title'])}
        # play with bookmark
        from resources.universal import playbackengine
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=str(infoLabels['title']),season=str(season), episode=str(episode), year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            from resources.universal import watchhistory
            wh = watchhistory.WatchHistory('plugin.video.movie25')
            wh.add_item(hname+' '+'[COLOR green]'+prettyName+'[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=str(img), fanart=str(fanart), is_folder=False)
        player.KeepAlive()
        return ok
    except Exception, e:
        if stream_url != False:
                main.ErrorReport(e)
        return ok
