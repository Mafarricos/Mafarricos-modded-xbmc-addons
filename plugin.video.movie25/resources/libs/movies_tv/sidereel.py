import urllib,re,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
MAINURL='https://www.sidereel.com/users'
prettyName='SideReel'

def downloadFile(url,dest):
    try:
        urllib.urlretrieve(url,dest)
    except Exception, e:
        dialog = xbmcgui.Dialog()
        main.ErrorReport(e)
        dialog.ok("Mash Up", "Report the error below at " + main.supportsite, str(e), "We will try our best to help you")

user = selfAddon.getSetting('srusername')
passw = selfAddon.getSetting('srpassword')
cookie_file = os.path.join(os.path.join(main.datapath,'Cookies'), 'sidereel.cookies')
if user == '' or passw == '':
    if os.path.exists(cookie_file):
        try: os.remove(cookie_file)
        except: pass
    dialog = xbmcgui.Dialog()
    ret = dialog.yesno('[COLOR=FF67cc33]MashUp[/COLOR]', 'Please set your SideReel credentials','or register if you don have an account','','Cancel','Login')
    if ret == 0:
        """
        TZList=['(GMT-11:00) American Samoa', '(GMT-11:00) International Date Line West', '(GMT-11:00) American Samoa', '(GMT-11:00) Midway Island', '(GMT-11:00) American Samoa', '(GMT-10:00) Hawaii', '(GMT-11:00) American Samoa', '(GMT-09:00) Alaska', '(GMT-11:00) American Samoa', '(GMT-08:00) Pacific Time (US & Canada)', '(GMT-11:00) American Samoa', '(GMT-08:00) Tijuana', '(GMT-11:00) American Samoa', '(GMT-07:00) Arizona', '(GMT-11:00) American Samoa', '(GMT-07:00) Chihuahua', '(GMT-11:00) American Samoa', '(GMT-07:00) Mazatlan', '(GMT-11:00) American Samoa', '(GMT-07:00) Mountain Time (US & Canada)', '(GMT-11:00) American Samoa', '(GMT-06:00) Central America', '(GMT-11:00) American Samoa', '(GMT-06:00) Central Time (US & Canada)', '(GMT-11:00) American Samoa', '(GMT-06:00) Guadalajara', '(GMT-11:00) American Samoa', '(GMT-06:00) Mexico City', '(GMT-11:00) American Samoa', '(GMT-06:00) Monterrey', '(GMT-11:00) American Samoa', '(GMT-06:00) Saskatchewan', '(GMT-11:00) American Samoa', '(GMT-05:00) Bogota', '(GMT-11:00) American Samoa', '(GMT-05:00) Eastern Time (US & Canada)', '(GMT-11:00) American Samoa', '(GMT-05:00) Indiana (East)', '(GMT-11:00) American Samoa', '(GMT-05:00) Lima', '(GMT-11:00) American Samoa', '(GMT-05:00) Quito', '(GMT-11:00) American Samoa', '(GMT-04:30) Caracas', '(GMT-11:00) American Samoa', '(GMT-04:00) Atlantic Time (Canada)', '(GMT-11:00) American Samoa', '(GMT-04:00) Georgetown', '(GMT-11:00) American Samoa', '(GMT-04:00) La Paz', '(GMT-11:00) American Samoa', '(GMT-04:00) Santiago', '(GMT-11:00) American Samoa', '(GMT-03:30) Newfoundland', '(GMT-11:00) American Samoa', '(GMT-03:00) Brasilia', '(GMT-11:00) American Samoa', '(GMT-03:00) Buenos Aires', '(GMT-11:00) American Samoa', '(GMT-03:00) Greenland', '(GMT-11:00) American Samoa', '(GMT-02:00) Mid-Atlantic', '(GMT-11:00) American Samoa', '(GMT-01:00) Azores', '(GMT-11:00) American Samoa', '(GMT-01:00) Cape Verde Is.', '(GMT-11:00) American Samoa', '(GMT+00:00) Casablanca', '(GMT-11:00) American Samoa', '(GMT+00:00) Dublin', '(GMT-11:00) American Samoa', '(GMT+00:00) Edinburgh', '(GMT-11:00) American Samoa', '(GMT+00:00) Lisbon', '(GMT-11:00) American Samoa', '(GMT+00:00) London', '(GMT-11:00) American Samoa', '(GMT+00:00) Monrovia', '(GMT-11:00) American Samoa', '(GMT+00:00) UTC', '(GMT-11:00) American Samoa', '(GMT+01:00) Amsterdam', '(GMT-11:00) American Samoa', '(GMT+01:00) Belgrade', '(GMT-11:00) American Samoa', '(GMT+01:00) Berlin', '(GMT-11:00) American Samoa', '(GMT+01:00) Bern', '(GMT-11:00) American Samoa', '(GMT+01:00) Bratislava', '(GMT-11:00) American Samoa', '(GMT+01:00) Brussels', '(GMT-11:00) American Samoa', '(GMT+01:00) Budapest', '(GMT-11:00) American Samoa', '(GMT+01:00) Copenhagen', '(GMT-11:00) American Samoa', '(GMT+01:00) Ljubljana', '(GMT-11:00) American Samoa', '(GMT+01:00) Madrid', '(GMT-11:00) American Samoa', '(GMT+01:00) Paris', '(GMT-11:00) American Samoa', '(GMT+01:00) Prague', '(GMT-11:00) American Samoa', '(GMT+01:00) Rome', '(GMT-11:00) American Samoa', '(GMT+01:00) Sarajevo', '(GMT-11:00) American Samoa', '(GMT+01:00) Skopje', '(GMT-11:00) American Samoa', '(GMT+01:00) Stockholm', '(GMT-11:00) American Samoa', '(GMT+01:00) Vienna', '(GMT-11:00) American Samoa', '(GMT+01:00) Warsaw', '(GMT-11:00) American Samoa', '(GMT+01:00) West Central Africa', '(GMT-11:00) American Samoa', '(GMT+01:00) Zagreb', '(GMT-11:00) American Samoa', '(GMT+02:00) Athens', '(GMT-11:00) American Samoa', '(GMT+02:00) Bucharest', '(GMT-11:00) American Samoa', '(GMT+02:00) Cairo', '(GMT-11:00) American Samoa', '(GMT+02:00) Harare', '(GMT-11:00) American Samoa', '(GMT+02:00) Helsinki', '(GMT-11:00) American Samoa', '(GMT+02:00) Istanbul', '(GMT-11:00) American Samoa', '(GMT+02:00) Jerusalem', '(GMT-11:00) American Samoa', '(GMT+02:00) Kyiv', '(GMT-11:00) American Samoa', '(GMT+02:00) Pretoria', '(GMT-11:00) American Samoa', '(GMT+02:00) Riga', '(GMT-11:00) American Samoa', '(GMT+02:00) Sofia', '(GMT-11:00) American Samoa', '(GMT+02:00) Tallinn', '(GMT-11:00) American Samoa', '(GMT+02:00) Vilnius', '(GMT-11:00) American Samoa', '(GMT+03:00) Baghdad', '(GMT-11:00) American Samoa', '(GMT+03:00) Kuwait', '(GMT-11:00) American Samoa', '(GMT+03:00) Minsk', '(GMT-11:00) American Samoa', '(GMT+03:00) Nairobi', '(GMT-11:00) American Samoa', '(GMT+03:00) Riyadh', '(GMT-11:00) American Samoa', '(GMT+03:30) Tehran', '(GMT-11:00) American Samoa', '(GMT+04:00) Abu Dhabi', '(GMT-11:00) American Samoa', '(GMT+04:00) Baku', '(GMT-11:00) American Samoa', '(GMT+04:00) Moscow', '(GMT-11:00) American Samoa', '(GMT+04:00) Muscat', '(GMT-11:00) American Samoa', '(GMT+04:00) St. Petersburg', '(GMT-11:00) American Samoa', '(GMT+04:00) Tbilisi', '(GMT-11:00) American Samoa', '(GMT+04:00) Volgograd', '(GMT-11:00) American Samoa', '(GMT+04:00) Yerevan', '(GMT-11:00) American Samoa', '(GMT+04:30) Kabul', '(GMT-11:00) American Samoa', '(GMT+05:00) Islamabad', '(GMT-11:00) American Samoa', '(GMT+05:00) Karachi', '(GMT-11:00) American Samoa', '(GMT+05:00) Tashkent', '(GMT-11:00) American Samoa', '(GMT+05:30) Chennai', '(GMT-11:00) American Samoa', '(GMT+05:30) Kolkata', '(GMT-11:00) American Samoa', '(GMT+05:30) Mumbai', '(GMT-11:00) American Samoa', '(GMT+05:30) New Delhi', '(GMT-11:00) American Samoa', '(GMT+05:30) Sri Jayawardenepura', '(GMT-11:00) American Samoa', '(GMT+05:45) Kathmandu', '(GMT-11:00) American Samoa', '(GMT+06:00) Almaty', '(GMT-11:00) American Samoa', '(GMT+06:00) Astana', '(GMT-11:00) American Samoa', '(GMT+06:00) Dhaka', '(GMT-11:00) American Samoa', '(GMT+06:00) Ekaterinburg', '(GMT-11:00) American Samoa', '(GMT+06:30) Rangoon', '(GMT-11:00) American Samoa', '(GMT+07:00) Bangkok', '(GMT-11:00) American Samoa', '(GMT+07:00) Hanoi', '(GMT-11:00) American Samoa', '(GMT+07:00) Jakarta', '(GMT-11:00) American Samoa', '(GMT+07:00) Novosibirsk', '(GMT-11:00) American Samoa', '(GMT+08:00) Beijing', '(GMT-11:00) American Samoa', '(GMT+08:00) Chongqing', '(GMT-11:00) American Samoa', '(GMT+08:00) Hong Kong', '(GMT-11:00) American Samoa', '(GMT+08:00) Krasnoyarsk', '(GMT-11:00) American Samoa', '(GMT+08:00) Kuala Lumpur', '(GMT-11:00) American Samoa', '(GMT+08:00) Perth', '(GMT-11:00) American Samoa', '(GMT+08:00) Singapore', '(GMT-11:00) American Samoa', '(GMT+08:00) Taipei', '(GMT-11:00) American Samoa', '(GMT+08:00) Ulaan Bataar', '(GMT-11:00) American Samoa', '(GMT+08:00) Urumqi', '(GMT-11:00) American Samoa', '(GMT+09:00) Irkutsk', '(GMT-11:00) American Samoa', '(GMT+09:00) Osaka', '(GMT-11:00) American Samoa', '(GMT+09:00) Sapporo', '(GMT-11:00) American Samoa', '(GMT+09:00) Seoul', '(GMT-11:00) American Samoa', '(GMT+09:00) Tokyo', '(GMT-11:00) American Samoa', '(GMT+09:30) Adelaide', '(GMT-11:00) American Samoa', '(GMT+09:30) Darwin', '(GMT-11:00) American Samoa', '(GMT+10:00) Brisbane', '(GMT-11:00) American Samoa', '(GMT+10:00) Canberra', '(GMT-11:00) American Samoa', '(GMT+10:00) Guam', '(GMT-11:00) American Samoa', '(GMT+10:00) Hobart', '(GMT-11:00) American Samoa', '(GMT+10:00) Melbourne', '(GMT-11:00) American Samoa', '(GMT+10:00) Port Moresby', '(GMT-11:00) American Samoa', '(GMT+10:00) Sydney', '(GMT-11:00) American Samoa', '(GMT+10:00) Yakutsk', '(GMT-11:00) American Samoa', '(GMT+11:00) New Caledonia', '(GMT-11:00) American Samoa', '(GMT+11:00) Vladivostok', '(GMT-11:00) American Samoa', '(GMT+12:00) Auckland', '(GMT-11:00) American Samoa', '(GMT+12:00) Fiji', '(GMT-11:00) American Samoa', '(GMT+12:00) Kamchatka', '(GMT-11:00) American Samoa', '(GMT+12:00) Magadan', '(GMT-11:00) American Samoa', '(GMT+12:00) Marshall Is.', '(GMT-11:00) American Samoa', '(GMT+12:00) Solomon Is.', '(GMT-11:00) American Samoa', '(GMT+12:00) Wellington', '(GMT-11:00) American Samoa', '(GMT+13:00) Nuku&#x27;alofa', '(GMT-11:00) American Samoa', '(GMT+13:00) Samoa', '(GMT-11:00) American Samoa', '(GMT+13:00) Tokelau Is.']
        BYList=['2001', '2000', '1999', '1998', '1997', '1996', '1995', '1994', '1993', '1992', '1991', '1990', '1989', '1988', '1987', '1986', '1985', '1984', '1983', '1982', '1981', '1980', '1979', '1978', '1977', '1976', '1975', '1974', '1973', '1972', '1971', '1970', '1969', '1968', '1967', '1966', '1965', '1964', '1963', '1962', '1961', '1960', '1959', '1958', '1957', '1956', '1955', '1954', '1953', '1952', '1951', '1950', '1949', '1948', '1947', '1946', '1945', '1944', '1943', '1942', '1941', '1940', '1939', '1938', '1937', '1936', '1935', '1934', '1933', '1932', '1931', '1930', '1929', '1928', '1927', '1926', '1925', '1924', '1923', '1922', '1921']
        puzzle_img = os.path.join(main.datapath, "SR_puzzle.jpg")
        link = main.OPENURL('https://www.sidereel.com/users/sign_up')
        captchalink=re.findall('<iframe src="(https://www.google.com/recaptcha/api/.+?)"',link,re.DOTALL)[0]
        linkcap = main.OPENURL(captchalink)
        keyb = xbmc.Keyboard('', 'Enter Email Address:')
        keyb.doModal()
        if (keyb.isConfirmed()):
            search = keyb.getText()
            email=search
            keyb = xbmc.Keyboard('', 'Enter Username: (5 characters)')
            keyb.doModal()
            if len(keyb.getText())<5:
                dialog.ok("[COLOR=FF67cc33]MashUp[/COLOR]", "Username must be at least 5 characters", "")
            if (keyb.isConfirmed()) and len(keyb.getText())>=5:
                search = keyb.getText()
                username=search
                keyb = xbmc.Keyboard('', 'Enter Password: (6 characters)')
                keyb.doModal()
                if len(keyb.getText())<6:
                    dialog.ok("[COLOR=FF67cc33]MashUp[/COLOR]", "Password must be at least 6 characters", "")
                if (keyb.isConfirmed()) and len(keyb.getText())>=6:
                    search = keyb.getText()
                    password=search
                    answer =dialog.select("Select Time Zone:", TZList)
                    if  answer != -1:
                        timezone=TZList[int(answer)]
                        answer2 =dialog.select("Select Birth Year:", BYList)
                        if  answer2 != -1:
                            birthyear=BYList[int(answer2)]
                            captchapic=re.findall('src="(image.+?)">',linkcap,re.DOTALL)[0]
                            capID=captchapic.split('image?c=')[1]
                            capImage='https://www.google.com/recaptcha/api/'+captchapic
                            downloadFile(capImage,puzzle_img)
                            img = xbmcgui.ControlImage(350,15,600,130,puzzle_img)
                            wdlg = xbmcgui.WindowDialog()
                            wdlg.addControl(img)
                            wdlg.show()
                            kb = xbmc.Keyboard('', 'Type the letters in the image', False)
                            kb.doModal()
                            if (keyb.isConfirmed()):
                                search = keyb.getText()
                                capres=search
                                net().http_GET('https://www.sidereel.com/users/sign_in')
                                cookieget=net().get_cookies()
                                link = main.OPENURL(MAINURL)
                                match=re.findall('<meta content="([^<]+)" name="csrf-token" />',link,re.DOTALL)
                                if match:
                                    CSRF=match[0]
                                session=re.findall("value='(.+?)'", str(cookieget))[0]
                                referer='https://www.sidereel.com/users/sign_in'
                                header={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding':'gzip,deflate,sdch','Accept-Language':'en-US,en;q=0.8','Cache-Control':'max-age=0','Connection':'keep-alive','Content-Type':'application/x-www-form-urlencoded','Referer':referer,'Cookie':'cookie-policy=true; __qca=P0-573233217-1389196433989; sign-up-promo=true; _sidereel_session='+session+'; SrLoginMethod=Anonymous; __utma=108050432.541580819.1389196431.1389196431.1389281568.2; __utmb=108050432.8.9.1389281740426; __utmc=108050432; __utmz=108050432.1389196431.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)','Host':'www.sidereel.com','Origin':'https://www.sidereel.com','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'}
                                post_data={'user[email]':email,'user[username]':username,'user[password]':password,'user[password_confirmation]:':password,'user[time_zone]':timezone,'user[birth_year]':birthyear,'recaptcha_challenge_field':capID,'recaptcha_response_field':capres,'user[receive_email_updates]':'0','Sign up':'Sign Up'}
                                #net().http_POST(MAINURL,post_data,header)
                                post=net().http_POST(MAINURL,post_data,header).content
                                print post

                                selfAddon.setSetting('srusername',username)
                                selfAddon.setSetting('srpassword',password)"""
    else:
        keyb = xbmc.Keyboard('', 'Enter Username or Email')
        keyb.doModal()
        if (keyb.isConfirmed()):
            username = keyb.getText()
            keyb = xbmc.Keyboard('', 'Enter Password:')
            keyb.doModal()
            if (keyb.isConfirmed()):
                password = keyb.getText()
                selfAddon.setSetting('srusername',username)
                selfAddon.setSetting('srpassword',password)


