# -*- coding: utf-8 -*-
import urllib,urllib2,re,cookielib,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art
tzname = selfAddon.getSetting('tzname')
BASEURL='http://www.coolsport.se/'

def CleanTime(time):
    tztime = selfAddon.getSetting('tztime')
    time=time.lower()
    if 'pm' in time:
        time=time.replace('pm','')
        digit=re.search('(\d+).(\d+)',time)
        if '-' in tztime:
            tztime=tztime.replace('-','')
            if int(digit.group(1))==12:
                settime=int(digit.group(1))-int(tztime)
                finaltime= str(settime)+':'+digit.group(2)+'AM'
            else:
                settime=int(digit.group(1))-int(tztime)
                if settime < 0:
                    settime=settime+12
                    finaltime= str(settime)+':'+digit.group(2)+'AM'
                elif settime > 12:
                    settime=settime-12
                    finaltime= str(settime)+':'+digit.group(2)+'AM'
                else:
                    finaltime= str(settime)+':'+digit.group(2)+'PM'
        else:
            tztime=tztime.replace('+','')
            settime=int(digit.group(1))+int(tztime)
            if settime < 0:
                settime=settime+12
                finaltime= str(settime)+':'+digit.group(2)+'AM'
            elif settime > 12:
                settime=settime-12
                finaltime= str(settime)+':'+digit.group(2)+'AM'
            
            else:
                finaltime= str(settime)+':'+digit.group(2)+'PM'
    else:
        time=time.replace('am','')
        digit=re.search('(\d+).(\d+)',time)
        if '-' in tztime:
            tztime=tztime.replace('-','')
            if int(digit.group(1))==12:
                settime=int(digit.group(1))-int(tztime)
                finaltime= str(settime)+':'+digit.group(2)+'PM'
            else:
                settime=int(digit.group(1))-int(tztime)
                if settime < 0:
                    settime=settime+12
                    finaltime= str(settime)+':'+digit.group(2)+'PM'
                elif settime > 12:
                    settime=settime-12
                    finaltime= str(settime)+':'+digit.group(2)+'PM'
                else:
                    finaltime= str(settime)+':'+digit.group(2)+'AM'
        else:
            tztime=tztime.replace('+','')
            settime=int(digit.group(1))+int(tztime)
            if settime < 0:
                settime=settime+12
                finaltime= str(settime)+':'+digit.group(2)+'PM'
            elif settime > 12:
                settime=settime-12
                finaltime= str(settime)+':'+digit.group(2)+'PM'
            else:
                finaltime= str(settime)+':'+digit.group(2)+'AM'
    return finaltime
            
                
    
def MAIN():
    main.addLink('[COLOR yellow]Time Zone:[/COLOR] [COLOR orange]'+tzname+'[/COLOR]','',art+'/kiwi.png')
    main.addSpecial('[COLOR blue]Change Time Zone[/COLOR]','tz',440,art+'/kiwi.png')
    main.addDir('[COLOR orange]****** All Streams ******[/COLOR]','tz',442,art+'/kiwi.png')
    link=main.OPENURL('http://www.coolsport.se')
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.compile('<font color="red" size="6">(.+?)</font><p>(.*?)size="6').findall(link)
    for date,streams in match:
        main.addLink('[COLOR red]'+date+'[/COLOR]','',art+'/twittermash.png')
        match2=re.compile("(?sim)<font color='.+?'> ([^<]+) -<font color='white'> (.+?) (\d+.\d+\D+)-(\d+.\d+\D+) </font></font><font color='red'>(.+?)</font>").findall(streams)
                                #<font color='white'> (.+?) </font></font><font color='red'> (Stream 27) </font></a></li><p>
        for lang,name,t1,t2,url in match2:
            t1=CleanTime(t1)
            t2=CleanTime(t2)
            #url=url.lower().replace(' ','').replace('skysports','ss')
            name = name.decode("ascii", "ignore")
            main.addPlayL('[COLOR orange]'+lang+'[/COLOR] '+name+' [COLOR yellow]'+t1+' - '+t2+'[/COLOR] [COLOR red]'+url+'[/COLOR]',BASEURL+url.lower().replace('(','').replace(')','').replace(' ','')+'.html',441,'','','','','','',secName='Kiwi',secIcon=art+'/kiwi.png')

