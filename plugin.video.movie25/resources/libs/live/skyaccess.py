import urllib,re,os,sys,urllib2
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from t0mm0.common.net import Net as net
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
#MAINURL='https://www.sidereel.com/users'
prettyName='Sports Access'


user = selfAddon.getSetting('skyusername')
passw = selfAddon.getSetting('skypassword')
cookie_file = os.path.join(os.path.join(main.datapath,'Cookies'), 'skyaccess.cookies')
if user == '' or passw == '':
    if os.path.exists(cookie_file):
        try: os.remove(cookie_file)
        except: pass
    dialog = xbmcgui.Dialog()
    ret = dialog.yesno('[COLOR=FF67cc33]MashUp[/COLOR]', 'Please set your SportsAccess credentials','or register if you don have an account','at sportsaccess.se','Cancel','Login')
    if ret == 1:
        keyb = xbmc.Keyboard('', 'Enter Username or Email')
        keyb.doModal()
        if (keyb.isConfirmed()):
            search = keyb.getText()
            username=search
            keyb = xbmc.Keyboard('', 'Enter Password:')
            keyb.doModal()
            if (keyb.isConfirmed()):
                search = keyb.getText()
                password=search
                selfAddon.setSetting('skyusername',username)
                selfAddon.setSetting('skypassword',password)
                
user = selfAddon.getSetting('skyusername')
passw = selfAddon.getSetting('skypassword')

def setCookie(srDomain):
    cookieExpired = False
    if os.path.exists(cookie_file):
        try:
            cookie = open(cookie_file).read()
            expire = re.search('expires="(.*?)"',cookie, re.I)
            if expire:
                expire = str(expire.group(1))
                import time
                if time.time() > time.mktime(time.strptime(expire, '%Y-%m-%d %H:%M:%SZ')):
                   cookieExpired = True
        except: cookieExpired = True 
    if not os.path.exists(cookie_file) or cookieExpired:
        html = net().http_GET(srDomain).content
        r = re.findall(r'<input type="hidden" name="(.+?)" value="(.+?)" />', html, re.I)
        post_data = {}
        post_data['amember_login'] = user
        post_data['amember_pass'] = passw
        for name, value in r:
            post_data[name] = value
        net().http_GET('https://hostaccess.org/amember/protect/new-rewrite?f=2&url=/member1/&host=hostaccess.org&ssl=off')
        net().http_POST('https://hostaccess.org/amember/protect/new-rewrite?f=2&url=/member1/&host=hostaccess.org&ssl=off',post_data)
        net().save_cookies(cookie_file)
    else:
        net().set_cookies(cookie_file)

           
def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))

def MAINSA():
    setCookie('http://hostaccess.org/7-SFE-SZE-HOSTACCESS/')
    response = net().http_GET('http://hostaccess.org/7-SFE-SZE-HOSTACCESS/')
    link = response.content
    link = cleanHex(link)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','')
    if '<title>Axxess Streams </title>' in link:
        main.addLink('[COLOR red]Elite Member[/COLOR]','','')
    else:
        main.addLink('[COLOR red]Free Member[/COLOR]','','')
    main.addDir('[COLOR blue]Schedule[/COLOR]','http://www.sportsaccess.se/forum/calendar.php?action=weekview&calendar=1',476,art+'/skyaccess.png')
    main.addDir('Free Streams','http://sportsaccess.se/forum/misc.php?page=livestreams',412,art+'/skyaccess.png')
    if '<title>Axxess Streams </title>' in link:
        main.addDir('Elite Streams',link,410,art+'/skyaccess.png')
    main.addPlayc('[COLOR blue]Click here for Subscription Info[/COLOR]','https://dl.dropboxusercontent.com/u/35068738/picture%20for%20post/sky.png',244,art+'/skyaccess.png','','','','','')
    main.GA("Live","SportsAccess")

        
def Calendar(murl):
    setCookie(murl)
    response = net().http_GET(murl)
    link = response.content
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','')
    print link
    month=re.findall('(?sim)<td class="tcat smalltext" colspan="2">([^<]+?)</td>',link)
    match=re.findall('(?sim)<td class="trow_sep.+?>([^<]+?)</td></tr><tr><td class=".+?<span class="largetext">(\d+)</span></td><td class="trow1.+?>(.+?)</td>',link)
    for day,num,data in match:
       main.addLink('[COLOR blue]'+day+' '+num+' '+month[0]+'[/COLOR]','','')
       match2=re.findall('(?sim)<a href=".+?" class=" public_event" title="(.+?)">.+?</a>',data)
       for title in match2:
           main.addLink(title,'','')

