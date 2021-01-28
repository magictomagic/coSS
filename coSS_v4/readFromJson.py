'''
Author: magictomagic
Date: 2020-11-19 19:13:50
LastEditors: magictomagic
LastEditTime: 2020-11-19 22:26:12
Description: file content
'''
import os
import json
dir_path = os.path.dirname(os.path.realpath(__file__))
defaultConfig = {
    "location" : ""
}

def accessFile():
    with open(os.path.join(dir_path, "custom.json")) as f:
        customInf = json.load(f)
    if "custom" in customInf:
        setting_1 = customInf["custom"]
        if "location" in setting_1:
            filePath = setting_1["location"]
        else:
            filePath = defaultConfig["location"]
    else:
        filePath = defaultConfig["location"]

    return filePath


def accessMD5_Append():
    with open(os.path.join(dir_path, "custom.json")) as f:
        customInf = json.load(f)
    if "md5_append" in customInf:
        md5_a = customInf["md5_append"]
    else:
        # 去js里读，存于custom中
        pass 
    return md5_a


def saveSentence(en, ch):
    filePath = accessFile()
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
    # print(accessFile())
    # with open("aa.json", 'a+') as f:
    #     f.write("adasd")
    # saveSentence("adas","1312")
    print(dir_path)
    pass