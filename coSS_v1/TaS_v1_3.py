'''
Author: magictomagic
Date: 2020-11-13 15:42:49
LastEditors: magictomagic
LastEditTime: 2020-11-13 18:08:04
Description: file content
'''
import requests
import json
import time
import hashlib
import test2
from random import randrange

TIMES = 1
distinctCookieFile = "save1.txt"


def genearteMD5(str):
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest()


def translate(word, stackDepth=0):
    if stackDepth >= 4:
        return "去看源碼，可能是 usign 改了"
    stackDepth += 1
    navigator_appVersion = "5.0 (Windows)"
    t = genearteMD5(navigator_appVersion) # bv
    curTime = round(time.time() * 1000)
    r = str(curTime + 3) # ts
    i = r + str(randrange(9)) # salt
    usign = "fanyideskweb" + word + i + "]BjuETDhU)zqSxf-=B#7m"
    sign = genearteMD5(usign) # sign
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
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
        result = json.loads(response.text)
        if result["errorCode"] == 0:
            return result['translateResult'][0][0]['tgt']
        else:
            saveDistinctCookie(distinctCookieFile)
            return translate(word, stackDepth)
    else: 
        return "T＿T" + "網絡鏈接不良" + "T＿T"
 

def saveDistinctCookie(distinctCookieFile):
    distinctCookie = test2.getCookie()
    with open(distinctCookieFile, "w") as f:
        f.write(distinctCookie)
    return distinctCookie

def getHeaders(rr, distinctCookieFile):
    global TIMES
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