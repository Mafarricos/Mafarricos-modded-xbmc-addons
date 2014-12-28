#-*- coding: utf-8 -*-
import xbmc,xbmcgui, xbmcaddon, xbmcplugin
import urllib,re,string,os,time,threading

try:
    from resources.libs import main,settings    
except Exception, e:
    elogo = xbmc.translatePath('special://home/addons/plugin.video.movie25/resources/art/bigx.png')
    dialog = xbmcgui.Dialog()
    ok=dialog.ok('[B][COLOR=FF67cc33]Mash Up Import Error[/COLOR][/B]','Failed To Import Needed Modules',str(e),'Report missing Module at [COLOR=FF67cc33]mashupxbmc.com[/COLOR] to Fix')
    xbmc.log('Mash Up ERROR - Importing Modules: '+str(e), xbmc.LOGERROR)
    
#Mash Up - by Mash2k3 2012.

#################### Set Environment ######################
ENV = "Prod"  # "Prod" or "Dev"
###########################################################

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
movie25url = 'http://www.movie25.cm/'

################################################################################ Directories ##########################################################################################################
UpdatePath=os.path.join(main.datapath,'Update')
try: os.makedirs(UpdatePath)
except: pass
CachePath=os.path.join(main.datapath,'Cache')
try: os.makedirs(CachePath)
except: pass
CookiesPath=os.path.join(main.datapath,'Cookies')
try: os.makedirs(CookiesPath)
except: pass
TempPath=os.path.join(main.datapath,'Temp')
try: os.makedirs(TempPath)
except: pass

def AtoZ():
    main.addDir('0-9',movie25url+'movies/0-9/',1,art+'/09.png')
    for i in string.ascii_uppercase: main.addDir(i,movie25url+'movies/'+i.lower()+'/',1,art+'/'+i.lower()+'.png')

def MAIN():
    xbmcgui.Window(10000).clearProperty('MASH_SSR_TYPE')
    d = settings.getHomeItems()
    for index, value in sorted(enumerate(d), key=lambda x:x[1]):
        if value==None: continue
        if index==0: main.addDirHome('Search',movie25url,420,art+'/search2.png')
        elif index==1: main.addDirHome("All Fav's",movie25url,639,art+'/favsu.png')
        elif index==2: main.addDirHome('A-Z',movie25url,6,art+'/az2.png')
        elif index==3: main.addDirHome('New Releases',movie25url+'movies/new-releases/',1,art+'/new2.png')
        elif index==4: main.addDirHome('Latest Added',movie25url+'movies/latest-added/',1,art+'/latest2.png')
        elif index==5: main.addDirHome('Featured Movies',movie25url+'movies/featured-movies/',1,art+'/feat2.png')
        elif index==6: main.addDirHome('Most Viewed',movie25url+'movies/most-viewed/',1,art+'/view2.png')
        elif index==7: main.addDirHome('Most Voted',movie25url+'movies/most-voted/',1,art+'/vote2.png')
        elif index==8: main.addDirHome('HD Releases',movie25url+'latest-hd-movies/',1,art+'/dvd2hd.png')
        elif index==9: main.addDirHome('Genre',movie25url,2,art+'/genre2.png')
        elif index==10: main.addDirHome('By Year',movie25url,7,art+'/year2.png')
        elif index==11: main.addDirHome('Watch History','history',222,art+'/whistory.png')
        elif index==12: main.addDirHome('HD Movies','_',33,art+'/hd2.png')
        elif index==13: main.addDirHome('3D Movies','3D',223,art+'/3d.png')
        elif index==14: main.addDirHome('International',movie25url,36,art+'/intl.png')
        elif index==15: main.addDirHome('TV Latest','_',27,art+'/tv2.png')
        elif index==16: main.addDirHome('Live Streams',movie25url,115,art+'/live.png')
        elif index==17: main.addDirHome('More TV Shows & Movies',movie25url,500,art+'/moretvmovies.png')
        elif index==18: main.addDirHome('Anime',movie25url,265,art+'/anime.png')
        elif index==19: main.addDirHome('[COLOR=FF67cc33]VIP[/COLOR]laylists',movie25url,234,art+'/vipp.png')
        elif index==20: main.addDirHome('Sports',movie25url,43,art+'/sportsec2.png')
        elif index==21: main.addDirHome('Adventure',movie25url,63,art+'/adv2.png')
        elif index==22: main.addDirHome('Kids Zone',movie25url,76,art+'/kidzone2.png')
        elif index==23: main.addDirHome('Documentaries',movie25url,85,art+'/docsec1.png')
        elif index==24: main.addDirHome("Mash Up How To's",'how',16,art+'/howto.png')
        elif index==25: main.addDirHome('Fixes',movie25url,784,art+'/fixes.png')
        elif index==26: main.addDirHome('HackerMils Stash','https://raw.github.com/HackerMil/HackerMilsMovieStash/master/Directory/HackerMil_Directory.xml',235,art+'/hackermil.png')
        elif index==29: main.addDirHome('Staael 1982','http://tuzla.watchkodi.com/maindir/main.xml',235,art+'/staael2014.png')
        elif index==34: main.addDirHome('Demon88 Movies','http://cairo.watchkodi.com/maindir/main.xml',235,art+'/demon88.png')
        elif index==37: main.addDirHome('ONE242415','http://gibraltar.watchkodi.com/maindir/main.xml',235,art+'/one252515.png')
        elif index==30: main.addDirHome('My XML Channels','nills',238,art+'/xml.png')
        elif index==31: main.addDirHome("K1M05's Streams",'https://raw.github.com/xbmctalk/MashUpK1m05/master/k1m05_mashupDirectory.xml',181,art+'/k1m05.png')
        elif index==32: main.addDirHome('Buzzy Sports','http://banjaluka.watchkodi.com/maindir/main.xml',181,art+'/mashsports.png')
        elif index==33: main.addDirHome('iLive Streams','ilive',119,art+'/ilive.png')
        elif index==35: main.addDirHome('Super Search','ss',19,art+'/supersearch.png')
        elif index==36:
            if selfAddon.getSetting("stracker") == '0': main.addDirHome("SideReel Show Tracker",'Mash Up',397,art+'/sidereel.png')
            elif selfAddon.getSetting("stracker") == '1': main.addDirHome("Trakt Show Tracker",'Mash Up',429,art+'/trakt.png')
            else:
                main.addDirHome("SideReel Show Tracker",'Mash Up',397,art+'/sidereel.png')
                main.addDirHome("Trakt Show Tracker",'Mash Up',429,art+'/trakt.png')
        elif index==38: main.addDirHome('Super Movies','index',1052,art+'/supermovies.png',index=True)
        elif index==39: main.addDirHome('Super TV Shows','index',1054,art+'/supershows.png',index=True)
    main.addPlayc('Need Help?',movie25url,100,art+'/help.png','','','','','')
    main.addPlayc('Upload Log',movie25url,156,art+'/loguploader.png','','','','','')
    main.addPlayc('Click Me!!!','https://raw.github.com/mash2k3/MashupArtwork/master/skins/vector/donation.png',244,art+'/paypalmash2.png','','','','','')
    main.addSpecial('@mashupxbmc','','',art+'/twittermash.png')
    main.addPlayc('MashUp Settings',movie25url,1999,art+'/MashSettings.png','','','','','')
              
def Announcements():
    #Announcement Notifier from xml file
    print 'No Messages'

def cacheSideReel():
    user = selfAddon.getSetting('srusername')
    passw = selfAddon.getSetting('srpassword')
    cached_path = os.path.join(CachePath, 'Sidereel')
    import datetime
    if (user and passw) and (not os.path.exists(cached_path) or time.mktime(datetime.date.today().timetuple()) > os.stat(cached_path).st_mtime):
        from resources.libs.movies_tv import sidereel
        sidereel.MAINSIDE(True)
        
def cacheTrakt():
    user = selfAddon.getSetting('trusername')
    passw = selfAddon.getSetting('trpassword')
    cached_path = os.path.join(CachePath, 'Trakt')
    import datetime
    if (user and passw) and (not os.path.exists(cached_path) or time.mktime(datetime.date.today().timetuple()) > os.stat(cached_path).st_mtime):
        from resources.libs.movies_tv import trakt
        trakt.showList(True)
        
def Notify():
    mashup=139
    runonce=os.path.join(main.datapath,'RunOnce')
    try: os.makedirs(runonce)
    except: pass
    notified=os.path.join(runonce,str(mashup))
    if not os.path.exists(notified):
        open(notified,'w').write('version="%s",'%mashup)
        dir = selfAddon.getAddonInfo('path')
        chlg = os.path.join(dir, 'changelog.txt')
        TextBoxes("[B][COLOR red]Mash Up Changelog[/B][/COLOR]",chlg)
        mashup=mashup-1
        notified=os.path.join(runonce,str(mashup))
        if  os.path.exists(notified): os.remove(notified)
        
def GENRE(url,index=False):
    main.addDir('Action',movie25url+'action/',1,art+'/act.png',index=index)
    main.addDir('Adventure',movie25url+'adventure/',1,art+'/adv.png',index=index)
    main.addDir('Animation',movie25url+'animation/',1,art+'/ani.png',index=index)
    main.addDir('Biography',movie25url+'biography/',1,art+'/bio.png',index=index)
    main.addDir('Comedy',movie25url+'comedy/',1,art+'/com.png',index=index)
    main.addDir('Crime',movie25url+'crime/',1,art+'/cri.png',index=index)
    main.addDir('Documentary',movie25url+'documentary/',1,art+'/doc.png',index=index)
    main.addDir('Drama',movie25url+'drama/',1,art+'/dra.png',index=index)
    main.addDir('Family',movie25url+'family/',1,art+'/fam.png',index=index)
    main.addDir('Fantasy',movie25url+'fantasy/',1,art+'/fant.png',index=index)
    main.addDir('History',movie25url+'history/',1,art+'/his.png',index=index)
    main.addDir('Horror',movie25url+'horror/',1,art+'/hor.png',index=index)
    main.addDir('Music',movie25url+'music/',1,art+'/mus.png',index=index)
    main.addDir('Musical',movie25url+'musical/',1,art+'/mucl.png',index=index)
    main.addDir('Mystery',movie25url+'mystery/',1,art+'/mys.png',index=index)
    main.addDir('Romance',movie25url+'romance/',1,art+'/rom.png',index=index)
    main.addDir('Sci-Fi',movie25url+'sci-fi/',1,art+'/sci.png',index=index)
    main.addDir('Short',movie25url+'short/',1,art+'/sho.png',index=index)
    main.addDir('Sport',movie25url+'sport/',1,art+'/sport.png',index=index)
    main.addDir('Thriller',movie25url+'thriller/',1,art+'/thr.png',index=index)
    main.addDir('War',movie25url+'war/',1,art+'/war.png',index=index)
    main.addDir('Western',movie25url+'western/',1,art+'/west.png',index=index)
    main.VIEWSB()
        
def YEAR(index=False):
	for x in reversed(xrange(2003,2015,1)): main.addDir(str(x),movie25url+'search.php?year='+str(x)+'/',8,art+'/'+str(x)+'.png',index=index)
	main.addDir('Enter Year',movie25url,23,art+'/enteryear.png',index=index)
	main.VIEWSB()

def GlobalFav():
    if selfAddon.getSetting("groupfavs") == "true": ListglobalFavALL()
    else:
        main.addLink("[COLOR red]Mash Up Fav's can also be favorited under XBMC favorites[/COLOR]",'','')
        main.addDir("Downloaded Content",'Mash Up',241,art+'/downloadlog.png')
        main.addDir("Movie Fav's",movie25url,641,art+'/fav.png')
        main.addDir("TV Show Fav's",movie25url,640,art+'/fav.png')
        main.addDir("TV Episode Fav's",movie25url,651,art+'/fav.png')
        main.addDir("Live Fav's",movie25url,648,art+'/fav.png')
        main.addDir("Misc. Fav's",movie25url,650,art+'/fav.png')
    
def TV():
    main.ClearDir(TempPath)
    if selfAddon.getSetting("stracker") == '0': main.addDir("SideReel Show Tracker",'Mash Up',397,art+'/sidereel.png')
    elif selfAddon.getSetting("stracker") == '1': main.addDir("Trakt Show Tracker",'Mash Up',429,art+'/trakt.png')
    else:
        main.addDir("SideReel Show Tracker",'Mash Up',397,art+'/sidereel.png')
        main.addDir("Trakt Show Tracker",'Mash Up',429,art+'/trakt.png')
    main.addDir('Latest Episodes (Newmyvideolinks) True HD[COLOR red] DC[/COLOR]','TV',34,art+'/tvb.png')
    main.addDir('Latest Episodes (Rlsmix)[COLOR red](Debrid Only)[/COLOR] True HD[COLOR red] DC[/COLOR]','TV',61,art+'/tvb.png')
    if selfAddon.getSetting("ddtv_my") == "true": main.addDir('My Latest Episodes (Rlsmix)[COLOR red](Debrid Only)[/COLOR] True HD[COLOR red] DC[/COLOR]','0#my',61,art+'/tvb.png')
    main.addDir('Latest Episodes (Sceper)[COLOR red](Debrid Only)[/COLOR] True HD','http://sceper.ws/home/category/tv-shows',545,art+'/tvb.png')
    main.addDir('Latest Episodes (TvRelease) True HD[COLOR red] DC[/COLOR]','http://www.tv-release.net/?cat=TV-720p',1001,art+'/tvb.png')
    main.addDir('Latest Episodes (SceneLog) True HD[COLOR red] DC[/COLOR]','TV',657,art+'/tvb.png')
    main.addDir('Latest Episodes (IceFilms) True HD[COLOR red] DC[/COLOR]','TV',291,art+'/tvb.png')
    main.addDir('Latest Episodes (TubePlus)[COLOR red] DC[/COLOR]','http://www.tubeplus.me/browse/tv-shows/Last/ALL/',1041,art+'/tvb.png')
    main.addDir('Latest Episodes (Watchseries)','http://watchseries.ag/tvschedule/-1',573,art+'/tvb.png')
    main.addDir('Latest Episodes (iWatchonline)','http://www.iwatchonline.to/tv-schedule',592,art+'/tvb.png')
    main.addDir('Latest Episodes (Movie1k)','movintv',30,art+'/tvb.png')
    main.addDir('Latest Episodes (Oneclickwatch)','http://oneclickwatch.org',32,art+'/tvb.png')
    main.addDir('Latest Episodes (Seriesgate)','http://seriesgate.tv/latestepisodes/',602,art+'/tvb.png')
    main.addDir('Latest 150 Episodes (ChannelCut)','http://www.channelcut.tv/last-150',546,art+'/tvb.png')

def ThreeDsec():
    main.addDir('3D Movies (Newmyvideolinks) True HD[COLOR red] DC[/COLOR]','3D',34,art+'/3d.png')
    link=getListFile('https://raw.github.com/Leinad4Mind/Leinad4Mind-xbmc-addons/master/Mash_modded/3D_Dir.xml', os.path.join(CachePath,'ThreeD'))
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.compile('<name>(.+?)</name><link>(.+?)</link><thumbnail>(.+?)</thumbnail><mode>(.+?)</mode>').findall(link)
    for name,url,thumb,mode in match:
        if re.findall('http',thumb): thumbs=thumb
        else: thumbs=art+'/'+thumb+'.png'
        main.addDir(name,url,int(mode),thumbs)

def TVAll():
    main.ClearDir(TempPath)
    main.addDir('Watchseries[COLOR red] DC[/COLOR]','TV',572,art+'/watchseries.png')
    main.addDir('tubePLUS[COLOR red] DC[/COLOR]','tp+',1020,art+'/tubeplus.png')
    main.addDir('Icefilms[COLOR red] DC[/COLOR]','ice',294,art+'/icefilms.png')
    main.addDir('PFTV[COLOR red] DC[/COLOR]','TV',459,art+'/pftv.png')
    main.addDir('Series Gate','TV',601,art+'/sg.png')
    main.addDir('iWatchOnline [COLOR red] DC[/COLOR]','TV',584,art+'/iwatchonline.png')
    main.addDir('TV-Release[COLOR red] DC[/COLOR][COLOR blue] (Works Best With Debrid)[/COLOR]','tvr',1000,art+'/tvrelease.png')
    main.addDir('Movie25 [COLOR red]DC[/COLOR]','TV',267,art+'/movie25.png')
    main.addDir('Sceper [COLOR red](Debrid Only)[/COLOR]','TV',539,art+'/sceper.png')
    main.addDir('SceneSource [COLOR red](Debrid Only)[/COLOR]','TV',387,art+'/scenesource.png')
    main.addDir('Noobroom [COLOR red]DC[/COLOR]','TV',296,art+'/noobroom.png')
    main.addDir('MBox [COLOR red]DC[/COLOR]','TV',276,art+'/mbox.png')
    main.addDir('Yify','yify',421,art+'/yify.png')
    #main.addDir('Shush','TV',451,art+'/shush.png')
    main.addDir('SominalTvFilms','TV',619,art+'/sominal.png')
    main.addDir('Dramania','TV',268,art+'/dramania.png')
    main.addDir('SokroStream','french',324,art+'/sokrostream.png')
    main.addDir('Aflam1','arabic',335,art+'/aflam1.png')
    main.addDir('3Arabtv','arabic',351,art+'/3arabtv.png')
    main.addDir('MailRu','http://my.mail.ru/video/top',357,art+'/mailru.png')
    #main.addDir('Watching Now','TV',530,art+'/watchingnow.png')
    #main.addDir('FMA','TV',567,art+'/fma.png')
    #main.addDir('Global BC','gbc',165,art+'/globalbc.png')       

