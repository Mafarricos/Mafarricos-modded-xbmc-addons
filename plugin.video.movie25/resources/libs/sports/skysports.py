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



def SKYSPORTS():
        main.addDir('All Videos','http://www1.skysports.com/watch/more/5/27452/200/1',173,art+'/skysports.png')
        main.addDir('Sports','http://www1.skysports.com/watch/tv-shows',178,art+'/skysports.png')
        main.addDir('TV Shows','http://www1.skysports.com/watch/tv-shows',175,art+'/skysports.png')


def SKYSPORTSCAT():
        main.addDir('Sports [COLOR red]All Videos[/COLOR]','http://www1.skysports.com/watch/more/5/28461/200/1',173,art+'/skysports.png')
        main.addDir('Football','football',179,art+'/skysports.png')
        main.addDir('Formula 1','formula-1',179,art+'/skysports.png')
        main.addDir('Cricket','http://www1.skysports.com//watch/video/sports/cricket',176,art+'/skysports.png')
        main.addDir('Rugby Union','rugby-union',179,art+'/skysports.png')
        main.addDir('Rugby League','http://www1.skysports.com//watch/video/sports/rugby-league',176,art+'/skysports.png')
        main.addDir('Golf','http://www1.skysports.com//watch/video/sports/golf',176,art+'/skysports.png')
        main.addDir('Tennis','http://www1.skysports.com//watch/video/sports/tennis',176,art+'/skysports.png')
        main.addDir('Boxing','http://www1.skysports.com//watch/video/sports/boxing',176,art+'/skysports.png')
        main.addDir('NFL','http://www1.skysports.com//watch/video/sports/nfl',176,art+'/skysports.png')
        main.addDir('Racing','http://www1.skysports.com//watch/video/sports/racing',176,art+'/skysports.png')
        main.addDir('Darts','http://www1.skysports.com//watch/video/sports/darts',176,art+'/skysports.png')
        main.addDir('Basketball','http://www1.skysports.com//watch/video/sports/basketball',176,art+'/skysports.png')
        main.addDir('Cycling','http://www1.skysports.com//watch/video/sports/cycling',176,art+'/skysports.png')
        main.addDir('Speedway','http://www1.skysports.com//watch/video/sports/speedway',176,art+'/skysports.png')
        main.addDir('Ice Hockey','http://www1.skysports.com//watch/video/sports/ice-hockey',176,art+'/skysports.png')
        main.addDir('UFC','http://www1.skysports.com//watch/video/sports/ufc',176,art+'/skysports.png')
        main.addDir('WWE','http://www1.skysports.com//watch/video/sports/wwe',176,art+'/skysports.png')

def SKYSPORTSCAT2(murl):
        if murl=='football':
                main.addDir('Football [COLOR red]All Videos[/COLOR]','http://www1.skysports.com/watch/more/5/12606/200/1',173,art+'/skysports.png')
                main.addDir('Premier League','premier-league',180,art+'/skysports.png')
                main.addDir('Championship','championship',180,art+'/skysports.png')
                main.addDir('League One','league-one',180,art+'/skysports.png')
                main.addDir('League Two','league-two',180,art+'/skysports.png')
                main.addDir('Scottish Football','scottish-football',180,art+'/skysports.png')
                main.addDir('Primera Liga','primera-liga',180,art+'/skysports.png')
                main.addDir('Champions League','http://www1.skysports.com/watch/video/sports/football/competitions/champions-league',176,art+'/skysports.png')
                main.addDir('Capital One Cup','http://www1.skysports.com/watch/video/sports/football/competitions/capital-one-cup',176,art+'/skysports.png')
        if murl=='formula-1':
                main.addDir('Formula 1 [COLOR red]All Videos[/COLOR]','http://www1.skysports.com/watch/more/5/12870/200/1',173,art+'/skysports.png')
                main.addDir('Grand Prix','grand-prix',180,art+'/skysports.png')
                main.addDir('Teams','f1Teams',180,art+'/skysports.png')
        if murl=='rugby-union':
                main.addDir('Rugby Union [COLOR red]All Videos[/COLOR]','http://www1.skysports.com/watch/more/5/12610/200/1',173,art+'/skysports.png')
                main.addDir('Aviva Premiership','http://www1.skysports.com/watch/video/sports/rugby-union/competitions/aviva-premiership',176,art+'/skysports.png')
                main.addDir('Super Rugby','http://www1.skysports.com/watch/video/sports/rugby-union/competitions/super-rugby',176,art+'/skysports.png')
                main.addDir('Heineken Cup','http://www1.skysports.com/watch/video/sports/rugby-union/competitions/heineken-cup',176,art+'/skysports.png')
