'''
Author: magictomagic
Date: 2020-11-19 22:20:49
LastEditors: magictomagic
LastEditTime: 2020-11-20 17:08:05
Description: file content
'''
import readFromJson 
import linecache
# from tkinter import *
from tkinter import messagebox
import tkinter

def getFeedBacks(afile):
    # afile = readFromJson.accessFile()
    preLastLine = ""
    curLine = ""
    for count, line in enumerate(open(afile)):
        preLastLine = curLine
        curLine = line
    return curLine.split("|")


if __name__=="__main__":
    # print(getFeedBacks(readFromJson.accessFile()))
    top = tkinter.Tk()
    top.withdraw()
    B1 = tkinter.Button(top, command = messagebox.showinfo("Success", "Hello World"))
  
