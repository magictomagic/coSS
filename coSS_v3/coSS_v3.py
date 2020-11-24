'''
Author: magictomagic
Date: 2020-11-19 21:34:32
LastEditors: magictomagic
LastEditTime: 2020-11-24 16:09:16
Description: file content
'''
import win32clipboard as w
import keyboard
import transEntoCh
import time
import win32api
import win32con
import readFromJson
import feedback

def getText():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return(d).decode('GBK')


def copyGfCSA():
    while keyboard.is_pressed("alt") or keyboard.is_pressed("l"):
        time.sleep(0.1)
    win32api.keybd_event(17,0,0,0)  #ctrl
    win32api.keybd_event(67,0,0,0)  #c
    win32api.keybd_event(67,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.1)
    processedText = getText().strip()
    readFromJson.saveSentence(processedText, transEntoCh.translate(processedText))
    feedback.toastWinInfo("asd.ico", 10, True)  # TODO: custom your feedback here


if __name__=="__main__":
    keyboard.add_hotkey('ctrl+alt+l', copyGfCSA, [], False)
    keyboard.wait('esc')