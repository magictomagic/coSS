'''
Author: magictomagic
Date: 2020-11-18 13:33:55
LastEditors: magictomagic
LastEditTime: 2020-11-19 15:59:10
Description: file content
'''
import win32clipboard as w
import win32con
from ctypes import windll

def getText():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT) # win32con.CF_TEXT
    # TODO: judge if not text
    w.EmptyClipboard()
    w.CloseClipboard()
    return(d).decode('GBK')

# def setText():
#     w.OpenClipboard()
#     w.EmptyClipboard()
#     # w.SetClipboardData(win32con.CF_TEXT, aString)
#     w.CloseClipboard()

# # windll.user32.EmptyClipboard()
# # windll.user32.CloseClipboard()
# # setText()
# print(getText())
# windll.user32.EmptyClipboard()
# windll.user32.CloseClipboard()