def Movie25(index=False):
    main.addDirHome('Search',movie25url,420,art+'/search2.png',index=index)
    main.addDirHome('A-Z',movie25url,6,art+'/az2.png',index=index)
    main.addDirHome('New Releases',movie25url+'new-releases/',1,art+'/new2.png',index=index)
    main.addDirHome('Latest Added',movie25url+'latest-added/',1,art+'/latest2.png',index=index)
    main.addDirHome('Featured Movies',movie25url+'featured-movies/',1,art+'/feat2.png',index=index)
    main.addDirHome('Most Viewed',movie25url+'most-viewed/',1,art+'/view2.png',index=index)
    main.addDirHome('Most Voted',movie25url+'most-voted/',1,art+'/vote2.png',index=index)
    main.addDirHome('HD Releases',movie25url+'latest-hd-movies/',1,art+'/dvd2hd.png',index=index)
    main.addDirHome('Genre',movie25url,2,art+'/genre2.png',index=index)
    main.addDirHome('By Year',movie25url,7,art+'/year2.png',index=index)

def ANIME():
    main.addDir('Animania','TV',343,art+'/animania.png')
    main.addDir('AnimeToon','TV',374,art+'/animetoon.png')
    main.addDir('dubzonline','TV',613,art+'/dubzonline.png')
    main.addDir('AnimeFreak TV','TV',625,art+'/animefreak.png')

def HD():
    main.addDir('Latest HD Movies (Newmyvideolinks) True HD[COLOR red] DC[/COLOR]','http://newmyvideolinks.com',34,art+'/hd2.png')
    main.addDir('Latest HD Movies (Dailyflix) True HD','HD',53,art+'/hd2.png')
    main.addDir('Latest HD Movies ([COLOR=FF67cc33]Noobroom[/COLOR]) Direct MP4 True HD[COLOR red] DC[/COLOR]','/latest.php',57,art+'/hd2.png')
    main.addDir('Latest HD Movies (MBox) True HD[COLOR red] DC[/COLOR]','movies',285,art+'/hd2.png')
    main.addDir('Latest HD Movies (Yify) True HD[COLOR red] DC[/COLOR]','http://yify.tv/files/movies/',422,art+'/hd2.png')
    main.addDir('Latest HD Movies (Icefilms) True HD[COLOR red] DC[/COLOR]','/movies/added/hd',282,art+'/hd2.png')
    main.addDir('Latest HD Movies (TV-Release) True HD[COLOR red] DC[/COLOR]','http://www.tv-release.net/?cat=Movies-720p',1001,art+'/hd2.png')
    #main.addDir('Latest HD Movies (Oneclickmovies)[COLOR red](Debrid Only)[/COLOR] True HD[COLOR red] DC[/COLOR]','www.scnsrc.me',55,art+'/hd2.png')
    main.addDir('Latest HD Movies (Sceper)[COLOR red](Debrid Only)[/COLOR] True HD','http://sceper.ws/category/movies/movies-bluray-rip',541,art+'/hd2.png')
    main.addDir('Latest HD Movies (SceneSource)[COLOR red](Debrid Only)[/COLOR] True HD','http://www.scenesource.me/films/bluray/',389,art+'/hd2.png')
    main.addDir('Latest True 1080p Movies (FilesTube)[COLOR red](Debrid Only)[/COLOR]','HD',405,art+'/hd2.png')
    main.addDir('Latest True 1080p Movies (Rls1Click)[COLOR red](Debrid Only)[/COLOR]','HD',407,art+'/hd2.png')
    main.addDir('Latest Movies (Oneclickwatch)','http://oneclickwatch.org/category/movies/',25,art+'/hd2.png')
    main.addDir('HackerMil HD Movies','https://raw.github.com/HackerMil/HackerMilsMovieStash/master/Movies/HD.xml',236,art+'/hd2.png')
    main.addDir('Staael1982 HD Movies','http://tuzla.watchkodi.com/veehdCollection.xml',236,art+'/hd2.png')
    main.addDir('Demon88 HD Movies','http://cairo.watchkodi.com/720p.xml',236,art+'/hd2.png')
    main.addDir('TNPB HD Movies','http://zenica.watchkodi.com/Movies/720p%20Movies.xml',236,art+'/hd2.png')
    main.addDir('HackerMil 1080p Movies','https://raw.githubusercontent.com/HackerMil/HackerMilsMovieStash/master/Movies/1080P.xml',236,art+'/hd2.png')
    main.addDir('Staael1982 1080p Movies','http://tuzla.watchkodi.com/1080p%20movies.xml',236,art+'/hd2.png')
    main.addDir('Demon88 1080p Movies','http://cairo.watchkodi.com/1080p.xml',236,art+'/hd2.png')
    main.addDir('TNPB 1080p Movies','http://zenica.watchkodi.com/Movies/1080p%20Movies.xml',236,art+'/hd2.png')
    
def INT():
    main.addDir('Hindi/Tamil/Telugu & more','hindi',15,art+'/folder.png')
    main.addDir('Spanish/Latino/Castelino','spanish',15,art+'/folder.png')
    main.addDir('French','french',15,art+'/folder.png')
    main.addDir('Italian','italian',15,art+'/folder.png')
    main.addDir('Arabic','arabic',15,art+'/folder.png')
    main.addDir('UK','uk',15,art+'/folder.png')
    main.addDir('Korean/Jappenese/Chinese','kor',15,art+'/folder.png')
    main.addDir('Russian','russian',15,art+'/folder.png')
    main.addDir('Danish','danish',15,art+'/folder.png')

def INTCAT(murl):
    if 'italian'in murl:
        main.addDir('Cinema Italiano','http://gibraltar.watchkodi.com/CinemaItaliano/cinemaitaliano_directory.xml',236,art+'/intl.png')
        main.addDir('Italian Series','http://gibraltar.watchkodi.com/Foriegn/italianseries.xml',236,art+'/intl.png')
        main.addDir('Live Italian TV','http://gibraltar.watchkodi.com/Foriegn/italianLiveTV.xml',236,art+'/intl.png')
    if 'russian' in murl:
        main.addDir('Latest Russian Movies (Cinemaxx)','russia',362,art+'/intl.png')
        main.addDir('Russian Videos(MailRu)','http://my.mail.ru/video/top',357,art+'/intl.png')
    if 'hindi' in murl:
        main.addDir('Latest Indian Subtitled Movies (einthusan)','http://www.einthusan.com',37,art+'/intl.png')
        main.addDir('Latest Hindi/Tamil/Telugu & more (sominaltv)','TV',619,art+'/intl.png')
        main.addDir('Latest Indian Movies (Movie1k)','movin',30,art+'/intl.png')
        main.addDir('Latest Indian Dubbed Movies (Movie1k)','movindub',30,art+'/intl.png')
        main.addDir("XcTech's Bollywood Playlist",'PLvNKtQkKaqg8IPssr3WG4-YkOEAe8TQ0j',205,art+'/intl.png')
    if 'arabic' in murl:
        main.addDir('Latest Arabic Movies/Series & more (Aflam1)','arabic',335,art+'/intl.png')
        main.addDir('Latest Arabic Movies/Series/Shows (3Arabtv)','arabic',351,art+'/intl.png')
    if 'uk' in murl:
        main.addDir('Latest UK and US (Mooviemaniac)','movindub',305,art+'/intl.png')
        main.addDir('Best of British (TNPB)','http://zenica.watchkodi.com/Directories/BoB%20Directory.xml',236,art+'/intl.png')
    if 'spanish' in murl:
        main.addDir('Latest Spanish Dubbed & Subtitled(ESP) Movies (peliculaspepito)','http://www.peliculaspepito.com',66,art+'/intl.png')
        main.addDir('Latest Spanish Dubbed & Subtitled(ESP) Movies (FXCine)','http://www.fxcine.com',308,art+'/intl.png')
    if 'french' in murl:
        main.addDir('Latest French Dubbed & Subtitled Movies (DPStreaming)','http://www.dps.com',311,art+'/intl.png')
        main.addDir('Latest French Dubbed & Subtitled Movies (SokroStream)','http://www.dps.com',324,art+'/intl.png')
        main.addDir('Latest French Dubbed & Subtitled Movies (Frenchstream)','http://www.dps.com',367,art+'/intl.png')
        main.addDir('Latest French (FullStream)','http://www.dps.com',786,art+'/intl.png')
        main.addDir('Latest French (FullStream 2)','http://www.dps.com',794,art+'/intl.png')
        main.addDir('Latest French Documentaire (Video Documentaire)','http://www.dps.com',331,art+'/intl.png')
    if 'kor' in murl:
        main.addDir('Latest Korean/Jappenese/Chinese Movies&Dramas (Dramania)','http://www.cinevip.org/',268,art+'/intl.png')
        main.addDir('Latest Korean/Jappenese/Chinese Movies&Dramas (Viki)','http://www.cinevip.org/',478,art+'/intl.png')
        #main.addDir('Latest Korean/Jappenese/Chinese Movies&Dramas (Catiii.tv)','http://www.cinevip.org/',434,art+'/intl.png')
    if 'danish' in murl: main.addDir('Staael1982 Danish Movies','http://tuzla.watchkodi.com/Danish%20movies/Danish%20movies%20directory.xml',236,art+'/intl.png')

def SPORTS():
    main.addDir('ESPN','http:/espn.com',44,art+'/espn.png')
    main.addDir('TSN','http:/tsn.com',95,art+'/tsn.png')
    main.addDir('SkySports.com','www1.skysports.com',172,art+'/skysports.png')
    main.addDir('Fox Soccer  [COLOR red](US ONLY)[/COLOR]','http:/tsn.com',124,art+'/foxsoc.png')
    main.addDir('MLB','mlb',447,art+'/mlb.png')
    main.addDir('All MMA','mma',537,art+'/mma.png')
    main.addDir('Outdoor Channel','http://outdoorchannel.com/',50,art+'/OC.png')
    main.addDir('My Outdoor TV','http://outdoorchannel.com/',360,art+'/myoutdoortv.png')
    main.addDir('Wild TV','https://www.wildtv.ca/shows',92,art+'/wildtv.png')
    main.addDir('Workouts','https://www.wildtv.ca/shows',194,art+'/workout.png')
    main.addDir('The Golf Channel','golf',217,art+'/golfchannel.png')
    main.addDir('HQZone','na',470,art+'/hqzone.png')
    link=getListFile('https://raw.github.com/Leinad4Mind/Leinad4Mind-xbmc-addons/master/Mash_modded/Sports_Dir.xml', os.path.join(CachePath,'Sports'))
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.compile('<name>(.+?)</name><link>(.+?)</link><thumbnail>(.+?)</thumbnail><mode>(.+?)</mode>').findall(link)
    for name,url,thumb,mode in match:
        if re.findall('http',thumb): thumbs=thumb
        else: thumbs=art+'/'+thumb+'.png'
        main.addDir(name,url,int(mode),thumbs)

def MMA():
    main.addDir('UFC','ufc',59,art+'/ufc.png')
    main.addDir('Bellator','BellatorMMA',47,art+'/bellator.png')
    main.addDir('MMA Fighting.com','http://www.mmafighting.com/videos',113,art+'/mmafig.png')
    main.addDir('HackerMil Fight Club','https://raw.github.com/HackerMil/HackerMilsMovieStash/master/Fight%20Club/Fight%20Club.xml',236,art+'/mma.png')
            
def WorkoutMenu():
    main.addDir('Fitness Blender[COLOR red](Full Workouts)[/COLOR]','fb',198,art+'/fitnessblender.png')
    main.addDir('Insanity','http://watchseries.ag/serie/INSANITY_-_The_Asylum',578,art+'/insanity.png')
    main.addDir('P90X','http://watchseries.ag/serie/p90x',578,art+'/p90x.png')
    main.addDir('Body Building[COLOR red](Instructional Only)[/COLOR]','bb',195,art+'/bodybuilding.png')
    main.addDir('HackerMil Workouts','https://raw.github.com/HackerMil/HackerMilsMovieStash/master/Workouts/Workouts.xml',236,art+'/workout.png')
            
def UFC():
    main.addDir('UFC.com','ufc',47,art+'/ufc.png')
    main.addDir('UFC(Movie25)','ufc',60,art+'/ufc.png')
    main.addDir('UFC(Newmyvideolinks)','ufc',103,art+'/ufc.png')

def ADVENTURE():
    main.addDir('Discovery Channel','http://dsc.discovery.com/videos',631,art+'/disco.png')
    main.addDir('National Geographic','ng',70,art+'/ngc.png')
    main.addDir('Military Channel','http://military.discovery.com/videos',80,art+'/milcha.png')
    main.addDir('Science Channel','http://science.discovery.com/videos',81,art+'/scicha.png')
    main.addDir('Velocity Channel','http://velocity.discovery.com/videos',82,art+'/velo.png')
    main.addDir('Animal Planet','http://animal.discovery.com/videos',83,art+'/anip.png')

def KIDZone(murl):
    main.addDir('Disney Jr.','djk',107,art+'/disjr.png')
    main.addDir('National Geographic Kids','ngk',71,art+'/ngk.png')
    main.addDir('WB Kids','wbk',77,art+'/wb.png')
    main.addDir('Youtube Kids','wbk',84,art+'/youkids.png')
    main.addDir('TNPB Kids Movies','http://zenica.watchkodi.com/Genre/kidszone.xml',236,art+'/kidzone2.png')
    main.addDir('TNPB Kids Collectionz','http://zenica.watchkodi.com/Directories/Kidz%20Collectionz.xml',236,art+'/kidzone2.png')
    main.addDir('TNPB Kids TV Shows','http://zenica.watchkodi.com/Directories/Kids%20TV%20Directory.xml',236,art+'/kidzone2.png')
    main.addDir('TNPB Kids Cartoons','http://zenica.watchkodi.com/Directories/Cartoonland%20Directory.xml',236,art+'/kidzone2.png')
    main.addDir('Staael1982 Animated Movies','http://tuzla.watchkodi.com/kids_animation.xml',236,art+'/kidzone2.png')
    main.addDir('Staael1982 Animated Movies 2','http://tuzla.watchkodi.com/test%20list.xml',236,art+'/kidzone2.png')
    main.VIEWSB()

def HOWTOCAT():
    main.addDir("MashUp Installation Instructions",'PLzXXwZxGnHxbv-UVWa-TIoFUIXWCaY_rm',205,art+'/howto.png')
    main.addDir("MashUp Tutorials",'PLzXXwZxGnHxaup4QuaJOk9lC5Oms9L6NL',205,art+'/howto.png')
    main.addDir("MashUp Features & Reviews",'PLzXXwZxGnHxZS61kC2t0RdT-4ZcX44Ltd',205,art+'/howto.png')

def LiveStreams():
    threading.Thread(target=showLiveAnnouncements).start()
    TVGuide = xbmc.translatePath('special://home/addons/script.tvguidedixie')
    if  os.path.exists(TVGuide): main.addSpecial('OnTapp.tv','guide',1500,art+'/ontapp.png')
    main.addDir('Livestation News','http://mobile.livestation.com/',116,art+'/livestation.png')
    main.addDir('iLive Streams','ilive',119,art+'/ilive.png')
    main.addDir('Castalba Streams','castalgba',122,art+'/castalba.png')
    main.addDir('Misc. Music Streams','music',127,art+'/miscmusic.png')
    main.addDir('By Country','navi',143,art+'/countrysec.png')
    main.addDir('Arabic Streams','navi',231,art+'/arabicstream.png')
    main.addDir('NHL [COLOR red]GOTHAM ONLY[/COLOR]','navi',394,art+'/nhl.png')
    #main.addDir('Kiwi','kiwi',439,art+'/kiwi.png')
    link=getListFile('https://raw.github.com/Leinad4Mind/Leinad4Mind-xbmc-addons/master/Mash_modded/Live_Dir.xml',os.path.join(CachePath,'LiveStreams'))
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('type=playlistname=Sorted by user-assigned order','').replace('name=Sorted [COLOR=FF00FF00]by user-assigned order[/COLOR]','').replace('name=Live Tv Channels Twothumb','')
    match=re.compile('<name>(.+?)</name><link>(.+?)</link><thumbnail>(.+?)</thumbnail><mode>(.+?)</mode>').findall(link)
    for name,url,thumb,mode in match:
        if re.findall('http',thumb): thumbs=thumb
        else: thumbs=art+'/'+thumb+'.png'
        main.addDir(name,url,int(mode),thumbs)
    main.addDir('USA Live','na',457,art+'/usalive.png')
    main.addDir('SportsAccess','na',409,art+'/sportsaccess.png')
    main.addDir('HQZone','na',470,art+'/hqzone.png')
    if selfAddon.getSetting("customchannel") == "true": main.addDir('My XML Channels','nills',238,art+'/xml.png')
    main.addDir('TubTub.com','http://tubtub.com/',185,art+'/tubtub.png')
    main.addDir('181.FM Radio Streams','nills',191,art+'/181fm.png')
    main.addDir('1.FM Radio Streams','nills',446,art+'/1fm.png')

def DOCS():
    main.addDir('John Locker','John Locker',318,art+'/johnlocker.png')
    main.addDir('Vice','http://www.vice.com/shows',104,art+'/vice.png')
    main.addDir('Documentary Heaven','doc1',86,art+'/dh.png')
    main.addDir('Watch Documentary','doc1',159,art+'/watchdoc.png')
    main.addDir('Documentary Wire','doc1',226,art+'/docwire.png')
    main.addDir('Top Documentary Films','doc2',86,art+'/topdoc.png')
    main.addDir('Video Documentaire (French)','doc2',331,art+'/videodocumentaire.png')
    main.addDir('Documentary Log','doc3',86,art+'/doclog.png')
    main.addDir('HackerMil Documentaries','https://raw.github.com/HackerMil/HackerMilsMovieStash/master/Misc/7%20DOCUMENTARY.xml',236,art+'/docsec1.png')
    main.addDir('Documentaries (Movie25)',movie25url+'documentary/',1,art+'/doc.png')

