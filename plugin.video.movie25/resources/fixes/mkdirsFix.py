import xbmc, xbmcgui, xbmcaddon, xbmcplugin,os
import urllib

def DownloaderClass2(url,dest):
        try:
            urllib.urlretrieve(url,dest)
        except Exception, e:
            dialog = xbmcgui.Dialog()
            dialog.ok("[B][COLOR=FF67cc33]Mash Up FIX[/COLOR]", "Report the error below at [COLOR=FF67cc33]MASHUPXBMC.COM[/COLOR]", str(e), "We will try our best to help you")    


try:
    dialog = xbmcgui.Dialog()
    ret = dialog.yesno('[B][COLOR=FF67cc33]Mash Up FIX[/COLOR][/B]', 'This will Replace Metahandler scripts.','Would you like to Replace now?','','No', 'Yes')
    if ret:
        url = 'https://raw.github.com/mash2k3/MashUpFixes/master/FIXES/metahandlers.py'
        print "#############  Downloading from "+ url+"  #####################"
        path = xbmc.translatePath(os.path.join('special://home/addons/script.module.metahandler/lib/','metahandler'))
        lib=os.path.join(path, 'metahandlers.py')
        DownloaderClass2(url,lib)

        url = 'https://raw.github.com/mash2k3/MashUpFixes/master/FIXES/metacontainers.py'
        print "#############  Downloading from "+ url+"  #####################"
        path = xbmc.translatePath(os.path.join('special://home/addons/script.module.metahandler/lib/','metahandler'))
        lib=os.path.join(path, 'metacontainers.py')
        DownloaderClass2(url,lib)

        dialog = xbmcgui.Dialog()
        dialog.ok("[B][COLOR=FF67cc33]Mash Up FIX[/COLOR]", "Thats It All Done", "[COLOR blue]Now Metahandler should be Fixed[/COLOR]")


except:
    dialog = xbmcgui.Dialog()
    ok=dialog.ok('[B][COLOR=FF67cc33]Mash Up FIX[/COLOR][/B]','Failed To Fix Metahandler mkdirs error','Please report to [COLOR=FF67cc33]MASHUPXBMC.COM[/COLOR].')
    pass
