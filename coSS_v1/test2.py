#导入需要的包
import requests
import json
import time
def getCookie():
    headers = {
        "Host": "fanyi.youdao.com",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Referer": "https://www.google.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
    }
    response = requests.get("http://fanyi.youdao.com/", headers=headers)
    cookie = response.headers['Set-Cookie']
    userid_start = cookie.index('OUTFOX_SEARCH_USER_ID')
    userid_end = cookie.index(';', userid_start)
    session_start = cookie.index('JSESSIONID')
    session_end = cookie.index(';', session_start)
    set_cookie = cookie[userid_start: userid_end] + '; ' + cookie[session_start: session_end] + '; YOUDAO_MOBILE_ACCESS_TYPE=1; ___rl__test__cookies='
    return set_cookie
# print(set_cookie)
# print(response.cookies)
# headers = {
#         "Host": "fanyi.youdao.com",
#         "Accept": "application/json, text/javascript, */*; q=0.01",
#         "Connection": "keep-alive",
#         "Referer": "http://fanyi.youdao.com/",
#         "Origin": "http://fanyi.youdao.com",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
#         "Accept-Language": "en-US,en;q=0.5",
#         "Accept-Encoding": "gzip, deflate",
#         "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#         'Cookie':'YOUDAO_MOBILE_ACCESS_TYPE=1; OUTFOX_SEARCH_USER_ID=-949849212@10.169.0.84; JSESSIONID=aaasCt0mLlFAdeC4VS7wx; ___rl__test__cookies=' + rr ,
#         "Content-Length": "253",
#         "X-Requested-With": "XMLHttpRequest"
#     }