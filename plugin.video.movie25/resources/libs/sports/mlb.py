import urllib,urllib2,re,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art
    
def MAIN():
    from datetime import date, timedelta
    i=0
    while i < 16:
        if i == 0:
            ago='Today'
        elif i==1:
            ago='Yesterday'
        else:
            ago=str(i)+" days ago"
        day = date.today() - timedelta(i)
        main.addDir(day.strftime("%A, %d. %B %Y")+" [COLOR yellow]"+ago+"[/COLOR]",str(day),448,art+'/mlb.png')
        i=i+1
        #print yesterday.strftime("%A, %d. %B %Y")
        
def LIST(murl):
    date=re.search('(\d+)-(\d{2})-(\d{2})',murl)
    xurl='http://mlb.mlb.com/gdcross/components/game/mlb/year_'+date.group(1)+'/month_'+date.group(2)+'/day_'+date.group(3)+'/grid.json'
    dialog = xbmcgui.Dialog()
    ret = dialog.select('Choose Type', ['Condensed Games','Highlights'])
    if ret == -1:
        return
    if ret == 0:
        link=main.OPENURL(xurl)
        match = re.compile('{"id":"([^"]+)","playback_scenario":"FLASH_1800K_.+?","state":"MEDIA_ARCHIVE","type":"condensed_game"}.+?"away_team_name":"([^"]+)".+?"home_team_name":"([^"]+)".+?"home_file_code":"([^"]+)"',re.DOTALL).findall(link)
        for id, away,home,fname in match:
            thumb='http://mlb.mlb.com/mlb/images/team_logos/logo_'+fname+'_79x76.jpg'
            mod=id[-3:]
            url='http://m.mlb.com/gen/multimedia/detail/'+mod[0]+'/'+mod[1]+'/'+mod[2]+'/'+id+'.xml'
            main.addPlayMs(away+" at "+home,url,449,thumb,'','','','','')
    if ret==1:
        link=main.OPENURL(xurl)
        match = re.compile('"away_team_name":"([^"]+)".+?"home_team_name":"([^"]+)".+?"game_pk":"([^"]+)".+?"home_file_code":"([^"]+)"',re.DOTALL).findall(link)
        for  away,home,id,fname in match:
            thumb='http://mlb.mlb.com/mlb/images/team_logos/logo_'+fname+'_79x76.jpg'
            main.addDir(away+" at "+home,id,450,thumb)

def LIST2(murl):
    url='http://mlb.mlb.com/ws/search/MediaSearchService?start=0&site=mlb&hitsPerPage=50&hitsPerSite=10&type=json&c_id=mlb&src=vpp&sort=desc&sort_type=date&game_pk='+murl
    refUrl='http://mlb.mlb.com/search/media.jsp?game_pk='+murl
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36')
    req.add_header('Referer',refUrl)
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    match = re.compile('{"src":"([^"]+)","type":".+?"}],"blurb":"([^"]+)","kicker":".+?","url":"([^"]+)",',re.DOTALL).findall(link)
    for thumb,name,url in match:
        main.addPlayMs(name,url,449,thumb,'','','','','')
    
def LINK(mname,murl,thumb):
    main.GA("MLB","Watched")
    strmL=[]
    link=main.OPENURL(murl)
    ok=True
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    m3u8=re.compile('''cdn="AKAMAI_FLASH_STREAM_ONDEMAND">([^<]*tablet.m3u8)<''').findall(link)
    link2=main.OPENURL(m3u8[0])
    links=re.compile("(.+?m3u8)").findall(link2)
    stmUrl=m3u8[0].replace('master_tablet.m3u8','')
    for strm in links:
        strmL.append(strm)
    if selfAddon.getSetting("disj-qua") == "0":
        stream_url = stmUrl+strmL[0]
    elif selfAddon.getSetting("disj-qua") == "1":
        stream_url = stmUrl+strmL[1]
    elif selfAddon.getSetting("disj-qua") == "2":
        stream_url = stmUrl+strmL[2]
    listitem = xbmcgui.ListItem(mname, thumbnailImage=thumb)
    infoL={'Title': mname, 'Genre': 'Live'} 
    from resources.universal import playbackengine
    player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='movie', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams='',imdb_id='')

    #WatchHistory
    if selfAddon.getSetting("whistory") == "true":
        from resources.universal import playbackengine, watchhistory    
        wh = watchhistory.WatchHistory('plugin.video.movie25')
        wh.add_item(mname+' '+'[COLOR green]MLB[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
    return ok