def EntCreds(murl):
    if 'USER' in murl:
        keyb = xbmc.Keyboard('', 'Enter Username or Email')
        keyb.doModal()
        if (keyb.isConfirmed()):
            username = keyb.getText()
            selfAddon.setSetting('srusername',username)
            xbmc.executebuiltin("XBMC.Container.Refresh")
    if 'PASS' in murl:
        keyb = xbmc.Keyboard('', 'Enter Password:')
        keyb.doModal()
        if (keyb.isConfirmed()):
            password = keyb.getText()
            selfAddon.setSetting('srpassword',password)
            xbmc.executebuiltin("XBMC.Container.Refresh")
            
user = selfAddon.getSetting('srusername')
passw = selfAddon.getSetting('srpassword')

def setCookie(srDomain):
    from t0mm0.common.net import Net as net
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
        loggedin = re.search('SrLoggedIn',cookie, re.I)
    if not os.path.exists(cookie_file) or cookieExpired or (not loggedin and user != '' and passw != ''):
        link = main.OPENURL(srDomain+'/sign_in')
        match=re.findall('<meta content="([^<]+)" name="csrf-token" />',link,re.DOTALL)
        token= match[0]
        net().http_GET(srDomain+'/sign_in')
        net().http_POST(srDomain+'/sign_in',{'authenticity_token':token,'user[email]':user,'user[password]':passw})
        net().save_cookies(cookie_file)
    else:
        net().set_cookies(cookie_file)
        
