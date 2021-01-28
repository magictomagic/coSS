'''
Author: magictomagic
Date: 2020-11-24 15:46:57
LastEditors: magictomagic
LastEditTime: 2020-11-24 16:09:28
Description: file content
'''
import readFromJson 
import win10toastSound
import os

def getFeedBacks(afile):
    preLastLine = ""
    curLine = ""
    for count, line in enumerate(open(afile)):
        preLastLine = curLine
        curLine = line
    return curLine.split("|")   # TODO: can not translate txt contains "|"

def toastWinInfo(iconPath, duration, threaded):
    iconPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), iconPath)
    win10toastSound.ToastNotifier().show_toast("success", getFeedBacks(readFromJson.accessFile())[2], icon_path=iconPath, duration=duration, threaded=threaded)


if __name__=="__main__":
    # toastWinInfo("asd.ico", 10, True)
    pass
    # win10toastSound.ToastNotifier().show_toast("success", getFeedBacks(readFromJson.accessFile())[2], icon_path="asd.ico", duration=10, threaded=True)
    # print(getFeedBacks(readFromJson.accessFile())[2])
  