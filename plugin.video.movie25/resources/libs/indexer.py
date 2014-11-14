import main
import xbmc,xbmcgui, xbmcaddon, xbmcplugin
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art


def SuperMovies(index=False):
    Mindex = selfAddon.getSetting('mindexer')
    if 'Movie25' in Mindex:
        main.addDir('Search','http://www.movie25.so/',420,art+'/search2.png',index=index)
        main.addDir('A-Z','http://www.movie25.so/',6,art+'/az2.png',index=index)
        main.addDir('New Releases','http://www.movie25.so/movies/new-releases/',1,art+'/new2.png',index=index)
        main.addDir('Latest Added','http://www.movie25.so/movies/latest-added/',1,art+'/latest2.png',index=index)
        main.addDir('Featured Movies','http://www.movie25.so/movies/featured-movies/',1,art+'/feat2.png',index=index)
        main.addDir('Most Viewed','http://www.movie25.so/movies/most-viewed/',1,art+'/view2.png',index=index)
        main.addDir('Most Voted','http://www.movie25.so/movies/most-voted/',1,art+'/vote2.png',index=index)
        main.addDir('HD Releases','http://www.movie25.so/movies/latest-hd-movies/',1,art+'/dvd2hd.png',index=index)
        main.addDir('Genre','http://www.movie25.so/',2,art+'/genre2.png',index=index)
        main.addDir('By Year','http://www.movie25.so/',7,art+'/year2.png',index=index)
        main.addSpecial('Current Index: [COLOR orange]'+Mindex+'[/COLOR]','movies',1053,art+'/movie25.png')
    elif 'IceFilms' in Mindex:
        main.addDir('Search for Movies','Movies',286,art+'/search.png',index=index)
        main.addDir('A-Z','movies',292,art+'/az.png',index=index)
        main.addDir('Highly Rated','/movies/rating/1',282,art+'/vote2.png',index=index)
        main.addDir('Popular Movies','/movies/popular/1',282,art+'/view2.png',index=index)
        main.addDir('Latest Released','/movies/release/1',282,art+'/new2.png',index=index)
        main.addDir('Latest Added','/movies/added/1',282,art+'/latest2.png',index=index)
        main.addDir('Genre','movies',293,art+'/genre.png',index=index)
        main.addSpecial('Current Index: [COLOR orange]'+Mindex+'[/COLOR]','movies',1053,art+'/icefilms.png')
    elif 'iWatchOnline' in Mindex:
        main.addDir('Search Movies','http://www.iwatchonline.to',644,art+'/search.png',index=index)
        main.addDir('A-Z','http://www.iwatchonline.to',595,art+'/az.png',index=index)
        main.addDir('Popular','http://www.iwatchonline.to/movies?sort=popular&p=0',587,art+'/view2.png',index=index)
        main.addDir('Latest Added','http://www.iwatchonline.to/movies?sort=latest&p=0',587,art+'/latest2.png',index=index)
        main.addDir('Featured Movies','http://www.iwatchonline.to/movies?sort=featured&p=0',587,art+'/feat2.png',index=index)
        main.addDir('Latest HD Movies','http://www.iwatchonline.to/movies?quality=hd&sort=latest&p=0',587,art+'/new2.png',index=index)
        main.addDir('Genre','http://www.iwatchonline.to',596,art+'/genre2.png',index=index)
        main.addDir('By Year','http://www.iwatchonline.so/',652,art+'/year2.png',index=index)
        main.addSpecial('Current Index: [COLOR orange]'+Mindex+'[/COLOR]','movies',1053,art+'/iwatchonline.png')
    main.VIEWSB2()