def SKYSPORTSTEAMS(murl):
        if murl=='premier-league':
                main.addDir('Premier League [COLOR red]All Videos[/COLOR]','http://www1.skysports.com/watch/more/5/16426/100/1',173,art+'/skysports.png')
                main.addDir('Arsenal','http://www1.skysports.com/watch/video/sports/football/teams/arsenal',176,art+'/skysports.png')
                main.addDir('Aston Villa','http://www1.skysports.com/watch/video/sports/football/teams/aston-villa',176,art+'/skysports.png')
                main.addDir('Chelsea','http://www1.skysports.com/watch/video/sports/football/teams/chelsea',176,art+'/skysports.png')
                main.addDir('Everton','http://www1.skysports.com/watch/video/sports/football/teams/everton',176,art+'/skysports.png')
                main.addDir('Fulham','http://www1.skysports.com/watch/video/sports/football/teams/fulham',176,art+'/skysports.png')
                main.addDir('Liverpool','http://www1.skysports.com/watch/video/sports/football/teams/liverpool',176,art+'/skysports.png')
                main.addDir('Manchester City','http://www1.skysports.com/watch/video/sports/football/teams/manchester-city',176,art+'/skysports.png')
                main.addDir('Manchester United','http://www1.skysports.com/watch/video/sports/football/teams/manchester-united',176,art+'/skysports.png')
                main.addDir('Newcastle United','http://www1.skysports.com/watch/video/sports/football/teams/newcastle-united',176,art+'/skysports.png')
                main.addDir('Norwich City','http://www1.skysports.com/watch/video/sports/football/teams/norwich-city',176,art+'/skysports.png')
                main.addDir('Queens Park Rangers','http://www1.skysports.com/watch/video/sports/football/teams/queens-park-rangers',176,art+'/skysports.png')
                main.addDir('Reading','http://www1.skysports.com/watch/video/sports/football/teams/reading',176,art+'/skysports.png')
                main.addDir('Southampton','http://www1.skysports.com/watch/video/sports/football/teams/southampton',176,art+'/skysports.png')
                main.addDir('Stoke City','http://www1.skysports.com/watch/video/sports/football/teams/stoke-city',176,art+'/skysports.png')
                main.addDir('Sunderland','http://www1.skysports.com/watch/video/sports/football/teams/sunderland',176,art+'/skysports.png')
                main.addDir('Swansea City','http://www1.skysports.com/watch/video/sports/football/teams/swansea-city',176,art+'/skysports.png')
                main.addDir('Tottenham Hotspur','http://www1.skysports.com/watch/video/sports/football/teams/tottenham-hotspur',176,art+'/skysports.png')
                main.addDir('West Bromwich Albion','http://www1.skysports.com/watch/video/sports/football/teams/west-bromwich-albion',176,art+'/skysports.png')
                main.addDir('West Ham United','http://www1.skysports.com/watch/video/sports/football/teams/west-ham-united',176,art+'/skysports.png')
                main.addDir('Wigan Athletic','http://www1.skysports.com/watch/video/sports/football/teams/wigan-athletic',176,art+'/skysports.png')
                
        if murl=='championship':
                main.addDir('Championship [COLOR red]All Videos[/COLOR]','http://www1.skysports.com/watch/more/5/16428/100/1',173,art+'/skysports.png')
                main.addDir('Barnsley','http://www1.skysports.com/watch/video/sports/football/teams/barnsley',176,art+'/skysports.png')
                main.addDir('Birmingham City','http://www1.skysports.com/watch/video/sports/football/teams/birmingham-city',176,art+'/skysports.png')
                main.addDir('Blackburn Rovers','http://www1.skysports.com/watch/video/sports/football/teams/blackburn-rovers',176,art+'/skysports.png')
                main.addDir('Blackpool','http://www1.skysports.com/watch/video/sports/football/teams/blackpool',176,art+'/skysports.png')
                main.addDir('Bolton Wanderers','http://www1.skysports.com/watch/video/sports/football/teams/bolton-wanderers',176,art+'/skysports.png')
                main.addDir('Brighton','http://www1.skysports.com/watch/video/sports/football/teams/brighton',176,art+'/skysports.png')
                main.addDir('Bristol City','http://www1.skysports.com/watch/video/sports/football/teams/bristol-city',176,art+'/skysports.png')
                main.addDir('Burnley','http://www1.skysports.com/watch/video/sports/football/teams/burnley',176,art+'/skysports.png')
                main.addDir('Cardiff City','http://www1.skysports.com/watch/video/sports/football/teams/cardiff-city',176,art+'/skysports.png')
                main.addDir('Charlton Athletic','http://www1.skysports.com/watch/video/sports/football/teams/charlton-athletic',176,art+'/skysports.png')
                main.addDir('Crystal Palace','http://www1.skysports.com/watch/video/sports/football/teams/crystal-palace',176,art+'/skysports.png')
                main.addDir('Derby County','http://www1.skysports.com/watch/video/sports/football/teams/derby-county',176,art+'/skysports.png')
                main.addDir('Huddersfield Town','http://www1.skysports.com/watch/video/sports/football/teams/huddersfield-town',176,art+'/skysports.png')
                main.addDir('Hull City','http://www1.skysports.com/watch/video/sports/football/teams/hull-city',176,art+'/skysports.png')
                main.addDir('Ipswich Town','http://www1.skysports.com/watch/video/sports/football/teams/ipswich-town',176,art+'/skysports.png')
                main.addDir('Leeds United','http://www1.skysports.com/watch/video/sports/football/teams/leeds-united',176,art+'/skysports.png')
                main.addDir('Leicester City','http://www1.skysports.com/watch/video/sports/football/teams/leicester-city',176,art+'/skysports.png')
                main.addDir('Middlesbrough','http://www1.skysports.com/watch/video/sports/football/teams/middlesbrough',176,art+'/skysports.png')
                main.addDir('Millwall','http://www1.skysports.com/watch/video/sports/football/teams/millwall',176,art+'/skysports.png')
                main.addDir('Nottingham Forest','http://www1.skysports.com/watch/video/sports/football/teams/nottingham-forest',176,art+'/skysports.png')
                main.addDir('Peterborough United','http://www1.skysports.com/watch/video/sports/football/teams/peterborough-united',176,art+'/skysports.png')
                main.addDir('Sheffield Wednesday','http://www1.skysports.com/watch/video/sports/football/teams/sheffield-wednesday',176,art+'/skysports.png')
                main.addDir('Watford','http://www1.skysports.com/watch/video/sports/football/teams/watford',176,art+'/skysports.png')
                main.addDir('Wolverhampton','http://www1.skysports.com/watch/video/sports/football/teams/wolverhampton',176,art+'/skysports.png')
        if murl=='league-one':
                main.addDir('League One [COLOR red]All Videos[/COLOR]','http://www1.skysports.com/watch/more/5/16478/100/1',173,art+'/skysports.png')
                main.addDir('Bournemouth','http://www1.skysports.com/watch/video/sports/football/teams/bournemouth',176,art+'/skysports.png')
                main.addDir('Brentford','http://www1.skysports.com/watch/video/sports/football/teams/brentford',176,art+'/skysports.png')
                main.addDir('Bury','http://www1.skysports.com/watch/video/sports/football/teams/bury',176,art+'/skysports.png')
                main.addDir('Carlisle United','http://www1.skysports.com/watch/video/sports/football/teams/carlisle-united',176,art+'/skysports.png')
                main.addDir('Colchester United','http://www1.skysports.com/watch/video/sports/football/teams/colchester-united',176,art+'/skysports.png')
                main.addDir('Coventry City','http://www1.skysports.com/watch/video/sports/football/teams/coventry-city',176,art+'/skysports.png')
                main.addDir('Crawley Town','http://www1.skysports.com/watch/video/sports/football/teams/crawley-town',176,art+'/skysports.png')
                main.addDir('Crewe Alexandra','http://www1.skysports.com/watch/video/sports/football/teams/crewe-alexandra',176,art+'/skysports.png')
                main.addDir('Doncaster','http://www1.skysports.com/watch/video/sports/football/teams/doncaster',176,art+'/skysports.png')
                main.addDir('Hartlepool United','http://www1.skysports.com/watch/video/sports/football/teams/hartlepool-united',176,art+'/skysports.png')
                main.addDir('Leyton Orient','http://www1.skysports.com/watch/video/sports/football/teams/leyton-orient',176,art+'/skysports.png')
                main.addDir('Milton Keynes Dons','http://www1.skysports.com/watch/video/sports/football/teams/milton-keynes-dons',176,art+'/skysports.png')
                main.addDir('Notts County','http://www1.skysports.com/watch/video/sports/football/teams/notts-county',176,art+'/skysports.png')
                main.addDir('Oldham Athletic','http://www1.skysports.com/watch/video/sports/football/teams/oldham-athletic',176,art+'/skysports.png')
                main.addDir('Portsmouth','http://www1.skysports.com/watch/video/sports/football/teams/portsmouth',176,art+'/skysports.png')
                main.addDir('Preston North End','http://www1.skysports.com/watch/video/sports/football/teams/preston-north-end',176,art+'/skysports.png')
                main.addDir('Scunthorpe United','http://www1.skysports.com/watch/video/sports/football/teams/scunthorpe-united',176,art+'/skysports.png')
                main.addDir('Sheffield United','http://www1.skysports.com/watch/video/sports/football/teams/sheffield-united',176,art+'/skysports.png')
                main.addDir('Shrewsbury Town','http://www1.skysports.com/watch/video/sports/football/teams/shrewsbury-town',176,art+'/skysports.png')
                main.addDir('Stevenage','http://www1.skysports.com/watch/video/sports/football/teams/stevenage',176,art+'/skysports.png')
                main.addDir('Swindon Town','http://www1.skysports.com/watch/video/sports/football/teams/swindon-town',176,art+'/skysports.png')
                main.addDir('Tranmere Rovers','http://www1.skysports.com/watch/video/sports/football/teams/tranmere-rovers',176,art+'/skysports.png')
                main.addDir('Walsall','http://www1.skysports.com/watch/video/sports/football/teams/walsall',176,art+'/skysports.png')
                main.addDir('Yeovil Town','http://www1.skysports.com/watch/video/sports/football/teams/yeovil-town',176,art+'/skysports.png')
        if murl=='league-two':
                main.addDir('League Two [COLOR red]All Videos[/COLOR]','http://www1.skysports.com/watch/more/5/16478/100/1',173,art+'/skysports.png')
                main.addDir('AFC Wimbledon','http://www1.skysports.com/watch/video/sports/football/teams/afc-wimbledon',176,art+'/skysports.png')
                main.addDir('Accrington Stanley','http://www1.skysports.com/watch/video/sports/football/teams/accrington-stanley',176,art+'/skysports.png')
                main.addDir('Aldershot','http://www1.skysports.com/watch/video/sports/football/teams/aldershot',176,art+'/skysports.png')
                main.addDir('Barnet FC','http://www1.skysports.com/watch/video/sports/football/teams/barnet-fc',176,art+'/skysports.png')
                main.addDir('Bradford City','http://www1.skysports.com/watch/video/sports/football/teams/bradford-city',176,art+'/skysports.png')
                main.addDir('Bristol Rovers','http://www1.skysports.com/watch/video/sports/football/teams/bristol-rovers',176,art+'/skysports.png')
                main.addDir('Burton Albion','http://www1.skysports.com/watch/video/sports/football/teams/burton-albion',176,art+'/skysports.png')
                main.addDir('Cheltenham Town','http://www1.skysports.com/watch/video/sports/football/teams/cheltenham-town',176,art+'/skysports.png')
                main.addDir('Chesterfield','http://www1.skysports.com/watch/video/sports/football/teams/chesterfield',176,art+'/skysports.png')
                main.addDir('Dagenham and Redbridge','http://www1.skysports.com/watch/video/sports/football/teams/dagenham-and-redbridge',176,art+'/skysports.png')
                main.addDir('Exeter City','http://www1.skysports.com/watch/video/sports/football/teams/exeter-city',176,art+'/skysports.png')
                main.addDir('Fleetwood Town','http://www1.skysports.com/watch/video/sports/football/teams/fleetwood-town',176,art+'/skysports.png')
                main.addDir('Gillingham','http://www1.skysports.com/watch/video/sports/football/teams/gillingham',176,art+'/skysports.png')
                main.addDir('Hereford','http://www1.skysports.com/watch/video/sports/football/teams/hereford',176,art+'/skysports.png')
                main.addDir('Macclesfield Town','http://www1.skysports.com/watch/video/sports/football/teams/macclesfield-town',176,art+'/skysports.png')
                main.addDir('Morecambe','http://www1.skysports.com/watch/video/sports/football/teams/morecambe',176,art+'/skysports.png')
                main.addDir('Northampton Town','http://www1.skysports.com/watch/video/sports/football/teams/northampton-town',176,art+'/skysports.png')
                main.addDir('Oxford Utd','http://www1.skysports.com/watch/video/sports/football/teams/oxford-utd',176,art+'/skysports.png')
                main.addDir('Plymouth Argyle','http://www1.skysports.com/watch/video/sports/football/teams/plymouth-argyle',176,art+'/skysports.png')
                main.addDir('Port Vale','http://www1.skysports.com/watch/video/sports/football/teams/port-vale',176,art+'/skysports.png')
                main.addDir('Rochdale','http://www1.skysports.com/watch/video/sports/football/teams/rochdale',176,art+'/skysports.png')
                main.addDir('Rotherham United','http://www1.skysports.com/watch/video/sports/football/teams/rotherham-united',176,art+'/skysports.png')
                main.addDir('Southend United','http://www1.skysports.com/watch/video/sports/football/teams/southend-united',176,art+'/skysports.png')
                main.addDir('Torquay United','http://www1.skysports.com/watch/video/sports/football/teams/torquay-united',176,art+'/skysports.png')
                main.addDir('Wycombe Wanderers','http://www1.skysports.com/watch/video/sports/football/teams/wycombe-wanderers',176,art+'/skysports.png')
                main.addDir('York City','http://www1.skysports.com/watch/video/sports/football/teams/york-city',176,art+'/skysports.png')
        if murl=='scottish-football':
                main.addDir('Scottish Football [COLOR red]All Videos[/COLOR]','http://www1.skysports.com/watch/more/5/16480/100/1',173,art+'/skysports.png')
                main.addDir('Aberdeen','http://www1.skysports.com/watch/video/sports/football/teams/aberdeen',176,art+'/skysports.png')
                main.addDir('Celtic','http://www1.skysports.com/watch/video/sports/football/teams/celtic',176,art+'/skysports.png')
                main.addDir('Rangers','http://www1.skysports.com/watch/video/sports/football/teams/rangers',176,art+'/skysports.png')
        if murl=='primera-liga':
                main.addDir('Primera Liga [COLOR red]All Videos[/COLOR]','http://www1.skysports.com/watch/more/5/16995/100/1',173,art+'/skysports.png')
                main.addDir('Athletic Bilbao','http://www1.skysports.com/watch/video/sports/football/teams/athletic-bilbao',176,art+'/skysports.png')
                main.addDir('Atletico Madrid','http://www1.skysports.com/watch/video/sports/football/teams/atletico-madrid',176,art+'/skysports.png')
                main.addDir('Barcelona','http://www1.skysports.com/watch/video/sports/football/teams/barcelona',176,art+'/skysports.png')
                main.addDir('Celta Vigo','http://www1.skysports.com/watch/video/sports/football/teams/celta-vigo',176,art+'/skysports.png')
                main.addDir('Deportivo La Coruna','http://www1.skysports.com/watch/video/sports/football/teams/deportivo-la-coruna',176,art+'/skysports.png')
                main.addDir('Espanyol','http://www1.skysports.com/watch/video/sports/football/teams/espanyol',176,art+'/skysports.png')
                main.addDir('Getafe','http://www1.skysports.com/watch/video/sports/football/teams/getafe',176,art+'/skysports.png')
                main.addDir('Granada','http://www1.skysports.com/watch/video/sports/football/teams/granada',176,art+'/skysports.png')
                main.addDir('Levante','http://www1.skysports.com/watch/video/sports/football/teams/levante',176,art+'/skysports.png')
                main.addDir('Malaga','http://www1.skysports.com/watch/video/sports/football/teams/malaga',176,art+'/skysports.png')
                main.addDir('Osasuna','http://www1.skysports.com/watch/video/sports/football/teams/osasuna',176,art+'/skysports.png')
                main.addDir('Racing Santander','http://www1.skysports.com/watch/video/sports/football/teams/racing-santander',176,art+'/skysports.png')
                main.addDir('Rayo Vallecano','http://www1.skysports.com/watch/video/sports/football/teams/rayo-vallecano',176,art+'/skysports.png')
                main.addDir('Real Betis','http://www1.skysports.com/watch/video/sports/football/teams/real-betis',176,art+'/skysports.png')
                main.addDir('Real Madrid','http://www1.skysports.com/watch/video/sports/football/teams/real-madrid',176,art+'/skysports.png')
                main.addDir('Real Mallorca','http://www1.skysports.com/watch/video/sports/football/teams/real-mallorca',176,art+'/skysports.png')
                main.addDir('Real Sociedad','http://www1.skysports.com/watch/video/sports/football/teams/real-sociedad',176,art+'/skysports.png')
                main.addDir('Real Valladolid','http://www1.skysports.com/watch/video/sports/football/teams/real-valladolid',176,art+'/skysports.png')
                main.addDir('Real Zaragoza','http://www1.skysports.com/watch/video/sports/football/teams/real-zaragoza',176,art+'/skysports.png')
                main.addDir('Sevilla','http://www1.skysports.com/watch/video/sports/football/teams/sevilla',176,art+'/skysports.png')
                main.addDir('Sporting Gijon','http://www1.skysports.com/watch/video/sports/football/teams/sporting-gijon',176,art+'/skysports.png')
                main.addDir('Tenerife','http://www1.skysports.com/watch/video/sports/football/teams/tenerife',176,art+'/skysports.png')
                main.addDir('UD Almeria','http://www1.skysports.com/watch/video/sports/football/teams/ud-almeria',176,art+'/skysports.png')
                main.addDir('Valencia','http://www1.skysports.com/watch/video/sports/football/teams/valencia',176,art+'/skysports.png')
                main.addDir('Villarreal','http://www1.skysports.com/watch/video/sports/football/teams/villarreal',176,art+'/skysports.png')
                main.addDir('Xerez','http://www1.skysports.com/watch/video/sports/football/teams/xerez',176,art+'/skysports.png')
        if murl=='grand-prix':
                main.addDir('Grand Prix [COLOR red]All Videos[/COLOR]','http://www1.skysports.com/watch/more/5/27438/100/1',173,art+'/skysports.png')
                main.addDir('Australia','http://www1.skysports.com/watch/video/sports/formula-1/grandprix/australia',176,art+'/skysports.png')
                main.addDir('Malaysia','http://www1.skysports.com/watch/video/sports/formula-1/grandprix/malaysia',176,art+'/skysports.png')
                main.addDir('China','http://www1.skysports.com/watch/video/sports/formula-1/grandprix/china',176,art+'/skysports.png')
                main.addDir('Bahrain','http://www1.skysports.com/watch/video/sports/formula-1/grandprix/bahrain',176,art+'/skysports.png')
                main.addDir('Spain','http://www1.skysports.com/watch/video/sports/formula-1/grandprix/spain',176,art+'/skysports.png')
                main.addDir('Monaco','http://www1.skysports.com/watch/video/sports/formula-1/grandprix/monaco',176,art+'/skysports.png')
                main.addDir('Canada','http://www1.skysports.com/watch/video/sports/formula-1/grandprix/canada',176,art+'/skysports.png')
                main.addDir('Great Britain','http://www1.skysports.com/watch/video/sports/formula-1/grandprix/great-britain',176,art+'/skysports.png')
                main.addDir('Germany','http://www1.skysports.com/watch/video/sports/formula-1/grandprix/germany',176,art+'/skysports.png')
                main.addDir('Hungary','http://www1.skysports.com/watch/video/sports/formula-1/grandprix/hungary',176,art+'/skysports.png')
                main.addDir('Belgium','http://www1.skysports.com/watch/video/sports/formula-1/grandprix/belgium',176,art+'/skysports.png')
                main.addDir('Italy','http://www1.skysports.com/watch/video/sports/formula-1/grandprix/italy',176,art+'/skysports.png')
                main.addDir('Singapore','http://www1.skysports.com/watch/video/sports/formula-1/grandprix/singapore',176,art+'/skysports.png')
                main.addDir('Korea','http://www1.skysports.com/watch/video/sports/formula-1/grandprix/korea',176,art+'/skysports.png')
                main.addDir('Japan','http://www1.skysports.com/watch/video/sports/formula-1/grandprix/japan',176,art+'/skysports.png')
                main.addDir('India','http://www1.skysports.com/watch/video/sports/formula-1/grandprix/india',176,art+'/skysports.png')
                main.addDir('Abu Dhabi','http://www1.skysports.com/watch/video/sports/formula-1/grandprix/abu-dhabi',176,art+'/skysports.png')
                main.addDir('United States','http://www1.skysports.com/watch/video/sports/formula-1/grandprix/united-states',176,art+'/skysports.png')
                main.addDir('Brazil','http://www1.skysports.com/watch/video/sports/formula-1/grandprix/brazil',176,art+'/skysports.png')
        if murl=='f1Teams':
                main.addDir('Teams [COLOR red]All Videos[/COLOR]','http://www1.skysports.com/watch/more/5/28292/100/1',173,art+'/skysports.png')
                main.addDir('Caterham','http://www1.skysports.com/watch/video/sports/formula-1/teams/caterham',176,art+'/skysports.png')
                main.addDir('Ferrari','http://www1.skysports.com/watch/video/sports/formula-1/teams/ferrari',176,art+'/skysports.png')
                main.addDir('Force India','http://www1.skysports.com/watch/video/sports/formula-1/teams/force-india',176,art+'/skysports.png')
                main.addDir('Lotus','http://www1.skysports.com/watch/video/sports/formula-1/teams/lotus',176,art+'/skysports.png')
                main.addDir('Marussia','http://www1.skysports.com/watch/video/sports/formula-1/teams/marussia',176,art+'/skysports.png')
                main.addDir('McLaren','http://www1.skysports.com/watch/video/sports/formula-1/teams/mclaren',176,art+'/skysports.png')
                main.addDir('Mercedes GP','http://www1.skysports.com/watch/video/sports/formula-1/teams/mercedes-gp',176,art+'/skysports.png')
                main.addDir('Red Bull','http://www1.skysports.com/watch/video/sports/formula-1/teams/red-bull',176,art+'/skysports.png')
                main.addDir('Sauber','http://www1.skysports.com/watch/video/sports/formula-1/teams/sauber',176,art+'/skysports.png')
                main.addDir('Toro Rosso','http://www1.skysports.com/watch/video/sports/formula-1/teams/toro-rosso',176,art+'/skysports.png')
                main.addDir('Williams','http://www1.skysports.com/watch/video/sports/formula-1/teams/williams',176,art+'/skysports.png')


