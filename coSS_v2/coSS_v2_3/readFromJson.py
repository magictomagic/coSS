'''
Author: magictomagic
Date: 2020-11-19 19:13:50
LastEditors: magictomagic
LastEditTime: 2020-11-19 21:37:51
Description: file content
'''
import os
import json

defaultConfig = {
    "location" : ""
}

def superAddtion(en, ch, outputFile):
    with open(outputFile, 'a+') as f:
        f.write('| ' + en + ' | ' + ch + ' |\n')
    # TODO: judge if have written and display result


def saveSentence(en, ch):
    with open("custom.json") as f:
        customInf = json.load(f)
    if "custom" in customInf:
        setting_1 = customInf["custom"]
        if "location" in setting_1:
            filePath = setting_1["location"]
        else:
            filePath = defaultConfig["location"]
    else:
        filePath = defaultConfig["location"]
    if os.path.exists(filePath):
        with open(filePath, 'a+') as f:
            f.write('| ' + en + ' | ' + ch + ' |\n')
    else:
        with open(filePath, 'a+') as f:
            f.write("| 原文 | 译文 |" + "\n" + "| :---- | ---- |\n")
            f.write('| ' + en + ' | ' + ch + ' |\n')


# TODO:
# if os does not has clipboard list, save clipboard before copy 
if __name__=="__main__":
    pass