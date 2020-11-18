'''
Author: magictomagic
Date: 2020-11-18 08:30:35
LastEditors: magictomagic
LastEditTime: 2020-11-18 09:12:53
Description: file content
'''
import win32clipboard as w
import win32con
import keyboard
import transEntoCh
import win32com.client
import pythoncom

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


# TODO:
# if os does not has clipboard list, save clipboard before copy 
# set ctrl+c after add ctrl+shift+a
keyboard.add_hotkey('ctrl+shift+a', lambda: superAddtion(getText().strip(), transEntoCh.translate(getText().strip())))
keyboard.wait('esc')
