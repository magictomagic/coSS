'''
Author: magictomagic
Date: 2020-11-17 08:07:55
LastEditors: magictomagic
LastEditTime: 2020-11-17 10:22:04
Description: file content
'''
import win32clipboard as w
import win32con
import keyboard
import TaS_v1_3

def getText():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return(d).decode('GBK')

def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, aString)
    w.CloseClipboard()

def superAddtion(en, ch):
    with open('add_to.txt', 'a+') as f:
        f.write(en + '\t\t\t\t' + ch + '\n')


keyboard.add_hotkey('ctrl+shift+a', lambda: superAddtion(getText(), TaS_v1_3.translate(getText())))
keyboard.wait('esc')