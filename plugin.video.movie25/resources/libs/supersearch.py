import urllib,re,sys,os
import xbmc,xbmcgui,xbmcaddon,xbmcplugin,threading,time
import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
cachedir = xbmc.translatePath('special://temp/')

def SEARCHistory():
    dialog = xbmcgui.Dialog()
    if xbmcgui.Window(10000).getProperty('MASH_SSR_TYPE'):
        ret = int(xbmcgui.Window(10000).getProperty('MASH_SSR_TYPE'))-1
    else:
        ret = dialog.select('[B]Choose A Search Type[/B]',['[B]TV Shows[/B]','[B]Movies[/B]','[B]By Artist[/B]'])
    if ret == -1:
        xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False)
    if ret == 0:
        searchType = 'TV'
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryTv')
        if not os.path.exists(SeaFile):
            SEARCH('',searchType)
        else:
            main.addDir('Search',searchType,20,art+'/search.png')
            main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
            thumb=art+'/link.png'
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                seahis=urllib.unquote(seahis)               
                main.addDir(seahis,searchType,20,thumb)
    if ret == 1:
        searchType = 'Movies'
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistory25')
        if not os.path.exists(SeaFile):
            SEARCH('',searchType)
        else:
            main.addDir('Search',searchType,20,art+'/search.png')
            main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
            thumb=art+'/link.png'
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                seahis=urllib.unquote(seahis)    
                main.addDir(seahis,searchType,20,thumb)
    if ret == 2:
        import artist
        searchType = 'Artist'
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryArtist')
        if not os.path.exists(SeaFile):
            artist.SearchArtist('','')
        else:
            main.addDir('Search','atrtist',487,art+'/search.png')
            main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
            thumb=art+'/link.png'
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                seahis=urllib.unquote(seahis)    
                main.addDir(seahis,searchType,487,thumb)

def sortSearchList(searchList,query):
    import locale
    loc = locale.getlocale()
    try:
        locale.setlocale(locale.LC_ALL, "")
    except:
        locale.setlocale(locale.LC_ALL, "C")
    searchList.sort(key=lambda tup: tup[0].decode('utf-8').encode('utf-8'),cmp=locale.strcoll)
    try:locale.setlocale(locale.LC_ALL, loc)
    except:pass
    temp = []
    itemstoremove = []
    i = 0
    if re.search('(?i)s(\d+)e(\d+)',query) or re.search('(?i)Season(.+?)Episode',query) or re.search('(?i)(\d+)x(\d+)',query):
        for item in searchList:
            if re.search('(?i)\ss(\d+)e(\d+)',item[0]) or re.search('(?i)Season(.+?)Episode',item[0]) or re.search('(?i)(\d+)x(\d+)',item[0]):
                temp.append(item)
                itemstoremove.append(i)
            i += 1
    i = 0
    for remove in itemstoremove:
        searchList.pop(remove - i)
        i += 1
    return temp + searchList

