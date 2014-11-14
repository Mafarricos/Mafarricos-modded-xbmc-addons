import urllib,re,os,sys,urllib2
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from t0mm0.common.net import Net as net
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
#MAINURL='https://www.sidereel.com/users'
prettyName='HQZone'


user = selfAddon.getSetting('hqusername')
passw = selfAddon.getSetting('hqpassword')
cookie_file = os.path.join(os.path.join(main.datapath,'Cookies'), 'hqzone.cookies')
if user == '' or passw == '':
    if os.path.exists(cookie_file):
        try: os.remove(cookie_file)
        except: pass
    dialog = xbmcgui.Dialog()
    ret = dialog.yesno('[COLOR=FF67cc33]MashUp[/COLOR]', 'Please set your HQZone credentials','or register if you dont have an account','at www.HQZone.Tv','Cancel','Login')
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
                selfAddon.setSetting('hqusername',username)
                selfAddon.setSetting('hqpassword',password)
                
user = selfAddon.getSetting('hqusername')
passw = selfAddon.getSetting('hqpassword')

def setCookie(srDomain):
    import hashlib
    m = hashlib.md5()
    m.update(passw)
    net().http_GET('http://www.hqzone.tv/forums/view.php?pg=live')
    net().http_POST('http://www.hqzone.tv/forums/login.php?do=login',{'vb_login_username':user,'vb_login_password':passw,'vb_login_md5password':m.hexdigest(),'vb_login_md5password_utf':m.hexdigest(),'do':'login','securitytoken':'guest','url':'http://www.hqzone.tv/forums/view.php?pg=live','s':''})


def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))

def MAINHQ():
    setCookie('http://www.hqzone.tv/forums/view.php?pg=live')
    response = net().http_GET('http://www.hqzone.tv/forums/view.php?pg=live')
    link = response.content
    #link = cleanHex(link)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','')
    #link.encode("ascii", "ignore")
    main.addDir('[COLOR blue]Schedule[/COLOR]','http://www.hqzone.tv/forums/calendar.php?c=1&do=displayweek',475,art+'/hqzone.png')
    match=re.findall('(?sim)<h4 class="panel_headin.+?">([^<]+?)</h4><ul>(.+?)</ul>',link)
    for name,links in match[0:3]:
        if 'Channels' == name:
            name='VIP Streams'
        main.addDir(name,links,471,art+'/hqzone.png')
    main.addLink('[COLOR red]VOD[/COLOR]','','')
    match=re.findall('(?sim)<h4 class="panel_headin.+?">([^<]+?)</h4><ul>(.+?)</ul>',link)
    for name,links in match[3:]:
        if 'Channels' == name:
            name='VIP Streams'
        main.addDir(name,links,473,art+'/hqzone.png')
    
    main.GA("Live",prettyName)

def Calendar(murl):
    setCookie(murl)
    response = net().http_GET(murl)
    link = response.content
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','')
    month=re.findall('(?sim)<h2 class="blockhead">([^<]+?)</h2>',link)
    match=re.findall('(?sim)<h3><span class=".+?">([^<]+?)</span><span class="daynum" style=".+?" onclick=".+?">(\d+)</span></h3><ul class="blockrow eventlist">(.+?)</ul>',link)
    for day,num,data in match:
       main.addLink('[COLOR blue]'+day+' '+num+' '+month[0]+'[/COLOR]','','')
       match2=re.findall('(?sim)<span class="eventtime">([^<]+?)</span><a href=".+?" title=".+?">([^<]+?)</a>',data)
       for time,title in match2:
           main.addLink('[COLOR yellow]'+time+'[/COLOR] '+title,'','')
    
def LISTMENU(murl):
    match=re.findall('(?sim)<li><a href="([^"]+?)" target="I1">([^<]+?)</a></li>',murl)
    if not match:
        match=re.findall('(?sim)<a href="([^"]+?)" target="I1"><img src="([^"]+?)"',murl)
    for url,name in match:
        url = 'http://www.hqzone.tv/forums/'+url
        main.addPlayL(name,url,474,'','','','','','')

def LISTMENU2(murl):
    match=re.findall('(?sim)<li><a href="([^"]+?)" target="I1">([^<]+?)</a></li>',murl)
    for url,name in match:
        url = 'http://www.hqzone.tv/forums/'+url
        main.addDir(name,url,472,art+'/hqzone.png')

def LISTCONTENT(murl,thumb):
    setCookie(murl)
    response = net().http_GET(murl)
    link = response.content
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','')
    match=re.findall('(?sim)sources: \[\{ file: "([^"]+?)" \}\],title: "([^"]+?)"',link)
    for url,name in match:
        main.addPlayL(name,url,474,'','','','','','')


def get_link(murl):
    if 'mp4' in murl:
        swf='http://www.hqzone.tv/forums/jwplayer/jwplayer.flash.swf'
        streamer=re.search('(?sim)(rtmp://.+?/vod/)(.+?.mp4)',murl)
        return streamer.group(1)+'mp4:'+streamer.group(2)+' swfUrl='+swf+' pageUrl=http://www.hqzone.tv/forums/view.php?pg=live# token=WY846p1E1g15W7s'
    setCookie(murl)
    response = net().http_GET(murl)
    link = response.content
    link = cleanHex(link)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','')
    m3u8=re.findall('<a href="([^"]+?.m3u8)">',link)
    flash=re.search('file=(.+?)&streamer=(.+?)&dock',link)
    if m3u8:
        return m3u8[0]
    elif flash:
        swf='http://www.hqzone.tv/forums/jwplayer/player.swf'
        return flash.group(2)+' playpath='+flash.group(1)+' swfUrl='+swf+' pageUrl='+murl+' live=true timeout=20 token=WY846p1E1g15W7s'

    else:
        swf='http://www.hqzone.tv/forums/jwplayer/jwplayer.flash.swf'
        streamer=re.findall("file: '([^']+)',",link)[0]
        return streamer.replace('redirect','live')+' swfUrl='+swf+' pageUrl='+murl+' live=true timeout=20 token=WY846p1E1g15W7s'
    
def PLAYLINK(mname,murl,thumb):
        ok=True
        main.GA(prettyName,"Watched")
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
                                             
        












    
