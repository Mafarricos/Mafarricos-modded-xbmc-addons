import urllib,urllib2,re,json,string
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from t0mm0.common.addon import Addon
from resources.libs import main

ADDON=xbmcaddon.Addon(id='plugin.video.movie25')
art = main.art

def MAIN():
    main.GA("Live","1fm")
    link=main.OPENURL('http://www.1.fm/jsonfm/allstUpcomingSng')
    field=json.loads(link)
    for data in field:        
        main.addLink(str(data["StationName"].encode('utf-8')),'http://'+str(data["StationStreamSrv"].encode('utf-8'))+':'+str(data["StationHiPort"].encode('utf-8'))+'/?type=.flv','http://www.1.fm/content/Images/stationsicons/orange/'+str(data["StationIdentity"].encode('utf-8'))+'.png?w=256&h=256')
