#-*- coding: utf-8 -*-
import urllib,re,string,urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
prettyName = 'Cinemaxx.ru'
MAINURL='http://cinemaxx.ru/'



def MAINCINEM():
    main.addDir('Search (ПОИСК)','aflam',365,art+'/search.png')
    main.addDir('Main List (ГЛАВНАЯ)',MAINURL,363,art+'/cinemaxx.png')
    main.addDir('New Movies (НОВИНКИ)','http://cinemaxx.ru/category/newfilms/',363,art+'/cinemaxx.png')
    main.addDir('Genre (ЖАНРЫ)','http://www.aflam1.com/arabic-movies.htm',366,art+'/cinemaxx.png')

def SEARCHCINEM():
        keyb = xbmc.Keyboard('', 'Search Movies')
        keyb.doModal()
        if (keyb.isConfirmed()):
            search = keyb.getText()
            encode=urllib.quote(search)
            from t0mm0.common.net import Net as net
            url='http://cinemaxx.ru/'
            data={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Content-Length':'54','do':'search','subaction':'search','story':encode,'x':'-1230','y':'-250'}
            link=net().http_POST(url,data).content
            match=re.compile('<a href="([^<]+)" ><h1>(.+?)</h1>.+?<img align=".+?src="(.+?)".+?/>',re.DOTALL).findall(link)
            for url,name,thumb in match:
                try:name=name.encode('windows-1251')
                except:pass
                main.addPlayc(name,url,364,thumb,'','','','','')

def GENRECINEM():
    main.addDir('Анимация','http://cinemaxx.ru/category/15/',363,art+'/cinemaxx.png')
    main.addDir('Анимэ','http://cinemaxx.ru/category/31/',363,art+'/cinemaxx.png')
    main.addDir('Биография','http://cinemaxx.ru/category/biography/',363,art+'/cinemaxx.png')
    main.addDir('Боевик','http://cinemaxx.ru/category/2/',363,art+'/cinemaxx.png')
    main.addDir('Вестерн','http://cinemaxx.ru/category/34/',363,art+'/cinemaxx.png')
    main.addDir('Видео','http://cinemaxx.ru/category/24/',363,art+'/cinemaxx.png')
    main.addDir('Военный','http://cinemaxx.ru/category/11/',363,art+'/cinemaxx.png')
    main.addDir('Детектив','http://cinemaxx.ru/category/10/',363,art+'/cinemaxx.png')
    main.addDir('Драма','http://cinemaxx.ru/category/7/',363,art+'/cinemaxx.png')
    main.addDir('Зарубежное','http://cinemaxx.ru/category/27/',363,art+'/cinemaxx.png')
    main.addDir('Индия','http://cinemaxx.ru/category/36/',363,art+'/cinemaxx.png')
    main.addDir('Исторический','http://cinemaxx.ru/category/20/',363,art+'/cinemaxx.png')
    main.addDir('Комедия','http://cinemaxx.ru/category/1/',363,art+'/cinemaxx.png')
    main.addDir('Короткометраж','http://cinemaxx.ru/category/short/',363,art+'/cinemaxx.png')
    main.addDir('Криминал','http://cinemaxx.ru/category/9/',363,art+'/cinemaxx.png')
    main.addDir('Мелодрама','http://cinemaxx.ru/category/8/',363,art+'/cinemaxx.png')
    main.addDir('Мистика','http://cinemaxx.ru/category/5/',363,art+'/cinemaxx.png')
    main.addDir('Мюзикл','http://cinemaxx.ru/category/17/',363,art+'/cinemaxx.png')
    main.addDir('Новости кино','http://cinemaxx.ru/category/21/',363,art+'/cinemaxx.png')
    main.addDir('Отечественное','http://cinemaxx.ru/category/23/',363,art+'/cinemaxx.png')
    main.addDir('Приключения','http://cinemaxx.ru/category/12/',363,art+'/cinemaxx.png')
    main.addDir('Ретро','http://cinemaxx.ru/retrofilms/',363,art+'/cinemaxx.png')
    main.addDir('Семейный','http://cinemaxx.ru/category/13/',363,art+'/cinemaxx.png')
    main.addDir('Сериалы','http://cinemaxx.ru/category/30/',363,art+'/cinemaxx.png')
    main.addDir('Сказка','http://cinemaxx.ru/category/14/',363,art+'/cinemaxx.png')
    main.addDir('Спорт','http://cinemaxx.ru/category/35/',363,art+'/cinemaxx.png')
    main.addDir('Триллер','http://cinemaxx.ru/category/3/',363,art+'/cinemaxx.png')
    main.addDir('Ужасы','http://cinemaxx.ru/category/6/',363,art+'/cinemaxx.png')
    main.addDir('Фантастика','http://cinemaxx.ru/category/4/',363,art+'/cinemaxx.png')
    main.addDir('Фэнтези','http://cinemaxx.ru/category/16/',363,art+'/cinemaxx.png')
    main.addDir('Эротика','http://cinemaxx.ru/category/22/',363,art+'/cinemaxx.png')
    main.addDir('Юмор','http://cinemaxx.ru/category/humor/',363,art+'/cinemaxx.png')
    main.addDir('Документальное','http://cinemaxx.ru/category/18/',363,art+'/cinemaxx.png')
    main.addDir('Криминальная Россия','http://cinemaxx.ru/category/krim_ross/',363,art+'/cinemaxx.png')
    main.addDir('Следствие вели','http://cinemaxx.ru/category/sledveli/',363,art+'/cinemaxx.png')


def LISTCINEM(murl):
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('&raquo;','')
    match=re.compile('style="float:left;"><div><a href="(.+?)"><img src="(.+?)" alt="(.+?)".+?<div id=".+?" style=".+?">(.+?)</div>',re.DOTALL).findall(link)
    for url,thumb,name,desc in match:
        main.addPlayc(name,url,364,thumb,desc,'','','','')
    paginate = re.compile('''<a href="([^<]+)"><strong>.+?span''').findall(link)
    if len(paginate)>0:
        main.addDir('Next',paginate[0],363,art+'/next2.png')

def LINKSCINEM(mname,murl,thumb,desc):   
    main.GA("MailRu","Watched")
    xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,5000)")
    link=main.OPENURL(murl)
    ok=True
    match = re.compile('<iframe src="(.+?)"').findall(link)
    if match:
        stream_url = main.resolve_url(match[0])

    try:
        if stream_url == False: return                                                            
        infoL={'Title': mname, 'Plot': desc, 'Genre': '', 'originaltitle': mname}
        # play with bookmark
        stream_url=stream_url.replace(' ','%20')
        from resources.universal import playbackengine
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            from resources.universal import watchhistory
            wh = watchhistory.WatchHistory(addon_id)
            #wh.add_item(mname+' '+'[COLOR green]MAILRU[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
        player.KeepAlive()
        return True
    except Exception, e:
        if stream_url != False: main.ErrorReport(e)
        return False
