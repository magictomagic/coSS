'''
Author: magictomagic
Date: 2020-11-24 15:46:57
LastEditors: magictomagic
LastEditTime: 2020-11-24 15:49:29
Description: file content
'''
import readFromJson 
import linecache
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
    win10toastSound.ToastNotifier().show_toast("success", getFeedBacks(readFromJson.accessFile())[2], icon_path="asd.ico", duration=10, threaded=True)
    # print(getFeedBacks(readFromJson.accessFile())[2])
  