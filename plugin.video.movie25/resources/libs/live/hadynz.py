import urllib,urllib2,re,cookielib,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main
from urllib2 import (urlopen, Request)
from BeautifulSoup import BeautifulSoup

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = main.art
from resources.universal import watchhistory
    
wh = watchhistory.WatchHistory('plugin.video.movie25')

def get(url):
    """Performs a GET request for the given url and returns the response"""
    try:
        conn = urlopen(url)
        resp = conn.read()
        conn.close()
        return resp
    except IOError:
        pass
    return ""

def _html(url):
    """Downloads the resource at the given url and parses via BeautifulSoup"""
    return BeautifulSoup(main.OPENURL(url), convertEntities=BeautifulSoup.HTML_ENTITIES)

def _parse_channels_from_html_dom(html):
    items = []
    items.append({
            'title': '2M',
            'thumbnail': 'http://www.teledunet.com/logo/2M.jpg',
            'path': '2m'})
    items.append({
            'title': 'Abu Dhabi Drama',
            'thumbnail': 'http://www.teledunet.com/logo/Abu%20Dhabi%20Drama.jpg',
            'path': 'abu_dhabi_drama'})
    items.append({
            'title': 'Abu Dhabi Sports 1',
            'thumbnail': 'http://www.teledunet.com/logo/Abu%20Dhabi%20Sports%201.jpg',
            'path': 'abu_dhabi_sports_1'})
    items.append({
            'title': 'Abu Dhabi',
            'thumbnail': 'http://www.teledunet.com/logo/Abu%20Dhabi.jpg',
            'path': 'abu_dhabi'})
    items.append({
            'title': 'Aghanina',
            'thumbnail': 'http://www.teledunet.com/logo/Aghanina.jpg',
            'path': 'aghanina'})
    items.append({
            'title': 'Ajyal',
            'thumbnail': 'http://www.teledunet.com/logo/Ajyal.jpg',
            'path': 'ajyal'})
    items.append({
            'title': 'Al Aoula Maroc',
            'thumbnail': 'http://www.teledunet.com/logo/Al%20Aoula%20Maroc.jpg',
            'path': 'al_aoula_maroc'})
    items.append({
            'title': 'Al Haneen Music',
            'thumbnail': 'http://www.teledunet.com/logo/Al%20Haneen%20Music.jpg',
            'path': 'al_haneen_music'})
    items.append({
            'title': 'Al Ikhbaria',
            'thumbnail': 'http://www.teledunet.com/logo/Al%20Ikhbaria.jpg',
            'path': 'al_ikhbaria'})
    items.append({
            'title': 'Al Janoubiya',
            'thumbnail': 'http://www.teledunet.com/logo/Al%20Janoubiya.jpg',
            'path': 'al_janoubiya'})
    items.append({
            'title': 'Al Maghribia',
            'thumbnail': 'http://www.teledunet.com/logo/Al%20Maghribia.jpg',
            'path': 'al_maghribia'})
    items.append({
            'title': 'Al Majd',
            'thumbnail': 'http://www.teledunet.com/logo/Al%20Majd.jpg',
            'path': 'al_majd'})
    items.append({
            'title': 'Al Manar',
            'thumbnail': 'http://www.teledunet.com/logo/Al%20Manar.jpg',
            'path': 'al_manar'})
    items.append({
            'title': 'Al Masriyah',
            'thumbnail': 'http://www.teledunet.com/logo/Al%20Masriyah.jpg',
            'path': 'al_masriyah'})
    items.append({
            'title': 'Al Moustakilla',
            'thumbnail': 'http://www.teledunet.com/logo/Al%20Moustakilla.jpg',
            'path': 'al_moustakilla'})
    items.append({
            'title': 'Al Mutawasit',
            'thumbnail': 'http://www.teledunet.com/logo/Al%20Mutawasit.jpg',
            'path': 'al_mutawasit'})
    items.append({
            'title': 'Al Rafidain',
            'thumbnail': 'http://www.teledunet.com/logo/Al%20Rafidain.jpg',
            'path': 'al_rafidain'})
    items.append({
            'title': 'Al Rahma',
            'thumbnail': 'http://www.teledunet.com/logo/Al%20Rahma.jpg',
            'path': 'al_rahma'})
    items.append({
            'title': 'Al Sharqiya',
            'thumbnail': 'http://www.teledunet.com/logo/Al%20Sharqiya.jpg',
            'path': 'al_sharqiya'})
    items.append({
            'title': 'Al Sumaria',
            'thumbnail': 'http://www.teledunet.com/logo/Al%20Sumaria.jpg',
            'path': 'al_sumaria'})
    items.append({
            'title': 'Al Thaniya',
            'thumbnail': 'http://www.teledunet.com/logo/Al%20Thaniya.jpg',
            'path': 'al_thaniya'})
    items.append({
            'title': 'Al Tunisia',
            'thumbnail': 'http://www.teledunet.com/logo/Al%20Tunisia.jpg',
            'path': 'al_tunisia'})
    items.append({
            'title': 'Al mayaden',
            'thumbnail': 'http://www.teledunet.com/logo/Al%20mayaden.jpg',
            'path': 'al_mayaden'})
    items.append({
            'title': 'Al nahar',
            'thumbnail': 'http://www.teledunet.com/logo/Al%20nahar.jpg',
            'path': 'al_nahar'})
    items.append({
            'title': 'Al-Hurria',
            'thumbnail': 'http://www.teledunet.com/logo/Al-Hurria.jpg',
            'path': 'al_hurria'})
    items.append({
            'title': 'Al-Nahar Drama',
            'thumbnail': 'http://www.teledunet.com/logo/Al-Nahar%20Drama.jpg',
            'path': 'al_nahar_drama'})
    items.append({
            'title': 'Al-Resalah',
            'thumbnail': 'http://www.teledunet.com/logo/Al-Resalah.jpg',
            'path': 'al_resalah'})
    items.append({
            'title': 'Al-hurra Iraq',
            'thumbnail': 'http://www.teledunet.com/logo/Al-hurra%20Iraq.jpg',
            'path': 'al_hurra_iraq'})
    items.append({
            'title': 'AlGeria',
            'thumbnail': 'http://www.teledunet.com/logo/AlGeria.jpg',
            'path': 'algeria'})
    items.append({
            'title': 'Alan',
            'thumbnail': 'http://www.teledunet.com/logo/Alan.jpg',
            'path': 'alan'})
    items.append({
            'title': 'Alarabiya',
            'thumbnail': 'http://www.teledunet.com/logo/Alarabiya.jpg',
            'path': 'alarabiya'})
    items.append({
            'title': 'Algeria 3',
            'thumbnail': 'http://www.teledunet.com/logo/Algeria%203.jpg',
            'path': 'algeria_3'})
    items.append({
            'title': 'Alhayat 1',
            'thumbnail': 'http://www.teledunet.com/logo/Alhayat%201.jpg',
            'path': 'alhayat_1'})
    items.append({
            'title': 'Alhayat 2',
            'thumbnail': 'http://www.teledunet.com/logo/Alhayat%202.jpg',
            'path': 'alhayet_2'})
    items.append({
            'title': 'Alhayat Cinema',
            'thumbnail': 'http://www.teledunet.com/logo/Alhayat%20Cinema.jpg',
            'path': 'alhayat_cinema'})
    items.append({
            'title': 'Alhayat-Series',
            'thumbnail': 'http://www.teledunet.com/logo/Alhayat-Series.jpg',
            'path': 'alhayat_series'})
    items.append({
            'title': 'Aliraqiya',
            'thumbnail': 'http://www.teledunet.com/logo/Aliraqiya.jpg',
            'path': 'aliraqiya'})
    items.append({
            'title': 'Aljadeed',
            'thumbnail': 'http://www.teledunet.com/logo/Aljadeed.jpg',
            'path': 'aljadeed'})
    items.append({
            'title': 'Aljazeera Children',
            'thumbnail': 'http://www.teledunet.com/logo/Aljazeera%20Children.jpg',
            'path': 'aljazeera_children'})
    items.append({
            'title': 'Aljazeera Doc',
            'thumbnail': 'http://www.teledunet.com/logo/Aljazeera%20Doc.jpg',
            'path': 'aljazeera_doc'})
    items.append({
            'title': 'Aljazeera',
            'thumbnail': 'http://www.teledunet.com/logo/Aljazeera.jpg',
            'path': 'aljazeera'})
    items.append({
            'title': 'Alqudis',
            'thumbnail': 'http://www.teledunet.com/logo/Alqudis.jpg',
            'path': 'alqudis'})
    items.append({
            'title': 'Alrashid',
            'thumbnail': 'http://www.teledunet.com/logo/Alrashid.jpg',
            'path': 'alrashid'})
    items.append({
            'title': 'Alriadia Sport',
            'thumbnail': 'http://www.teledunet.com/logo/Alriadia%20Sport.jpg',
            'path': 'alriadia_sport'})
    items.append({
            'title': 'Arabica Music',
            'thumbnail': 'http://www.teledunet.com/logo/Arabica%20Music.jpg',
            'path': 'arabica_music'})
    items.append({
            'title': 'Arrabia',
            'thumbnail': 'http://www.teledunet.com/logo/Arrabia.jpg',
            'path': 'arrabia'})
    items.append({
            'title': 'Assadissa',
            'thumbnail': 'http://www.teledunet.com/logo/Assadissa.jpg',
            'path': 'assadissa'})
    items.append({
            'title': 'BBC Arabic',
            'thumbnail': 'http://www.teledunet.com/logo/BBC%20Arabic.jpg',
            'path': 'bbc_arabic'})
    items.append({
            'title': 'Baghdadia',
            'thumbnail': 'http://www.teledunet.com/logo/Baghdadia.jpg',
            'path': 'baghdadia'})
    items.append({
            'title': 'Bahrain',
            'thumbnail': 'http://www.teledunet.com/logo/Bahrain.jpg',
            'path': 'bahrain'})
    items.append({
            'title': 'Baraem',
            'thumbnail': 'http://www.teledunet.com/logo/Baraem.jpg',
            'path': 'baraem'})
    items.append({
            'title': 'Blue Nile',
            'thumbnail': 'http://www.teledunet.com/logo/Blue%20Nile.jpg',
            'path': 'blue_nile'})
    items.append({
            'title': 'CBC 2',
            'thumbnail': 'http://www.teledunet.com/logo/CBC%202.jpg',
            'path': 'cbc_2'})
    items.append({
            'title': 'CBC Drama',
            'thumbnail': 'http://www.teledunet.com/logo/CBC%20Drama.jpg',
            'path': 'cbc_drama'})
    items.append({
            'title': 'CBC Extra',
            'thumbnail': 'http://www.teledunet.com/logo/CBC%20Extra.jpg',
            'path': 'cbc_extra'})
    items.append({
            'title': 'CBC Sofra',
            'thumbnail': 'http://www.teledunet.com/logo/CBC%20Sofra.jpg',
            'path': 'cbc_sofra'})
    items.append({
            'title': 'CBC',
            'thumbnail': 'http://www.teledunet.com/logo/CBC.jpg',
            'path': 'cbc'})
    items.append({
            'title': 'CCTV Arabic',
            'thumbnail': 'http://www.teledunet.com/logo/CCTV%20Arabic.jpg',
            'path': 'cctv_arabic'})
    items.append({
            'title': 'Cairo Cinema',
            'thumbnail': 'http://www.teledunet.com/logo/Cairo%20Cinema.jpg',
            'path': 'cairo_cinema'})
    items.append({
            'title': 'Cairo Drama',
            'thumbnail': 'http://www.teledunet.com/logo/Cairo%20Drama.jpg',
            'path': 'cairo_drama'})
    items.append({
            'title': 'Cima',
            'thumbnail': 'http://www.teledunet.com/logo/Cima.jpg',
            'path': 'cima'})
    items.append({
            'title': 'Coran',
            'thumbnail': 'http://www.teledunet.com/logo/Coran.jpg',
            'path': 'coran'})
    items.append({
            'title': 'Djibouti',
            'thumbnail': 'http://www.teledunet.com/logo/Djibouti.jpg',
            'path': 'djibouti'})
    items.append({
            'title': 'Dream 1',
            'thumbnail': 'http://www.teledunet.com/logo/Dream%201.jpg',
            'path': 'dream_1'})
    items.append({
            'title': 'Dubai One',
            'thumbnail': 'http://www.teledunet.com/logo/Dubai%20One.jpg',
            'path': 'dubai_one'})
    items.append({
            'title': 'Dubai Sport 1',
            'thumbnail': 'http://www.teledunet.com/logo/Dubai%20Sport%201.jpg',
            'path': 'dubai_sport_1'})
    items.append({
            'title': 'Dubai Sport 2',
            'thumbnail': 'http://www.teledunet.com/logo/Dubai%20Sport%202.jpg',
            'path': 'dubai_sport_2'})
    items.append({
            'title': 'Dubai',
            'thumbnail': 'http://www.teledunet.com/logo/Dubai.jpg',
            'path': 'dubai'})
    items.append({
            'title': 'Dzair 24',
            'thumbnail': 'http://www.teledunet.com/logo/Dzair%2024.jpg',
            'path': 'dzair_24'})
    items.append({
            'title': 'EL DJAZAIRIA',
            'thumbnail': 'http://www.teledunet.com/logo/EL%20DJAZAIRIA.jpg',
            'path': 'el_djazairia'})
    items.append({
            'title': 'ETV Ethiopia',
            'thumbnail': 'http://www.teledunet.com/logo/ETV%20Ethiopia.jpg',
            'path': 'etv_ethiopia'})
    items.append({
            'title': 'Echorouk Tv',
            'thumbnail': 'http://www.teledunet.com/logo/Echorouk%20Tv.jpg',
            'path': 'echorouk_tv'})
    items.append({
            'title': 'Eriteria TV',
            'thumbnail': 'http://www.teledunet.com/logo/Eriteria%20TV.jpg',
            'path': 'eriteria_tv'})
    items.append({
            'title': 'Fatafeat',
            'thumbnail': 'http://www.teledunet.com/logo/Fatafeat.jpg',
            'path': 'fatafeat'})
    items.append({
            'title': 'Fox Movies',
            'thumbnail': 'http://www.teledunet.com/logo/Fox%20Movies.jpg',
            'path': 'fox_movies'})
    items.append({
            'title': 'Fox',
            'thumbnail': 'http://www.teledunet.com/logo/Fox.jpg',
            'path': 'fox'})
    items.append({
            'title': 'France24 Arabic',
            'thumbnail': 'http://www.teledunet.com/logo/France24%20Arabic.jpg',
            'path': 'france24_arabic'})
    items.append({
            'title': 'Funoon',
            'thumbnail': 'http://www.teledunet.com/logo/Funoon.jpg',
            'path': 'funoon'})
    items.append({
            'title': 'Hanibal',
            'thumbnail': 'http://www.teledunet.com/logo/Hanibal.jpg',
            'path': 'hanibal'})
    items.append({
            'title': 'Heya',
            'thumbnail': 'http://www.teledunet.com/logo/Heya.jpg',
            'path': 'heya'})
    items.append({
            'title': 'Iqra',
            'thumbnail': 'http://www.teledunet.com/logo/Iqra.jpg',
            'path': 'iqra'})
    items.append({
            'title': 'Jordan',
            'thumbnail': 'http://www.teledunet.com/logo/Jordan.jpg',
            'path': 'jordan'})
    items.append({
            'title': 'KSA 1',
            'thumbnail': 'http://www.teledunet.com/logo/KSA%201.jpg',
            'path': 'ksa_1'})
    items.append({
            'title': 'Kalsan Tv',
            'thumbnail': 'http://www.teledunet.com/logo/Kalsan%20Tv.jpg',
            'path': 'kalsan_tv'})
    items.append({
            'title': 'Kuwait',
            'thumbnail': 'http://www.teledunet.com/logo/Kuwait.jpg',
            'path': 'kuwait'})
    items.append({
            'title': 'LBC',
            'thumbnail': 'http://www.teledunet.com/logo/LBC.jpg',
            'path': 'lbc'})
    items.append({
            'title': 'LLBN',
            'thumbnail': 'http://www.teledunet.com/logo/LLBN.jpg',
            'path': 'llbn'})
    items.append({
            'title': 'Lbc Europe',
            'thumbnail': 'http://www.teledunet.com/logo/Lbc%20Europe.jpg',
            'path': 'lbc_europe'})
    items.append({
            'title': 'Libya Alwatania 1',
            'thumbnail': 'http://www.teledunet.com/logo/Libya%20Alwatania%201.jpg',
            'path': 'libya_alwatania_1'})
    items.append({
            'title': 'Libya alahrar',
            'thumbnail': 'http://www.teledunet.com/logo/Libya%20alahrar.jpg',
            'path': 'libya_alahrar'})
    items.append({
            'title': 'Libya',
            'thumbnail': 'http://www.teledunet.com/logo/Libya.jpg',
            'path': 'libya'})
    items.append({
            'title': 'M6',
            'thumbnail': 'http://www.teledunet.com/logo/M6.jpg',
            'path': 'm6'})
    items.append({
            'title': 'MBC 1',
            'thumbnail': 'http://www.teledunet.com/logo/MBC%201.jpg',
            'path': 'mbc_1'})
    items.append({
            'title': 'MBC 2',
            'thumbnail': 'http://www.teledunet.com/logo/MBC%202.jpg',
            'path': 'mbc_2'})
    items.append({
            'title': 'MBC 3',
            'thumbnail': 'http://www.teledunet.com/logo/MBC%203.jpg',
            'path': 'mbc_3'})
    items.append({
            'title': 'MBC 4',
            'thumbnail': 'http://www.teledunet.com/logo/MBC%204.jpg',
            'path': 'mbc_4'})
    items.append({
            'title': 'MBC Action',
            'thumbnail': 'http://www.teledunet.com/logo/MBC%20Action.jpg',
            'path': 'mbc_action'})
    items.append({
            'title': 'MBC Bollywood',
            'thumbnail': 'http://www.teledunet.com/logo/MBC%20Bollywood.jpg',
            'path': 'mbc_bollywood'})
    items.append({
            'title': 'MBC Drama',
            'thumbnail': 'http://www.teledunet.com/logo/MBC%20Drama.jpg',
            'path': 'mbc_drama'})
    items.append({
            'title': 'MBC Masr',
            'thumbnail': 'http://www.teledunet.com/logo/MBC%20Masr.jpg',
            'path': 'mbc_masr'})
    items.append({
            'title': 'MBC Max',
            'thumbnail': 'http://www.teledunet.com/logo/MBC%20Max.jpg',
            'path': 'mbc_max'})
    items.append({
            'title': 'MBC Persia',
            'thumbnail': 'http://www.teledunet.com/logo/MBC%20Persia.jpg',
            'path': 'mbc_persia'})
    items.append({
            'title': 'MTV',
            'thumbnail': 'http://www.teledunet.com/logo/MTV.jpg',
            'path': 'mtv'})
    items.append({
            'title': 'Maghreb 1',
            'thumbnail': 'http://www.teledunet.com/logo/Maghreb%201.jpg',
            'path': 'maghreb_1'})
    items.append({
            'title': 'Masrawi Aflam',
            'thumbnail': 'http://www.teledunet.com/logo/Masrawi%20Aflam.jpg',
            'path': 'masrawi_aflam'})
    items.append({
            'title': 'Mauritanie',
            'thumbnail': 'http://www.teledunet.com/logo/Mauritanie.jpg',
            'path': 'mauritanie'})
    items.append({
            'title': 'Mazeka zoom',
            'thumbnail': 'http://www.teledunet.com/logo/Mazeka%20zoom.jpg',
            'path': 'mazeka_zoom'})
    items.append({
            'title': 'Mazzika',
            'thumbnail': 'http://www.teledunet.com/logo/Mazzika.jpg',
            'path': 'mazzika'})
    items.append({
            'title': 'Medi 1 Sat',
            'thumbnail': 'http://www.teledunet.com/logo/Medi%201%20Sat.jpg',
            'path': 'medi_1_sat'})
    items.append({
            'title': 'Mehwar',
            'thumbnail': 'http://www.teledunet.com/logo/Mehwar.jpg',
            'path': 'mehwar'})
    items.append({
            'title': 'Moga Comedy',
            'thumbnail': 'http://www.teledunet.com/logo/Moga%20Comedy.jpg',
            'path': 'moga_comedy'})
    items.append({
            'title': 'NBN',
            'thumbnail': 'http://www.teledunet.com/logo/NBN.jpg',
            'path': 'nbn'})
    items.append({
            'title': 'National Geo Ad',
            'thumbnail': 'http://www.teledunet.com/logo/National%20Geo%20Ad.jpg',
            'path': 'national_geo_ad'})
    items.append({
            'title': 'Nessma',
            'thumbnail': 'http://www.teledunet.com/logo/Nessma.jpg',
            'path': 'nessma'})
    items.append({
            'title': 'Nile Cinema',
            'thumbnail': 'http://www.teledunet.com/logo/Nile%20Cinema.jpg',
            'path': 'nile_cinema'})
    items.append({
            'title': 'Nile Comedy',
            'thumbnail': 'http://www.teledunet.com/logo/Nile%20Comedy.jpg',
            'path': 'nile_comedy'})
    items.append({
            'title': 'Nile Drama 2',
            'thumbnail': 'http://www.teledunet.com/logo/Nile%20Drama%202.jpg',
            'path': 'nile_drama_2'})
    items.append({
            'title': 'Nile Drama',
            'thumbnail': 'http://www.teledunet.com/logo/Nile%20Drama.jpg',
            'path': 'nile_drama'})
    items.append({
            'title': 'Nile Family',
            'thumbnail': 'http://www.teledunet.com/logo/Nile%20Family.jpg',
            'path': 'nile_family'})
    items.append({
            'title': 'Nile Life',
            'thumbnail': 'http://www.teledunet.com/logo/Nile%20Life.jpg',
            'path': 'nile_life'})
    items.append({
            'title': 'Nile News',
            'thumbnail': 'http://www.teledunet.com/logo/Nile%20News.jpg',
            'path': 'nile_news'})
    items.append({
            'title': 'Nile Sport',
            'thumbnail': 'http://www.teledunet.com/logo/Nile%20Sport.jpg',
            'path': 'nile_sport'})
    items.append({
            'title': 'Noor Dubai',
            'thumbnail': 'http://www.teledunet.com/logo/Noor%20Dubai.jpg',
            'path': 'noor_dubai'})
    items.append({
            'title': 'Noursat',
            'thumbnail': 'http://www.teledunet.com/logo/Noursat.jpg',
            'path': 'noursat'})
    items.append({
            'title': 'OTV Lebanon',
            'thumbnail': 'http://www.teledunet.com/logo/OTV%20Lebanon.jpg',
            'path': 'otv_lebanon'})
    items.append({
            'title': 'On TV',
            'thumbnail': 'http://www.teledunet.com/logo/On%20TV.jpg',
            'path': 'on_tv'})
    items.append({
            'title': 'Oromia TV',
            'thumbnail': 'http://www.teledunet.com/logo/Oromia%20TV.jpg',
            'path': 'oromia_tv'})
    items.append({
            'title': 'Palestine',
            'thumbnail': 'http://www.teledunet.com/logo/Palestine.jpg',
            'path': 'palestine'})
    items.append({
            'title': 'Panorama Comedy',
            'thumbnail': 'http://www.teledunet.com/logo/Panorama%20Comedy.jpg',
            'path': 'panorama_comedy'})
    items.append({
            'title': 'Panorama Drama',
            'thumbnail': 'http://www.teledunet.com/logo/Panorama%20Drama.jpg',
            'path': 'panorama_drama'})
    items.append({
            'title': 'Rotana Aflam',
            'thumbnail': 'http://www.teledunet.com/logo/Rotana%20Aflam.jpg',
            'path': 'rotana_aflam'})
    items.append({
            'title': 'Rotana Classic',
            'thumbnail': 'http://www.teledunet.com/logo/Rotana%20Classic.jpg',
            'path': 'rotana_classic'})
    items.append({
            'title': 'Rotana Clip',
            'thumbnail': 'http://www.teledunet.com/logo/Rotana%20Clip.jpg',
            'path': 'rotana_clip'})
    items.append({
            'title': 'Rotana Khaligi',
            'thumbnail': 'http://www.teledunet.com/logo/Rotana%20Khaligi.jpg',
            'path': 'rotana_khaligi'})
    items.append({
            'title': 'Rotana Masriya',
            'thumbnail': 'http://www.teledunet.com/logo/Rotana%20Masriya.jpg',
            'path': 'rotana_masriya'})
    items.append({
            'title': 'Rotana Music',
            'thumbnail': 'http://www.teledunet.com/logo/Rotana%20Music.jpg',
            'path': 'rotana_music'})
    items.append({
            'title': 'Rotana cinema',
            'thumbnail': 'http://www.teledunet.com/logo/Rotana%20cinema.jpg',
            'path': 'rotana_cinema'})
    items.append({
            'title': 'Roya',
            'thumbnail': 'http://www.teledunet.com/logo/Roya.jpg',
            'path': 'roya'})
    items.append({
            'title': 'Royali Somali',
            'thumbnail': 'http://www.teledunet.com/logo/Royali%20Somali.jpg',
            'path': 'royali_somali'})
    items.append({
            'title': 'Russia Alyaum',
            'thumbnail': 'http://www.teledunet.com/logo/Russia%20Alyaum.jpg',
            'path': 'russia_alyaum'})
    items.append({
            'title': 'Sada Albalad',
            'thumbnail': 'http://www.teledunet.com/logo/Sada%20Albalad.jpg',
            'path': 'sada_albalad'})
    items.append({
            'title': 'Sama Dubai',
            'thumbnail': 'http://www.teledunet.com/logo/Sama%20Dubai.jpg',
            'path': 'sama_dubai'})
    items.append({
            'title': 'Samira Tv',
            'thumbnail': 'http://www.teledunet.com/logo/Samira%20Tv.jpg',
            'path': 'samira_tv'})
    items.append({
            'title': 'Sharjah',
            'thumbnail': 'http://www.teledunet.com/logo/Sharjah.jpg',
            'path': 'sharjah'})
    items.append({
            'title': 'Somali Channel',
            'thumbnail': 'http://www.teledunet.com/logo/Somali%20Channel.jpg',
            'path': 'somali_channel'})
    items.append({
            'title': 'Spacetoon',
            'thumbnail': 'http://www.teledunet.com/logo/Spacetoon.jpg',
            'path': 'spacetoon'})
    items.append({
            'title': 'Sudan TV',
            'thumbnail': 'http://www.teledunet.com/logo/Sudan%20TV.jpg',
            'path': 'sudan_tv'})
    items.append({
            'title': 'Syria Drama',
            'thumbnail': 'http://www.teledunet.com/logo/Syria%20Drama.jpg',
            'path': 'syria_drama'})
    items.append({
            'title': 'Syria',
            'thumbnail': 'http://www.teledunet.com/logo/Syria.jpg',
            'path': 'syria'})
    items.append({
            'title': 'TF1',
            'thumbnail': 'http://www.teledunet.com/logo/TF1.jpg',
            'path': 'tf1'})
    items.append({
            'title': 'TNN',
            'thumbnail': 'http://www.teledunet.com/logo/TNN.jpg',
            'path': 'tnn'})
    items.append({
            'title': 'Tamazigh Algeria',
            'thumbnail': 'http://www.teledunet.com/logo/Tamazigh%20Algeria.jpg',
            'path': 'tamazigh_algeria'})
    items.append({
            'title': 'Tchad',
            'thumbnail': 'http://www.teledunet.com/logo/Tchad.jpg',
            'path': 'tchad'})
    items.append({
            'title': 'Tele Liban',
            'thumbnail': 'http://www.teledunet.com/logo/Tele%20Liban.jpg',
            'path': 'tele_liban'})
    items.append({
            'title': 'Tele Sports',
            'thumbnail': 'http://www.teledunet.com/logo/Tele%20Sports.jpg',
            'path': 'tele_sports'})
    items.append({
            'title': 'Time Comedy',
            'thumbnail': 'http://www.teledunet.com/logo/Time%20Comedy.jpg',
            'path': 'time_comedy'})
    items.append({
            'title': 'Tounesna',
            'thumbnail': 'http://www.teledunet.com/logo/Tounesna.jpg',
            'path': 'tounesna'})
    items.append({
            'title': 'Toyor Al Janah',
            'thumbnail': 'http://www.teledunet.com/logo/Toyor%20Al%20Janah.jpg',
            'path': 'toyor_al_janah'})
    items.append({
            'title': 'Toyor baby',
            'thumbnail': 'http://www.teledunet.com/logo/Toyor%20baby.jpg',
            'path': 'toyor_baby'})
    items.append({
            'title': 'Tunisia national 1',
            'thumbnail': 'http://www.teledunet.com/logo/Tunisia%20national%201.jpg',
            'path': 'tunisia_national_1'})
    items.append({
            'title': 'Tunisia national 2',
            'thumbnail': 'http://www.teledunet.com/logo/Tunisia%20national%202.jpg',
            'path': 'tunisia_national_2'})
    items.append({
            'title': 'Wanasah',
            'thumbnail': 'http://www.teledunet.com/logo/Wanasah.jpg',
            'path': 'wanasah'})
    items.append({
            'title': 'Yemen',
            'thumbnail': 'http://www.teledunet.com/logo/Yemen.jpg',
            'path': 'yemen'})
    items.append({
            'title': 'Zagros',
            'thumbnail': 'http://www.teledunet.com/logo/Zagros.jpg',
            'path': 'zagros'})
    items.append({
            'title': 'Zaitouna',
            'thumbnail': 'http://www.teledunet.com/logo/Zaitouna.jpg',
            'path': 'zaitouna'})
    items.append({
            'title': 'Zee Aflam',
            'thumbnail': 'http://www.teledunet.com/logo/Zee%20Aflam.jpg',
            'path': 'zee_aflam'})
    items.append({
            'title': 'Zee Alwan',
            'thumbnail': 'http://www.teledunet.com/logo/Zee%20Alwan.jpg',
            'path': 'zee_alwan'})
    
    return items

