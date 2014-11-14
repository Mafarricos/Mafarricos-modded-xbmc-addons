import urllib,urllib2,re,cookielib,string,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
from resources.universal import playbackengine, watchhistory
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art
    
wh = watchhistory.WatchHistory('plugin.video.movie25')

def MAINBB():
    main.GA("Sports","BodyBuilding")   
    main.addDir('Abdominals','http://www.bodybuilding.com/exercises/list/muscle/selected/abdominals',196,art+'/bodybuilding.png')
    main.addDir('Abductors','http://www.bodybuilding.com/exercises/list/muscle/selected/abductors',196,art+'/bodybuilding.png')
    main.addDir('Adductors','http://www.bodybuilding.com/exercises/list/muscle/selected/adductors',196,art+'/bodybuilding.png')
    main.addDir('Biceps','http://www.bodybuilding.com/exercises/list/muscle/selected/biceps',196,art+'/bodybuilding.png')
    main.addDir('Calves','http://www.bodybuilding.com/exercises/list/muscle/selected/calves',196,art+'/bodybuilding.png')
    main.addDir('Chest','http://www.bodybuilding.com/exercises/list/muscle/selected/chest',196,art+'/bodybuilding.png')
    main.addDir('Forearms','http://www.bodybuilding.com/exercises/list/muscle/selected/forearms',196,art+'/bodybuilding.png')
    main.addDir('Glutes','http://www.bodybuilding.com/exercises/list/muscle/selected/glutes',196,art+'/bodybuilding.png')
    main.addDir('Hamstrings','http://www.bodybuilding.com/exercises/list/muscle/selected/hamstrings',196,art+'/bodybuilding.png')
    main.addDir('Lats','http://www.bodybuilding.com/exercises/list/muscle/selected/lats',196,art+'/bodybuilding.png')
    main.addDir('Lower Back','http://www.bodybuilding.com/exercises/list/muscle/selected/lower-back',196,art+'/bodybuilding.png')
    main.addDir('Middle Back','http://www.bodybuilding.com/exercises/list/muscle/selected/middle-back',196,art+'/bodybuilding.png')
    main.addDir('Neck','http://www.bodybuilding.com/exercises/list/muscle/selected/neck',196,art+'/bodybuilding.png')
    main.addDir('Quadriceps','http://www.bodybuilding.com/exercises/list/muscle/selected/quadriceps',196,art+'/bodybuilding.png')
    main.addDir('Shoulders','http://www.bodybuilding.com/exercises/list/muscle/selected/shoulders',196,art+'/bodybuilding.png')
    main.addDir('Traps','http://www.bodybuilding.com/exercises/list/muscle/selected/traps',196,art+'/bodybuilding.png')
    main.addDir('Triceps','http://www.bodybuilding.com/exercises/list/muscle/selected/triceps',196,art+'/bodybuilding.png')

def LISTBB(murl):
    main.GA("BodyBuilding","List")   
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('img src="http://assets.bodybuilding.com','')
    match=re.compile('''img src="(.+?)".+? title="(.+?)" /></a>.+?<h3>.+?<a href=\'(.+?)'> .+? </a>.+?Muscle Targeted:.+?> (.+?) </a>''').findall(link)
    for thumb,name,url,body in match:    
        main.addPlayMs(name+"   [COLOR red]"+body+"[/COLOR]",url,197,thumb,'','','','','')


def LINKBB(mname,murl,thumb):
    main.GA("BodyBuilding","Watched")
    ok=True
    namelist=[]
    urllist=[]
    thumblist=[]
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('img src="http://assets.bodybuilding.com','')
    match=re.compile('<div id=".+?" style="display:.+?">                <div id="(.+?)Video">                    <div class="BBCOMVideoEmbed" data-video-id="(.+?)" data-thumbnail-url="(.+?)"').findall(link)
    for gender,vidid,thumb in match:
        namelist.append(gender)
        urllist.append(vidid)
        thumblist.append(thumb)
    dialog = xbmcgui.Dialog()
    answer =dialog.select("Playlist", namelist)
    listitem = xbmcgui.ListItem(mname, thumbnailImage=thumblist[int(answer)])
    stream_url = "http://videocdn.bodybuilding.com/video/mp4/"+urllist[int(answer)]+"m.mp4"
    # play with bookmark
    player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels='', watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
    #WatchHistory
    if selfAddon.getSetting("whistory") == "true":
        wh.add_item(mname+' '+'[COLOR green]BodyBuilding[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
    player.KeepAlive()
    return ok