def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    return re.sub("(?i)&#\w+;", fixup, text.encode('utf-8'))

def getRelativeDate(days):
    if days < -1: days = str(abs(days)) + ' days ago'
    elif days == -1: days = 'Yesterday'
    elif days == 0: days = 'Today'
    elif days == 1: days = 'Tomorrow'
    elif days > 1: days = 'In ' + str(days) + ' days'
    return str(days)


def MAINSIDE(cacheOnly = False):
    import time
    import datetime
    cached_path = os.path.join(os.path.join(main.datapath,'Cache'), 'Sidereel')
    cached = main.getFile(cached_path)
    if (not cached or (cached and time.mktime(datetime.date.today().timetuple()) > os.stat(cached_path).st_mtime)
         or xbmcgui.Window(10000).getProperty('Refresh_Sidreel')):
        from t0mm0.common.net import Net as net
        setCookie(MAINURL)
        response = net().http_GET(MAINURL)
        link = response.content
        link = cleanHex(link)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','')
        today=re.compile("<li class='current'>[^/]+?<h2 class='[^']*?'><span>(.+?)</span></h2><div(.+?)/div></div></li>",re.DOTALL).findall(link)
        match=re.compile("<li class=''>[^/]+?<h2 class='[^']+?'><span>(.+?)</span></h2><div(.+?)/div></div></li>",re.DOTALL).findall(link)
        match = today + match
        if match:
            main.setFile(cached_path,str(match),True)
        else:
            main.addLink('[COLOR red]Something is wrong, Check if you credentials are correct[/COLOR]','TV','')
            main.addSpecial('[COLOR yellow]User: [/COLOR][COLOR white]'+user+'[/COLOR] --- Click to EDIT','USER',456,'')
            main.addSpecial('[COLOR yellow]Pass: [/COLOR][COLOR white]'+passw+'[/COLOR] --- Click to EDIT','PASS',456,'')
            main.addLink('[COLOR orange]If they are correct Clear Cache & Cookies Below[/COLOR]','TV','')
            main.addDir('[COLOR blue]Clear Cache & Cookies[/COLOR]','MashCache',416,art+'/maintenance.png')
            main.addLink('[COLOR red]If that does not solve the issue post log on forums[/COLOR]','TV','')
        xbmcgui.Window(10000).clearProperty('Refresh_Sidreel')
    else: match = eval(cached)
    if cacheOnly: return False
    main.GA("None","SideReel")
    main.addDir('Search for Shows','TV',398,art+'/search.png')
    main.addDir('All Tracked Shows','TV',402,art+'/sidereel.png')
    
    import calendar
    todaytimestamp = calendar.timegm(time.strptime(time.strftime("%b") + " " + time.strftime("%d"), "%b %d"))
    showsdisplayed = 0
    for date,shows in match:
        print shows
        if 'data-track-label="TrackerPage"' in shows:
            s = re.sub('(?i)^.*?,(.*)$','\\1',date).strip()
            timestamp =  calendar.timegm(time.strptime(s, "%b %d"))
            days = (timestamp - todaytimestamp) / 86400
            relative = getRelativeDate(days)
            main.addLink('[COLOR yellow]'+date+'[/COLOR]  [COLOR orange]('+relative+')[/COLOR]','',art+'/link.png')
            
            match2=re.compile("""data-track-label="TrackerPage" href=".+?">([^<]+?)</a><div><a class=".+?data-track-label="TrackerPage" href="([^"]+?)">([^<]+?)</a></div>""",re.DOTALL).findall(shows)
            for showname,seaepi, epiname in match2:
                se=re.search('season-(\d+)/episode-(\d+)',seaepi)
                if se:
                    if len(se.group(1))==1:
                        sea='0'+str(se.group(1))
                    else:
                        sea=str(se.group(1))
                    if len(se.group(2))==1:
                        epi='0'+str(se.group(2))
                    else:
                        epi=str(se.group(2))
                    final= 'S'+sea+'E'+epi
                else:
                    final=''

                main.addDir(showname+' '+final+' [COLOR red] "'+epiname+'"[/COLOR]','TV',20,art+'/sidereel.png')
                showsdisplayed += 1
    if not showsdisplayed: main.removeFile(cached_path)
    
