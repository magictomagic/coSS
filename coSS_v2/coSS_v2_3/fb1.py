'''
Author: magictomagic
Date: 2020-11-24 15:25:28
LastEditors: magictomagic
LastEditTime: 2020-11-24 15:35:56
Description: file content
'''
import win10toastSound

# NIIF_NOSOUND.Shell_NotifyIcon
win10toastSound.ToastNotifier().show_toast("success", "make usa great again", icon_path="asd.ico", duration=1, threaded=True)