def AllStreams():
    link=main.OPENURL('http://www.coolsport.se')
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('>Twitter</a></li>','').replace('>Contact Us</a></li>','')
    match=re.compile('<li><a href="([^"]+)">([^<]+)</a></li>').findall(link)
    for url,name in match:
        main.addPlayL(name,BASEURL+url,441,'','','','','','',secName='Kiwi',secIcon=art+'/kiwi.png')
    
def setTimeZone():
    dialog = xbmcgui.Dialog()
    timezones=["(GMT-12:00) International Date Line West",  "(GMT-11:00) Midway Island, Samoa",  "(GMT-10:00) Hawaii",  "(GMT-09:00) Alaska",  "(GMT-08:00) Pacific Time (US and Canada); Tijuana",  "(GMT-07:00) Mountain Time (US and Canada)",  "(GMT-07:00) Chihuahua, La Paz, Mazatlan",  "(GMT-07:00) Arizona",  "(GMT-06:00) Central Time (US and Canada",  "(GMT-06:00) Saskatchewan",  "(GMT-06:00) Guadalajara, Mexico City, Monterrey",  "(GMT-06:00) Central America",  "(GMT-05:00) Eastern Time (US and Canada)",  "(GMT-05:00) Indiana (East)",  "(GMT-05:00) Bogota, Lima, Quito",  "(GMT-04:00) Atlantic Time (Canada)",  "(GMT-04:00) Caracas, La Paz",  "(GMT-04:00) Santiago",  "(GMT-03:30) Newfoundland and Labrador",  "(GMT-03:00) Brasilia",  "(GMT-03:00) Buenos Aires, Georgetown",  "(GMT-03:00) Greenland",  "(GMT-02:00) Mid-Atlantic",  "(GMT-01:00) Azores",  "(GMT-01:00) Cape Verde Islands",  "(GMT) Greenwich Mean Time: Dublin, Edinburgh, Lisbon, London",  "(GMT) Casablanca, Monrovia",  "(GMT+01:00) Belgrade, Bratislava, Budapest, Ljubljana, Prague",  "(GMT+01:00) Sarajevo, Skopje, Warsaw, Zagreb",  "(GMT+01:00) Brussels, Copenhagen, Madrid, Paris",  "(GMT+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna",  "(GMT+01:00) West Central Africa",  "(GMT+02:00) Bucharest",  "(GMT+02:00) Cairo",  "(GMT+02:00) Helsinki, Kiev, Riga, Sofia, Tallinn, Vilnius",  "(GMT+02:00) Athens, Istanbul, Minsk",  "(GMT+02:00) Jerusalem",  "(GMT+02:00) Harare, Pretoria",  "(GMT+03:00) Moscow, St. Petersburg, Volgograd",  "(GMT+03:00) Kuwait, Riyadh",  "(GMT+03:00) Nairobi",  "(GMT+03:00) Baghdad",  "(GMT+03:30) Tehran",  "(GMT+04:00) Abu Dhabi, Muscat",  "(GMT+04:00) Baku, Tbilisi, Yerevan",  "(GMT+04:30) Kabul",  "(GMT+05:00) Ekaterinburg",  "(GMT+05:00) Islamabad, Karachi, Tashkent",  "(GMT+05:30) Chennai, Kolkata, Mumbai, New Delhi",  "(GMT+05:45) Kathmandu",  "(GMT+06:00) Astana, Dhaka",  "(GMT+06:00) Sri Jayawardenepura",  "(GMT+06:00) Almaty, Novosibirsk",  "(GMT+06:30) Yangon Rangoon",  "(GMT+07:00) Bangkok, Hanoi, Jakarta",  "(GMT+07:00) Krasnoyarsk",  "(GMT+08:00) Beijing, Chongqing, Hong Kong SAR, Urumqi",  "(GMT+08:00) Kuala Lumpur, Singapore",  "(GMT+08:00) Taipei",  "(GMT+08:00) Perth",  "(GMT+08:00) Irkutsk, Ulaanbaatar",  "(GMT+09:00) Seoul",  "(GMT+09:00) Osaka, Sapporo, Tokyo",  "(GMT+09:00) Yakutsk",  "(GMT+09:30) Darwin",  "(GMT+09:30) Adelaide",  "(GMT+10:00) Canberra, Melbourne, Sydney",  "(GMT+10:00) Brisbane",  "(GMT+10:00) Hobart",  "(GMT+10:00) Vladivostok",  "(GMT+10:00) Guam, Port Moresby",  "(GMT+11:00) Magadan, Solomon Islands, New Caledonia",  "(GMT+12:00) Fiji Islands, Kamchatka, Marshall Islands",  "(GMT+12:00) Auckland, Wellington",  "(GMT+13:00) Nuku'alofa"]
    zonedig=["-12",  "-11",  "-10",  "-09",  "-08",  "-07",  "-07",  "-07",  "-06",  "-06",  "-06",  "-06",  "-05",  "-05",  "-05",  "-04",  "-04",  "-04",  "-03",  "-03",  "-03",  "-03",  "-02",  "-01",  "-01",  "0", "0",  "+01",  "+01",  "+01",  "+01",  "+01",  "+02",  "+02",  "+02",  "+02",  "+02",  "+02",  "+03",  "+03",  "+03",  "+03",  "+03",  "+04",  "+04",  "+04",  "+05",  "+05",  "+05",  "+05",  "+06",  "+06",  "+06",  "+06",  "+07",  "+07",  "+08",  "+08",  "+08",  "+08",  "+08",  "+09",  "+09",  "+09",  "+09",  "+09",  "+10",  "+10",  "+10",  "+10",  "+10",  "+11",  "+12",  "+12",  "+13"]
    ret = dialog.select('[COLOR=FF67cc33][B]Select TimeZone[/COLOR][/B]',timezones)
    if ret == -1:
        return
    else:
        selfAddon.setSetting('tzname',timezones[ret])
        selfAddon.setSetting('tztime',zonedig[ret])
        xbmc.executebuiltin("XBMC.Container.Refresh")