def SEARCHSR():
    search  = ''
    refresh = xbmcgui.Window(10000).getProperty('MASH_SR_REFRESH') == 'True'
    if refresh:
        search = xbmcgui.Window(10000).getProperty('MASH_SR_TERM')
        
    xbmcgui.Window(10000).clearProperty('MASH_SR_REFRESH')
    xbmcgui.Window(10000).clearProperty('MASH_SR_TERM')
    
    if len(search) < 1:
        keyb = xbmc.Keyboard('', 'Search Shows')
        keyb.doModal()
        if (keyb.isConfirmed()):
            search = keyb.getText()
            
    if not search:
        xbmcplugin.endOfDirectory(int(sys.argv[1]),False,False)
        return
        
    xbmcgui.Window(10000).setProperty('MASH_SR_TERM', search)
    
    encode=urllib.quote(search)
    surl='http://www.sidereel.com/_television/search?utf8=%E2%9C%93&q='+encode
    sys.argv.append(surl)
    SEARCHED(surl)

def SEARCHED(surl):
    main.GA("SideReel","Search")
    from t0mm0.common.net import Net as net
    setCookie(MAINURL)
    response = net().http_GET(surl)
    link = response.content
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','')
    link= cleanHex(link)
    match=re.compile("""<div class='show-image'><a href[^>]+?><img alt="(.+?) poster" src="([^"]+?)".{,450}?<a href[^>]+?>[^<]+?<(.+?)</form""",re.DOTALL).findall(link)
    for name,thumb,track in match:
        if "<div class='authenticated hidden track-show'>" in track:
            name=name+'     [COLOR blue]Tracking Show[/COLOR]'
            main.addPlayc(name,track+' <xo>'+surl+'</xo>',400,thumb,'','','','','')
        else:
            name=name+'     [COLOR orange]Track Show[/COLOR]'
            main.addPlayc(name,track+' <xo>'+surl+'</xo>',399,thumb,'','','','','')


