import urllib,urllib2,re,cookielib,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art
from resources.universal import watchhistory
    
wh = watchhistory.WatchHistory('plugin.video.movie25')

def USALIST(murl):
        main.GA("Live","USA Live")
        main.addPlayL('AETV','aetv',458,'https://raw.githubusercontent.com/mash2k3/MashupArtwork/master/misc/aetv.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
        main.addPlayL('ABC','abc',458,'https://raw.githubusercontent.com/mash2k3/MashupArtwork/master/misc/abc.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
        main.addPlayL('HBO','hbo',458,'https://raw.githubusercontent.com/mash2k3/MashupArtwork/master/misc/hbo.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
        main.addPlayL('NBA TV','nbatv',458,'https://raw.githubusercontent.com/mash2k3/MashupArtwork/master/misc/nbatv.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
        main.addPlayL('NBC','nbc',458,'https://raw.githubusercontent.com/mash2k3/MashupArtwork/master/misc/nbc.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
        main.addPlayL('Nickelodeon','nick',458,'https://raw.githubusercontent.com/mash2k3/MashupArtwork/master/misc/nick.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
        main.addPlayL('SPIKE','spike',458,'https://raw.githubusercontent.com/mash2k3/MashupArtwork/master/misc/spike.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
        main.addPlayL('SYFY','syfy',458,'https://raw.githubusercontent.com/mash2k3/MashupArtwork/master/misc/syfy.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
        main.addPlayL('TBS','tbs',458,'https://raw.githubusercontent.com/mash2k3/MashupArtwork/master/misc/tbs.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
        main.addPlayL('TNT','tnt',458,'https://raw.githubusercontent.com/mash2k3/MashupArtwork/master/misc/tnt.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
        main.addPlayL('USA','usa',458,'https://raw.githubusercontent.com/mash2k3/MashupArtwork/master/misc/usa.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
        main.addPlayL('ABC FAMILY','abcfam',458,'https://raw.githubusercontent.com/mash2k3/MashupArtwork/master/misc/abcfam.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
        main.addPlayL('AMC','amc',458,'https://raw.githubusercontent.com/mash2k3/MashupArtwork/master/misc/amc.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
        main.addPlayL('Bravo','bravo',458,'https://raw.githubusercontent.com/mash2k3/MashupArtwork/master/misc/bravo.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
        main.addPlayL('Cartoon Network','cn',458,'https://raw.githubusercontent.com/mash2k3/MashupArtwork/master/misc/cn.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
        main.addPlayL('CBS','cbs',458,'https://raw.githubusercontent.com/mash2k3/MashupArtwork/master/misc/cbs.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
        main.addPlayL('CW','cw',458,'https://raw.githubusercontent.com/mash2k3/MashupArtwork/master/misc/cw.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
        main.addPlayL('ESPN','espn',458,'https://raw.githubusercontent.com/mash2k3/MashupArtwork/master/misc/espn.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
        main.addPlayL('FOX','fox',458,'https://raw.githubusercontent.com/mash2k3/MashupArtwork/master/misc/fox.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
        main.addPlayL('FX','fx',458,'https://raw.githubusercontent.com/mash2k3/MashupArtwork/master/misc/fx.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
        main.addPlayL('Special Event 1','event1',458,art+'/usalive.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
        main.addPlayL('Special Event 2','event2',458,art+'/usalive.png','','','','','',secName='USA Live',secIcon=art+'/usalive.png')
                       
            
def USALINK(mname,murl,thumb):
        main.GA("USA Live","Watched")
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Playing Link,1000)")
        stream_url ='rtmp://mob.golive.pw:1935/tumadre/ playpath='+murl+'.stream'
        listitem = xbmcgui.ListItem(thumbnailImage=thumb)
        infoL={'Title': mname, 'Genre': 'Live'} 
        from resources.universal import playbackengine
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='movie', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams='',imdb_id='')

        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
                wh.add_item(mname+' '+'[COLOR green]USA Live[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
        return ok
