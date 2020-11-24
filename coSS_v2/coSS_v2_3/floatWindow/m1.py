'''
Author: magictomagic
Date: 2020-11-22 23:37:12
LastEditors: magictomagic
LastEditTime: 2020-11-23 01:13:13
Description: file content
'''
import win10toastSound

# NIIF_NOSOUND.Shell_NotifyIcon
win10toastSound.ToastNotifier().show_toast("success", "make usa great again",
                             icon_path="asd.ico", duration=1, threaded=True)