def MAIN():
    main.GA("Live","ArabicStreams")
    items = _parse_channels_from_html_dom('http://www.teledunet.com/')
    for channels in sorted(items):
        main.addPlayL(channels['title'],channels['path'],232,channels['thumbnail'],'','','','','',secName='Arabic Streams',secIcon=art+'/arabicstream.png')

        

def _get_channel_time_player(channel_name):
    req = urllib2.Request('http://www.teledunet.com/mobile/')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    req.add_header('Referer', 'http://www.teledunet.com/')
    req.add_header('Cookie', 'PHPSESSID=a91675d1784ad263e7863aef4d79aa18')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    auth=re.findall("var aut='.?id0=(.+?)';",link)[0]
    try:rtmp_url =re.findall('value="(.+?)'+channel_name+'"',link)[0]
    except:rtmp_url = 'rtmp://178.33.241.201:1935/teledunet'
    play_path= channel_name
    #auth=auth.replace('.','').split('+')[0].replace('E','0')
    swfUrl='http://www.teledunet.com/mobile//player.swf?id0='+auth+'&channel='+channel_name+' live=true timeout=15 conn=N:1 flashVer=WIN12,0,0,77'
    return rtmp_url+' playpath='+play_path+' swfUrl='+swfUrl+' pageUrl=http://www.teledunet.com/mobile/'



        
def LINK(mname,url,thumb):
        main.GA("ArabicStreams","Watched")
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Opening Stream,3000)")
        stream_url = _get_channel_time_player(url)
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        
        listitem = xbmcgui.ListItem(thumbnailImage=thumb)
        infoL={'Title': mname, 'Genre': 'Live'} 
        from resources.universal import playbackengine
        player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type='movie', title=mname,season='', episode='', year='',img=thumb,infolabels=infoL, watchedCallbackwithParams='',imdb_id='')

        #WatchHistory
        if selfAddon.getSetting("whistory") == "true":
            wh.add_item(mname+' '+'[COLOR green]ArabicStreams[/COLOR]', sys.argv[0]+sys.argv[2], infolabels='', img=thumb, fanart='', is_folder=False)
        return ok