def TRACKEDSHOWS():
    main.GA("SideReel","Tracked Shows")
    from t0mm0.common.net import Net as net
    setCookie(MAINURL)
    cookie = main.getFile(cookie_file)
    user = re.findall('SrLoggedIn=(.+?);',cookie)
    if user:
        user = user[0]
        method=re.findall('SrLoginMethod=(.+?);',cookie)[0]
        token=re.findall('remember_user_token="(.+?)";',cookie)[0]
        session=re.findall('sidereel_session=(.+?);',cookie)[0]
        header={'Accept':'application/json, text/javascript, */*; q=0.01','Accept-Encoding':'gzip,deflate,sdch','Accept-Language':'en-US,en;q=0.8','Cache-Control':'max-age=0',
                'Connection':'keep-alive','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie':'SrLoggedIn='+user+'; SrLoginMethod='+method+'; remember_user_token='+token+'; _sidereel_session='+session+';',
                'Referer':MAINURL,'X-Requested-With':'XMLHttpRequest'}
        #post_data={'authenticity_token':auth,'tv_show_id':showID}
        data=net().http_GET('http://www.sidereel.com/users/tracked_tv_shows',header).content
        data=data.encode("utf8", "ignore")
        match=re.compile('"tv_show":{"id":(.+?),"name":"(.+?)",.+?,"status":(.+?),"summary":(.+?),"network":(.+?),.+?,"cached_genre_list":(.+?),.+?,"canonical_url":"(.+?)",.+?,"image_url_medium":"(.+?)",',re.DOTALL).findall(data)
        for id,name,status,plot,network,genre,url,thumb in match:
            main.addPlayc(name+' [COLOR blue]'+network.replace('"','').replace('null','')+'[/COLOR] [COLOR red]'+status.replace('"','').replace('null','')+'[/COLOR]' ,'<id>'+id+'<xo>'+url+'</xo>',400,thumb,plot.replace('"','').replace('null',''),'','',genre.replace('"','').replace('null',''),'')

