# -*- coding: cp1252 -*-
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

def MAINFB():
    main.GA("Sports","FitnessBlender")   
    main.addDir('Body Focus','bf',199,art+'/fitnessblender.png')
    main.addDir('Difficulty','bf',200,art+'/fitnessblender.png')
    main.addDir('Training Type','bf',201,art+'/fitnessblender.png')

def DIFFFB():  
    main.addDir('Level 1','http://www.fitnessblender.com/v/full-length-workouts/?all=1p=1&str=&time_min=&time_max=&cal_min=&cal_max=&difficulty[]=1&type[]=&equipment[]=&body_focus[]=',202,art+'/fitnessblender.png')
    main.addDir('Level 2','http://www.fitnessblender.com/v/full-length-workouts/?all=1p=1&str=&time_min=&time_max=&cal_min=&cal_max=&difficulty[]=2&type[]=&equipment[]=&body_focus[]=',202,art+'/fitnessblender.png')
    main.addDir('Level 3','http://www.fitnessblender.com/v/full-length-workouts/?all=1p=1&str=&time_min=&time_max=&cal_min=&cal_max=&difficulty[]=3&type[]=&equipment[]=&body_focus[]=',202,art+'/fitnessblender.png')
    main.addDir('Level 4','http://www.fitnessblender.com/v/full-length-workouts/?all=1p=1&str=&time_min=&time_max=&cal_min=&cal_max=&difficulty[]=4&type[]=&equipment[]=&body_focus[]=',202,art+'/fitnessblender.png')
    main.addDir('Level 5','http://www.fitnessblender.com/v/full-length-workouts/?all=1p=1&str=&time_min=&time_max=&cal_min=&cal_max=&difficulty[]=5&type[]=&equipment[]=&body_focus[]=',202,art+'/fitnessblender.png')

def BODYFB():
    main.addDir('Upper Body','http://www.fitnessblender.com/v/full-length-workouts/?all=1p=1&str=&time_min=&time_max=&cal_min=&cal_max=&difficulty[]=&type[]=&equipment[]=&body_focus[]=36',202,art+'/fitnessblender.png')
    main.addDir('Core','http://www.fitnessblender.com/v/full-length-workouts/?all=1p=1&str=&time_min=&time_max=&cal_min=&cal_max=&difficulty[]=&type[]=&equipment[]=&body_focus[]=34',202,art+'/fitnessblender.png')
    main.addDir('Lower Body','http://www.fitnessblender.com/v/full-length-workouts/?all=1p=1&str=&time_min=&time_max=&cal_min=&cal_max=&difficulty[]=&type[]=&equipment[]=&body_focus[]=35',202,art+'/fitnessblender.png')
    main.addDir('Total Body','http://www.fitnessblender.com/v/full-length-workouts/?all=1p=1&str=&time_min=&time_max=&cal_min=&cal_max=&difficulty[]=&type[]=&equipment[]=&body_focus[]=37',202,art+'/fitnessblender.png')

