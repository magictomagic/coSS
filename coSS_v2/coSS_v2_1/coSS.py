'''
Author: magictomagic
Date: 2020-11-17 08:07:55
LastEditors: magictomagic
LastEditTime: 2020-11-18 11:58:39
Description: file content
'''
import win32clipboard as w
import win32con
import keyboard
import transEntoCh
import win32com.client
import pythoncom
import pyperclip
import pyautogui
import time
# import getS
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
    # pythoncom.CoInitialize()
    # shell = win32com.client.Dispatch("WScript.Shell")
    # shell.SendKeys(shotcut)
    # wait() 阻塞，直到上一条语句执行完
    # keyboard.wait("ctrl+c")
    # time.sleep(3)
    # print(getText())
    # pythoncom.CoUninitialize()
    # print(getText())

    print("asd")
    while keyboard.is_pressed("alt") or keyboard.is_pressed("l"):
        time.sleep(0.1)
        pass
    print("asd end")
    
    win32api.keybd_event(17,0,0,0)  #ctrl键位码是17
    win32api.keybd_event(67,0,0,0)  #v键位码是86
    win32api.keybd_event(67,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
    # time.sleep(2)
    # getS.copy()
    time.sleep(0.1)
    print(getText())

# TODO:
# if os does not has clipboard list, save clipboard before copy 
# set ctrl+c after add ctrl+shift+a

keyboard.add_hotkey('ctrl+alt+l', copyGfCSA, ["^c"], False)
keyboard.wait('esc')