def TRACKSHOW(track):
    from t0mm0.common.net import Net as net
    referer=re.findall('<xo>(.+?)</xo>',track)[0]
    showID=re.findall('name="tv_show_id" type="hidden" value="(.+?)"',track)[0]
    auth=re.findall('name="authenticity_token" type="hidden" value="(.+?)"',track)[0]
    cookie = open(cookie_file).read()
    user=re.findall('SrLoggedIn=(.+?);',cookie)[0]
    method=re.findall('SrLoginMethod=(.+?);',cookie)[0]
    token=re.findall('remember_user_token="(.+?)";',cookie)[0]
    session=re.findall('sidereel_session=(.+?);',cookie)[0]
    header={'Accept':'application/json, text/javascript, */*; q=0.01','Accept-Encoding':'gzip,deflate,sdch','Accept-Language':'en-US,en;q=0.8','Referer':referer,'Cookie':'cookie-policy=true; __qca=P0-573233217-1389196433989; sign-up-promo=true; SrLoggedIn='+user+'; SrLoginMethod='+method+'; remember_user_token='+token+'; _sidereel_session='+session+'; __utma=108050432.541580819.1389196431.1389196431.1389196431.1; __utmb=108050432.55.9.1389211544772; __utmc=108050432; __utmz=108050432.1389196431.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)'}
    post_data={'authenticity_token':auth,'tv_show_id':showID}
    net().http_POST('http://www.sidereel.com/tracked_tv_show.js',post_data,header)
    xbmcgui.Window(10000).setProperty('Refresh_Sidreel', '1')
    xbmcgui.Window(10000).setProperty('MASH_SR_REFRESH', 'True')
    xbmc.executebuiltin("XBMC.Container.Refresh")