def SEARCH(mname,type,libID=''):
    if libID=='':
        main.GA("None","SuperSearch")
    else:
        libName=mname
        if re.search('(?i).\s\([12][90]\d{2}\)',mname):
            mname = re.sub('(?i)^(.+?)\s\([12][90]\d{2}\).*','\\1',mname)
        elif re.search('(?i).\s[12][90]\d{2}',mname):
            mname = re.sub('(?i)^(.+?)\s[12][90]\d{2}.*','\\1',mname)
        mname = re.sub('(?i)\s\s+',' ',mname).strip()
    try: import Queue as queue
    except ImportError: import queue
    results = []
    searchList=[]
    #mname=main.unescapes(mname)
    mname=main.removeColoredText(mname)
    if mname=='Search': mname=''
    encode = main.updateSearchFile(mname,type)
    if not encode: return False
    else:
        sources = []
        encodeunquoted = urllib.unquote(encode)
        encode = re.sub('(?i)[^a-zA-Z0-9]',' ',encodeunquoted)
        encode = re.sub('(?i)\s\s+',' ',encode).strip()
        try: year = int(re.sub('(?i)^.+?\s\(?([12][90]\d{2})\)?.*','\\1',mname))
        except: year = 0
        encodeorg = encode
        encode = re.sub('(?i)^(.+?)\s\(?[12][90]\d{2}\)?.*','\\1',encode)
        encode = urllib.quote(encode)
        if type=='Movies':
            if selfAddon.getSetting('ssm_iwatch') != 'false':
                sources.append('iWatchOnline')
                q = queue.Queue()
                threading.Thread(target=iwatch,args=(encode,type,q)).start()
                results.append(q)
            if selfAddon.getSetting('ssm_movie25') != 'false':
                sources.append('Movie25')
                q = queue.Queue()
                threading.Thread(target=movie25,args=(encode,type,q)).start()
                results.append(q)
            if selfAddon.getSetting('ssm_icefilms') != 'false':
                sources.append('IceFilms')
                q = queue.Queue()
                threading.Thread(target=icefilms,args=(encode,type,q)).start()
                results.append(q)
            if selfAddon.getSetting('ssm_watchingnow') != 'false':
                sources.append('Watching Now')
                q = queue.Queue()
                threading.Thread(target=watchingnow,args=(encode,type,q)).start()
            if selfAddon.getSetting('ssm_filestube') != 'false':
                sources.append('FilesTube')
                q = queue.Queue()
                threading.Thread(target=filestube,args=(encode,type,q)).start()
                results.append(q)
            if selfAddon.getSetting('ssm_mbox') != 'false':
                sources.append('MBox')
                q = queue.Queue()
                threading.Thread(target=mbox,args=(encode,type,q)).start()
                results.append(q)
            if selfAddon.getSetting('ssm_yify') != 'false':
                sources.append('Yify')
                q = queue.Queue()
                threading.Thread(target=yify,args=(encode,type,q)).start()
                results.append(q)
#             if selfAddon.getSetting('ssm_noobroom') != 'false':
#                 if selfAddon.getSetting('username') != '' and selfAddon.getSetting('password') != '':
#                     sources.append('NoobRoom')
#                     q = queue.Queue()
#                     threading.Thread(target=noobroom,args=(encode,type,q)).start()
#                     results.append(q)
            if selfAddon.getSetting('ssm_tubeplus') != 'false':
                sources.append('TubePlus')
                q = queue.Queue()
                threading.Thread(target=tubeplus,args=(encode,type,q)).start()
                results.append(q)
            if selfAddon.getSetting('ssm_tvrelease') != 'false':
                sources.append('TVRelease')
                q = queue.Queue()
                threading.Thread(target=tvrelease,args=(encode,type,q)).start()
                results.append(q)
            if selfAddon.getSetting('ssm_mynewvideolinks') != 'false':
                sources.append('MyNewVideoLinks')
                q = queue.Queue()
                threading.Thread(target=mynewvideolinks,args=(encode,type,q)).start()
                results.append(q)
            if selfAddon.getSetting('ssm_sceper') != 'false':
                sources.append('Sceper')
                q = queue.Queue()
                threading.Thread(target=sceper,args=(encode,type,q)).start()
                results.append(q)
            if selfAddon.getSetting('ssm_fma') != 'false':
                sources.append('FMA')
                q = queue.Queue()
                threading.Thread(target=fma,args=(encode,type,q)).start()
                results.append(q)
            if selfAddon.getSetting('ssm_scenesource') != 'false':
                sources.append('SceneSource')
                q = queue.Queue()
                threading.Thread(target=scenesource,args=(encode,type,q)).start()
                results.append(q)
            if selfAddon.getSetting('ssm_vip') != 'false':
                sources.append('VIP')
                q = queue.Queue()
                threading.Thread(target=vip,args=(encode,type,q)).start()
                results.append(q)