def SKYSPORTSTV(murl):
        main.GA("SkySportsTV","List")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match = re.compile('<img src=".+?" data-src="([^"]+)" class=".+?<a href="([^"]+)" class=".+?<h4 class=".+?">([^<]+)</h4>').findall(link)
        for thumb,url, name in match:
            thumb=thumb.replace('16-9/#{30}','384x216')
            url=url.replace('watch/tv-shows','watch/video/tv-shows').replace('/fantasyFC','/watch/video/tv-shows/fantasyFC')
            main.addDir(name,'http://www1.skysports.com'+url,176,thumb)
        main.VIEWSB()

def SKYSPORTSList(murl):
        main.GA("SkySports","List")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<a href="([^"]+)" class=".+?data-src="([^"]+)" class=".+?<h4 class=".+?">([^<]+)</h4>.+?">([^<]+)</p>.+?">([^<]+)</button>').findall(link)
        for url,thumb,name,date,typ in match:
                thumb=thumb.replace('16-9/#{30}','384x216')
                if name!='Sky Sports News Report':
                        if typ=='Watch Now':
                                main.addPlayMs(name+'   [COLOR red]'+date+'[/COLOR]',url,174,thumb,'','','','','')
                        else:
                                main.addPlayMs('[COLOR red]'+name+'[/COLOR]'+'   '+date,url,177,thumb,'','','','','')

