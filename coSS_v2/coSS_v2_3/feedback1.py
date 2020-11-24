'''
Author: magictomagic
Date: 2020-11-19 22:20:49
LastEditors: magictomagic
LastEditTime: 2020-11-24 15:46:25
Description: file content
'''
import readFromJson 
import linecache
# from tkinter import *
from tkinter import messagebox
import tkinter
import win10toastSound
def getFeedBacks(afile):
    # afile = readFromJson.accessFile()
    preLastLine = ""
    curLine = ""
    for count, line in enumerate(open(afile)):
        preLastLine = curLine
        curLine = line
    return curLine.split("|")


if __name__=="__main__":
    # win10toastSound.ToastNotifier().show_toast("success", "make usa great again", icon_path="asd.ico", duration=1, threaded=True)
    print(getFeedBacks(readFromJson.accessFile())[2])
    # top = tkinter.Tk()
    # top.withdraw()
    # B1 = tkinter.Button(top, command = messagebox.showinfo("Success", "Hello World"))
  