#             if selfAddon.getSetting('ssm_rls1click') != 'false':
#                 sources.append('Rls1Click')
#                 q = queue.Queue()
#                 threading.Thread(target=rls1click,args=(encode,type,q)).start()

        else:
            encodetv = urllib.quote(re.sub('(?i)^(.*?((\ss(\d+)e(\d+))|(Season(.+?)Episode \d+)|(\d+)x(\d+))).*','\\1',urllib.unquote(encode)))
            encodewithoutepi = urllib.quote(re.sub('(?i)(\ss(\d+)e(\d+))|(Season(.+?)Episode)|(\d+)x(\d+)','',urllib.unquote(encodetv)).strip())
            print encodetv
            if selfAddon.getSetting('sstv_mbox') != 'false':
                sources.append('MBox')
                q = queue.Queue()
                threading.Thread(target=mbox,args=(encodetv,type,q)).start()
                results.append(q)
            if selfAddon.getSetting('sstv_watchseries') != 'false':
                sources.append('WatchSeries')
                q = queue.Queue()
                threading.Thread(target=watchseries,args=(encodetv,type,q)).start()
                results.append(q)
            if selfAddon.getSetting('sstv_iwatch') != 'false':
                sources.append('iWatchOnline')
                q = queue.Queue()
                threading.Thread(target=iwatch,args=(encodetv,type,q)).start()
                results.append(q)
            if selfAddon.getSetting('sstv_pftv') != 'false':
                sources.append('PFTV')
                q = queue.Queue()
                threading.Thread(target=pftv,args=(encodetv,type,q)).start()
                results.append(q)
            if selfAddon.getSetting('sstv_icefilms') != 'false':
                sources.append('IceFilms')
                q = queue.Queue()
                threading.Thread(target=icefilms,args=(encodetv,type,q)).start()
                results.append(q)
            if selfAddon.getSetting('sstv_tubeplus') != 'false':
                sources.append('TubePlus')
                q = queue.Queue()
                threading.Thread(target=tubeplus,args=(encodetv,type,q)).start()
                results.append(q)
            if selfAddon.getSetting('sstv_tvrelease') != 'false':
                sources.append('TVRelease')
                q = queue.Queue()
                threading.Thread(target=tvrelease,args=(encodetv,type,q)).start()
                results.append(q)
            if selfAddon.getSetting('sstv_mynewvideolinks') != 'false':
                sources.append('MyNewVideoLinks')
                q = queue.Queue()
                threading.Thread(target=mynewvideolinks,args=(encodetv,type,q)).start()
                results.append(q)
            if selfAddon.getSetting('sstv_rlsmix') != 'false':
                if selfAddon.getSetting('rlsusername') != '' and selfAddon.getSetting('rlspassword') != '':
                    sources.append('Rlsmix')
                    q = queue.Queue()
                    threading.Thread(target=rlsmix,args=(encodetv,type,q)).start()
                    results.append(q)
            if selfAddon.getSetting('sstv_scenelog') != 'false':
                sources.append('SceneLog')
                q = queue.Queue()
                threading.Thread(target=scenelog,args=(encodetv,type,q)).start()
                results.append(q)
            if selfAddon.getSetting('sstv_sceper') != 'false':
                sources.append('Sceper')
                q = queue.Queue()
                threading.Thread(target=sceper,args=(encodetv,type,q)).start()
                results.append(q)
            if selfAddon.getSetting('sstv_scenesource') != 'false':
                sources.append('SceneSource')
                q = queue.Queue()
                threading.Thread(target=scenesource,args=(encodetv,type,q)).start()
                results.append(q)

            encodewithoutepi = urllib.unquote(encodewithoutepi)
        encode = urllib.unquote(encode)
        if libID=='':
            dialogWait = xbmcgui.DialogProgress()
            ret = dialogWait.create('Please wait. Super Search is searching...')
            loadedLinks = 0
            remaining_display = 'Sources searched :: [B]'+str(loadedLinks)+' / '+str(len(results))+'[/B].'
            dialogWait.update(0,'[B]'+type+' Super Search - ' + encodeunquoted + '[/B]',remaining_display)
            totalLinks = len(results)
            whileloopps = 0
            xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")
            while totalLinks > loadedLinks:
                for n in range(len(results)):
                    try:
                        searchList.extend(results[n].get_nowait())
                        loadedLinks += 1
                        percent = (loadedLinks * 100)/len(results)
                        remaining_display = 'Sources searched :: [B]'+str(loadedLinks)+' / '+str(len(results))+'[/B].'
                        dialogWait.update(percent,'[B]'+type+' Super Search - ' + encodeunquoted + '[/B]',remaining_display,sources[n] + ' finished searching')
                        if dialogWait.iscanceled(): break;
                    except: pass
                if dialogWait.iscanceled(): break;
                time.sleep(.1)
            ret = dialogWait.create('Please wait until Video list is cached.')
            totalLinks = len(searchList)
            loadedLinks = 0
            remaining_display = 'Videos loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
            dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display,' ')
            searchList = sortSearchList(searchList,mname)

        if not libID=='':
            for n in range(len(results)):
                searchList.extend(results[n].get())
            searchList = sortSearchList(searchList,mname)
            import library
            t=threading.Thread(target=library.buildHostDB,args=(searchList,libID,libName))
            t.start()
            t.join()
            
        else:
            encode = encodeorg
            if type == 'TV':
                wordsalt = set(encodewithoutepi.lower().split())
                encode = urllib.unquote(encodetv)
            wordsorg = set(encode.lower().split())
            for name,section,url,thumb,mode,dir in searchList:
                name = name.replace('&rsquo;',"'").replace('&quot;','"').strip()
                cname = re.sub('(?i)[^a-zA-Z0-9]',' ',name)
                try: cyear = int(re.sub('(?i)^.+?\s\(?([12][90]\d{2})\)?.*','\\1',cname))
                except: cyear = 0 
                if year and not re.search('(?i)^.+?\s\(?([12][90]\d{2})\)?.*',cname): cname += ' ' + str(year)
                elif (cyear + 1) == year or (cyear - 1) == year: cname = cname.replace(str(cyear),str(year))
                name = name +' [COLOR=FF67cc33]'+section+'[/COLOR]'
                if type == 'TV' and (section == 'MBox' or section == 'WatchSeries' or section == 'iWatchOnline' or section == 'IceFilms' or section == 'TubePlus'):
                    words = wordsalt
                else: words = wordsorg
                if words.issubset(cname.lower().split()):
                    if dir:
                        if type=='Movies':
                            main.addDirM(name,url,int(mode),thumb,'','','','','')
                        else:
                            if re.search('(?i)\ss(\d+)e(\d+)',name) or re.search('(?i)Season(.+?)Episode',name) or re.search('(?i)(\d+)x(\d+)',name):
                                main.addDirTE(name,url,int(mode),thumb,'','','','','')
                            else:
                                main.addDirT(name,url,int(mode),thumb,'','','','','')
                    else:
                        if type=='Movies':
                            main.addPlayM(name,url,int(mode),thumb,'','','','','')
                        else:
                            if re.search('(?i)\ss(\d+)e(\d+)',name) or re.search('(?i)Season(.+?)Episode',name) or re.search('(?i)(\d+)x(\d+)',name):
                                main.addPlayTE(name,url,int(mode),thumb,'','','','','')
                            else:
                                main.addPlayT(name,url,int(mode),thumb,'','','','','')
                    loadedLinks = loadedLinks + 1
                    percent = (loadedLinks * 100)/totalLinks
                    remaining_display = 'Videos loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                    dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                    if dialogWait.iscanceled(): return False    
            dialogWait.close()
            del dialogWait
            if type=='Movies':
                xbmcgui.Window(10000).setProperty('MASH_SSR_TYPE', '2')
            elif type == 'TV':
                xbmcgui.Window(10000).setProperty('MASH_SSR_TYPE', '1')
            try:
                filelist = [ f for f in os.listdir(cachedir) if f.endswith(".fi") ]
                for f in filelist: os.remove(os.path.join(cachedir,f))
            except:pass
            if not loadedLinks:
                xbmc.executebuiltin("XBMC.Notification(Super Search - "+encode.replace("%20"," ")+",No Results Found,3000)")
                xbmcplugin.endOfDirectory(int(sys.argv[1]), False, False) 
                return False

