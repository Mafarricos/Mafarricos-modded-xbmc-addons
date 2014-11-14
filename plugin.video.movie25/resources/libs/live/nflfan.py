import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main
import re,sys

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art

def NFLMAIN():
    link=main.OPENURL('http://www.nfl.com/feeds-rs/videos/byChannel/nfl-videos.json')
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.findall('(?sim)"headline":"([^"]+)".+?"mediumImageUrl":"([^"]+)".+?"videoPath":"([^"]+)","bitrate":3000000',link)
    for name,thumb,url in match:
        main.addPlayc(name,url,183,thumb,'','','','','')
        