def PlaylistDir():
    link=getListFile('https://raw.github.com/Leinad4Mind/Leinad4Mind-xbmc-addons/master/Mash_modded/MoviesList_Dir.xml',os.path.join(CachePath,'Playlist'))
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.compile('<name>(.+?)</name><link>(.+?)</link><thumbnail>(.+?)</thumbnail><mode>(.+?)</mode>').findall(link)
    for name,url,thumb,mode in match:
        if re.findall('http',thumb): thumbs=thumb
        else: thumbs=art+'/'+thumb+'.png'
        main.addDir(name,url,int(mode),thumbs)

def MAINDEL(murl):
    if 'packages' in murl:
        dialog = xbmcgui.Dialog()
        ret = dialog.yesno('Mash Up', 'Are you sure you want to delete packages folder','','','No', 'Yes')
        if ret:
            import os 
            folder = xbmc.translatePath(os.path.join('special://home/addons/packages', ''))
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
                try:
                    if os.path.isfile(file_path): os.unlink(file_path)
                except Exception, e: main.ErrorReport(e)
    if 'Malformed' in murl: xbmc.executebuiltin('XBMC.RunScript(special://home/addons/plugin.video.movie25/resources/fixes/malformedFix.py)')
    elif 'UrlResolver' in murl:
        from resources.fixes import importsDoctor
        module = 'script.module.urlresolver'
        prettyName = 'UrlResolver'
        fileurl = importsDoctor.getFileUrl(module)
        importsDoctor.fixModule(prettyName,fileurl)
    elif 'MetaHandler' in murl:
        from resources.fixes import importsDoctor
        module = 'script.module.metahandler'
        prettyName = 'MetaHandler'
        fileurl = importsDoctor.getFileUrl(module)
        importsDoctor.fixModule(prettyName,fileurl)
    elif 'ClearCache' in murl:
        dialog = xbmcgui.Dialog()
        if dialog.yesno('Mash Up', 'Are you sure you want to clear XBMC cache ?','','','No', 'Yes'):
            main.ClearDir(xbmc.translatePath('special://temp/'),True)
            xbmc.executebuiltin("XBMC.Notification(Clear XBMC Cache,Successful,5000,"")")
    elif 'MashCache' in murl:
        dialog = xbmcgui.Dialog()
        if dialog.yesno('Mash Up', 'Are you sure you want to clear MashUp Cache & Cookies?','','','No', 'Yes'):
            import os
            cached_path = os.path.join(main.datapath,'Cache')
            cookie_file = os.path.join(main.datapath,'Cookies')
            main.ClearDir(xbmc.translatePath(cached_path),True)
            main.ClearDir(xbmc.translatePath(cookie_file),True)
            xbmc.executebuiltin("XBMC.Notification(Clear XBMC Cache,Successful,5000,"")")

