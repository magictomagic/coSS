'''
Author: magictomagic
Date: 2020-11-22 23:37:12
LastEditors: magictomagic
LastEditTime: 2020-11-23 00:04:25
Description: file content
'''
import win10toast

# NIIF_NOSOUND.Shell_NotifyIcon
win10toast.ToastNotifier().show_toast("success", "make usa great again",
                             icon_path="asd.ico", duration=1, threaded=True)
