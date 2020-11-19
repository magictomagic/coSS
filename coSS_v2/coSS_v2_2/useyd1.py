'''
Author: magictomagic
Date: 2020-11-18 14:54:52
LastEditors: magictomagic
LastEditTime: 2020-11-18 14:58:20
Description: file content
'''
from ctypes import *

dll = cdll.LoadLibrary("C:\\backsupport\\youdao\\Stable\\YoudaoGetWord64.dll")
print(type(dll))