def UNTRACKSHOW(track):
    from t0mm0.common.net import Net as net
    check=re.search('<id>(.+?)<xo>(.+?)</xo>',track)
    if check:
        showID=check.group(1)
        showURL='http://www.sidereel.com'+check.group(2)
        link = main.OPENURL(showURL)
        match=re.findall('<meta content="([^<]+)" name="csrf-token" />',link,re.DOTALL)
        if match:
            CSRF=match[0]
        link = main.OPENURL(MAINURL)
        match2=re.findall('<meta content="([^<]+)" name="csrf-token" />',link,re.DOTALL)
        if match2:
            sitetoken=match2[0]
        dialog = xbmcgui.Dialog()
        ret = dialog.yesno('Mash Up', 'Are you sure you want to stop tracking show?','','','No', 'Yes')
        if ret == 1:
            cookie = open(cookie_file).read()
            user=re.findall('SrLoggedIn=(.+?);',cookie)[0]
            method=re.findall('SrLoginMethod=(.+?);',cookie)[0]
            token=re.findall('remember_user_token="(.+?)";',cookie)[0]
            session=re.findall('sidereel_session=(.+?);',cookie)[0]
            header={'Accept':'application/json, text/javascript, */*; q=0.01','Accept-Encoding':'gzip,deflate,sdch','Accept-Language':'en-US,en;q=0.8','Referer':MAINURL,'Cookie':'cookie-policy=true; __qca=P0-573233217-1389196433989; sign-up-promo=true; SrLoggedIn='+user+'; SrLoginMethod='+method+'; remember_user_token='+token+'; _sidereel_session='+session+'; __utma=108050432.541580819.1389196431.1389196431.1389196431.1; __utmb=108050432.55.9.1389211544772; __utmc=108050432; __utmz=108050432.1389196431.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)'}
            post_data={'_method':'delete','authenticity_token':CSRF,'tv_show_id':showID,'authenticity_token':sitetoken}
            net().http_POST('http://www.sidereel.com/tracked_tv_show.js',post_data,header)
        else:
            return
    else:    
        referer=re.findall('<xo>(.+?)</xo>',track)[0]
        showID=re.findall('name="tv_show_id" type="hidden" value="(.+?)"',track)[0]
        auth=re.findall('name="authenticity_token" type="hidden" value="(.+?)"',track)[0]
        cookie = open(cookie_file).read()
        user=re.findall('SrLoggedIn=(.+?);',cookie)[0]
        method=re.findall('SrLoginMethod=(.+?);',cookie)[0]
        token=re.findall('remember_user_token="(.+?)";',cookie)[0]
        session=re.findall('sidereel_session=(.+?);',cookie)[0]
        header={'Accept':'application/json, text/javascript, */*; q=0.01','Accept-Encoding':'gzip,deflate,sdch','Accept-Language':'en-US,en;q=0.8','Referer':referer,'Cookie':'cookie-policy=true; __qca=P0-573233217-1389196433989; sign-up-promo=true; SrLoggedIn='+user+'; SrLoginMethod='+method+'; remember_user_token='+token+'; _sidereel_session='+session+'; __utma=108050432.541580819.1389196431.1389196431.1389196431.1; __utmb=108050432.55.9.1389211544772; __utmc=108050432; __utmz=108050432.1389196431.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)'}
        post_data={'_method':'delete','authenticity_token':auth,'tv_show_id':showID}
        net().http_POST('http://www.sidereel.com/tracked_tv_show.js',post_data,header)
    xbmcgui.Window(10000).setProperty('Refresh_Sidreel', '1')
    xbmcgui.Window(10000).setProperty('MASH_SR_REFRESH', 'True')
    xbmc.executebuiltin("XBMC.Container.Refresh")
    
