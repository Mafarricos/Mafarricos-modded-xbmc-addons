#-*- coding: utf-8 -*-
import urllib,re,string,urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
prettyName = 'MailRu'
MAINURL='http://api.video.mail.ru/videos/embed/mail/'


def geturl(referer):
    from t0mm0.common.net import Net as net
    print referer
    url='http://my.mail.ru/cgi-bin/my/ajax?user='
    if '/search?' in referer:
        match=re.compile('search.?q=(.+?)&sort=popular',re.DOTALL).findall(referer) 
        arg_tag=match[0]
        data={'Accept':'application/json, text/javascript, */*; q=0.01','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Host':'my.mail.ru','Referer':referer,'arg_tag':arg_tag,'arg_sort':'popular','Content-Length':'199','ajax_call':'1','func_name':'video.get_list','mna':'','mnb':'','encoding':'windows-1251','arg_type':'search','arg_html':'1','arg_offset':'0','arg_limit':'100'}
    else:
        data={'Accept':'application/json, text/javascript, */*; q=0.01','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Host':'my.mail.ru','Referer':referer,'Content-Length':'120','ajax_call':'1','func_name':'video.get_list','mna':'','mnb':'','encoding':'windows-1251','arg_type':'top','arg_html':'1','arg_offset':'0','arg_limit':'100'}
    link=net().http_POST(url,data).content
    return link

def MAINMAILRU(murl):
    main.addDir('Search(поиск)','aflam',359,art+'/search.png')
    link=geturl(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('&raquo;','').replace('\\','')           
    match=re.compile("""class="b-catalog__video-item-time font-small">([^<]+)</span><span.+?title="([^"]+)"><a type="videolayer"href="http://my.mail.ru/mail/(.+?)"data-clns=.+?style="background-image: url\('([^']+)'\);">""",re.DOTALL).findall(link)
    for dur,name,url,thumb in match:
        name=name.encode('windows-1251')
        url=url.replace('/video','')
        main.addPlayc(name,MAINURL+url,358,thumb,'','','','','')
    main.GA("Plugin","MailRu")



def SEARCHMAILRU():
        keyb = xbmc.Keyboard('', 'Search Videos')
        keyb.doModal()
        if (keyb.isConfirmed()):
            search = keyb.getText()
            encode=urllib.quote(search)
            surl='http://my.mail.ru/video/search?q='+encode+'&sort=popular'
            MAINMAILRU(surl)

def resolve_mailru(url):
        from t0mm0.common.net import Net as net
        import cookielib,urllib2
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving MashUp MailRU Link...')       
        dialog.update(0)
        print 'MashUp MailRU - Requesting GET URL: %s' % url
        link = net().http_GET(url).content
        match=re.compile('videoSrc = "(.+?)",',re.DOTALL).findall(link)
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), urllib2.HTTPHandler())
        req = urllib2.Request(url)
        f = opener.open(req)
        html = f.read()
        for cookie in cj:
            cookie=str(cookie)

        rcookie=cookie.replace('<Cookie ','').replace(' for .video.mail.ru/>','')

        vlink=match[0]+'|Cookie='+rcookie
        return vlink


def LINKSMAILRU(mname,murl,thumb):   
    main.GA("MailRu","Watched")
    xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,5000)")
    link=main.OPENURL(murl)
    ok=True
    stream_url = resolve_mailru(murl)

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
            #wh.add_item(mname+' '+'[COLOR green]MAILRU[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
        player.KeepAlive()
        return True
    except Exception, e:
        if stream_url != False: main.ErrorReport(e)
        return False
