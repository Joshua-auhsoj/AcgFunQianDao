import requests
import os
import json

import cloudscraper

scraper = cloudscraper.create_scraper()  # 创建一个scraper对象

url = "https://rjhome.me/wp-json/b2/v1/getUserMission"



cookie_value = os.getenv('COOKIE')
cookies = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookie_value.split('; ')}





headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvcmpob21lLm1lIiwiaWF0IjoxNzE4MTc1MDAxLCJuYmYiOjE3MTgxNzUwMDEsImV4cCI6MTcxOTM4NDYwMSwiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiODIxNDkifX19.z0e7fy-FLjpzxIjNJ514fGT4rWidc5KSNlrw6AmyRWc',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://rjhome.me',
    'priority': 'u=1, i',
    'referer': 'https://rjhome.me/message',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

data = {
    'count': '10',
    'paged': '1',
}

#response = requests.post('https://rjhome.me/wp-json/b2/v1/getUserMission', cookies=cookies, headers=headers, data=data)
response = scraper.post(url, cookies=cookies, headers=headers, data=data)

json_data = json.loads(response.text)

# 提取所需的内容
my_credit = json_data['mission']['my_credit']
credit = json_data['mission']['credit']

# 格式化输出
output = f"签到积分: {credit}\n总积分: {my_credit}"

# 打印结果
print(output)






