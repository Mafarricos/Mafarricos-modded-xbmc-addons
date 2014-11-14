import urllib,re,sys,os
import xbmc,xbmcgui,xbmcaddon,xbmcplugin,threading,time
import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
MainUrl='http://www.imdb.com'

def SearchArtist(encode,murl):
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryArtist')
        if 'Artist' in murl:
            surl='http://www.imdb.com/find?ref_=nv_sr_fn&q='+encode+'&s=nm'
        else:
            keyb = xbmc.Keyboard('', 'Search For Artist by Name')
            keyb.doModal()
            if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
                surl='http://www.imdb.com/find?ref_=nv_sr_fn&q='+encode+'&s=nm'
                if not os.path.exists(SeaFile):
                    open(SeaFile,'w').write('search="%s",'%encode)
                else:
                    open(SeaFile,'a').write('search="%s",'%encode)
        html = main.OPENURL(surl)
        link=main.unescapes(html).decode('ascii', 'ignore')
        match = re.findall('(?sim)<img src="([^"]+)" /></a> </td> <td class="result_text"> <a href="([^"]+)" >([^<]+)</a> <small>\((.+?), <a href=".+?" >([^<]+)</a>([^<]+)\)</small>',link.replace('  ',''))
        for thumb,url,name,job,star,year in match:
            thumbs=thumb.split('_V1')[0]
            if 'http' not in job:
                main.addDir(name+' [COLOR orange]'+job+'[/COLOR] [COLOR aqua]'+star+'[/COLOR][COLOR yellow]'+year+'[/COLOR]',MainUrl+url,488,thumbs+'_V1_SY317_CR124,0,214,317_AL_.jpg')
        
                
                        
def ListArtist(murl,thumb):
        html = main.OPENURL(murl)
        link=main.unescapes(html).decode('ascii', 'ignore')
        match = re.findall('(?sim)<a href=".+?">([^<]+)</a></b([^<]+)<br/>(.+?)<.+?<span class="year_column"> ([^<]+)</span>',link.replace('  ',''))
        for film,type,fname,year in match:
            type=type.replace('>','')
            fname = re.sub('<a href=".+?"','',fname)
            fname=fname.replace('>','')
            if type == '':
                type='(Movie)'
            if 'TV Series' in type:
                main.addDir(film+' [COLOR yellow]'+type+'[/COLOR] [COLOR aqua]'+fname+'[/COLOR][COLOR yellow]'+year+'[/COLOR]','TVx',20,thumb)
            else:
                main.addDir(film+' ('+year+') [COLOR yellow]'+type+'[/COLOR] [COLOR aqua]'+fname+'[/COLOR]','Movies',20,thumb)
    
