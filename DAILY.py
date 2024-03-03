import requests
import os
import xml.etree.ElementTree as ET
import json

cookie_value = os.getenv('COOKIE')
cookies = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookie_value.split('; ')}



cookies = {
    'wordpress_sec_ce72810736f5acb43dee489afc07d300': 'joshua3423%7C1710676443%7Cdj4UF6umqTtBpjdyNIevwcvZOU7ZU7YjQ9BGdGDuVqm%7C64af5fbee503cd9771809074e6c19ead213790d02450a74437b09400ba15ba2d',
    'showed_system_notice': 'showed',
    'PHPSESSID': 'nqou6308p0b9slhijvj77gco5n',
    'wordpress_test_cookie': 'WP%20Cookie%20check',
    'wordpress_logged_in_ce72810736f5acb43dee489afc07d300': 'joshua3423%7C1710676443%7Cdj4UF6umqTtBpjdyNIevwcvZOU7ZU7YjQ9BGdGDuVqm%7Cdee5ce35e2f1f918dec85c97137f61e58d90b28e2f6d79d0eb45f8056c86f98a',
}

headers = {
    'authority': 'www.eohut.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'dnt': '1',
    'origin': 'https://www.eohut.com',
    'referer': 'https://www.eohut.com/',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'action': 'user_checkin',
}

response = requests.post('https://www.eohut.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
print(response.text)
# 解析返回值
data = json.loads(response)

# 提取可读信息
msg = data["msg"]
integral = data["data"]["integral"]
points = data["data"]["points"]

# 打印可读信息
print("返回信息:", msg)
print("积分:", integral)
print("经验值:", points)