def SuperTV(index=False):
    Tindex = selfAddon.getSetting('tindexer')
    if 'WatchSeries' in Tindex:
        main.addDir('Search','s',581,art+'/search.png',index=index)
        main.addDir('A-Z','s',577,art+'/az.png',index=index)
        main.addDir('Yesterdays Episodes','http://watchseries.ag/tvschedule/-2',573,art+'/yesepi.png',index=index)
        main.addDir('Todays Episodes','http://watchseries.ag/tvschedule/-1',573,art+'/toepi2.png',index=index)
        main.addDir('Popular Shows','http://watchseries.ag/',580,art+'/popshowsws.png',index=index)
        main.addDir('This Weeks Popular Episodes','http://watchseries.ag/new',573,art+'/thisweek.png',index=index)
        main.addDir('Newest Episodes Added','http://watchseries.ag/latest',573,art+'/newadd.png',index=index)
        main.addDir('By Genre','genre',583,art+'/genre.png',index=index)
        main.addSpecial('Current Index: [COLOR orange]'+Tindex+'[/COLOR]','tv',1053,art+'/watchseries.png')
    elif 'IceFilms' in Tindex:
        main.addDir('Search for TV Shows','TV',286,art+'/search.png',index=index)
        main.addDir('A-Z','tv',292,art+'/az.png',index=index)
        main.addDir('Latest Releases','TV',291,art+'/new2.png',index=index)
        main.addDir('Highly Rated','/tv/rating/1',282,art+'/vote2.png',index=index)
        main.addDir('Popular Shows','/tv/popular/1',282,art+'/view2.png',index=index)
        main.addDir('Latest Released','/tv/release/1',282,art+'/new2.png',index=index)
        main.addDir('Latest Added','/tv/added/1',282,art+'/latest2.png',index=index)
        main.addDir('Genre','tv',293,art+'/genre.png',index=index)
        main.addSpecial('Current Index: [COLOR orange]'+Tindex+'[/COLOR]','tv',1053,art+'/icefilms.png')
    elif 'iWatchOnline' in Tindex:
        main.addDir('Search TV Shows','http://www.iwatchonline.to',642,art+'/search.png',index=index)
        main.addDir('A-Z','http://www.iwatchonline.to',593,art+'/az.png',index=index)
        main.addDir('Todays Episodes','http://www.iwatchonline.to/tv-schedule',592,art+'/toepi2.png',index=index)
        main.addDir('Featured Shows','http://www.iwatchonline.to/tv-show?sort=featured&p=0',589,art+'/feat2.png',index=index)
        main.addDir('Popular Shows','http://www.iwatchonline.to/tv-show?sort=popular&p=0',589,art+'/view2.png',index=index)
        main.addDir('Latest Additions','http://www.iwatchonline.to/tv-show?sort=latest&p=0',589,art+'/latest2.png',index=index)
        main.addDir('Genre','http://www.iwatchonline.to',594,art+'/genre.png',index=index)   
        main.addSpecial('Current Index: [COLOR orange]'+Tindex+'[/COLOR]','tv',1053,art+'/iwatchonline.png')
    elif 'PFTV' in Tindex:
        main.addDir('Search','s',468,art+'/search.png',index=index)
        main.addDir('A-Z','s',463,art+'/az.png',index=index)
        main.addDir('Yesterdays Episodes','http://www.free-tv-video-online.me/internet/index_last_3_days.html',460,art+'/yesepi.png',index=index)
        main.addDir('Todays Episodes','http://www.free-tv-video-online.me/internet/index_last.html',460,art+'/toepi2.png',index=index)
        main.addDir('Popular Shows','shows',467,art+'/popshowsws.png',index=index)
        main.addDir('This Weeks Popular Episodes','season',467,art+'/thisweek.png',index=index)
        main.addSpecial('Current Index: [COLOR orange]'+Tindex+'[/COLOR]','tv',1053,art+'/pftv.png')
    main.VIEWSB2()

        
def ChangeIndex(type):
    if type == 'movies':
        namelist=['Movie25','IceFilms','iWatchOnline']
    else:
        namelist=['WatchSeries','PFTV','IceFilms','iWatchOnline']
    dialog = xbmcgui.Dialog()
    answer =dialog.select("Pick A Source",namelist)
    if answer != -1:
        if type == 'movies':
            selfAddon.setSetting('mindexer', namelist[int(answer)])
        else:
            selfAddon.setSetting('tindexer', namelist[int(answer)])
        xbmc.executebuiltin("XBMC.Container.Refresh")
    
