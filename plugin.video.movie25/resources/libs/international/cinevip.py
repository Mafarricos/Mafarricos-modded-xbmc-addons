#-*- coding: utf-8 -*-
import urllib,urllib2,re,cookielib,urlresolver,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
from resources.universal import playbackengine, watchhistory
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
art = main.art
wh = watchhistory.WatchHistory(addon_id)


def GetAK():
    req = urllib2.Request('http://www.peliculaspepito.com/peliculas/')
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:10.0a1) Gecko/20111029 Firefox/10.0a1'
    req.add_header('User-Agent',user_agent)
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    link=link.replace('&#39;',"'").replace('&quot;','"').replace('&amp;',"&").replace("&#39;","'").replace('&lt;i&gt;','').replace("#8211;","-").replace('&lt;/i&gt;','').replace("&#8217;","'").replace('&amp;quot;','"').replace('&#215;','').replace('&#038;','').replace('&#8216;','').replace('&#8211;','').replace('&#8220;','').replace('&#8221;','').replace('&#8212;','')
    match=re.compile("JS_AK = '(.+?)';").findall(link)
    return match[0]

def LISTINT3(xurl):
        final=[]
        from t0mm0.common.net import Net
        net = Net()
        ak=GetAK()
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Collecting Source Data,10000)")
        main.addDir('Search Peliculaspepito','movieNEW',303,art+'/search.png')
        if xurl=='http://www.peliculaspepito.com':
            i=0
            while i != 450:
                    header={'Accept':'application/json, text/javascript, */*; q=0.01','Accept-Encoding':'gzip,deflate,sdch','Accept-Language':'en-US,en;q=0.8','Cache-Control':'max-age=0',
                    'Connection':'keep-alive','Content-Length':'314','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Referer':'http://www.peliculaspepito.com/peliculas/',
                    'X-Requested-With':'XMLHttpRequest'}
                    post_data={'fblistado_pag':str(i),'fblistado_generos':'','fblistado_letras':'','fblistado_idiomas':'','fblistado_calidades':'','fblistado_ano_min':'','fblistado_ano_max':''
                       ,'fblistado_ord_tipo':'','listado_bcad':'','ak':ak,'ourl':'http://www.peliculaspepito.com/peliculas/','spfin':'buscador_Listar_Fin'}
                    html = net.http_POST('http://www.peliculaspepito.com/ajax/buscador_catalogo',post_data,header).content
                    html=html.replace('\\\\','')
                    html=html.replace('\\','')
                    final.append(html)
                    i=i+45
        else:
                    header={'Accept':'application/json, text/javascript, */*; q=0.01','Accept-Encoding':'gzip,deflate,sdch','Accept-Language':'en-US,en;q=0.8','Cache-Control':'max-age=0',
                    'Connection':'keep-alive','Content-Length':'314','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Referer':'http://www.peliculaspepito.com/peliculas/',
                    'X-Requested-With':'XMLHttpRequest'}
                    post_data={'fblistado_pag':'0','fblistado_generos':'','fblistado_letras':'','fblistado_idiomas':'','fblistado_calidades':'','fblistado_ano_min':'','fblistado_ano_max':''
                       ,'fblistado_ord_tipo':'','listado_bcad':xurl,'ak':ak,'ourl':'http://www.peliculaspepito.com/peliculas/','spfin':'buscador_Listar_Fin'}
                    html = net.http_POST('http://www.peliculaspepito.com/ajax/buscador_catalogo',post_data,header).content
                    html=html.replace('\\\\','')
                    html=html.replace('\\','')
                    final=html
        match=re.compile('src=\\\"(.+?)\\\" \/><\/a><div id=\\\".+?\\\" class=\\\".+?\\\"><p><a title=\\\"(.+?)\\\" href=\\\"(.+?)\/\\\">.+?<\/a><\/p><p class=\\\".+?\\\">(.+?)class="pidilis',re.DOTALL).findall(str(final))
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for thumb, name, url, lang in match:
                if 'flag flag_0' in lang:
                        name= name+' [COLOR blue]ESP[/COLOR]'
                if 'flag flag_1' in lang:
                        name= name+' [COLOR yellow]LAT[/COLOR]'
                if 'flag flag_2' in lang:
                        name= name+' [COLOR red]ENG[/COLOR]'
                if 'flag flag_3' in lang:
                        name= name+' [COLOR green]SUB[/COLOR]'
                main.addDirM(name,url,307,thumb,'','','','','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        main.GA("INT","Peliculaspepito")

def Searchhistory(murl):
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistory25')
        if not os.path.exists(SeaFile):
            url='moviexx'
            SEARCHNEW('',url)
        else:
            main.addDir('Search','moviexx',304,art+'/search.png')
            main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
            thumb=art+'/link.png'
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                url='mNEW'
                seahis=seahis.replace('%20',' ')
                main.addDir(seahis,url,304,thumb)
            

def SEARCH(mname,murl):
    if murl == 'moviexx':
        encode = main.updateSearchFile(mname,'Movies','Search')
    else:
        encode = mname.replace(' ','%20')
    
    LISTINT3(encode)
    main.GA("Peliculaspepito","Search")

def getlink(murl):
    link=main.OPENURL(murl)
    try:
        match=re.compile('<a class="btn btn-mini enlace_link".+?title=".+?..." href="(.+?)"><',re.DOTALL).findall(link)[0]
        return match
    except:
        return 'nolink'



def LINKLIST(mname,url):
    link=main.OPENURL(url)
    link=main.unescapes(link)
    if selfAddon.getSetting("hide-download-instructions") != "true":
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
    match=re.compile('<span class="(.+?)">.+?</span></td><td class="tdcalidad">(.+?)</td><td class=".+?<img src=".+?" alt="(.+?)" />.+?</td>.+?title=".+?" href="(.+?)">',re.DOTALL).findall(link)
    for lang,qua,host,url in match:
        if 'flag flag_0' in lang:
            lang= ' [COLOR red]ESP[/COLOR]'
        if 'flag flag_1' in lang:
            lang= ' [COLOR yellow]LAT[/COLOR]'
        if 'flag flag_2' in lang:
            lang= ' [COLOR purple]ENG[/COLOR]'
        if 'flag flag_3' in lang:
            lang= ' [COLOR green]SUB[/COLOR]'
        if main.supportedHost(host):
            mname=main.removeColoredText(mname)
            main.addDown2(mname+' [COLOR blue]'+host.upper()+' [/COLOR]'+ lang+' [COLOR aqua]'+qua+'[/COLOR]',url,67,art+'/hosts/'+host.lower()+".png",art+'/hosts/'+host.lower()+".png")    

def LINKINT3(name,murl,thumb):
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
        main.GA("Peliculaspepito","Watched")
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
        url=getlink(murl)
        stream_url = main.resolve_url(url)
        try:
                    listitem = xbmcgui.ListItem(thumbnailImage=thumb)
                    listitem.setInfo('video', {'Title': name, 'Year': ''} )         
                
                    infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre']}
                    # play with bookmark
                    player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=infoLabels['title'],season=season, episode=episode, year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
                    #WatchHistory
                    if selfAddon.getSetting("whistory") == "true":
                        wh.add_item(name+' '+'[COLOR green]Peliculaspepito[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
                    player.KeepAlive()
                    return ok
        except Exception, e:
                    if stream_url != False:
                        main.ErrorReport(e)
                    return ok