def TRAINFB():
    main.addDir('Balance/Agility','http://www.fitnessblender.com/v/full-length-workouts/?all=1p=1&str=&time_min=&time_max=&cal_min=&cal_max=&difficulty[]=&type[]=3e&equipment[]=&body_focus[]=',202,art+'/fitnessblender.png')
    main.addDir('Barre','http://www.fitnessblender.com/v/full-length-workouts/?all=1p=1&str=&time_min=&time_max=&cal_min=&cal_max=&difficulty[]=&type[]=3a&equipment[]=&body_focus[]=',202,art+'/fitnessblender.png')
    main.addDir('Cardiovascular','http://www.fitnessblender.com/v/full-length-workouts/?all=1p=1&str=&time_min=&time_max=&cal_min=&cal_max=&difficulty[]=&type[]=3f&equipment[]=&body_focus[]=',202,art+'/fitnessblender.png')
    main.addDir('HIIT','http://www.fitnessblender.com/v/full-length-workouts/?all=1p=1&str=&time_min=&time_max=&cal_min=&cal_max=&difficulty[]=&type[]=38&equipment[]=&body_focus[]=',202,art+'/fitnessblender.png')
    main.addDir('Kettlebell','http://www.fitnessblender.com/v/full-length-workouts/?all=1p=1&str=&time_min=&time_max=&cal_min=&cal_max=&difficulty[]=&type[]=39&equipment[]=&body_focus[]=',202,art+'/fitnessblender.png')
    main.addDir('Low Impact','http://www.fitnessblender.com/v/full-length-workouts/?all=1p=1&str=&time_min=&time_max=&cal_min=&cal_max=&difficulty[]=&type[]=3c&equipment[]=&body_focus[]=',202,art+'/fitnessblender.png')
    main.addDir('Pilates','http://www.fitnessblender.com/v/full-length-workouts/?all=1p=1&str=&time_min=&time_max=&cal_min=&cal_max=&difficulty[]=&type[]=3d&equipment[]=&body_focus[]=',202,art+'/fitnessblender.png')
    main.addDir('Plyometric','http://www.fitnessblender.com/v/full-length-workouts/?all=1p=1&str=&time_min=&time_max=&cal_min=&cal_max=&difficulty[]=&type[]=3h&equipment[]=&body_focus[]=',202,art+'/fitnessblender.png')
    main.addDir('Strength Training','http://www.fitnessblender.com/v/full-length-workouts/?all=1p=1&str=&time_min=&time_max=&cal_min=&cal_max=&difficulty[]=&type[]=3i&equipment[]=&body_focus[]=',202,art+'/fitnessblender.png')
    main.addDir('Toning','http://www.fitnessblender.com/v/full-length-workouts/?all=1p=1&str=&time_min=&time_max=&cal_min=&cal_max=&difficulty[]=&type[]=3j&equipment[]=&body_focus[]=',202,art+'/fitnessblender.png')
    main.addDir('Warm Up/Cool Down','http://www.fitnessblender.com/v/full-length-workouts/?all=1p=1&str=&time_min=&time_max=&cal_min=&cal_max=&difficulty[]=&type[]=3v&equipment[]=&body_focus[]=',202,art+'/fitnessblender.png')
    main.addDir('Yoga/Stretching/Flexibility','http://www.fitnessblender.com/v/full-length-workouts/?all=1p=1&str=&time_min=&time_max=&cal_min=&cal_max=&difficulty[]=&type[]=3b&equipment[]=&body_focus[]=',202,art+'/fitnessblender.png')

def LISTBF(murl):
    main.GA("FitnessBlender","List")   
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('–','-')
    main.addLink("[COLOR red]Body Focus   [/COLOR]"+"[COLOR yellow]Calorie Burn   [/COLOR]"+"[COLOR blue]Difficulty   [/COLOR]"+"[COLOR green]Duration[/COLOR]",'','')
    match=re.compile('<a class="teaser group" href="(.+?)"><div class=".+?<img id=".+?" class="fit_img.+?data-original="(.+?)" alt="([^"]+)".+?"><p>Calorie Burn:(.+?)</p><p>Minutes:(.+?)</p><p>Difficulty:(.+?)</p><p>Body Focus:(.+?)</p></div>').findall(link)
    for url,thumb,name,cal,dur,diff,bf in match:    
        main.addPlayMs(name+"  [COLOR red]"+bf+"[/COLOR]"+"[COLOR yellow]"+cal+"[/COLOR]"+"[COLOR blue]"+diff+"[/COLOR]"+"[COLOR green]"+dur+"[/COLOR]",'http://www.fitnessblender.com/'+url,203,thumb,'','','','','')

def LINKBB(mname,murl,thumb):
    ok=True
    main.GA("FitnessBlender","Watched")
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('–','-')
    match=re.compile('src="http://www.youtube.com/embed/(.+?).?rel').findall(link)
    for url in match:
        url = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+url
    stream_url = url
    # play with bookmark
    player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='', title=mname,season='', episode='', year='',img=thumb,infolabels='', watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id='')
    #WatchHistory
    if selfAddon.getSetting("whistory") == "true":
            wh.add_item(mname+' '+'[COLOR green]Fitness Blender[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
    player.KeepAlive()
    return ok