def SelectHost(url):
    dialog = xbmcgui.Dialog()
    hostlist=['Link 1','Link 2 (No Sound)']
    host=['http://cdn.kingofplayers.com/'+url+'.js','http://1cdn.filotv.pw/'+url+'.js']
    ret = dialog.select('[COLOR=FF67cc33][B]Select Stream[/COLOR][/B]',hostlist)
    if ret == -1:
        return
    else:
        return host[ret]

def GetStream(url):
    link=main.OPENURL(url)
    surl2=re.findall('url=(http.+?)">',link)
    try:surl=re.findall('<div id="I12_html">.+?src="([^"]+)"',main.OPENURL(surl2[0]))
    except:surl=re.findall('<div id="I12_html">.+?src="([^"]+)"',link)
    if url:
        link=main.OPENURL(surl[0])
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace("\/",'/')
        playpath=re.compile("<script type='text/javascript'>id='([^']+?)';").findall(link)
        rtmp='rtmp://185.2.137.204:443/liverepeater'
        pageurl='http://thesun.pw/player2.php?id='+playpath[0]+'&width=640&height=460'
        token='#atd%#$ZH'
        stream_url =rtmp+' playpath='+playpath[0]+' swfUrl=http://static.surk.tv/atdedead.swf pageUrl=' + pageurl +' live=1 timeout=14 swfVfy=1 token='+token
        return stream_url
  
def Link(mname,murl,thumb):
        main.GA("Kiwi","Watched")
        stream_url=False
        stream_url=GetStream(murl)
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Opening Stream,3000)") 
        
        ok=True
        if stream_url:
                playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                playlist.clear()
                listitem = xbmcgui.ListItem(thumbnailImage=thumb)
                infoL={'Title': mname, 'Genre': 'Live'} 
                from resources.universal import playbackengine
                player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='movie', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams='',imdb_id='')

                #WatchHistory
                if selfAddon.getSetting("whistory") == "true":
                    from resources.universal import watchhistory
                    wh = watchhistory.WatchHistory('plugin.video.movie25')
                    wh.add_item(mname+' '+'[COLOR green]Kiwi[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
                return ok