def movie25(encode,type,q):
    from resources.libs import movie25
    returnList = movie25.superSearch(encode,type)
    if q: q.put(returnList)
    return returnList

def iwatch(encode,type,q):
    from resources.libs.plugins import iwatchonline
    returnList = iwatchonline.superSearch(encode,type)
    if q: q.put(returnList)
    return returnList

def pftv(encode,type,q):
    from resources.libs.plugins import pftv
    returnList = pftv.superSearch(encode,type)
    if q: q.put(returnList)
    return returnList
        
def icefilms(encode,type,q):
    from resources.libs.movies_tv import icefilms
    returnList = icefilms.superSearch(encode,type)
    if q: q.put(returnList)
    return returnList

def watchingnow(encode,type,q):
    from resources.libs.plugins import extramina
    returnList = extramina.superSearch(encode,type)
    if q: q.put(returnList)
    return returnList

def fma(encode,type,q):
    from resources.libs.plugins import fma
    returnList = fma.superSearch(encode,type)
    if q: q.put(returnList)
    return returnList

# def noobroom(encode,type,q):
#     from resources.libs.movies_tv import starplay
#     returnList = starplay.superSearch(encode,type)
#     if q: q.put(returnList)
#     return returnList

def tubeplus(encode,type,q):
    from resources.libs.plugins import tubeplus
    returnList = tubeplus.superSearch(encode,type)
    if q: q.put(returnList)
    return returnList

