'''
Author: magictomagic
Date: 2020-11-18 12:48:50
LastEditors: magictomagic
LastEditTime: 2020-11-18 12:52:47
Description: file content
'''
import win32clipboard as w
import keyboard
import transEntoCh
import time
import win32api
import win32con

def getText():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    # TODO: judge if not text
    w.CloseClipboard()
    return(d).decode('GBK')

def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, aString)
    w.CloseClipboard()

def superAddtion(en, ch):
    with open('add_to.md', 'a+') as f:
        f.write('| ' + en + ' | ' + ch + ' |\n')
    # TODO: judge if have written and display result


def copyGfCSA(shotcut):
    # TODO: save clipboard content first
    while keyboard.is_pressed("alt") or keyboard.is_pressed("l"):
        time.sleep(0.1)
    win32api.keybd_event(17,0,0,0)  #ctrl
    win32api.keybd_event(67,0,0,0)  #c
    win32api.keybd_event(67,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.1)
    superAddtion(getText().strip(), transEntoCh.translate(getText().strip()))
    # print(getText())

# TODO:
# if os does not has clipboard list, save clipboard before copy 
# set ctrl+c after add ctrl+shift+a

keyboard.add_hotkey('ctrl+alt+l', copyGfCSA, ["^c"], False)
keyboard.wait('esc')