def SKYSPORTSList2(murl):
        main.GA("SkySports","List")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        page=re.compile('data-current-page=".+?" data-pattern="(.+?)">').findall(link)
        if len(page)>0:
                for durl in page:
                        durl=durl.replace('{currentPage}','1').replace('/12/','/75/')
                link2=main.OPENURL('http://www1.skysports.com'+durl)
                link2=link2.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                match=re.compile('<a href="([^"]+)" class=".+?data-src="([^"]+)" class=".+?<h4 class=".+?">([^<]+)</h4>.+?">([^<]+)</p>.+?">([^<]+)</button>').findall(link)
                for url,thumb,name,date,typ in match:
                        thumb=thumb.replace('16-9/#{30}','384x216')
                        if name!='Sky Sports News Report':
                                if typ=='Watch Now':
                                        main.addPlayMs(name+'   [COLOR red]'+date+'[/COLOR]',url,174,thumb,'','','','','')
                                else:
                                        main.addPlayMs('[COLOR red]'+name+'[/COLOR]'+'   '+date,url,177,thumb,'','','','','')
        else:
                xbmc.executebuiltin("XBMC.Notification(Sorry!,No Video's to list,3000)")

  
        

def SKYSPORTSLink(mname,murl):
        main.GA("SkySports","Watched")
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Playing Video,1500)")
        ok= True
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('data-video-id="([^"]+?)"').findall(link)
        vlink='http://cf.c.ooyala.com/'+match[0]+'/'+match[0]+'_1.f4m'
        desc=re.compile('<meta name="description" content="(.+?)"/>').findall(link)
        thumb=re.compile("<link rel='image_src' href='([^']+?)' />").findall(link)[0]
        print
        infoL={ "Title": mname, "Plot": desc[0]}
        from resources.universal import F4mProxy
        player=F4mProxy.f4mProxyHelper()
        proxy=None
        use_proxy_for_chunks=False
        player.playF4mLink(vlink, mname, proxy, use_proxy_for_chunks,'',thumb)
        if selfAddon.getSetting("whistory") == "true":
            from resources.universal import watchhistory
            wh = watchhistory.WatchHistory(addon_id)
            wh.add_item(mname+' '+'[COLOR green]SkySports[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infoL, img=thumb, fanart='', is_folder=False)