def tvrelease(encode,type,q):
    from resources.libs.plugins import tvrelease
    returnList = tvrelease.superSearch(encode,type)
    if q: q.put(returnList)
    return returnList

def watchseries(encode,type,q):
    from resources.libs.plugins import watchseries
    returnList = watchseries.superSearch(encode,type)
    if q: q.put(returnList)
    return returnList

def mynewvideolinks(encode,type,q):
    from resources.libs.movies_tv import newmyvideolinks
    returnList = newmyvideolinks.superSearch(encode,type)
    if q: q.put(returnList)
    return returnList

def rlsmix(encode,type,q):
    from resources.libs.movies_tv import rlsmix
    returnList = rlsmix.superSearch(encode,type)
    if q: q.put(returnList)
    return returnList

def scenelog(encode,type,q):
    from resources.libs.movies_tv import scenelog
    returnList = scenelog.superSearch(encode,type)
    if q: q.put(returnList)
    return returnList

def sceper(encode,type,q):
    from resources.libs.plugins import sceper
    returnList = sceper.superSearch(encode,type)
    if q: q.put(returnList)
    return returnList

def mbox(encode,type,q):
    from resources.libs.plugins import mbox
    returnList = mbox.superSearch(encode,type)
    if q: q.put(returnList)
    return returnList

def scenesource(encode,type,q):
    from resources.libs.plugins import scenesource
    returnList = scenesource.superSearch(encode,type)
    if q: q.put(returnList)
    return returnList

def yify(encode,type,q):
    from resources.libs.plugins import yify
    returnList = yify.superSearch(encode,type)
    if q: q.put(returnList)
    return returnList

def filestube(encode,type,q):
    from resources.libs.movies_tv import filestube
    returnList = filestube.superSearch(encode,type)
    if q: q.put(returnList)
    return returnList

# def rls1click(encode,type,q):
#     from resources.libs.movies_tv import rls1click
#     returnList = rls1click.superSearch(encode,type)
#     if q: q.put(returnList)
#     return returnList


def vip(encode,type,q):
    from resources.libs.movies_tv import filestube
    returnList = vipSuperSearch(encode,type)
    if q: q.put(returnList)
    return returnList

def vipSuperSearch(encode,type):
    try:
        returnList=[]
        encode = encode.replace('%20',' ')
        urls = []
        urls.append('https://raw.githubusercontent.com/dm88/demon88/master/1080pMovies%20.xml')
        urls.append('https://raw.githubusercontent.com/Coolstreams/bobbyelvis/master/veehdCollection.xml')
        urls.append('https://raw.githubusercontent.com/Coolstreams/bobbyelvis/master/2013%20HD.xml')
        urls.append('https://raw.githubusercontent.com/Coolstreams/bobbyelvis/master/2014%20HD.xml')
        urls.append('https://raw.githubusercontent.com/HackerMil/HackerMilsMovieStash/master/Movies/HD.xml')
        xml = main.batchOPENURL(urls,verbose=False)
        match=re.compile('(?sim)(<poster>.*?(?=<poster>|\Z))').findall(xml)
        for posterXML in match:
            poster = re.compile('(?sim)<poster>(.*?)</poster>').findall(posterXML)[0]
            posterXML=posterXML.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
            match2 = re.compile('<title>([^<]+)</title.+?link>(.+?)</link.+?thumbnail>([^<]+)</thumbnail>').findall(posterXML)
            for title,url,thumb in match2:
                if re.search('(?i)'+encode,title):
                    if 'sublink' in url:
                        returnList.append((title.strip(),poster,url,thumb,249,True))
                    else:
                        returnList.append((title.strip(),poster,url,thumb,237,False))
                    
        return returnList
    except: return []