def LISTMENU(murl):
    i=0
    match=re.compile('<li><a href="([^"]+)"><center>(.+?)</a>').findall(murl)                 
    for url,name in match:
        thumb=['http://i.imgur.com/zo1FeZA.png','http://i.imgur.com/R7xiSJg.png','http://i.imgur.com/KF3PQAV.png','http://i.imgur.com/uQunKHh.png','http://i.imgur.com/OOaeIzT.png']
        name = re.sub('(?sim)<[^>]*?>','',name)
        if 'http' not in url: url = 'http://hostaccess.org'+url
        main.addDir(name,url,411,thumb[i])
        i=i+1

def LISTMENU2(murl):
    response = net().http_GET(murl)
    link = response.content
    link = cleanHex(link)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','')
    match=re.compile('<li><a href="(.+?)"><center>(.+?)<img src="(.+?)".+?>').findall(link)
    for url,name,thumb in match:
        thumb=thumb.replace('http://i.imgur.com/D2gzK0U.png','http://i.imgur.com/zo1FeZA.png').replace('http://cdn0.agoda.net/images/default/icon_questionmark.png','http://i.imgur.com/R7xiSJg.png').replace('http://i.imgur.com/8h0WVhG.png','http://i.imgur.com/KF3PQAV.png').replace('http://i.imgur.com/my0hcfg.png','http://i.imgur.com/uQunKHh.png').replace('http://i.imgur.com/ufhNZ8q.png','http://i.imgur.com/OOaeIzT.png')
        name = re.sub('(?sim)<[^>]*?>','',name)
        main.addDir(name,'http://sportsaccess.se'+url,411,thumb)

def LISTCONTENT(murl,thumb):
    setCookie(murl)
    response = net().http_GET(murl)
    link = response.content
    link = cleanHex(link)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','')
    if 'http://hostaccess.org/7-SFE-SZE-HOSTACCESS/media/vod.php' == murl:
        response = net().http_GET('http://sportsaccess.se/forum/misc.php?page=Replays')
        link = response.content
        link = cleanHex(link)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','')
        
        match=re.compile('<a href="([^"]+)"><img src="([^"]+)" width=".+?alt="([^"]+)"></a>').findall(link)
        for url,thumb,name in match:
            if 'http' not in thumb:
                    thumb='http://sportsaccess.se/forum/'+thumb
            main.addDir(name,url,411,thumb)
    else:
        match=re.compile('<a href="(.+?)">(.+?)</a>').findall(link)
        for url,name in match:
            if 'GO BACK' not in name and '1 Year Subscriptions' not in name and 'Live Broadcasts' not in name and '<--- Return To On Demand Guide' not in name:
                name = re.sub('(?sim)<[^>]*?>','',name)
                if 'http' not in url:
                    url='http://sportsaccess.se'+url
                main.addPlayL(name,url,413,thumb,'','','','','')


def get_link(murl):
    setCookie(murl)
    response = net().http_GET(murl)
    link = response.content
    link = cleanHex(link)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','')
    m3u8=re.findall('<a href="([^"]+?.m3u8)">',link)
    iframe=re.findall('<iframe src="(http://admin.livestreamingcdn.com[^"]+?)"',link)
    if m3u8:
        return m3u8[0]
    elif iframe:
        response = net().http_GET(iframe[0])
        link = response.content
        link = cleanHex(link)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','')
        vlink=re.findall('file: "([^"]+?.m3u8)"',link)
        return vlink[0]
    else:
        swf=re.findall("src='([^<]+).swf'",link)[0]
        file=re.findall("file=(.+?)&",link)[0] 
        file=file.replace('.flv','')
        streamer=re.findall("streamer=(.+?)&",link)[0]
        if '.mp4' in file and 'vod' in streamer:
            file='mp4:'+file
            return streamer+' playpath='+file+' swfUrl='+swf+'.swf pageUrl='+murl
        else:
            return streamer+' playpath='+file+' swfUrl='+swf+'.swf pageUrl='+murl+' live=true timeout=20'
    
def PLAYLINK(mname,murl,thumb):
        ok=True
        main.GA("Live","SportsAccess")
        stream_url = get_link(murl)     
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        listitem = xbmcgui.ListItem(thumbnailImage=thumb)
        infoL={'Title': mname, 'Genre': 'Live'} 
        from resources.universal import playbackengine, watchhistory
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='movie', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams='',imdb_id='')
        wh = watchhistory.WatchHistory('plugin.video.movie25')
        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            wh.add_item(mname+' '+'[COLOR green]'+prettyName+'[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
        return ok
                                             
        












    
