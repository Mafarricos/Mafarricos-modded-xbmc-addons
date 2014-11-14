# -*- coding: cp1252 -*-
import urllib,re,string,sys,os
import xbmc,xbmcgui,xbmcaddon,xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
prettyName = 'WatchSeries'

def MAINWATCHS(index=False):
        main.addDir('Search','s',581,art+'/search.png',index=index)
        main.addDir('A-Z','s',577,art+'/az.png',index=index)
        main.addDir('Yesterdays Episodes','http://watchseries.ag/tvschedule/-2',573,art+'/yesepi.png',index=index)
        main.addDir('Todays Episodes','http://watchseries.ag/tvschedule/-1',573,art+'/toepi2.png',index=index)
        main.addDir('Popular Shows','http://watchseries.ag/',580,art+'/popshowsws.png',index=index)
        main.addDir('This Weeks Popular Episodes','http://watchseries.ag/new',573,art+'/thisweek.png',index=index)
        main.addDir('Newest Episodes Added','http://watchseries.ag/latest',573,art+'/newadd.png',index=index)
        main.addDir('By Genre','genre',583,art+'/genre.png',index=index)
        main.GA("Plugin","Watchseries")
        main.VIEWSB()

def POPULARWATCHS(murl,index=False):
        main.GA("Watchseries","PopularShows")
        link=main.OPENURL2(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        
        match=re.compile('href="([^"]+)" title=".+?">([^<]+)</a><br />').findall(link)
        main.addLink('[COLOR red]Most Popular Series[/COLOR]','',art+'/link.png')
        for url, name in match[0:12]:
            main.addDirT(name,'http://watchseries.ag'+url,578,'','','','','','',index=index)
        main.addLink('[COLOR red]Most Popular Cartoons[/COLOR]','',art+'/link.png')
        for url, name in match[12:24]:
            main.addDirT(name,'http://watchseries.ag'+url,578,'','','','','','',index=index)
        main.addLink('[COLOR red]Most Popular Documentaries[/COLOR]','',art+'/link.png')
        for url, name in match[24:36]:
            main.addDirT(name,'http://watchseries.ag'+url,578,'','','','','','',index=index)
        main.addLink('[COLOR red]Most Popular Shows[/COLOR]','',art+'/link.png')
        for url, name in match[36:48]:
            main.addDirT(name,'http://watchseries.ag'+url,578,'','','','','','',index=index)
        main.addLink('[COLOR red]Most Popular Sports[/COLOR]','',art+'/link.png')
        for url, name in match[48:60]:
            main.addDirT(name,'http://watchseries.ag'+url,578,'','','','','','',index=index)

            
def GENREWATCHS(index=False):
        main.addDir('Action','http://watchseries.ag/genres/action',576,art+'/act.png',index=index)
        main.addDir('Adventure','http://watchseries.ag/genres/adventure',576,art+'/adv.png',index=index)
        main.addDir('Animation','http://watchseries.ag/genres/animation',576,art+'/ani.png',index=index)
        main.addDir('Comedy','http://watchseries.ag/genres/comedy',576,art+'/com.png',index=index)
        main.addDir('Crime','http://watchseries.ag/genres/crime',576,art+'/cri.png',index=index)
        main.addDir('Documentary','http://watchseries.ag/genres/documentary',576,art+'/doc.png',index=index)
        main.addDir('Drama','http://watchseries.ag/genres/drama',576,art+'/dra.png',index=index)
        main.addDir('Family','http://watchseries.ag/genres/family',576,art+'/fam.png',index=index)
        main.addDir('Fantasy','http://watchseries.ag/genres/fantasy',576,art+'/fant.png',index=index)
        main.addDir('History','http://watchseries.ag/genres/history',576,art+'/his.png',index=index)
        main.addDir('Horror','http://watchseries.ag/genres/horror',576,art+'/hor.png',index=index)
        main.addDir('Music','http://watchseries.ag/genres/music',576,art+'/mus.png',index=index)
        main.addDir('Mystery','http://watchseries.ag/genres/mystery',576,art+'/mys.png',index=index)
        main.addDir('Reality','http://watchseries.ag/genres/reality-tv',576,art+'/rea.png',index=index)
        main.addDir('Sci-Fi','http://watchseries.ag/genres/sci-fi',576,art+'/sci.png',index=index)
        main.addDir('Sport','http://watchseries.ag/genres/sport',576,art+'/spo.png',index=index)
        main.addDir('Talk Show','http://watchseries.ag/genres/talk-show',576,art+'/tals.png',index=index)
        main.addDir('Thriller','http://watchseries.ag/genres/thriller',576,art+'/thr.png',index=index)
        main.addDir('War','http://watchseries.ag/genres/war',576,art+'/war.png',index=index)
        main.GA("Watchseries","Genre")
        main.VIEWSB()

def AtoZWATCHS(index=False):
    main.addDir('0-9','http://watchseries.ag/letters/09',576,art+'/09.png',index=index)
    for i in string.ascii_uppercase:
            main.addDir(i,'http://watchseries.ag/letters/'+i.lower()+'/list-type/a_z',576,art+'/'+i.lower()+'.png',index=index)
    main.GA("Watchseries","A-Z")
    main.VIEWSB()

def LISTWATCHS(murl,index=False):
        main.GA("Watchseries","List")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','')
        match=re.compile('<a class=".+?" title=".+?" href="(.+?)">.+?</span>(.+?)</a>').findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Show list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for url, name in match:
            name=re.sub('\((\d+)x(\d+)\)','',name,re.I)
            episode = re.search('Seas(on)?\.? (\d+).*?Ep(isode)?\.? (\d+)',name, re.I)
            if(episode):
                e = str(episode.group(4))
                if(len(e)==1): e = "0" + e
                s = episode.group(2)
                if(len(s)==1): s = "0" + s
                name = re.sub('Seas(on)?\.? (\d+).*?Ep(isode)?\.? (\d+)','',name,re.I)
                name = name.strip() + " " + "S" + s + "E" + e
            if 'watchseries.' not in name and 'watchtvseries.' not in name:
                    if index == 'True':
                            name=re.sub('(\d{4})','',name.replace(' (','').replace(')',''))
                            main.addDirTE(name,'http://watchseries.ag'+url,21,'','','','','','')
                    else:
                            main.addDirTE(name,'http://watchseries.ag'+url,575,'','','','','','')
                    loadedLinks = loadedLinks + 1
                    percent = (loadedLinks * 100)/totalLinks
                    remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                    dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                    if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait

def LISTSHOWWATCHS(murl,index=False):
        main.GA("Watchseries","List")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','')
        match=re.compile('<a title="(.+?)" href="(.+?)">.+?<span class="epnum">(.+?)</span></a>').findall(link)
        for name, url, year in match:
            main.addDirT(name,'http://watchseries.ag'+url,578,'','','','','','',index=index)

def LISTWATCHSEASON(mname, murl,index=False):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','')
        thumb=art+'/folder.png'
        match=re.compile('<a class="null" href="(.+?)">(.+?)</a>').findall(link)
        for url, name in reversed(match):
            main.addDir(mname+' [COLOR red]'+name+'[/COLOR]',murl,579,thumb,index=index)


def LISTWATCHEPISODE(mname, murl,index=False):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace("&nbsp;&nbsp;&nbsp;"," ")
        print mname
        xname=re.findall('(Season .+?)',mname)[0]
        print xname
        match=re.compile('<a title=".+?- '+xname+' -.+?" href="([^"]+)"><span class="" >([^<]+)</span>').findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Show list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        season = re.search('Seas(on)?\.? (\d+)',main.removeColorTags(mname),re.I)
        for url, episode in reversed(match):
            name = mname
            epi= re.search('Ep(isode)?\.? (\d+)(.*)',episode, re.I)
            if(epi):
                e = str(epi.group(2))
                if(len(e)==1): e = "0" + e
                if(season):
                    s = season.group(2)
                    if(len(s)==1): s = "0" + s
                    name = main.removeColoredText(mname).strip()
                    name = name + " " + "S" + s + "E" + e
                    episode = epi.group(3).strip()
            if index == 'True':
                    name=re.sub('(\d{4})','',name.replace(' (','').replace(')',''))
                    main.addDirTE(name + ' [COLOR red]'+str(episode)+'[/COLOR]','http://watchseries.ag'+url,21,'','','','','','')
            else:
                    main.addDirTE(name + ' [COLOR red]'+str(episode)+'[/COLOR]','http://watchseries.ag'+url,575,'','','','','','')
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

def SearchhistoryWS(index=False):
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryTv')
        if not os.path.exists(SeaFile):
            SEARCHWS(index=index)
        else:
            main.addDir('Search','###',582,art+'/search.png',index=index)
            main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
            thumb=art+'/link.png'
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                    url=seahis
                    seahis=seahis.replace('%20',' ')
                    main.addDir(seahis,url,582,thumb,index=index)

def superSearch(encode,type):
    try:
        returnList=[]
        surl='http://watchseries.ag/search/'+encode
        epi = re.search('(?i)s(\d+?)e(\d+?)$',encode)
        if epi:
            epistring = encode.rpartition('%20')[2].upper()
            e = int(epi.group(2))
            s = int(epi.group(1))
            encodewithoutepi = urllib.quote(re.sub('(?i)(\ss(\d+)e(\d+))|(Season(.+?)Episode)|(\d+)x(\d+)','',urllib.unquote(encode)).strip())
            encode=encodewithoutepi+' season '+str(s)+' episode '+str(e)
            site = 'site:http://watchseries.ag/'
            results = main.SearchGoogle(urllib.unquote(encode), site)
            for res in results:
                t = res.title.encode('utf8').strip('...')
                u = res.url.encode('utf8')
                if type == 'TV':
                    if re.search('(?sim)season '+str(s)+' episode '+str(e),t):
                        t = re.sub('(?i)^[a-z] - (.*?)','\\1',t)
                        t = re.sub('(.*\)).*','\\1',t)
                        t= t.strip(" -").replace("-","").replace(" WatchSeries.lt","").replace(" Watch Series","").replace("Watch Online ","").replace("Watch Online","").replace("  "," ")
                        name=re.sub('\((\d+)x(\d+)\)','',t,re.I)
                        episode = re.search('Seas(on)?\.? (\d+).*?Ep(isode)?\.? (\d+)',name, re.I)
                        if(episode):
                            e = str(episode.group(4))
                            if(len(e)==1): e = "0" + e
                            s = episode.group(2)
                            if(len(s)==1): s = "0" + s
                            name = re.sub('Seas(on)?\.? (\d+).*?Ep(isode)?\.? (\d+)',"S" + s + "E" + e,name,re.I).strip()
                            name = re.sub('(?i)(s\d+e\d+\s?)(.*?)$','\\1[COLOR blue]\\2[/COLOR]',name)
                        returnList.append((name,prettyName,u,'',575,True))
                        return returnList
        link=main.OPENURL(surl,verbose=False)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<img src="([^"]+?)">               </a>.*?<a title="[^"]+?" href="([^<]+)"><b>(.+?)</b>',re.DOTALL).findall(link)
        for thumb,url,name in match:
            url = 'http://watchseries.ag' + url
            returnList.append((name,prettyName,url,thumb,578,True))
        return returnList
    except: return []
            
def SEARCHWS(murl = '',index=False):
        encode = main.updateSearchFile(murl,'TV')
        if not encode: return False   
        surl='http://watchseries.ag/search/'+encode
        link=main.OPENURL(surl)
        link=link.replace('\r','').replace('\n','').replace('\t','')
        match=re.compile('<a title=".+?" href="([^<]+)"><b>(.+?)</b></a>                <br>                <b>Description:</b>(.+?)</td></tr>            <tr></tr>            <tr><td valign="top">                <a title=".+?<img src="(.+?)">               </a>',re.DOTALL).findall(link)
        for url,name,desc,thumb in match:
                main.addDirT(name,'http://watchseries.ag'+url,578,thumb,desc,'','','','',index=index)
        main.GA("Watchseries","Search")

def LISTHOST(name,murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','')
        if selfAddon.getSetting("hide-download-instructions") != "true":
            main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        putlocker=re.compile('<span>putlocker</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(putlocker) > 0:
            for url in putlocker:
                main.addDown2(name+"[COLOR blue] : Putlocker[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/putlocker.png',art+'/hosts/putlocker.png')
        sockshare=re.compile('<span>sockshare</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(sockshare) > 0:
            for url in sockshare:
                main.addDown2(name+"[COLOR blue] : Sockshare[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/sockshare.png',art+'/hosts/sockshare.png')
        nowvideo=re.compile('<span>nowvideo</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(nowvideo) > 0:
            for url in nowvideo:
                main.addDown2(name+"[COLOR blue] : Nowvideo[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/nowvideo.png',art+'/hosts/nowvideo.png')
        oeupload=re.compile('<span>180upload</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(oeupload) > 0:
            for url in oeupload:
                main.addDown2(name+"[COLOR blue] : 180upload[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/180upload.png',art+'/hosts/180upload.png')
        filenuke=re.compile('<span>filenuke</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(filenuke) > 0:
            for url in filenuke:
                main.addDown2(name+"[COLOR blue] : Filenuke[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/filenuke.png',art+'/hosts/filenuke.png')
        flashx=re.compile('<span>flashx</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(flashx) > 0:
            for url in flashx:
                main.addDown2(name+"[COLOR blue] : Flashx[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/flashx.png',art+'/hosts/flashx.png')
        novamov=re.compile('<span>novamov</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(novamov) > 0:
            for url in novamov:
                main.addDown2(name+"[COLOR blue] : Novamov[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/novamov.png',art+'/hosts/novamov.png')
        uploadc=re.compile('<span>uploadc</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(uploadc) > 0:
            for url in uploadc:
                main.addDown2(name+"[COLOR blue] : Uploadc[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/uploadc.png',art+'/hosts/uploadc.png')
        xvidstage=re.compile('<span>xvidstage</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(xvidstage) > 0:
            for url in xvidstage:
                main.addDown2(name+"[COLOR blue] : Xvidstage[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/xvidstage.png',art+'/hosts/xvidstage.png')
        stagevu=re.compile('<span>stagevu</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(stagevu) > 0:
            for url in stagevu:
                main.addDown2(name+"[COLOR blue] : StageVu[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/stagevu.png',art+'/hosts/stagevu.png')        
        gorillavid=re.compile('<span>gorillavid</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(gorillavid)==0:
                gorillavid=re.compile('<span>gorillavid</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(gorillavid) > 0:
            for url in gorillavid:
                main.addDown2(name+"[COLOR blue] : Gorillavid[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/gorillavid.png',art+'/hosts/gorillavid.png')
        divxstage=re.compile('<span>divxstage</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(divxstage) > 0:
            for url in divxstage:
                main.addDown2(name+"[COLOR blue] : Divxstage[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/divxstage.png',art+'/hosts/divxstage.png')
        moveshare=re.compile('<span>moveshare</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(moveshare) > 0:
            for url in moveshare:
                main.addDown2(name+"[COLOR blue] : Moveshare[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/moveshare.png',art+'/hosts/moveshare.png')
        sharesix=re.compile('<span>sharesix</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(sharesix) > 0:
            for url in sharesix:
                main.addDown2(name+"[COLOR blue] : Sharesix[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/sharesix.png',art+'/hosts/sharesix.png')
        movpod=re.compile('<span>movpod</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(movpod)==0:
                movpod=re.compile('<span>movpod</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(movpod) > 0:
            for url in movpod:
                main.addDown2(name+"[COLOR blue] : Movpod[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/movpod.png',art+'/hosts/movpod.png')
        daclips=re.compile('<span>daclips</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(daclips)==0:
                daclips=re.compile('<span>daclips</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(daclips) > 0:
            for url in daclips:
                main.addDown2(name+"[COLOR blue] : Daclips[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/daclips.png',art+'/hosts/daclips.png')
        videoweed=re.compile('<span>videoweed</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(videoweed) > 0:
            for url in videoweed:
                main.addDown2(name+"[COLOR blue] : Videoweed[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/videoweed.png',art+'/hosts/videoweed.png')        
        zooupload=re.compile('<span>zooupload</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(zooupload) > 0:
            for url in zooupload:
                main.addDown2(name+"[COLOR blue] : Zooupload[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/zooupload.png',art+'/hosts/zooupload.png')
        zalaa=re.compile('<span>zalaa</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(zalaa) > 0:
            for url in zalaa:
                main.addDown2(name+"[COLOR blue] : Zalaa[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/zalaa.png',art+'/hosts/zalaa.png')
        vidxden=re.compile('<span>vidxden</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(vidxden) > 0:
            for url in vidxden:
                main.addDown2(name+"[COLOR blue] : Vidxden[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/vidxden.png',art+'/hosts/vidxden.png')
        vidbux=re.compile('<span>vidbux</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(vidbux) > 0:
            for url in vidbux:
                main.addDown2(name+"[COLOR blue] : Vidbux[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/vidbux.png',art+'/hosts/vidbux.png')
        thefile=re.compile('<span>thefile</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(thefile) > 0:
            for url in thefile:
                main.addDown2(name+"[COLOR blue] : thefile[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/thefile.png',art+'/hosts/thefile.png')
	vodlocker=re.compile('<span>vodlocker</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(vodlocker) > 0:
            for url in vodlocker:
                main.addDown2(name+"[COLOR blue] : vodlocker[/COLOR]",url+'xocx'+murl+'xocx',574,art+'/hosts/vodlocker.png',art+'/hosts/vodlocker.png')

def geturl(murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','')
        match=re.compile('<a class="myButton" href="(.+?)">Click Here to Play</a>').findall(link)
        if len(match)==0:
                match=re.compile('<a class="myButton" href="(.+?)">Click Here to Play Part1</a><a class="myButton" href="(.+?)">Click Here to Play Part2</a>').findall(link)
                return match[0]
        else:
                return match[0]

def LINKWATCHS(mname,murl):
        main.GA("Watchseries","Watched")
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        match=re.compile('(.+?)xocx(.+?)xocx').findall(murl)
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Checking Link,3000)")
        for hurl, durl in match:
                furl=geturl('http://watchseries.ag'+hurl)
        link=main.OPENURL(durl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match2=re.compile('<h1 class=".+?"><a href=".+?">.+?</a> - <a href="(.+?)" title=".+?">.+?</a>').findall(link)
        for xurl in match2:
                link2=main.OPENURL('http://watchseries.ag'+xurl)
                link2=link2.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        descr=re.compile('<b>Description :</b>(.+?)<').findall(link2)
        if len(descr)>0:
                desc=descr[0]
        else:
                desc=''
        thumbs=re.compile('<td style=".+?"><a href=".+?"><img src="(.+?)"').findall(link2)
        if len(thumbs)>0:
                thumb=thumbs[0]
        else:
                thumb=''
        genres=re.compile('<b>Genre: <a href=.+?>(.+?)</a>').findall(link2)
        if len(genres)>0:
                genre=genres[0]
        else:
                genre=''
        infoLabels =main.GETMETAEpiT(mname,thumb,desc)
        video_type='episode'
        season=infoLabels['season']
        episode=infoLabels['episode']
        img=infoLabels['cover_url']
        fanart =infoLabels['backdrop_url']
        imdb_id=infoLabels['imdb_id']
        infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }
        try:
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                stream_url = main.resolve_url(furl)

                infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre']}
                # play with bookmark
                from resources.universal import playbackengine
                player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=str(infoLabels['title']),season=str(season), episode=str(episode), year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
                #WatchHistory
                if selfAddon.getSetting("whistory") == "true":
                    from resources.universal import watchhistory
                    wh = watchhistory.WatchHistory('plugin.video.movie25')
                    wh.add_item(mname+' '+'[COLOR green]WatchSeries[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
                player.KeepAlive()
                return ok
        except Exception, e:
                if stream_url != False:
                        main.ErrorReport(e)
                return ok
