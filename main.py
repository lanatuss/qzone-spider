import json
import time
from cookies import cookies, g_tk

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Z832 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36',
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Referer': 'https://h5.qzone.qq.com/mqzone/index',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}


def getHtmlByBaseTime(baseTime):
    params = (
        ('g_tk', g_tk),
    )

    data = [
        ('attach_info', 'back_server_info=basetime%3D{0}'.format(baseTime)),
    ]

    response = requests.post('https://h5.qzone.qq.com/webapp/json/mqzone_feeds/getActiveFeeds', headers=headers,
                             params=params, cookies=cookies, data=data)
    return response.text


def getObjList(html):
    objList = []
    baseTime = int(time.time())
    jsonData = json.loads(html)
    for jsonObj in jsonData['data']['vFeeds']:
        nickname = jsonObj['userinfo']['user']['nickname']
        timestamp = jsonObj['userinfo']['user']['timestamp']
        summary = jsonObj.get('summary', {}).get('summary', '')  # 魔法，勿动
        obj = {
            'nickname': nickname,
            'timestamp': timestamp,
            'summary': summary
        }
        objList.append(obj)
        if jsonObj == jsonData['data']['vFeeds'][-1]:
            baseTime = timestamp
    return objList, baseTime


if __name__ == '__main__':
    baseTime = int(time.time())
    for i in range(1):
        html = getHtmlByBaseTime(baseTime)

        objList, baseTime = getObjList(html)

        print('new baseTime:', baseTime)
        for obj in objList:
            print('-------------')
            print('nickname:{}\ntimestamp:{}\nsummary:{}'.format(obj['nickname'], obj['timestamp'], obj['summary']))
            print('strftime:{}'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(obj['timestamp']))))