def LIBRTMP(mname,murl,xname=''):
    xname=str(xname)+' '+mname
    url='http://www.mediafire.com/api/folder/get_content.php?folder_key='+murl+'&chunk=1&content_type=folders&response_format=json&rand=1789'
    link = main.OPENURL(url)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.findall('{"folderkey":"([^"]+?)","name":"([^"]+?)","description":".+?,"created":"([^"]+?)","revision":".+?}',link)
    for key,name,date in match:
        if 'Android' in name and 'APK' not in name: name= name +' [COLOR red](Requires Root)[/COLOR] Use APK for ALT solution'
        main.addDirc(name,key,454,art+'/folder.png',xname,'','','','')
    lurl='http://www.mediafire.com/api/folder/get_content.php?r=srhp&content_type=files&filter=all&order_by=name&order_direction=asc&chunk=1&version=2&folder_key='+murl+'&response_format=json'
    link = main.OPENURL(lurl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.findall('{"quickkey":"([^"]+?)","hash":"([^"]+?)","filename":"([^"]+?)","description":".+?,"created":"([^"]+?)",.+?}}',link)
    for key,hash,fname,date in match:
        if 'librtmp.' in fname: main.addPlayc(fname,key,455,art+'/maintenance.png',xname,'','','','')
        if '.apk' in fname: main.addPlayc(fname,key,455,art+'/maintenance.png','APKINSTALLER','','','','')

def DLLIBRTMP(mname,key,trigger):
    import os
    dialog = xbmcgui.Dialog()
    if re.search('(?i)windows',trigger): path=xbmc.translatePath('special://xbmc/system/players/dvdplayer/')
    if re.search('(?i)ios',trigger):
        ret = dialog.select('[COLOR=FF67cc33][B]Select Device[/COLOR][/B]',['iDevice','ATV2'])
        if ret == -1: return
        elif ret == 0:
            path=xbmc.translatePath('special://xbmc')
            path=path.replace('XBMCData/XBMCHome','Frameworks')
        elif ret == 1:
            path=xbmc.translatePath('special://xbmc')
            path=path.replace('XBMCData/XBMCHome','Frameworks')
    if re.search('(?i)android',trigger):
        path=xbmc.translatePath('/data/data/org.xbmc.xbmc/lib/')
    if re.search('(?i)linux',trigger):
        if re.search('(?i)32bit',trigger):
            retex = dialog.select('[COLOR=FF67cc33][B]Select Device[/COLOR][/B]',['Linux Build','ATV1'])
            if retex == -1: return
            elif retex == 0: path=xbmc.translatePath(main.datapath)
            elif retex == 1: path=xbmc.translatePath(main.datapath)
        else: path=xbmc.translatePath(main.datapath)
    if re.search('(?i)mac',trigger):
        path=xbmc.translatePath('special://xbmc')
        path=path.replace('Resources/XBMC','Frameworks')
    if re.search('(?i)raspi',trigger): path=xbmc.translatePath('/opt/xbmc-bcm/xbmc-bin/lib/xbmc/system/')
    if re.search('APKINSTALLER',trigger): path=xbmc.translatePath('special://home')
    url='http://www.mediafire.com/download/'+key+'/'+name
    link = main.OPENURL(url)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')    
    match=re.findall('kNO = "([^"]+?)";',link)[0]
    lib=os.path.join(path,name)
    main.downloadFile(match,lib)
    if re.search('(?i)linux',trigger):
        keyb = xbmc.Keyboard('', 'Enter Root Password')
        keyb.doModal()
        if (keyb.isConfirmed()):
            sudoPassword = keyb.getText()
            if retex == 1: command = 'mv '+path+' /usr/lib/i386-linux-gnu/'
            else: command = 'mv '+path+' /usr/lib/'
            p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
            os.remove(lib)
    if re.search('APKINSTALLER',trigger): dialog.ok("Mash Up", "Thats It All Done", "[COLOR blue]Download location[/COLOR]",path) 
    else: dialog.ok("Mash Up", "Thats It All Done", "[COLOR blue]Now should be Updated[/COLOR]")
        
def MAINTENANCE(name):
    if name == 'MAINTENANCE':
        main.addSpecial('Delete Packages Folder','packages',416,art+'/maintenance.png')
        main.addSpecial('Fix Database Malformed','Malformed',416,art+'/maintenance.png')
        main.addSpecial('Install latest UrlResolver','UrlResolver',416,art+'/maintenance.png')
        main.addSpecial('Install latest MetaHandler','MetaHandler',416,art+'/maintenance.png')
        main.addDir('Update LibRTMP by RedPenguin','x4cvp5hl4m9xr',454,art+'/maintenance.png')
        main.addSpecial('Clear XBMC Cache','ClearCache',416,art+'/maintenance.png')
        main.addSpecial('Clear MashUp Cache & Cookies','MashCache',416,art+'/maintenance.png')
    else:
        main.addSpecial('Zero Cache (0)','ZeroCache.xml',417,art+'/maintenance.png')
        main.addSpecial('Cache Less (20971520)','CacheLess.xml',417,art+'/maintenance.png')
        main.addSpecial('Cache Medium (34603008)','CacheMedium.xml',417,art+'/maintenance.png')
        main.addSpecial('Cache More (52428800)','CacheMore.xml',417,art+'/maintenance.png')
        main.addSpecial('Remove AdvancedSettings.xml','rmv',418,art+'/maintenance.png')

def FIXES():
    main.addDir('MAINTENANCE','maintenance',415,art+'/maintenance.png')
    main.addDir('Advanced Setting Tweaks','adt',415,art+'/maintenance.png')
    main.addLink('[COLOR red]Apply fix only if your current one is broken[/COLOR]','','')
    try: link=main.OPENURL('https://raw.github.com/mash2k3/MashUpFixes/master/Fixes.xml')
    except: xbmc.executebuiltin("XBMC.Notification(Sorry!,Repo is Down,5000,"")")
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.compile('<item><name>([^<]+)</name.+?filename>([^<]+)</filename.+?location>([^<]+)</location.+?path>([^<]+)</path.+?thumbnail>([^<]+)</thumbnail></item>').findall(link)
    for name,filename,location,path,thumb in match: main.addDirFIX(name,filename,785,art+'/'+thumb+'.png',location,path)

def FIXDOWN(name,filename,location,path):
    url = 'https://raw.github.com/mash2k3/MashUpFixes/master/FIXES/'+filename
    print "#############  Downloading from "+ url+"  #####################"
    path = xbmc.translatePath(os.path.join(str(location),str(path)))
    lib=os.path.join(path, str(filename))
    main.downloadFile(url,lib)
    dialog = xbmcgui.Dialog()
    name  = name.split('[COLOR red]')[0]
    dialog.ok("Mash Up", "Thats It All Done", "[COLOR blue]Now "+name+" should be Fixed[/COLOR]")

def ADSettings(name,filename):
    url = 'https://raw.github.com/mash2k3/MashUpFixes/master/AdvancedSettings/'+filename
    print "#############  Downloading from "+ url+"  #####################"
    path = xbmc.translatePath(os.path.join('special://home/','userdata'))
    lib=os.path.join(path,'advancedsettings.xml')
    main.downloadFile(url,lib)
    dialog = xbmcgui.Dialog()
    name  = name.split('[COLOR red]')[0]
    dialog.ok("Mash Up", "Thats It All Done", "[COLOR blue]Now "+name+" should be Installed[/COLOR]")

def delAS():
    dialog = xbmcgui.Dialog()
    if dialog.yesno('Mash Up', 'Are you sure you want to remove advancedsettings.xml?','','','No', 'Yes'):
        path = xbmc.translatePath(os.path.join('special://home/','userdata'))
        file=os.path.join(path, 'advancedsettings.xml')
        os.remove(file)
        dialog.ok("Mash Up", "Thats It All Done", "[COLOR blue]Now AdvancedSettings.xml is removed[/COLOR]")
    
def HTVList(murl):
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.compile('<title>([^<]+)</title.+?link>(.+?)</link.+?thumbnail>([^<]+)</thumbnail>').findall(link)
    for name,url,thumb in match: main.addPlayc(name,url,259,thumb,'','','','','')
        
def showLiveAnnouncements():
    #Announcement Notifier from xml file
    print 'No Messages'

def getListFile(url, path, excepturl = None ):
    link = ''
    t = threading.Thread(target=setListFile,args=(url,path,excepturl))
    t.start()
    if not os.path.exists(path): t.join()
    if os.path.exists(path):
        try: link = open(path).read()
        except: pass
    return link

def setListFile(url, path, excepturl = None):
    content = None
    try: content=main.OPENURL(url, verbose=False)
    except:
        if excepturl: content=main.OPENURL(excepturl, verbose=False)
    if content:
        try: open(path,'w+').write(content)
        except: pass
    return

############################################################################### TV GUIDE DIXIE ###################################################################################################

def openMGuide():
   try:
       dialog = xbmcgui.DialogProgress()
       dialog.create('Pleat Wait!', 'Opening TV Guide Dixie...')
       dialog.update(0)
       dixie = xbmcaddon.Addon('script.tvguidedixie')
       path  = dixie.getAddonInfo('path') 
       sys.path.insert(0, os.path.join(path, ''))
       xbmc.executebuiltin('ActivateWindow(HOME)')
       dialog.update(33)
       dixie.setSetting('mashmode', 'true')
       import gui
       dialog.update(66)
       w = gui.TVGuide()
       dialog.update(100)
       dialog.close()
       w.doModal()
       del w
       cmd = 'AlarmClock(%s,RunAddon(%s),%d,True)' % ('Restart', addon_id, 0)
       xbmc.executebuiltin(cmd)
   except Exception, e: pass
       
def AddToDixie(secName,name,murl,secIcon):
    link=main.OPENURL('https://raw2.github.com/DixieDean/Dixie-Deans-XBMC-Repo/master/tvgdatafiles/cats.xml')
    dialog = xbmcgui.Dialog()
    finalList=[]
    idList=[]
    match=re.compile('<channel>([^<]+)</channel>',re.DOTALL).findall(link)
    for id in match: idList.append(id)
    for i in idList:
        name=name.replace('jsc','al jazeera')
        name=name.replace('ajs','al jazeera')
        if name[0:4] in i.lower(): finalList.append(i)
    ret = dialog.select('[COLOR=FF67cc33][B]Select Channel ID[/COLOR][/B]',finalList)
    if ret == -1: return
    else:
        header = {}
        source = {}
        Dixie=os.path.join(main.datapath,'Dixie')
        try: os.makedirs(Dixie)
        except: pass
        SectionSource=os.path.join(Dixie,secName+'.ini')
        if not os.path.exists(SectionSource):
            path = murl
            id = finalList[ret]
            open(SectionSource,'w').write("\n["+secName.upper()+"]")
            open(SectionSource,'a').write("\nicon="+secIcon)
            open(SectionSource,'a').write("\n"+id+"="+path)
            xbmc.executebuiltin("XBMC.Notification(MashUp,Successfully Added,2500,"+main.slogo+")")
        else:
            path = murl
            id = finalList[ret]
            open(SectionSource,'a').write("\n"+id+"="+path)
            xbmc.executebuiltin("XBMC.Notification(MashUp,Successfully Added,2500,"+main.slogo+")")

################################################################################ XBMCHUB Repo & Hub Maintenance Installer ##########################################################################################################
def UploadLog():
    from resources.fixes import addon
    addon.LogUploader()

repopath = xbmc.translatePath(os.path.join('special://home/addons', 'repository.divingmule.addons'))
try: 
    if not os.path.exists(repopath):
        url = 'https://divingmules-repo.googlecode.com/files/repository.divingmule.addons.zip'
        path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
        lib=os.path.join(path, 'repository.divingmule.addons.zip')
        if main.downloadFile(url,lib):
            print lib
            addonfolder = xbmc.translatePath(os.path.join('special://home/addons',''))
            xbmc.executebuiltin("XBMC.Extract(%s,%s)"%(lib,addonfolder))
except: pass

################################################################################ XBMCHUB POPUP ##########################################################################################################
class HUB( xbmcgui.WindowXMLDialog ):
    def __init__( self, *args, **kwargs ):
        self.shut = kwargs['close_time'] 
        xbmc.executebuiltin( "Skin.Reset(AnimeWindowXMLDialogClose)" )
        xbmc.executebuiltin( "Skin.SetBool(AnimeWindowXMLDialogClose)" )
                                       
    def onInit( self ):
        xbmc.Player().play('%s/resources/skins/DefaultSkin/media/theme.ogg'%selfAddon.getAddonInfo('path'))# Music.
        while self.shut > 0:
            xbmc.sleep(1000)
            self.shut -= 1
        xbmc.Player().stop()
        self._close_dialog()
                
    def onFocus( self, controlID ): pass
    
    def onClick( self, controlID ): 
        if controlID == 12:
            xbmc.Player().stop()
            self._close_dialog()
        if controlID == 7:
            xbmc.Player().stop()
            self._close_dialog()

    def onAction( self, action ):
        if action in [ 5, 6, 7, 9, 10, 92, 117 ] or action.getButtonCode() in [ 275, 257, 261 ]:
            xbmc.Player().stop()
            self._close_dialog()

    def _close_dialog( self ):
        xbmc.executebuiltin( "Skin.Reset(AnimeWindowXMLDialogClose)" )
        time.sleep( .4 )
        self.close()
        
def pop():
    if xbmc.getCondVisibility('system.platform.ios'):
        if not xbmc.getCondVisibility('system.platform.atv'):
            popup = HUB('hub1.xml',selfAddon.getAddonInfo('path'),'DefaultSkin',close_time=34,logo_path='%s/resources/skins/DefaultSkin/media/Logo/'%selfAddon.getAddonInfo('path'))
    if xbmc.getCondVisibility('system.platform.android'):
        popup = HUB('hub1.xml',selfAddon.getAddonInfo('path'),'DefaultSkin',close_time=34,logo_path='%s/resources/skins/DefaultSkin/media/Logo/'%selfAddon.getAddonInfo('path'))
    else:
        popup = HUB('hub.xml',selfAddon.getAddonInfo('path'),'DefaultSkin',close_time=34,logo_path='%s/resources/skins/DefaultSkin/media/Logo/'%selfAddon.getAddonInfo('path'))
    popup.doModal()
    del popup
#######################################################################################

class HUBx( xbmcgui.WindowXMLDialog ):
    def __init__( self, *args, **kwargs ):
        self.shut = kwargs['close_time'] 
        xbmc.executebuiltin( "Skin.Reset(AnimeWindowXMLDialogClose)" )
        xbmc.executebuiltin( "Skin.SetBool(AnimeWindowXMLDialogClose)" )
                                   
    def onInit( self ):
        xbmc.Player().play('%s/resources/skins/DefaultSkin/media/theme.ogg'%selfAddon.getAddonInfo('path'))# Music
        while self.shut > 0:
            xbmc.sleep(1000)
            self.shut -= 1
        xbmc.Player().stop()
        self._close_dialog()
            
    def onFocus( self, controlID ): pass

    def onClick( self, controlID ): 
        if controlID == 12 or controlID == 7:
            xbmc.Player().stop()
            self._close_dialog()

    def onAction( self, action ):
        if action in [ 5, 6, 7, 9, 10, 92, 117 ] or action.getButtonCode() in [ 275, 257, 261 ]:
            xbmc.Player().stop()
            self._close_dialog()

    def _close_dialog( self ):
        path = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.movie25/resources/skins/DefaultSkin','media'))
        popimage=os.path.join(path, 'tempimage.jpg')
        xbmc.executebuiltin( "Skin.Reset(AnimeWindowXMLDialogClose)" )
        time.sleep( .4 )
        self.close()
        os.remove(popimage)
        
def popVIP(image):
    path = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.movie25/resources/skins/DefaultSkin','media'))
    popimage=os.path.join(path, 'tempimage.jpg')
    main.downloadFile(image,popimage)
    if xbmc.getCondVisibility('system.platform.ios'):
        if not xbmc.getCondVisibility('system.platform.atv'):
            popup = HUBx('pop1.xml',selfAddon.getAddonInfo('path'),'DefaultSkin',close_time=60,logo_path='%s/resources/skins/DefaultSkin/media/Logo/'%selfAddon.getAddonInfo('path'),)
    if xbmc.getCondVisibility('system.platform.android'):
        popup = HUBx('pop1.xml',selfAddon.getAddonInfo('path'),'DefaultSkin',close_time=60,logo_path='%s/resources/skins/DefaultSkin/media/Logo/'%selfAddon.getAddonInfo('path'))
    else:
        popup = HUBx('pop.xml',selfAddon.getAddonInfo('path'),'DefaultSkin',close_time=60,logo_path='%s/resources/skins/DefaultSkin/media/Logo/'%selfAddon.getAddonInfo('path'))
    popup.doModal()
    del popup
################################################################################ Favorites Function##############################################################################################################
def getFavorites(section_title = None):
    from resources.universal import favorites
    fav = favorites.Favorites(addon_id, sys.argv)
    if(section_title): fav_items = fav.get_my_favorites(section_title=section_title, item_mode='addon')
    else: fav_items = fav.get_my_favorites(item_mode='addon')
    if len(fav_items) > 0:
        for fav_item in fav_items:
            if (fav_item['isfolder'] == 'false'):
                if (fav_item['section_addon_title'] == "iWatchOnline Fav's" or 
                    fav_item['section_addon_title'] == "Movie Fav's"):
                    main.addPlayM(fav_item['title'],fav_item['infolabels'].get('item_url',''),  
                        fav_item['infolabels'].get('item_mode',''), fav_item['image_url'], 
                        fav_item['infolabels'].get('plot',''), fav_item['fanart_url'],
                        fav_item['infolabels'].get('duration',''), fav_item['infolabels'].get('genre',''),
                        fav_item['infolabels'].get('year',''))
                elif (fav_item['section_addon_title'] == "TV Show Fav's"):
                    main.addPlayT(fav_item['title'],fav_item['infolabels'].get('item_url',''),  
                        fav_item['infolabels'].get('item_mode',''), fav_item['image_url'], 
                        fav_item['infolabels'].get('plot',''), fav_item['fanart_url'],
                        fav_item['infolabels'].get('duration',''), fav_item['infolabels'].get('genre',''),
                        fav_item['infolabels'].get('year',''))
                elif (fav_item['section_addon_title'] == "TV Episode Fav's"):
                    main.addPlayTE(fav_item['title'],fav_item['infolabels'].get('item_url',''),  
                        fav_item['infolabels'].get('item_mode',''), fav_item['image_url'], 
                        fav_item['infolabels'].get('plot',''), fav_item['fanart_url'],
                        fav_item['infolabels'].get('duration',''), fav_item['infolabels'].get('genre',''),
                        fav_item['infolabels'].get('year',''))
                elif (fav_item['section_addon_title'] == "Misc. Fav's"):
                    main.addPlayMs(fav_item['title'],fav_item['infolabels'].get('item_url',''),  
                        fav_item['infolabels'].get('item_mode',''), fav_item['image_url'], 
                        fav_item['infolabels'].get('plot',''), fav_item['fanart_url'],
                        fav_item['infolabels'].get('duration',''), fav_item['infolabels'].get('genre',''),
                        fav_item['infolabels'].get('year',''))
                elif (fav_item['section_addon_title'] == "Live Fav's"):
                    main.addPlayL(fav_item['title'],fav_item['infolabels'].get('item_url',''),  
                        fav_item['infolabels'].get('item_mode',''), fav_item['image_url'], 
                        fav_item['infolabels'].get('plot',''), fav_item['fanart_url'],
                        fav_item['infolabels'].get('duration',''), fav_item['infolabels'].get('genre',''),
                        fav_item['infolabels'].get('year',''))
                elif (fav_item['section_addon_title'] == "Movie25 Fav's"):
                    main.addInfo(fav_item['title'],fav_item['infolabels'].get('item_url',''),  
                        fav_item['infolabels'].get('item_mode',''), fav_item['image_url'], 
                        fav_item['infolabels'].get('genre',''), fav_item['infolabels'].get('year',''))
            else:
                if (fav_item['section_addon_title'] == "iWatchOnline Fav's" or 
                    fav_item['section_addon_title'] == "Movie Fav's"):
                    main.addDirM(fav_item['title'],fav_item['infolabels'].get('item_url',''),  
                        fav_item['infolabels'].get('item_mode',''), fav_item['image_url'], 
                        fav_item['infolabels'].get('plot',''), fav_item['fanart_url'],
                        fav_item['infolabels'].get('duration',''), fav_item['infolabels'].get('genre',''),
                        fav_item['infolabels'].get('year',''))
                elif (fav_item['section_addon_title'] == "TV Show Fav's"):
                    main.addDirT(fav_item['title'],fav_item['infolabels'].get('item_url',''),  
                        fav_item['infolabels'].get('item_mode',''), fav_item['image_url'], 
                        fav_item['infolabels'].get('plot',''), fav_item['fanart_url'],
                        fav_item['infolabels'].get('duration',''), fav_item['infolabels'].get('genre',''),
                        fav_item['infolabels'].get('year',''))
                elif (fav_item['section_addon_title'] == "TV Episode Fav's"):
                    main.addDirTE(fav_item['title'],fav_item['infolabels'].get('item_url',''),  
                        fav_item['infolabels'].get('item_mode',''), fav_item['image_url'], 
                        fav_item['infolabels'].get('plot',''), fav_item['fanart_url'],
                        fav_item['infolabels'].get('duration',''), fav_item['infolabels'].get('genre',''),
                        fav_item['infolabels'].get('year',''))
                elif (fav_item['section_addon_title'] == "Misc. Fav's"):
                    main.addDirMs(fav_item['title'],fav_item['infolabels'].get('item_url',''),  
                        fav_item['infolabels'].get('item_mode',''), fav_item['image_url'], 
                        fav_item['infolabels'].get('plot',''), fav_item['fanart_url'],
                        fav_item['infolabels'].get('duration',''), fav_item['infolabels'].get('genre',''),
                        fav_item['infolabels'].get('year',''))
                elif (fav_item['section_addon_title'] == "Live Fav's"):
                    main.addDirL(fav_item['title'],fav_item['infolabels'].get('item_url',''),  
                        fav_item['infolabels'].get('item_mode',''), fav_item['image_url'], 
                        fav_item['infolabels'].get('plot',''), fav_item['fanart_url'],
                        fav_item['infolabels'].get('duration',''), fav_item['infolabels'].get('genre',''),
                        fav_item['infolabels'].get('year',''))
                elif (fav_item['section_addon_title'] == "Movie25 Fav's"):
                    main.addInfo(fav_item['title'],fav_item['infolabels'].get('item_url',''),  
                        fav_item['infolabels'].get('item_mode',''), fav_item['image_url'], 
                        fav_item['infolabels'].get('genre',''), fav_item['infolabels'].get('year',''))
    else: xbmc.executebuiltin("XBMC.Notification([B][COLOR=FF67cc33]Mash Up[/COLOR][/B],[B]You Have No Saved Favourites[/B],5000,"")")
    return
    
def ListglobalFavALL():
    getFavorites()
    xbmcplugin.setContent(int(sys.argv[1]), 'Movies')

def ListglobalFavM25():
    getFavorites("Movie25 Fav's")
    xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
    
def ListglobalFavIWO():
    getFavorites("iWatchOnline Fav's")
    xbmcplugin.setContent(int(sys.argv[1]), 'Movies')

def ListglobalFavT():
    getFavorites("TV Show Fav's")
    xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
    
def ListglobalFavTE():
    getFavorites("TV Episode Fav's")
    xbmcplugin.setContent(int(sys.argv[1]), 'Movies')

def ListglobalFavM():
    getFavorites("Movie25 Fav's")
    getFavorites("Movie Fav's")
    getFavorites("iWatchOnline Fav's")
    xbmcplugin.setContent(int(sys.argv[1]), 'Movies')

def ListglobalFavMs():
    getFavorites("Misc. Fav's")
    xbmcplugin.setContent(int(sys.argv[1]), 'Movies')

def ListglobalFavL():
    getFavorites("Live Fav's")
    xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
    
################################################################################ Histroy ##########################################################################################################
def WHClear(url):
    dialog = xbmcgui.Dialog()
    ret = dialog.yesno('MashUp Watch History', 'Are you sure you want to clear your','watch history, you can not restore','once you press yes','No', 'Yes')
    if ret:
        os.remove(url)
        xbmc.executebuiltin("XBMC.Container.Refresh")


def History():
    whprofile = xbmc.translatePath(selfAddon.getAddonInfo('profile'))
    whdb=os.path.join(whprofile,'Universal','watch_history.db')
    if  os.path.exists(whdb): main.addPlayc('Clear Watch History',whdb,414,art+'/cleahis.png','','','','','')
    from resources.universal import watchhistory
    wh = watchhistory.WatchHistory(addon_id)
    if selfAddon.getSetting("whistory") == "true":
        history_items = wh.get_my_watch_history()
        for item in history_items:
            item_title = item['title']
            item_url = item['url']
            item_image = item['image_url']
            item_fanart = item['fanart_url']
            item_infolabels = item['infolabels']
            item_isfolder = item['isfolder']
            if item_image =='': item_image= art+'/noimage.png'
            item_title=item_title.replace('[COLOR green]','[COLOR=FF67cc33]')
            main.addLink(item_title,item_url,item_image)
    else:
        dialog = xbmcgui.Dialog()
        ok=dialog.ok('[B]Mash Up History[/B]', 'Watch history is disabled' ,'To enable go to addon settings','and enable Watch History')
        history_items = wh.get_my_watch_history()
        for item in history_items:
            item_title = item['title']
            item_url = item['url']
            item_image = item['image_url']
            item_fanart = item['fanart_url']
            item_infolabels = item['infolabels']
            item_isfolder = item['isfolder']
            item_title=item_title.replace('[COLOR green]','[COLOR=FF67cc33]')
            main.addLink(item_title,item_url,item_image)
    
################################################################################ Message ##########################################################################################################

def Message():
    help = SHOWMessage()
    help.doModal()
    del help

class SHOWMessage(xbmcgui.Window):
    def __init__(self): self.addControl(xbmcgui.ControlImage(0,0,1280,720,art+'/infoposter.png'))
    def onAction(self, action):
        if action == 92 or action == 10:
            xbmc.Player().stop()
            self.close()

def TextBoxes(heading,anounce):
    class TextBox():
        """Thanks to BSTRDMKR for this code:)"""
            # constants
        WINDOW = 10147
        CONTROL_LABEL = 1
        CONTROL_TEXTBOX = 5

        def __init__( self, *args, **kwargs):
            # activate the text viewer window
            xbmc.executebuiltin( "ActivateWindow(%d)" % ( self.WINDOW, ) )
            # get window
            self.win = xbmcgui.Window( self.WINDOW )
            # give window time to initialize
            xbmc.sleep( 500 )
            self.setControls()

        def setControls( self ):
            # set heading
            self.win.getControl( self.CONTROL_LABEL ).setLabel(heading)
            try:
                f = open(anounce)
                text = f.read()
            except: text=anounce
            self.win.getControl( self.CONTROL_TEXTBOX ).setText(text)
            return
    TextBox()
################################################################################ Modes ##########################################################################################################

def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'): params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2: param[splitparams[0]]=splitparams[1]
    return param
              
params=get_params()

url=None
name=None
mode=None
iconimage=None
fanart=None
plot=None
genre=None
title=None
season=None
episode=None
location=None
path=None
index=None

try: name=urllib.unquote_plus(params["name"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: mode=int(params["mode"])
except: pass
try:
    iconimage=urllib.unquote_plus(params["iconimage"])
    iconimage = iconimage.replace(' ','%20')
except: pass
try: plot=urllib.unquote_plus(params["plot"])
except: pass
try:
    fanart=urllib.unquote_plus(params["fanart"])
    fanart = fanart.replace(' ','%20')
except: pass
try: genre=urllib.unquote_plus(params["genre"])
except: pass
try: title=urllib.unquote_plus(params["title"])
except: pass
try: episode=int(params["episode"])
except: pass
try: season=int(params["season"])
except: pass
try: location=urllib.unquote_plus(params["location"])
except: pass
try: path=urllib.unquote_plus(params["path"])
except: pass
try: index=urllib.unquote_plus(params["index"])
except: pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Thumb: "+str(iconimage)

if mode==None or url==None or len(url)<1:
    threading.Thread(target=cacheSideReel).start()
    threading.Thread(target=cacheTrakt).start()
    threading.Thread(target=Notify).start()
    MAIN()
    main.VIEWSB()
elif mode==1:
    from resources.libs import movie25
    movie25.LISTMOVIES(url,index=index)
elif mode==2:
    print ""+url
    GENRE(url,index=index)
elif mode==4:
    from resources.libs import movie25
    print ""+url
    movie25.SEARCH(url,index=index)
elif mode==420:
    from resources.libs import movie25
    print ""+url
    movie25.Searchhistory(index=index)
elif mode==3:
    from resources.libs import movie25
    print ""+url
    movie25.VIDEOLINKS(name,url)
elif mode==5:
    from resources.libs import movie25
    print ""+url
    movie25.PLAY(name,url)
elif mode==171:
    from resources.libs import movie25
    print ""+url
    movie25.PLAYB(name,url)
elif mode==6:
    AtoZ(index=index)
elif mode==7:
    YEAR(index=index)
elif mode==19:
    from resources.libs import supersearch
    supersearch.SEARCHistory()
elif mode==20:
    from resources.libs import supersearch
    supersearch.SEARCH(name,url)
elif mode==21:
    from resources.libs import supersearch
    name = re.sub('(?i)\[B\].*?\[/B\]','',name)
    name = main.removeColoredText(name)
#     name = re.sub('(?i)[^a-zA-Z0-9]',' ',name)
    if re.search('(?i)s(\d+)e(\d+)',name) or re.search('(?i)Season(.+?)Episode',name) or re.search('(?i)(\d+)x(\d+)',name):
        episode = re.search('(?i)Season\s*?(\d+)\s*?Episode\s*?(\d+)',name)
        if episode:
            e = str(episode.group(2))
            if(len(e)==1): e = "0" + e
            s = episode.group(1)
            if(len(s)==1): s = "0" + s
            name = re.sub('(?i)Season\s*?(\d+)\s*?Episode\s*?(\d+)',"S" + s + "E" + e,name)
        else:
            episode = re.search('(?i)(\d+)x(\d+)',name)
            if episode:
                e = str(episode.group(2))
                if(len(e)==1): e = "0" + e
                s = episode.group(1)
                if(len(s)==1): s = "0" + s
                name = re.sub('(?i)(\d+)x(\d+)',"S" + s + "E" + e,name)
        supersearch.SEARCH(name,'TV')
    else:
        if re.search('(?i).\s\([12][90]\d{2}\)',name): name = re.sub('(?i)^(.+?)\s\(([12][90]\d{2})\).*','\\1 \\2',name)
        elif re.search('(?i).\s[12][90]\d{2}',name): name = re.sub('(?i)^(.+?)\s([12][90]\d{2}).*','\\1 \\2',name)
        name = re.sub('(?i)\s\s+',' ',name).strip()
        supersearch.SEARCH(name,'Movies')
elif mode==23:
    from resources.libs import movie25
    movie25.ENTYEAR(index=index)
elif mode==8:
    from resources.libs import movie25
    print ""+url
    movie25.YEARB(url,index=index)
elif mode==9:
    from resources.libs import movie25
    print ""+url
    movie25.NEXTPAGE(url,index=index)
elif mode==10:
    from resources.libs import movie25
    ListglobalFavM25()
elif mode==11:
    from resources.libs import movie25
    print ""+url
    movie25.GroupedHosts(name,url,iconimage)
elif mode==15:
    print ""+url
    INTCAT(url)
elif mode==16:
    print ""+url
    HOWTOCAT()
elif mode==25:
    from resources.libs.movies_tv import oneclickwatch
    print ""+url
    oneclickwatch.LISTSP(url)
elif mode==26:
    from resources.libs.movies_tv import oneclickwatch
    print ""+url
    oneclickwatch.LINKSP(name,url)
elif mode==27:
    print ""+url
    TV()
elif mode==28:
    from resources.libs.plugins import iwatchonline
    print ""+url
    iwatchonline.LISTTV(url)
elif mode==29:
    from resources.libs.plugins import iwatchonline
    print ""+url
    iwatchonline.VIDEOLINKST(name,url)
elif mode==30:
    from resources.libs.movies_tv import movie1k
    print ""+url
    movie1k.LISTTV2(url)
elif mode==31:
    from resources.libs.movies_tv import movie1k
    print ""+url
    movie1k.VIDEOLINKST2(name,url,iconimage)
elif mode==32:
    from resources.libs.movies_tv import oneclickwatch
    print ""+url
    oneclickwatch.LISTTV3(url)
elif mode==33:
    print ""+url
    HD()
elif mode==34:
    from resources.libs.movies_tv import newmyvideolinks
    print ""+url
    newmyvideolinks.LISTSP2(url)
elif mode==35:
    from resources.libs.movies_tv import newmyvideolinks
    print ""+url
    newmyvideolinks.LINKSP2(name,url)
elif mode==36:
    print ""+url
    INT()
elif mode==37:
    from resources.libs.international import  einthusan
    print ""+url
    einthusan.MAINFULLS()
elif mode==38:
    from resources.libs.international import  einthusan
    print ""+url
    einthusan.LINKINT(name,url)
elif mode==39:
    from resources.libs.international import einthusan
    print ""+url
    einthusan.DIRINT(url)
elif mode==40:
    from resources.libs.international import einthusan
    print ""+url
    einthusan.AZMOVIES(url)
elif mode==41:
    from resources.libs.international import einthusan
    print ""+url
    einthusan.AZBLURAY(url)
elif mode==42:
    from resources.libs.international import einthusan
    print ""+url
    einthusan.LISTINT(url)
elif mode==43:
    print ""+url
    SPORTS()
elif mode==44:
    from resources.libs.sports import espn
    print ""+url
    espn.ESPN()
elif mode==45:
    from resources.libs.sports import espn
    print ""+url
    espn.ESPNList(url)
elif mode==46:
    from resources.libs.sports import espn
    print ""+url
    espn.ESPNLink(name,url,iconimage,plot)
elif mode==47:
    from resources.libs import youtube
    print ""+url
    youtube.YOUList(name,url)
elif mode==48:
    from resources.libs import youtube
    print ""+url
    youtube.YOULink(name,url,iconimage)
elif mode==50:
    from resources.libs.sports import outdoorch
    print ""+url
    outdoorch.OC()
elif mode==51:
    from resources.libs.sports import outdoorch
    print ""+url
    outdoorch.OCList(url)
elif mode==52:
    from resources.libs.sports import outdoorch
    print ""+url
    outdoorch.OCLink(name,url,iconimage,plot)
elif mode==53:
    from resources.libs.movies_tv import dailyflix
    print ""+url
    dailyflix.LISTSP3(url)
elif mode==54:
    from resources.libs.movies_tv import dailyflix
    print ""+url
    dailyflix.LINKSP3(name,url)
elif mode==55:
    from resources.libs.movies_tv import oneclickmoviez
    print ""+url
    oneclickmoviez.LISTSP4(url)
elif mode==56:
    from resources.libs.movies_tv import oneclickmoviez
    print ""+url
    oneclickmoviez.LINKSP4(name,url)
elif mode==57:
    from resources.libs.movies_tv import starplay
    print ""+url
    starplay.LISTSP5(url)
elif mode==58:
    from resources.libs.movies_tv import starplay
    print ""+url
    starplay.LINKSP5(name,url)
elif mode==59:
    print ""+url
    UFC()
elif mode==60:
    from resources.libs import movie25
    print ""+url
    movie25.UFCMOVIE25()
elif mode==61:
    from resources.libs.movies_tv import rlsmix
    print ""+url
    rlsmix.ListDirectDownloadTVItems(url)
elif mode==62:
    from resources.libs.movies_tv import rlsmix
    print ""+url
    rlsmix.ListDirectDownloadTVLinks(name,url)
elif mode==63:
    print ""+url
    ADVENTURE()
elif mode==631:
    from resources.libs.adventure import discovery
    print ""+url
    discovery.DISC(url)
elif mode==64:
    from resources.libs.adventure import discovery
    print ""+url
    discovery.LISTDISC(name,url)
elif mode==65:
    from resources.libs.adventure import discovery
    print ""+url
    discovery.LINKDISC(name,url)
elif mode==66:
    from resources.libs.international import cinevip
    print ""+url
    cinevip.LISTINT3(url)
elif mode==67:
    from resources.libs.international import cinevip
    print ""+url
    cinevip.LINKINT3(name,url,iconimage)
elif mode==68:
    print ""+url
    useme(url)
elif mode==69:
    print ""+url
    useMe(name,url)
elif mode==70:
    from resources.libs.adventure import nationalgeo
    print ""+url
    nationalgeo.NG()
elif mode==71:
    from resources.libs.adventure import nationalgeo
    print ""+url
    nationalgeo.NGDir(url)
elif mode==72:
    from resources.libs.adventure import nationalgeo
    print ""+url
    nationalgeo.LISTNG(url)
elif mode==73:
    from resources.libs.adventure import nationalgeo
    print ""+url
    nationalgeo.LISTNG2(url)

elif mode==74:
    from resources.libs.adventure import nationalgeo
    print ""+url
    nationalgeo.LINKNG(name,url)
elif mode==75:
    from resources.libs.adventure import nationalgeo
    print ""+url
    nationalgeo.LINKNG2(name,url)
elif mode==76:
    print ""+url
    KIDZone(url)
elif mode==77:
    from resources.libs.kids import wbkids
    print ""+url
    wbkids.WB()
elif mode==78:
    from resources.libs.kids import wbkids
    print ""+url
    wbkids.LISTWB(url)
elif mode==79:
    from resources.libs.kids import wbkids
    print ""+url
    wbkids.LINKWB(name,url)
elif mode==80:
    from resources.libs.adventure import discovery
    print ""+url
    discovery.MILIT(url)
elif mode==81:
    from resources.libs.adventure import discovery
    print ""+url
    discovery.SCI(url)
elif mode==82:
    from resources.libs.adventure import discovery
    print ""+url
    discovery.VELO(url)
elif mode==83:
    from resources.libs.adventure import discovery
    print ""+url
    discovery.ANIP(url)
elif mode==84:
    from resources.libs import youtube
    print ""+url
    youtube.YOUKIDS()
elif mode==85:
    print ""+url
    DOCS()
elif mode==86:
    from resources.libs.documentaries import documentary
    print ""+url
    documentary.LISTDOC(url)
elif mode==87:
    from resources.libs.documentaries import documentary
    print ""+url
    documentary.LISTDOC2(url)
elif mode==88:
    from resources.libs.documentaries import documentary
    print ""+url
    documentary.LINKDOC(name,url,iconimage)
elif mode==89:
    from resources.libs.documentaries import documentary
    print ""+url
    documentary.LISTDOCPOP(url)
elif mode==90:
    from resources.libs.adventure import airaces
    print ""+url
    airaces.LISTAA()
elif mode==91:
    from resources.libs.adventure import airaces
    print ""+url
    airaces.PLAYAA(name,url,iconimage)
elif mode==92:
    from resources.libs.sports import wildtv
    print ""+url
    wildtv.WILDTV(url)
elif mode==93:
    from resources.libs.sports import wildtv
    print ""+url
    wildtv.LISTWT(url)
elif mode==94:
    from resources.libs.sports import wildtv
    print ""+url
    wildtv.LINKWT(name,url)
elif mode==95:
    from resources.libs.sports import tsn
    print ""+url
    tsn.TSNDIR()
elif mode==96:
    from resources.libs.sports import tsn
    print ""+url
    tsn.TSNDIRLIST(url)
elif mode==97:
    from resources.libs.sports import tsn
    print ""+url
    tsn.TSNLIST(url)
elif mode==98:
    from resources.libs.sports import tsn
    print ""+url
    tsn.TSNLINK(name,url,iconimage)
elif mode==100: pop()
elif mode==101:
    from resources.libs.movies_tv import newmyvideolinks
    newmyvideolinks.SEARCHNEW(name,url)
elif mode==102:
    from resources.libs.movies_tv import newmyvideolinks
    newmyvideolinks.SearchhistoryNEW(url)
elif mode==103:
    from resources.libs.movies_tv import newmyvideolinks
    newmyvideolinks.UFCNEW()
elif mode==104:
    from resources.libs.documentaries import vice
    vice.Vice(url)
elif mode==105:
    from resources.libs.documentaries import vice
    vice.ViceList(url)
elif mode==106:
    from resources.libs.documentaries import vice
    vice.ViceLink(name,url,iconimage)
elif mode==107:
    from resources.libs.kids import disneyjr
    disneyjr.DISJR()
elif mode==108:
    from resources.libs.kids import disneyjr
    disneyjr.DISJRList(url)
elif mode==109:
    from resources.libs.kids import disneyjr
    disneyjr.DISJRList2(url)
elif mode==110:
    from resources.libs.kids import disneyjr
    disneyjr.DISJRLink(name,url,iconimage)
elif mode==111: StrikeFList(url)
elif mode==112: StrikeFLink(name,url)
elif mode==113:
    from resources.libs.sports import mmafighting
    mmafighting.MMAFList(url)
elif mode==114:
    from resources.libs.sports import mmafighting
    mmafighting.MMAFLink(name,url,iconimage)  
elif mode==115: LiveStreams()
elif mode==116:
    from resources.libs.live import livestation
    livestation.LivestationList(url)
elif mode==117:
    from resources.libs.live import livestation
    livestation.LivestationLink(name,url,iconimage)
elif mode==118:
    from resources.libs.live import livestation
    livestation.LivestationLink2(name,url,iconimage)
elif mode==119:
    from resources.libs.live import ilive
    ilive.iLive()
elif mode==120:
    from resources.libs.live import ilive
    ilive.iLiveList(url)
elif mode==121:
    from resources.libs.live import ilive
    ilive.iLiveLink(name,url,iconimage)
elif mode==122:
    from resources.libs.live import castalba
    castalba.CastalbaList(url)
elif mode==123:
    from resources.libs.live import castalba
    castalba.CastalbaLink(name,url,iconimage)
elif mode==124:
    from resources.libs.sports import foxsoccer
    foxsoccer.FOXSOC()
elif mode==125:
    from resources.libs.sports import foxsoccer
    foxsoccer.FOXSOCList(url)
elif mode==126:
    from resources.libs.sports import foxsoccer
    foxsoccer.FOXSOCLink(name,url)
elif mode==127:
    from resources.libs.live import musicstreams
    musicstreams.MUSICSTREAMS()
elif mode==128: main.Clearhistory(url)
elif mode==129:
    from resources.libs.live import desistreams
    desistreams.DESISTREAMS()
elif mode==130:
    from resources.libs.live import desistreams
    desistreams.DESISTREAMSList(url)
elif mode==131:
    from resources.libs.live import desistreams
    desistreams.DESISTREAMSLink(name,url)
elif mode==132:
    from resources.libs.movies_tv import movie1k
    movie1k.SearchhistoryMovie1k()
elif mode==133:
    from resources.libs.movies_tv import movie1k
    movie1k.SEARCHMovie1k(url)
elif mode==134:
    from resources.libs.movies_tv import oneclickwatch
    oneclickwatch.PLAYOCW(name,url)
elif mode==135:
    from resources.libs.movies_tv import oneclickwatch
    oneclickwatch.VIDEOLINKST3(name,url)
elif mode==136:
    from resources.libs.movies_tv import rlsmix
    rlsmix.StartDirectDownloadTVSearch()
elif mode==137:
    from resources.libs.movies_tv import rlsmix
    rlsmix.SearchDirectDownloadTV(url)
elif mode==138:
    from resources.libs.live import naviplaylists
    naviplaylists.playlists()
elif mode==139:
    from resources.libs.live import naviplaylists
    naviplaylists.playlistList(name,url)
elif mode==140:
    from resources.libs.live import naviplaylists
    naviplaylists.playlistList2(name,url)
elif mode==141:
    from resources.libs.live import naviplaylists
    naviplaylists.playlistList3(name,url)
elif mode==142:
    from resources.libs.live import naviplaylists
    naviplaylists.playlistList4(name,url)
elif mode==149:
    from resources.libs.live import naviplaylists
    naviplaylists.playlistList5(name,url)
elif mode==158:
    from resources.libs.live import naviplaylists
    naviplaylists.playlistList6(name,url)
elif mode==168:
    from resources.libs.live import naviplaylists
    naviplaylists.playlistList7(name,url)
elif mode==143:
    from resources.libs.live import countries
    countries.COUNTRIES()
elif mode==144:
    from resources.libs.live import countries
    countries.COUNTRIESList(name,url)
elif mode==204:
    from resources.libs.live import countries
    countries.COUNTRIESLink(name,url,iconimage)
elif mode==145:
    from resources.libs import movie25
    print ""+url
    movie25.MOVSHLINKS(name,url)
elif mode==146:
    from resources.libs import movie25
    print ""+url
    movie25.DIVXSLINKS(name,url)
elif mode==147:
    from resources.libs import movie25
    print ""+url
    movie25.SSIXLINKS(name,url)
elif mode==148:
    from resources.libs import movie25
    print ""+url
    movie25.GORLINKS(name,url)
elif mode==150:
    from resources.libs import movie25
    print ""+url
    movie25.MOVPLINKS(name,url)
elif mode==151:
    from resources.libs import movie25
    print ""+url
    movie25.DACLINKS(name,url)
elif mode==152:
    from resources.libs import movie25
    print ""+url
    movie25.VWEEDLINKS(name,url)
elif mode==153:
    from resources.libs import movie25
    print ""+url
    movie25.MOVDLINKS(name,url)
elif mode==154:
    from resources.libs import movie25
    print ""+url
    movie25.MOVRLINKS(name,url)
elif mode==155:
    from resources.libs import movie25
    print ""+url
    movie25.BUPLOADSLINKS(name,url)
elif mode==156:
    print ""+url
    UploadLog()
elif mode==157:
    from resources.libs import movie25
    print ""+url
    movie25.PLAYEDLINKS(name,url)
elif mode==159:
    from resources.libs.documentaries import watchdocumentary
    print ""+url
    watchdocumentary.WATCHDOC()
elif mode==160:
    from resources.libs.documentaries import watchdocumentary
    print ""+url
    watchdocumentary.WATCHDOCList(url)
elif mode==161:
    from resources.libs.documentaries import watchdocumentary
    print ""+url
    watchdocumentary.WATCHDOCLink(name,url,iconimage)
elif mode==162:
    from resources.libs.documentaries import watchdocumentary
    print ""+url
    watchdocumentary.CATEGORIES()
elif mode==163:
    from resources.libs.documentaries import watchdocumentary
    print ""+url
    watchdocumentary.WATCHDOCList2(url)
elif mode==164:
    from resources.libs.documentaries import watchdocumentary
    print ""+url
    watchdocumentary.WATCHDOCSearch()
elif mode==165:
    from resources.libs.plugins import globalbc
    print ""+url
    globalbc.GLOBALBC()
elif mode==166:
    from resources.libs.plugins import globalbc
    print ""+url
    globalbc.GLOBALBCList(url)
elif mode==167:
    from resources.libs.plugins import globalbc
    print ""+url
    globalbc.GLOBALBCLink(name,url)
elif mode==169:
    from resources.libs.plugins import globalbc
    print ""+url
    globalbc.GLOBALBCList2(url)
elif mode==170:
    from resources.libs.plugins import globalbc
    print ""+url
    globalbc.GLOBALBCSearch()
#171 taken
elif mode==172:
    from resources.libs.sports import skysports
    print ""+url
    skysports.SKYSPORTS()
elif mode==173:
    from resources.libs.sports import skysports
    print ""+url
    skysports.SKYSPORTSList(url)
elif mode==174:
    from resources.libs.sports import skysports
    print ""+url
    skysports.SKYSPORTSLink(name,url)
elif mode==175:
    from resources.libs.sports import skysports
    print ""+url
    skysports.SKYSPORTSTV(url)
elif mode==176:
    from resources.libs.sports import skysports
    print ""+url
    skysports.SKYSPORTSList2(url)
elif mode==177:
    dialog = xbmcgui.Dialog()
    dialog.ok("Mash Up", "Sorry this video requires a SkySports Suscription.","Will add this feature in later Version.","Enjoy the rest of the videos ;).")
elif mode==178:
    from resources.libs.sports import skysports
    print ""+url
    skysports.SKYSPORTSCAT()
elif mode==179:
    from resources.libs.sports import skysports
    print ""+url
    skysports.SKYSPORTSCAT2(url)
elif mode==180:
    from resources.libs.sports import skysports
    print ""+url
    skysports.SKYSPORTSTEAMS(url)
elif mode==181:
    from resources.libs.live import vipplaylist
    print ""+url
    vipplaylist.VIPplaylists(url)
elif mode==182:
    from resources.libs.live import vipplaylist
    print ""+url
    vipplaylist.VIPList(name,url)
elif mode==183:
    from resources.libs.live import vipplaylist
    print ""+url
    vipplaylist.VIPLink(name,url,iconimage)
elif mode==184:
    from resources.libs.live import musicstreams
    print ""+url
    musicstreams.MUSICSTREAMSLink(name,url,iconimage)
elif mode==185:
    from resources.libs.live import tubtub
    print ""+url
    tubtub.TubTubMAIN(url)
elif mode==186:
    from resources.libs.live import tubtub
    print ""+url
    tubtub.TubTubLink(name,url)
elif mode==187:
    print ""+url
    arabic.ArabicMAIN(url)
elif mode==188:
    print ""+url
    arabic.ArabicLink(name,url)
elif mode==189:
    print ""+url
    arabic.ArabicList(url)
elif mode==190:
    print ""+url
    main.Download_Source(name,url)
elif mode==191:
    from resources.libs.live import oneeightone
    print ""+url
    oneeightone.MAINFM()
elif mode==192:
    from resources.libs.live import oneeightone
    print ""+url
    oneeightone.LISTFM(name,url)
elif mode==193:
    from resources.libs.live import oneeightone
    print ""+url
    oneeightone.LINKFM(name,url)
elif mode==194:
    print ""+url
    WorkoutMenu()
elif mode==195:
    from resources.libs.sports import bodybuilding
    print ""+url
    bodybuilding.MAINBB()
elif mode==196:
    from resources.libs.sports import bodybuilding
    print ""+url
    bodybuilding.LISTBB(url)
elif mode==197:
    from resources.libs.sports import bodybuilding
    print ""+url
    bodybuilding.LINKBB(name,url,iconimage)
elif mode==198:
    from resources.libs.sports import fitnessblender
    print ""+url
    fitnessblender.MAINFB()
elif mode==199:
    from resources.libs.sports import fitnessblender
    print ""+url
    fitnessblender.BODYFB()
elif mode==200:
    from resources.libs.sports import fitnessblender
    print ""+url
    fitnessblender.DIFFFB()
elif mode==201:
    from resources.libs.sports import fitnessblender
    print ""+url
    fitnessblender.TRAINFB()
elif mode==202:
    from resources.libs.sports import fitnessblender
    print ""+url
    fitnessblender.LISTBF(url)
elif mode==203:
    from resources.libs.sports import fitnessblender
    print ""+url
    fitnessblender.LINKBB(name,url,iconimage)
elif mode==205:
    from resources.libs import youplaylist
    print ""+url
    youplaylist.YOUList(name,url)
elif mode==206:
    from resources.libs import youplaylist
    print ""+url
    youplaylist.YOULink(name,url,iconimage)
elif mode==207:
    from resources.libs import movie25
    print ""+url
    movie25.GotoPage(url,index=index)
elif mode==208:
    from resources.libs import movie25
    print ""+url
    movie25.GotoPageB(url,index=index)
elif mode==209:
    from resources.libs.movies_tv import newmyvideolinks
    print ""+url
    newmyvideolinks.LINKSP2B(name,url)
elif mode==210:
    from resources.libs.movies_tv import rlsmix
    print ""+url
    rlsmix.PlayDirectDownloadTVLink(name,url)
elif mode==211:
    from resources.libs.movies_tv import oneclickmoviez
    print ""+url
    oneclickmoviez.LINKSP4B(name,url)
elif mode == 213 or mode == 214:
    if xbmc.Player().isPlayingAudio():
        info   = xbmc.Player().getMusicInfoTag()
        artist = info.getTitle().split(' - ')[0]
        track  = info.getTitle()
        track  = track.split(' (')[0]
        print track
        artist=artist.replace('f/','ft ')
        cmd = '%s?mode=%s&name=%s&artist=%s' % ('plugin://plugin.audio.xbmchubmusic/', str(mode), track, artist)
        xbmc.executebuiltin('XBMC.Container.Update(%s)' % cmd)
elif mode==217:
    from resources.libs.sports import golfchannel
    golfchannel.MAIN()
elif mode==218:
    from resources.libs.sports import golfchannel
    print ""+url
    golfchannel.LIST(url)
elif mode==219:
    from resources.libs.sports import golfchannel
    print ""+url
    golfchannel.LIST2(name,url,iconimage,plot)
elif mode==220:
    from resources.libs.sports import golfchannel
    print ""+url
    golfchannel.LINK(name,url,iconimage)
elif mode==221:
    from resources.libs.sports import golfchannel
    print ""+url
    golfchannel.LIST3(url)
elif mode==222:
    print ""+url
    History()
elif mode==223:
    print ""+url
    ThreeDsec()
elif mode==226:
    from resources.libs.documentaries import documentarywire
    documentarywire.MAIN()
elif mode==227:
    from resources.libs.documentaries import documentarywire
    print ""+url
    documentarywire.LIST(url)
elif mode==228:
    from resources.libs.documentaries import documentarywire
    print ""+url
    documentarywire.LINK(name,url,iconimage,plot)
elif mode==229:
    from resources.libs.documentaries import documentarywire
    print ""+url
    documentarywire.SEARCH(url)
elif mode==230:
    from resources.libs.documentaries import documentarywire
    print ""+url
    documentarywire.CATLIST(url)
elif mode==231:
    from resources.libs.live import hadynz
    print ""+url
    hadynz.MAIN()
elif mode==232:
    from resources.libs.live import hadynz
    print ""+url
    hadynz.LINK(name,url,iconimage)
elif mode==233:
    print ""+url
elif mode==234:
    print ""+url
    PlaylistDir()
elif mode==235:
    from resources.libs.movies_tv import movieplaylist
    print ""+url
    movieplaylist.Mplaylists(url)
elif mode==236:
    from resources.libs.movies_tv import movieplaylist
    print ""+url
    movieplaylist.MList(name,url)
elif mode==237:
    from resources.libs.movies_tv import movieplaylist
    print ""+url
    movieplaylist.MLink(name,url,iconimage)
elif mode==238:
    from resources.libs.live import customchannel
    print ""+url
    customchannel.MAIN()
elif mode==239:
    from resources.libs.live import customchannel
    print ""+url
    customchannel.LIST(name,url)
elif mode==240:
    from resources.libs.live import customchannel
    print ""+url
    customchannel.LINK(name,url,iconimage)
elif mode==241:
    from resources.libs import downloadedcontent
    print ""+url
    downloadedcontent.LIST()
elif mode==242:
    from resources.libs import downloadedcontent
    print ""+url
    downloadedcontent.LINK(name,url)
elif mode==243:
    from resources.libs import downloadedcontent
    print ""+url
    downloadedcontent.REMOVE(name,url)
elif mode==244: popVIP(url)
elif mode==245:
    from resources.libs.movies_tv import multilinkplaylist
    print ""+url
    multilinkplaylist.Mplaylists(url)
elif mode==246:
    from resources.libs.movies_tv import multilinkplaylist
    print ""+url
    multilinkplaylist.MList(name,url)
elif mode==247:
    from resources.libs.movies_tv import multilinkplaylist
    print ""+url
    multilinkplaylist.MLink(name,url,iconimage)
elif mode==248:
    from resources.libs.live import customchannel
    customchannel.XmlIns()
elif mode==249:
    from resources.libs.movies_tv import movieplaylist
    movieplaylist.subLink(name,url)
elif mode==250:
    from resources.libs.live import customchannel
    customchannel.addPlaylist(url)
elif mode==251:
    from resources.libs.live import customchannel
    customchannel.removePlaylist(name,url,iconimage)
elif mode==252:
    from resources.libs.live import customchannel
    customchannel.addFolder(url)
elif mode==253:
    from resources.libs.live import customchannel
    customchannel.openFolder(name,url)
elif mode==254:
    from resources.libs.live import customchannel
    customchannel.removeFolder(name,url)
elif mode==255:
    from resources.libs.live import customchannel
    customchannel.editPlaylist(name,url,iconimage)
elif mode==256:
    from resources.libs.live import customchannel
    customchannel.editFolder(name,url)
elif mode==257:
    from resources.libs.live import customchannel
    customchannel.listLS(name,url,fanart)
elif mode==259:
    from resources.libs.movies_tv import movieplaylist
    print ""+url
    movieplaylist.MLink2(name,url,iconimage)
elif mode==260:
    from resources.libs.movies_tv import viplus
    viplus.VIP(url)
elif mode==261:
    from resources.libs.movies_tv import viplus
    viplus.VIPList(url)
elif mode==262:
    from resources.libs.movies_tv import viplus
    viplus.subLink(name,url)
elif mode==263:
    from resources.libs.movies_tv import viplus
    viplus.MLink(name,url,iconimage)
elif mode==264: HTVList(url)
elif mode==265: ANIME()
elif mode==266:
    from resources.libs.live import customchannel
    print ""+url
    customchannel.subLink(name,url)
elif mode==267:
    Movie25(index=index)
    main.VIEWSB()
elif mode==268:
    from resources.libs.plugins import dramania
    print ""+url
    dramania.MAIN()
elif mode==269:
    from resources.libs.plugins import dramania
    print ""+url
    dramania.MOVIES()
elif mode==270:
    from resources.libs.plugins import dramania
    print ""+url
    dramania.LIST(url)
elif mode==271:
    from resources.libs.plugins import dramania
    print ""+url
    dramania.LISTHOSTS(name,url,iconimage)
elif mode==272:
    from resources.libs.plugins import dramania
    print ""+url
    dramania.PLAY(name,url,iconimage)
elif mode==273:
    from resources.libs.plugins import dramania
    print ""+url
    dramania.DRAMAS()
elif mode==274:
    from resources.libs.plugins import dramania
    print ""+url
    dramania.SEARCH()
elif mode==275:
    from resources.libs.plugins import dramania
    print ""+url
    dramania.LISTEPISODES(name,url,iconimage)
elif mode==276:
    from resources.libs.plugins import mbox
    print ""+url
    mbox.MAIN()
elif mode==277:
    from resources.libs.plugins import mbox
    print ""+url
    mbox.MOVIES()
elif mode==278:
    from resources.libs.plugins import mbox
    print ""+url
    mbox.LIST(url)
elif mode==279:
    from resources.libs.plugins import mbox
    print ""+url
    mbox.PLAY(name,url,iconimage)
elif mode==280:
    from resources.libs.plugins import mbox
    print ""+url
    mbox.SEASONS(name,url)
elif mode==281:
    from resources.libs.plugins import mbox
    print ""+url
    mbox.EPISODES(name,url)
elif mode==282:
    from resources.libs.movies_tv import icefilms
    print ""+url
    icefilms.LISTICE(url,index=index)
elif mode==283:
    from resources.libs.movies_tv import icefilms
    print ""+url
    icefilms.LISTLINKS(name,url)
elif mode==284:
    from resources.libs.movies_tv import icefilms
    print ""+url
    icefilms.PLAYLINK(name,url)
elif mode==285:
    from resources.libs.plugins import mbox
    print ""+url
    mbox.DownloadAndList(url)
elif mode==286:
    from resources.libs.movies_tv import icefilms
    print ""+url
    icefilms.StartIceFilmsSearch(url,index=index)
elif mode==287:
    from resources.libs.movies_tv import icefilms
    print ""+url
    icefilms.SearchIceFilms(url,plot,index=index)
elif mode==288:
    from resources.libs.movies_tv import icefilms
    print ""+url
    icefilms.ICETVMAIN(index=index)
elif mode==289:
    from resources.libs.movies_tv import icefilms
    print ""+url
    icefilms.ICESEASONS(name,url,index=index)
elif mode==290:
    from resources.libs.movies_tv import icefilms
    print ""+url
    icefilms.ICEEPISODES(name,url,index=index)
elif mode==291:
    from resources.libs.movies_tv import icefilms
    print ""+url
    icefilms.ICETODAY(url,index=index)
elif mode==292:
    from resources.libs.movies_tv import icefilms
    print ""+url
    icefilms.AtoZICE(url,index=index)
elif mode==293:
    from resources.libs.movies_tv import icefilms
    print ""+url
    icefilms.ICEGENRE(url,index=index)
elif mode==294:
    from resources.libs.movies_tv import icefilms
    print ""+url
    icefilms.ICEMAIN()
elif mode==295:
    from resources.libs.movies_tv import icefilms
    print ""+url
    icefilms.ICEMOVIEMAIN(index=index)
elif mode==296:
    from resources.libs.movies_tv import starplay
    print ""+url
    starplay.NBMAIN()
elif mode==297:
    from resources.libs.movies_tv import starplay
    print ""+url
    starplay.NBGENRE()
elif mode==298:
    from resources.libs.movies_tv import starplay
    print ""+url
    starplay.NBSearchhistory()
elif mode==299:
    from resources.libs.movies_tv import starplay
    print ""+url
    starplay.NBSearch(name,url)
elif mode==300:
    from resources.libs.movies_tv import starplay
    print ""+url
    starplay.AtoZNB()
elif mode==301:
    from resources.libs.movies_tv import starplay
    print ""+url
    starplay.AZLISTNB(url)
elif mode==302:
    from resources.libs.plugins import mbox
    print ""+url
    mbox.MUSICLIST(name,url)
elif mode==303:
    from resources.libs.international import cinevip
    print ""+url
    cinevip.Searchhistory(url)
elif mode==304:
    from resources.libs.international import cinevip
    print ""+url
    cinevip.SEARCH(name,url)
elif mode==305:
    from resources.libs.international import mooviemaniac
    print ""+url
    mooviemaniac.LISTMOO()
elif mode==306:
    from resources.libs.international import mooviemaniac
    print ""+url
    mooviemaniac.LINKMOO(name,url,iconimage)
elif mode==307:
    from resources.libs.international import cinevip
    print ""+url
    cinevip.LINKLIST(name,url)
elif mode==308:
    from resources.libs.international import fxcine
    print ""+url
    fxcine.LISTFX()
elif mode==309:
    from resources.libs.international import fxcine
    print ""+url
    fxcine.LANGFX(name,url,iconimage)
elif mode==309:
    from resources.libs.international import fxcine
    print ""+url
    fxcine.LINKLIST(mname,url)
elif mode==310:
    from resources.libs.international import fxcine
    print ""+url
    fxcine.LINKFX(name,url)
elif mode==311:
    from resources.libs.plugins import dpstreaming
    print ""+url
    dpstreaming.MAINDP()
elif mode==312:
    from resources.libs.plugins import dpstreaming
    print ""+url
    dpstreaming.LISTDP(url)

elif mode==313:
    from resources.libs.plugins import dpstreaming
    print ""+url
    dpstreaming.LINKLIST(name,url)
elif mode==314:
    from resources.libs.plugins import dpstreaming
    print ""+url
    dpstreaming.LINKDP(name,url)
elif mode==315:
    from resources.libs.plugins import dpstreaming
    print ""+url
    dpstreaming.LISTEPISODE(name,url)
elif mode==316:
    from resources.libs.plugins import dpstreaming
    print ""+url
    dpstreaming.LINKLIST2(name,url)
elif mode==317:
    from resources.libs.plugins import dpstreaming
    print ""+url
    dpstreaming.SEARCHDP()
elif mode==318:
    from resources.libs.documentaries import johnlocker
    print ""+url
    johnlocker.MAINJL()
elif mode==319:
    from resources.libs.documentaries import johnlocker
    print ""+url
    johnlocker.LISTJL(name,url)
elif mode==320:
    from resources.libs.documentaries import johnlocker
    print ""+url
    johnlocker.LINKJL(name,url,iconimage,plot)
elif mode==321:
    from resources.libs.documentaries import johnlocker
    print ""+url
    johnlocker.LISTJL2(name,url)
elif mode==322:
    from resources.libs.documentaries import johnlocker
    print ""+url
    johnlocker.CATJL()
elif mode==323:
    from resources.libs.documentaries import johnlocker
    print ""+url
    johnlocker.SEARCHJL()

elif mode==324:
    from resources.libs.plugins import sokrostream
    print ""+url
    sokrostream.MAINSS()
elif mode==325:
    from resources.libs.plugins import sokrostream
    print ""+url
    sokrostream.LISTSS(url)
elif mode==326:
    from resources.libs.plugins import sokrostream
    print ""+url
    sokrostream.LINKLISTSS(name,url)
elif mode==327:
    from resources.libs.plugins import sokrostream
    print ""+url
    sokrostream.LINKSS(name,url)
elif mode==328:
    from resources.libs.plugins import sokrostream
    print ""+url
    sokrostream.GENRESS(url)
elif mode==329:
    from resources.libs.plugins import sokrostream
    print ""+url
    sokrostream.SearchhistorySS()
elif mode==330:
    from resources.libs.plugins import sokrostream
    print ""+url
    sokrostream.SEARCHSS(url)
elif mode==331:
    from resources.libs.documentaries import videodocumentaire
    print ""+url
    videodocumentaire.MAINVD()
elif mode==332:
    from resources.libs.documentaries import videodocumentaire
    print ""+url
    videodocumentaire.LISTVD(url)
elif mode==333:
    from resources.libs.documentaries import videodocumentaire
    print ""+url
    videodocumentaire.LINKVD(name,url,iconimage)
elif mode==334:
    from resources.libs.documentaries import videodocumentaire
    print ""+url
    videodocumentaire.SEARCHVD()
elif mode==335:
    from resources.libs.plugins import aflam
    print ""+url
    aflam.MAINAFLAM()
elif mode==336:
    from resources.libs.plugins import aflam
    print ""+url
    aflam.LISTProg(url)
elif mode==337:
    from resources.libs.plugins import aflam
    print ""+url
    aflam.LISTEPI(name,url,iconimage)
elif mode==338:
    from resources.libs.plugins import aflam
    print ""+url
    aflam.LINKSAFLAM(name,url,iconimage)
elif mode==339:
    from resources.libs.plugins import aflam
    print ""+url
    aflam.SERIESAFLAM(url)
elif mode==340:
    from resources.libs.plugins import aflam
    print ""+url
    aflam.MOVIESAFLAM(url)
elif mode==341:
    from resources.libs.plugins import aflam
    print ""+url
    aflam.LISTMov(url)
elif mode==342:
    from resources.libs.plugins import aflam
    print ""+url
    aflam.SEARCHAFLAM()
elif mode==343:
    from resources.libs.plugins import animania
    print ""+url
    animania.MAIN()
elif mode==344:
    from resources.libs.plugins import animania
    print ""+url
    animania.MOVIES()
elif mode==345:
    from resources.libs.plugins import animania
    print ""+url
    animania.LIST(url)
elif mode==346:
    from resources.libs.plugins import animania
    print ""+url
    animania.LISTHOSTS(name,url,iconimage)
elif mode==347:
    from resources.libs.plugins import animania
    print ""+url
    animania.PLAY(name,url,iconimage)
elif mode==348:
    from resources.libs.plugins import animania
    print ""+url
    animania.DRAMAS()
elif mode==349:
    from resources.libs.plugins import animania
    print ""+url
    animania.SEARCH()
elif mode==350:
    from resources.libs.plugins import animania
    print ""+url
    animania.LISTEPISODES(name,url,iconimage)
elif mode==351:
    from resources.libs.plugins import arabtv
    print ""+url
    arabtv.MAIN3arabtv()
elif mode==352:
    from resources.libs.plugins import arabtv
    print ""+url
    arabtv.CAT3arabtv(url)
elif mode==353:
    from resources.libs.plugins import arabtv
    print ""+url
    arabtv.LIST3arabtv(url)
elif mode==354:
    from resources.libs.plugins import arabtv
    print ""+url
    arabtv.SEARCHarabtv()
elif mode==355:
    from resources.libs.plugins import arabtv
    print ""+url
    arabtv.LINKS3arabtv(name,url,iconimage)
elif mode==356:
    from resources.libs.plugins import arabtv
    print ""+url
    arabtv.LIST3arabtvEPI(url,iconimage)
elif mode==357:
    from resources.libs.plugins import mailru
    print ""+url
    mailru.MAINMAILRU(url)
elif mode==358:
    from resources.libs.plugins import mailru
    print ""+url
    mailru.LINKSMAILRU(name,url,iconimage)
elif mode==359:
    from resources.libs.plugins import mailru
    print ""+url
    mailru.SEARCHMAILRU()
elif mode==360:
    from resources.libs.sports import outdoorch
    print ""+url
    outdoorch.MAINOTV()
elif mode==361:
    from resources.libs.sports import outdoorch
    print ""+url
    outdoorch.OTVList(url)
elif mode==362:
    from resources.libs.international import cinemaxx
    print ""+url
    cinemaxx.MAINCINEM()
elif mode==363:
    from resources.libs.international import cinemaxx
    print ""+url
    cinemaxx.LISTCINEM(url)
elif mode==364:
    from resources.libs.international import cinemaxx
    print ""+url
    cinemaxx.LINKSCINEM(name,url,iconimage,plot)
elif mode==365:
    from resources.libs.international import cinemaxx
    print ""+url
    cinemaxx.SEARCHCINEM()
elif mode==366:
    from resources.libs.international import cinemaxx
    print ""+url
    cinemaxx.GENRECINEM()
elif mode==367:
    from resources.libs.plugins import frenchstream
    print ""+url
    frenchstream.MAINFS()
elif mode==368:
    from resources.libs.plugins import frenchstream
    print ""+url
    frenchstream.LISTFS(url)
elif mode==369:
    from resources.libs.plugins import frenchstream
    print ""+url
    frenchstream.LINKLISTFS(name,url)
elif mode==370:
    from resources.libs.plugins import frenchstream
    print ""+url
    frenchstream.LINKFS(name,url)
elif mode==371:
    from resources.libs.plugins import frenchstream
    print ""+url
    frenchstream.GENREFS(url)
elif mode==372:
    from resources.libs.plugins import frenchstream
    print ""+url
    frenchstream.SearchhistoryFS()
elif mode==373:
    from resources.libs.plugins import frenchstream
    print ""+url
    frenchstream.SEARCHFS(url)
elif mode==374:
    from resources.libs.plugins import animetoon
    print ""+url
    animetoon.MAIN()
elif mode==375:
    from resources.libs.plugins import animetoon
    print ""+url
    animetoon.DUBBED()
elif mode==376:
    from resources.libs.plugins import animetoon
    print ""+url
    animetoon.LIST(url)
elif mode==377:
    from resources.libs.plugins import animetoon
    print ""+url
    animetoon.LISTEPI(name,url,iconimage,plot,genre)
elif mode==378:
    from resources.libs.plugins import animetoon
    print ""+url
    animetoon.LISTHOSTS(name,url,iconimage)
elif mode==379:
    from resources.libs.plugins import animetoon
    print ""+url
    animetoon.PLAY(name,url,iconimage)
elif mode==380:
    from resources.libs.plugins import animetoon
    print ""+url
    animetoon.MOVIES()
elif mode==381:
    from resources.libs.plugins import animetoon
    print ""+url
    animetoon.GETMOVIE(name,url,iconimage)
elif mode==382:
    from resources.libs.plugins import animetoon
    print ""+url
    animetoon.CARTOONS()
elif mode==383:
    from resources.libs.plugins import animetoon
    print ""+url
    animetoon.AZAT(url)
elif mode==384:
    from resources.libs.plugins import animetoon
    print ""+url
    animetoon.LISTPOP()
elif mode==385:
    from resources.libs.plugins import animetoon
    print ""+url
    animetoon.SEARCHAT()
elif mode==386:
    from resources.libs.plugins import animetoon
    print ""+url
    animetoon.GENREAT(url)
elif mode==387:
    from resources.libs.plugins import scenesource
    print ""+url
    scenesource.MAINSCENE()
elif mode==388:
    from resources.libs.plugins import scenesource
    print ""+url
    scenesource.SECSCENE(url)
elif mode==389:
    from resources.libs.plugins import scenesource
    print ""+url
    scenesource.LISTMOVIES(url)
elif mode==390:
    from resources.libs.plugins import scenesource
    print ""+url
    scenesource.VIDEOLINKSSCENE(name,url,iconimage)
elif mode==391:
    from resources.libs.plugins import scenesource
    print ""+url
    scenesource.LISTTV(url)
elif mode==392:
    from resources.libs.plugins import scenesource
    print ""+url
    scenesource.SearchhistorySCENE()
elif mode==393:
    from resources.libs.plugins import scenesource
    print ""+url
    scenesource.SEARCHSCENE(url)
elif mode==394:
    from resources.libs.live import nhl
    print ""+url
    nhl.MAINNHL(url)
elif mode==395:
    from resources.libs.live import nhl
    print ""+url
    nhl.LISTSTREAMS(name,url)
elif mode==396:
    from resources.libs.live import nhl
    print ""+url
    nhl.LINK(name,url,iconimage)
elif mode==397:
    from resources.libs.movies_tv import sidereel
    print ""+url
    sidereel.MAINSIDE()
elif mode==398:
    from resources.libs.movies_tv import sidereel
    print ""+url
    sidereel.SEARCHSR()
elif mode==399:
    from resources.libs.movies_tv import sidereel
    print ""+url
    sidereel.TRACKSHOW(url)
elif mode==400:
    from resources.libs.movies_tv import sidereel
    print ""+url
    sidereel.UNTRACKSHOW(url)
elif mode==401:
    from resources.libs.movies_tv import sidereel
    print ""+url
    sidereel.SEARCHED(url)
elif mode==402:
    from resources.libs.movies_tv import sidereel
    print ""+url
    sidereel.TRACKEDSHOWS()
elif mode==405:
    from resources.libs.movies_tv import filestube
    print ""+url
    filestube.LISTSP3(url)
elif mode==406:
    from resources.libs.movies_tv import filestube
    print ""+url
    filestube.LINKSP3(name,url)
elif mode==407:
    from resources.libs.movies_tv import rls1click
    print ""+url
    rls1click.LISTSP3(url)
elif mode==408:
    from resources.libs.movies_tv import rls1click
    print ""+url
    rls1click.LINKSP3(name,url)
elif mode==409:
    from resources.libs.live import skyaccess
    skyaccess.MAINSA()
elif mode==410:
    from resources.libs.live import skyaccess
    skyaccess.LISTMENU(url)
elif mode==411:
    from resources.libs.live import skyaccess
    skyaccess.LISTCONTENT(url,iconimage)
elif mode==412:
    from resources.libs.live import skyaccess
    skyaccess.LISTMENU2(url)
elif mode==413:
    from resources.libs.live import skyaccess
    skyaccess.PLAYLINK(name,url,iconimage)
elif mode==414: WHClear(url)
elif mode==415: MAINTENANCE(name)
elif mode==416: MAINDEL(url)
elif mode==417: ADSettings(name,url)
elif mode==418: delAS()
elif mode==419:
    from resources.libs.international import  einthusan
    einthusan.SEARCHEIN(url)
elif mode==421:
    from resources.libs.plugins import yify
    yify.MAIN()
elif mode==422:
    from resources.libs.plugins import yify
    yify.LIST(url)
elif mode==423:
    from resources.libs.plugins import yify
    yify.LINK(name,url,iconimage)
elif mode==424:
    from resources.libs.plugins import yify
    yify.Searchhistory()
elif mode==425:
    from resources.libs.plugins import yify
    yify.SEARCH(url)
elif mode==426:
    from resources.libs.plugins import yify
    yify.SortBy(url)
elif mode==427:
    from resources.libs.plugins import yify
    yify.GotoPage(url)
elif mode==428:
    from resources.libs.plugins import yify
    yify.ENTYEAR()
elif mode==429:
    from resources.libs.movies_tv import trakt
    trakt.showList()
elif mode==430:
    from resources.libs.movies_tv import trakt
    trakt.searchShow()
elif mode==431:
    from resources.libs.movies_tv import trakt
    trakt.trackedShows()
elif mode==432:
    from resources.libs.movies_tv import trakt
    trakt.trackShow(name,url)
elif mode==433:
    from resources.libs.movies_tv import trakt
    trakt.untrackShow(name,url)
elif mode==434:
    from resources.libs.international import catiii
    catiii.MAIN()
elif mode==435:
    from resources.libs.international import catiii
    catiii.LIST(url)
elif mode==436:
    from resources.libs.international import catiii
    catiii.LINK(name,url,iconimage)
elif mode==437:
    from resources.libs.international import catiii
    catiii.GotoPage(url)
elif mode==438:
    from resources.libs.international import catiii
    catiii.SEARCH(url)
elif mode==439:
    from resources.libs.live import kiwi
    print ""+url
    kiwi.MAIN()
elif mode==440:
    from resources.libs.live import kiwi
    print ""+url
    kiwi.setTimeZone()
elif mode==441:
    from resources.libs.live import kiwi
    print ""+url
    kiwi.Link(name,url,iconimage)
elif mode==442:
    from resources.libs.live import kiwi
    print ""+url
    kiwi.AllStreams()
elif mode==443:
    from resources.libs.live import sportspack
    print ""+url
    sportspack.MAIN()
elif mode==444:
    from resources.libs.live import sportspack
    print ""+url
    sportspack.LIST(url)
elif mode==445:
    from resources.libs.live import sportspack
    print ""+url
    sportspack.LINK(name,url,iconimage)
elif mode==446:
    from resources.libs.live import onefm
    print ""+url
    onefm.MAIN()
elif mode==447:
    from resources.libs.sports import mlb
    print ""+url
    mlb.MAIN()
elif mode==448:
    from resources.libs.sports import mlb
    print ""+url
    mlb.LIST(url)
elif mode==449:
    from resources.libs.sports import mlb
    print ""+url
    mlb.LINK(name,url,iconimage)
elif mode==450:
    from resources.libs.sports import mlb
    print ""+url
    mlb.LIST2(url)
elif mode==451:
    from resources.libs.plugins import shush
    print ""+url
    shush.MAIN(url)
elif mode==452:
    from resources.libs.plugins import shush
    print ""+url
    shush.LIST(name,url,iconimage)
elif mode==453:
    from resources.libs.plugins import shush
    print ""+url
    shush.LINK(name,url,iconimage)
elif mode==454:
    LIBRTMP(name,url,plot)
elif mode==455:
    DLLIBRTMP(name,url,plot)
elif mode==456:
    from resources.libs.movies_tv import sidereel
    print ""+url
    sidereel.EntCreds(url)
elif mode==457:
    from resources.libs.live import ibrod
    print ""+url
    ibrod.USALIST(url)
elif mode==458:
    from resources.libs.live import ibrod
    print ""+url
    ibrod.USALINK(name,url,iconimage)
elif mode==459:
    from resources.libs.plugins import pftv
    pftv.MAINPFTV(index=index)
elif mode==460:
    from resources.libs.plugins import pftv
    pftv.LISTPFTV(url,index=index)
elif mode==461:
    from resources.libs.plugins import pftv
    pftv.LISTHOST(name,url,iconimage)
elif mode==462:
    from resources.libs.plugins import pftv
    pftv.PLAYPFTV(name,url)
elif mode==463:
    from resources.libs.plugins import pftv
    pftv.AtoZPFTV(index=index)
elif mode==464:
    from resources.libs.plugins import pftv
    pftv.LISTSHOW(name,url,index=index)
elif mode==465:
    from resources.libs.plugins import pftv
    pftv.LISTSEASON(name,url,index=index)
elif mode==466:
    from resources.libs.plugins import pftv
    pftv.LISTEPISODE(name,url,index=index)
elif mode==467:
    from resources.libs.plugins import pftv
    pftv.POPULARPFTV(url,index=index)
elif mode==468:
    from resources.libs.plugins import pftv
    pftv.SearchhistoryPFTV(index=index)
elif mode==469:
    from resources.libs.plugins import pftv
    pftv.SEARCHPFTV(url,index=index)
elif mode==470:
    from resources.libs.live import hqzone
    hqzone.MAINHQ()
elif mode==471:
    from resources.libs.live import hqzone
    hqzone.LISTMENU(url)
elif mode==472:
    from resources.libs.live import hqzone
    hqzone.LISTCONTENT(url,iconimage)
elif mode==473:
    from resources.libs.live import hqzone
    hqzone.LISTMENU2(url)
elif mode==474:
    from resources.libs.live import hqzone
    hqzone.PLAYLINK(name,url,iconimage)
elif mode==475:
    from resources.libs.live import hqzone
    hqzone.Calendar(url)
elif mode==476:
    from resources.libs.live import skyaccess
    skyaccess.Calendar(url)
elif mode==477:
    from resources.libs.live import nflfan
    nflfan.NFLMAIN()
elif mode==478:
    from resources.libs.international import viki
    viki.VIKIMAIN()
elif mode==479:
    from resources.libs.international import viki
    viki.VIKICAT(url)
elif mode==480:
    from resources.libs.international import viki
    viki.LISTVIKIT(url)
elif mode==481:
    from resources.libs.international import viki
    viki.LISTVIKIEPI(url)
elif mode==482:
    from resources.libs.international import viki
    viki.LINKINT(name,url,iconimage)
elif mode==483:
    from resources.libs.international import viki
    viki.LISTVIKIM(url)
elif mode==484:
    from resources.libs.international import viki
    viki.VIKIGENREM(url)
elif mode==485:
    from resources.libs.international import viki
    viki.SEARCHVIKI()
elif mode==487:
    from resources.libs import artist
    artist.SearchArtist(name,url)
elif mode==488:
    from resources.libs import artist
    artist.ListArtist(url,iconimage)
elif mode==500: TVAll()        
elif mode==530:
    from resources.libs.plugins import extramina
    extramina.MAINEXTRA()
elif mode==531:
    from resources.libs.plugins import extramina
    print ""+url
    extramina.LISTEXgenre(url)
elif mode==532:
    from resources.libs.plugins import extramina
    print ""+url
    extramina.LISTEXrecent(url)
elif mode==533:
    from resources.libs.plugins import extramina
    print ""+url
    extramina.GENREEXTRA(url)
elif mode==534:
    from resources.libs.plugins import extramina
    print ""+url
    extramina.SEARCHEXTRA(url)
elif mode==535:
    from resources.libs.plugins import extramina
    print ""+url
    extramina.SearchhistoryEXTRA()
elif mode==536:
    from resources.libs.plugins import extramina
    print ""+url
    extramina.VIDEOLINKSEXTRA(name,url,iconimage,plot)
elif mode==538:
    from resources.libs.plugins import extramina
    print ""+url
    extramina.AtoZEXTRA()
elif mode==537:
    print ""+url
    MMA()        
elif mode==539:
    from resources.libs.plugins import sceper
    sceper.MAINSCEPER()
elif mode==540:
    from resources.libs.plugins import sceper
    sceper.MORTSCEPER(url)
elif mode==541:
    from resources.libs.plugins import sceper
    print ""+url
    sceper.LISTSCEPER(name,url)
elif mode==545:
    from resources.libs.plugins import sceper
    print ""+url
    sceper.LISTSCEPER2(name,url)
elif mode==542:
    from resources.libs.plugins import sceper
    print ""+url
    sceper.SEARCHSCEPER(url)
elif mode==543:
    from resources.libs.plugins import sceper
    print ""+url
    sceper.SearchhistorySCEPER()
elif mode==544:
    from resources.libs.plugins import sceper
    print ""+url
    sceper.VIDEOLINKSSCEPER(name,url,iconimage)
elif mode==546:
    from resources.libs.movies_tv import backuptv
    print ""+url
    backuptv.CHANNELCList(url)
elif mode==547:
    from resources.libs.movies_tv import backuptv
    print ""+url
    backuptv.CHANNELCLink(name,url)
elif mode==548:
    from resources.libs.movies_tv import newmyvideolinks
    print ""+url
    newmyvideolinks.LISTEtowns(url)
elif mode==549:
    from resources.libs.movies_tv import newmyvideolinks
    newmyvideolinks.SEARCHEtowns(url)
elif mode==550:
    from resources.libs.movies_tv import newmyvideolinks
    newmyvideolinks.SearchhistoryEtowns(url)
if mode==3000: print""
elif mode==567:
    from resources.libs.plugins import fma
    print ""+url
    fma.MAINFMA()
elif mode==568:
    from resources.libs.plugins import fma
    print ""+url
    fma.LISTFMA(url)
elif mode==569:
    from resources.libs.plugins import fma
    print ""+url
    fma.LINKFMA(name,url,iconimage,plot)
elif mode==570:
    from resources.libs.plugins import fma
    print ""+url
    fma.AtoZFMA()
elif mode==571:
    from resources.libs.plugins import fma
    print ""+url
    fma.GENREFMA(url)
elif mode==646:
    from resources.libs.plugins import fma
    print ""+url
    fma.SearchhistoryM()
elif mode==647:
    from resources.libs.plugins import fma
    print ""+url
    fma.SEARCHM(url)
elif mode==572:
    from resources.libs.plugins import watchseries
    print ""+url
    watchseries.MAINWATCHS(index=index)
elif mode==573:
    from resources.libs.plugins import watchseries
    print ""+url
    watchseries.LISTWATCHS(url,index=index)
elif mode==574:
    from resources.libs.plugins import watchseries
    print ""+url
    watchseries.LINKWATCHS(name,url)
elif mode==575:
    from resources.libs.plugins import watchseries
    print ""+url
    watchseries.LISTHOST(name,url)
elif mode==576:
    from resources.libs.plugins import watchseries
    print ""+url
    watchseries.LISTSHOWWATCHS(url,index=index)
elif mode==577:
    from resources.libs.plugins import watchseries
    print ""+url
    watchseries.AtoZWATCHS(index=index)
elif mode==578:
    from resources.libs.plugins import watchseries
    print ""+url
    watchseries.LISTWATCHSEASON(name, url,index=index)
elif mode==579:
    from resources.libs.plugins import watchseries
    print ""+url
    watchseries.LISTWATCHEPISODE(name, url,index=index)
elif mode==580:
    from resources.libs.plugins import watchseries
    print ""+url
    watchseries.POPULARWATCHS(url,index=index)
elif mode==581:
    from resources.libs.plugins import watchseries
    print ""+url
    watchseries.SearchhistoryWS(index=index)
elif mode==582:
    from resources.libs.plugins import watchseries
    print ""+url
    watchseries.SEARCHWS(url,index=index)
elif mode==583:
    from resources.libs.plugins import watchseries
    print ""+url
    watchseries.GENREWATCHS(index=index)
elif mode==584:
    from resources.libs.plugins import iwatchonline
    print ""+url
    iwatchonline.iWatchMAIN()
elif mode==642:
    from resources.libs.plugins import iwatchonline
    print ""+url
    iwatchonline.SearchhistoryTV(index=index)
elif mode==643:
    from resources.libs.plugins import iwatchonline
    print ""+url
    iwatchonline.SEARCHTV(url,index=index)
elif mode==644:
    from resources.libs.plugins import iwatchonline
    print ""+url
    iwatchonline.SearchhistoryM(index=index)
elif mode==645:
    from resources.libs.plugins import iwatchonline
    print ""+url
    iwatchonline.SEARCHM(url,index=index)
elif mode==585:
    from resources.libs.plugins import iwatchonline
    print ""+url
    iwatchonline.iWatchTV(index=index)
elif mode==586:
    from resources.libs.plugins import iwatchonline
    print ""+url
    iwatchonline.iWatchMOVIES(index=index)
elif mode==587:
    from resources.libs.plugins import iwatchonline
    print ""+url
    iwatchonline.iWatchLISTMOVIES(url,index=index)
elif mode==588:
    from resources.libs.plugins import iwatchonline
    print ""+url
    iwatchonline.iWatchLINK(name,url)
elif mode==589:
    from resources.libs.plugins import iwatchonline
    print ""+url
    iwatchonline.iWatchLISTSHOWS(url,index=index)
elif mode==590:
    from resources.libs.plugins import iwatchonline
    print ""+url
    iwatchonline.iWatchSeason(name,url,iconimage,index=index)
elif mode==591:
    from resources.libs.plugins import iwatchonline
    print ""+url
    iwatchonline.iWatchEpisode(name,url,index=index)
elif mode==592:
    from resources.libs.plugins import iwatchonline
    print ""+url
    iwatchonline.iWatchToday(url,index=index)
elif mode==593:
    from resources.libs.plugins import iwatchonline
    print ""+url
    iwatchonline.AtoZiWATCHtv(index=index)
elif mode==594:
    from resources.libs.plugins import iwatchonline
    print ""+url
    iwatchonline.iWatchGenreTV(index=index)
elif mode==595:
    from resources.libs.plugins import iwatchonline
    print ""+url
    iwatchonline.AtoZiWATCHm(index=index)
elif mode==596:
    from resources.libs.plugins import iwatchonline
    print ""+url
    iwatchonline.iWatchGenreM(index=index)
elif mode==601:
    from resources.libs.plugins import seriesgate
    seriesgate.MAINSG()
elif mode==602:
    from resources.libs.plugins import seriesgate
    print ""+url
    seriesgate.LISTEpiSG(url)
elif mode==603:
    from resources.libs.plugins import seriesgate
    print ""+url
    seriesgate.LISTShowsSG(url)
elif mode==604:
    from resources.libs.plugins import seriesgate
    print ""+url
    seriesgate.LISTSeasonSG(name,url,iconimage)
elif mode==605:
    from resources.libs.plugins import seriesgate
    print ""+url
    seriesgate.LISTEpilistSG(name,url)
elif mode==606:
    from resources.libs.plugins import seriesgate
    print ""+url
    seriesgate.LISTPopSG(url)
elif mode==607:
    from resources.libs.plugins import seriesgate
    print ""+url
    seriesgate.GENRESG(url)
elif mode==608:
    from resources.libs.plugins import seriesgate
    print ""+url
    seriesgate.SEARCHSG(url)
elif mode==612:
    from resources.libs.plugins import seriesgate
    print ""+url
    seriesgate.SearchhistorySG()
elif mode==609:
    from resources.libs.plugins import seriesgate
    print ""+url
    seriesgate.VIDEOLINKSSG(name,url,iconimage)
elif mode==610:
    from resources.libs.plugins import seriesgate
    print ""+url
    seriesgate.AtoZSG()
elif mode==611:
    from resources.libs.plugins import seriesgate
    print ""+url
    seriesgate.AllShows(url)
elif mode==613:
    from resources.libs.plugins import dubzonline
    dubzonline.MAINdz()
elif mode==614:
    from resources.libs.plugins import dubzonline
    print ""+url
    dubzonline.AtoZdz()
elif mode==615:
    from resources.libs.plugins import dubzonline
    print ""+url
    dubzonline.AZLIST(name,url)
elif mode==616:
    from resources.libs.plugins import dubzonline
    print ""+url
    dubzonline.EPILIST(url)
elif mode==617:
    from resources.libs.plugins import dubzonline
    print ""+url
    dubzonline.LINK(name,url)
elif mode==618:
    from resources.libs.plugins import dubzonline
    print ""+url
    dubzonline.latestLIST(url)
elif mode==619:
    from resources.libs.plugins import sominaltvfilms
    sominaltvfilms.MAIN()
elif mode==620:
    from resources.libs.plugins import sominaltvfilms
    print ""+url
    sominaltvfilms.LIST(name,url)
elif mode==621:
    from resources.libs.plugins import sominaltvfilms
    print ""+url
    sominaltvfilms.LINK(name,url,iconimage,fanart,plot)
elif mode==622:
    from resources.libs.plugins import sominaltvfilms
    print ""+url
    sominaltvfilms.LINK2(name,url,iconimage,plot)
elif mode==623:
    from resources.libs.plugins import sominaltvfilms
    print ""+url
    sominaltvfilms.AtoZ(url)
elif mode==624:
    from resources.libs.plugins import sominaltvfilms
    print ""+url
    sominaltvfilms.SEARCH()
elif mode==625:
    from resources.libs.plugins import animefreak
    animefreak.MAIN()
elif mode==626:
    from resources.libs.plugins import animefreak
    print ""+url
    animefreak.LIST(name,url)
elif mode==627:
    from resources.libs.plugins import animefreak
    print ""+url
    animefreak.LINK(name,url,iconimage,plot)
elif mode==628:
    from resources.libs.plugins import animefreak
    print ""+url
    animefreak.AtoZ()
elif mode==629:
    from resources.libs.plugins import animefreak
    print ""+url
    animefreak.AZLIST(name,url)
elif mode==630:
    from resources.libs.plugins import animefreak
    print ""+url
    animefreak.LIST2(name,url,iconimage,plot)
elif mode==632:
    from resources.libs.plugins import animefreak
    print ""+url
    animefreak.LATESTE(name,url)
elif mode==633:
    from resources.libs.plugins import animefreak
    print ""+url
    animefreak.LATESTA(name,url)
elif mode==634:
    from resources.libs.plugins import animefreak
    print ""+url
    animefreak.GENRE(url)
elif mode==635:
    from resources.libs.plugins import animefreak
    print ""+url
    animefreak.GENRELIST(url)
elif mode==636:
    from resources.libs.plugins import animefreak
    print ""+url
    animefreak.LATESTA(name,url)
elif mode==637:
    from resources.libs.plugins import animefreak
    print ""+url
    animefreak.LISTPOP(url)
elif mode==638:
    from resources.libs.plugins import animefreak
    print ""+url
    animefreak.SEARCH()
elif mode==639:
    print ""+url
    GlobalFav()
elif mode==640:
    print ""+url
    ListglobalFavT()
elif mode==641:
    print ""+url
    ListglobalFavM()
#642-47 taken
elif mode==648:
        print ""+url
        ListglobalFavL()
elif mode==649:
    from resources.libs.plugins import iwatchonline
    print ""+url
    iwatchonline.iWatchLINKB(name,url)
elif mode==650:
    print ""+url
    ListglobalFavMs()
elif mode==651:
    print ""+url
    ListglobalFavTE()
elif mode==652:
    from resources.libs.plugins import iwatchonline
    iwatchonline.iWatchYearM(index=index)
elif mode==653:
    from resources.libs.plugins import iwatchonline
    iwatchonline.ENTYEAR(index=index)
elif mode==654:
    from resources.libs.plugins import iwatchonline
    iwatchonline.GotoPage(url,index=index)
elif mode==655:
    print ""+url
    ListglobalFavIWO()
elif mode==656:
    print ""+url
    from resources.libs.movies_tv import scenelog
    scenelog.ListSceneLogLinks(name,url)
elif mode==657:
    print ""+url
    from resources.libs.movies_tv import scenelog
    scenelog.ListSceneLogItems(url,'HD')
elif mode==658:
    print ""+url
    from resources.libs.movies_tv import scenelog
    scenelog.PlaySceneLogLink(name,url)
elif mode==659:
    print ""+url
    from resources.libs.movies_tv import scenelog
    scenelog.StartSceneLogSearch(url)
elif mode==660:
    print ""+url
    from resources.libs.movies_tv import scenelog
    scenelog.SearchSceneLog(name,url)
elif mode == 776: main.jDownloader(url)        
elif mode == 777: main.ChangeWatched(iconimage, url, name, '', '')
elif mode == 778: main.refresh_movie(name,iconimage)
elif mode == 779: main.ChangeWatched(iconimage, url, name, season, episode)
elif mode == 780: main.episode_refresh(name, iconimage, season, episode)
elif mode == 781: main.trailer(url)
elif mode == 782: main.TRAILERSEARCH(url, name, iconimage)
elif mode == 783: main.SwitchUp()
elif mode == 784: FIXES()
elif mode == 785: FIXDOWN(name,url,location,path)
elif mode==786:
    from resources.libs.plugins import fullstream
    print ""+url
    fullstream.MAINFULLS()
elif mode==787:
    from resources.libs.plugins import fullstream
    print ""+url
    fullstream.LISTFULLS(url)
elif mode==788:
    from resources.libs.plugins import fullstream
    print ""+url
    fullstream.LINKLIST(name,url)
elif mode==789:
    from resources.libs.plugins import fullstream
    print ""+url
    fullstream.LINKFULLS(name,url)
elif mode==790:
    from resources.libs.plugins import fullstream
    print ""+url
    fullstream.LISTEPISODE(name,url)
elif mode==791:
    from resources.libs.plugins import fullstream
    print ""+url
    fullstream.LINKLIST2(name,url)
elif mode==792:
    from resources.libs.plugins import fullstream
    print ""+url
    fullstream.SEARCHFULLS()
elif mode==793:
    from resources.libs.plugins import fullstream
    print ""+url
    fullstream.GENRESFULLS()
elif mode==794:
    from resources.libs.plugins import fullstream2
    print ""+url
    fullstream2.MAINFULLS()
elif mode==795:
    from resources.libs.plugins import fullstream2
    print ""+url
    fullstream2.LISTFULLS(url)
elif mode==796:
    from resources.libs.plugins import fullstream2
    print ""+url
    fullstream2.LINKLIST(name,url)
elif mode==797:
    from resources.libs.plugins import fullstream2
    print ""+url
    fullstream2.LINKFULLS(name,url)
elif mode==798:
    from resources.libs.plugins import fullstream2
    print ""+url
    fullstream2.LISTEPISODE(name,url)
elif mode==799:
    from resources.libs.plugins import fullstream2
    print ""+url
    fullstream2.SEARCHFULLS()
elif mode==800:
    from resources.libs.plugins import fullstream2
    print ""+url
    fullstream2.GENRESFULLS()
elif mode==801:
    from resources.libs.plugins import fullstream2
    print ""+url
    fullstream2.QLTFULLS()
elif mode == 1000:
    from resources.libs.plugins import tvrelease
    tvrelease.MAINMENU()
elif mode == 1001:
    from resources.libs.plugins import tvrelease
    tvrelease.INDEX(url)
elif mode == 1002:
    from resources.libs.plugins import tvrelease
    tvrelease.GOTOP(url)
elif mode == 1003:
    from resources.libs.plugins import tvrelease
    tvrelease.LISTHOSTERS(name,url)
elif mode == 1004:
    if selfAddon.getSetting("tube-proxy") == "true": selfAddon.setSetting('tube-proxy', 'false')
    else: selfAddon.setSetting('tube-proxy', 'true')
    xbmc.executebuiltin("XBMC.Container.Refresh")
elif mode == 1005:
    from resources.libs.plugins import tvrelease
    tvrelease.PLAYMEDIA(name,url)
elif mode == 1006:
    from resources.libs.plugins import tvrelease
    tvrelease.SEARCHhistory()
elif mode == 1007:
    from resources.libs.plugins import tvrelease
    tvrelease.TVPACKS(url)
elif mode == 1008:
    from resources.libs.plugins import tvrelease
    tvrelease.SEARCH(url)
elif mode == 1020:
    from resources.libs.plugins import tubeplus
    tubeplus.MAINMENU()
elif mode == 1021:
    from resources.libs.plugins import tubeplus
    tubeplus.TVMENU()
elif mode == 1022:
    from resources.libs.plugins import tubeplus
    tubeplus.MOVIE_MENU()
elif mode == 1023:
    from resources.libs.plugins import tubeplus
    tubeplus.TUBE_CHARTS(url)
elif mode == 1024:
    from resources.libs.plugins import tubeplus
    tubeplus.SEARCHhistory()
elif mode == 1025:
    from resources.libs.plugins import tubeplus
    tubeplus.SEARCH(url)
elif mode == 1026:
    from resources.libs.plugins import tubeplus
    tubeplus.LINK(name,url)
elif mode == 1027:
    from resources.libs.plugins import tubeplus
    tubeplus.VIDEOLINKS(name,url)
elif mode == 1028:
    from resources.libs.plugins import tubeplus
    tubeplus.GOTOP(url)
elif mode == 1040:
    from resources.libs.plugins import tubeplus
    tubeplus.MOVIES_SPECIAL(url)
elif mode == 1041:
    from resources.libs.plugins import tubeplus
    tubeplus.LATEST_TV(url)
elif mode == 1042:
    from resources.libs.plugins import tubeplus
    tubeplus.LAST_AIRED(url)
elif mode == 1043:
    from resources.libs.plugins import tubeplus
    tubeplus.TV_TOP10(url)
elif mode == 1044:
    from resources.libs.plugins import tubeplus
    tubeplus.GENRES(url)
elif mode == 1045:
    from resources.libs.plugins import tubeplus
    tubeplus.POPGENRES(url)
elif mode == 1046:
    from resources.libs.plugins import tubeplus
    tubeplus.INDEXONE(url)
elif mode == 1047:
    from resources.libs.plugins import tubeplus
    tubeplus.MOVIEAZ(url)
elif mode == 1048:
    from resources.libs.plugins import tubeplus
    tubeplus.INDEX2(url)
elif mode == 1049:
    from resources.libs.plugins import tubeplus
    tubeplus.SEASONS(name,url,iconimage)
elif mode == 1050:
    from resources.libs.plugins import tubeplus
    tubeplus.EPISODES(name,url,plot)        
elif mode == 1051:
    from resources.libs.plugins import tubeplus
    tubeplus.INDEXtv(url)
elif mode == 1052:
    from resources.libs import indexer
    indexer.SuperMovies(index=index)
elif mode == 1053:
    from resources.libs import indexer
    indexer.ChangeIndex(url)
elif mode == 1054:
    from resources.libs import indexer
    indexer.SuperTV(index=index)
elif mode == 1500: openMGuide()      
elif mode == 1501: AddToDixie(plot,name,url,iconimage)
elif mode == 1998: print ""
elif mode == 1999: settings.openSettings()
elif mode == 2000:
    xbmc.executebuiltin("XBMC.Container.Update(path,replace)")
    xbmc.executebuiltin("XBMC.ActivateWindow(Home)")        
xbmcplugin.endOfDirectory(int(sys.argv[1]))
