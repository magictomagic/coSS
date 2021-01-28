'''
Author: magictomagic
Date: 2020-11-13 15:42:49
LastEditors: magictomagic
LastEditTime: 2020-11-19 21:55:23
Description: file content
'''
import requests
import json
import time
import hashlib
import ydCookie
import readFromJson
from random import randrange

TIMES = 0 # set TIMES = 0 to creat/update cookie / first launch
distinctCookieFile = "save.txt"


def genearteMD5(str):
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest()


def translate(word, stackDepth=0):
    if stackDepth >= 4:
        return "去看源碼，可能是 usign 改了"
    stackDepth += 1
    # TODO: 伪装
    navigator_appVersion = "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
    t = genearteMD5(navigator_appVersion) # bv
    curTime = round(time.time() * 1000)
    r = str(curTime + 3) # ts
    i = r + str(randrange(9)) # salt
    usign = "fanyideskweb" + word + i + readFromJson.accessMD5_Append() # "]BjuETDhU)zqSxf-=B#7m"
    sign = genearteMD5(usign) # sign
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    # url = 'http://fanyi.youdao.com/' 是域名，translate_o?smartresult=dict&smartresult=rule是ajax请求
    # 上次有道停服更新了一下它们的翻译网站，只是变了一下md5加密前拼接的某个字符串，一点长进也没有，秋招题目还出的这么难
    rr = str(curTime)
    headers = getHeaders(rr, distinctCookieFile)
    key = {
        'i': word,
        'from':	"AUTO",
        'to':	"AUTO",
        'smartresult':	"dict",
        'client':	"fanyideskweb",
        'salt':	i,
        'sign':	sign,
        'lts':	r,
        'bv':	navigator_appVersion,
        'doctype':	"json",
        'version':	"2.1",
        'keyfrom':	"fanyi.web",
        'action':	"FY_BY_REALTlME"
    }
    response = requests.post(url, data=key, headers=headers)
    if response.status_code == 200:
        # print(response.text)
        # print(type(response.text))
        result = json.loads(response.text)
        if result["errorCode"] == 0:
            return result['translateResult'][0][0]['tgt']
        else:
            saveDistinctCookie(distinctCookieFile)
            return translate(word, stackDepth)
    else: 
        return "T＿T" + "網絡鏈接不良" + "T＿T"
 

def saveDistinctCookie(distinctCookieFile):
    distinctCookie = ydCookie.getCookie()
    with open(distinctCookieFile, "w") as f:
        f.write(distinctCookie)
    return distinctCookie

def getHeaders(rr, distinctCookieFile):
    global TIMES
    # TODO: UA伪装
    headers = {
        "Host": "fanyi.youdao.com",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Connection": "keep-alive",
        "Referer": "http://fanyi.youdao.com/",
        "Origin": "http://fanyi.youdao.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Content-Length": "253",
        "X-Requested-With": "XMLHttpRequest"
    }
    if TIMES == 0 :
        headers_Cookie = saveDistinctCookie(distinctCookieFile) + rr
    else: 
        with open(distinctCookieFile, "r") as f:
            headers_Cookie = f.read().strip() + rr
    headers["Cookie"] = headers_Cookie
    TIMES += 1
    return headers

if __name__=="__main__":
    print(translate('make usa great again'))
    # print(translate('they shut down their conscious system and instead rely on their well trained intuition, drawing on their deeply ingraind repertoire of chunks'))
    pass