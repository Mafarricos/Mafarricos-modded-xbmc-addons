pythonOK = False
xbmcOK = False
importsOK = True
msg = 'Imports Doctor'
fixmsg = ''
fixmsg2 = ''
file = False
fileurl = False
try:
    import xbmc,xbmcgui,xbmcaddon,xbmcplugin
    xbmc.executebuiltin("ActivateWindow(busydialog)")
    xbmcOK = True
except Exception as e:
    if not msg:
        msg = 'XBMC modules couldn\'t be loaded'
    fixmsg = 're-install (latest stable) XBMC'
    fixmsg2 = str(e)
try:
    import urllib,urllib2,re,string,cookielib,sys,os,threading,time
    import zipfile
    import shutil
    pythonOK = True
except Exception as e:
    msg = 'modules from Python Standard Library couldn\'t be loaded'
    fixmsg = 're-install (latest stable) XBMC'
    fixmsg2 = str(e)
    
def downloadFile(url,dest):
    try:
        urllib.urlretrieve(url,dest)
        return True
    except Exception, e:
        dialog = xbmcgui.Dialog()
        dialog.ok("[B][COLOR=FF67cc33]Mash Up FIX[/COLOR]", "Report the error below at [COLOR=FF67cc33]mashupxbmc.com[/COLOR]", str(e), "We will try our best to help you")
        return False
            
def installModule(path):
    try:
        addonspath = xbmc.translatePath('special://home/addons/')
        xbmc.executebuiltin("XBMC.Extract(%s,%s)"%(path,addonspath))
        return True
    except Exception as e:
        print str(e)
        return False
    
def additionalFixes(msg):
    if 'UrlResolver' in msg:
        url = 'https://raw.github.com/mash2k3/MashUpFixes/master/FIXES/realdebrid.py'
        path = xbmc.translatePath('special://home/addons/script.module.urlresolver/lib/urlresolver/plugins/realdebrid.py')
        downloadFile(url,path)
        
def fixModule(name,fileurl):
    global importsOK
    importsOK = False
    file = os.path.basename(fileurl)
    modulepath = xbmc.translatePath(os.path.join('special://home/addons/packages',file))
    if downloadFile(fileurl,modulepath):
        msg2 = "("+file.replace(".zip","")+")"
        if installModule(modulepath):
            msg = "Successfully Installed " + name + " Module!"
            additionalFixes(msg)
        else:
            msg = "Install of " + name + " Failed!"
        dialog = xbmcgui.Dialog()
        ok=dialog.ok("Imports Doctor",msg,'',msg2)
    else:
        dialog = xbmcgui.Dialog()
        ok=dialog.ok("Imports Doctor","Install of " + name + " Failed!")
        
def getFileUrl(module,url = False):
    if not url:
        url = 'http://ftp.heanet.ie/mirrors/xbmc/addons/frodo/'+module+'/'
    html = urllib2.urlopen(url).read()
    match = re.findall('(?sim)"('+module+'[^"]+\.zip)"',html)
    if match:
        return url + match[-1]
    return

def doctor():
    if pythonOK and xbmcOK:
        try:
            import xml.etree.ElementTree
        except Exception as e:
            module = 'script.module.elementtree'
            prettyName = 'ElementTree'
            fileurl = getFileUrl(module)
            fixModule(prettyName,fileurl)
        try:
            import urlresolver
        except Exception as e:
            module = 'script.module.urlresolver'
            prettyName = 'UrlResolver'
            fileurl = getFileUrl(module)
            fixModule(prettyName,fileurl)
        try:
            import metahandler
        except Exception as e:
            module = 'script.module.metahandler'
            prettyName = 'MetaHandler'
            fileurl = getFileUrl(module)
            fixModule(prettyName,fileurl)
        try:
            from t0mm0.common.net import Net
            from t0mm0.common.addon import Addon
        except Exception as e:
            module = 'script.module.t0mm0.common'
            prettyName = 't0mm0.common'
            fileurl = getFileUrl(module)
            fixModule(prettyName,fileurl)
    
    xbmc.executebuiltin("Dialog.Close(busydialog)")        
    # if not importsOK:
    #     dialog = xbmcgui.Dialog()
    #     dialog.ok('Imports Doctor', 'Probably you\'ll need to delete Addons15.db manually','from XBMC/userdata/Databases path','to force XBMC to recognize installed modules')
          
    if pythonOK and xbmcOK and importsOK:
        dialog = xbmcgui.Dialog()
        ok=dialog.ok("Imports Doctor","No Problems with Imports Detected")
    elif importsOK: 
        dialog = xbmcgui.Dialog()
        ok=dialog.ok(msg,fixmsg,'',fixmsg2)

if __name__ == "__main__": doctor()
else: xbmc.executebuiltin("Dialog.Close(busydialog)")
