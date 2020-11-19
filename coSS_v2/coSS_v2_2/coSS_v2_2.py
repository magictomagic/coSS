'''
Author: magictomagic
Date: 2020-11-18 12:48:50
LastEditors: magictomagic
LastEditTime: 2020-11-19 21:28:34
Description: file content
'''
import win32clipboard as w
import keyboard
import transEntoCh
import time
import win32api
import win32con
import c3


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

def superAddtion(en, ch, outputFile):
    with open(outputFile, 'a+') as f:
        f.write('| ' + en + ' | ' + ch + ' |\n')
    # TODO: judge if have written and display result


def copyGfCSA(outputFile):
    # TODO: save clipboard content first
    while keyboard.is_pressed("alt") or keyboard.is_pressed("l"):
        time.sleep(0.1)
    win32api.keybd_event(17,0,0,0)  #ctrl
    win32api.keybd_event(67,0,0,0)  #c
    win32api.keybd_event(67,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.1)
    processedText = getText().strip()
    superAddtion(processedText, transEntoCh.translate(processedText), outputFile)
    # print(getText())



# TODO:
# if os does not has clipboard list, save clipboard before copy 
if __name__=="__main__":
    outputFile = 'add_to.md'
    keyboard.add_hotkey('ctrl+alt+l', copyGfCSA, ['add_to.md'], False)
    keyboard.wait('esc')