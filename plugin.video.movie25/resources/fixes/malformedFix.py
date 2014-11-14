import xbmc, xbmcgui, xbmcaddon, xbmcplugin,os
from t0mm0.common.addon import Addon


addon_id = 'script.module.metahandler'
addon = Addon(addon_id)
datapath = addon.get_profile()
videodb = os.path.join(datapath,'meta_cache/')
try:
    if os.path.exists(videodb):
        dialog = xbmcgui.Dialog()
        ret = dialog.yesno('[B][COLOR=FF67cc33]Mash Up FIX[/COLOR][/B]', 'This will delete Metadata datadase.','Would you like to delete now?','','No', 'Yes')
        if ret:
            cachefile=os.path.join(videodb,'video_cache.db')
            if os.path.exists(cachefile):
                os.remove(cachefile)
                dialog.ok("[B][COLOR=FF67cc33]Mash Up FIX[/COLOR][/B]", "Thats It All Done", "Please reboot XBMC!(required)")
            else:
                ok=dialog.ok('[B][COLOR=FF67cc33]Mash Up FIX[/COLOR][/B]','Failed To Fix Database Malformed error','Please report to [COLOR=FF67cc33]MASHUPXBMC.COM[/COLOR].')

        
except:
    dialog = xbmcgui.Dialog()
    ok=dialog.ok('[B][COLOR=FF67cc33]Mash Up FIX[/COLOR][/B]','Failed To Fix Database Malformed error','Please report to [COLOR=FF67cc33]MASHUPXBMC.COM[/COLOR].')
    pass
