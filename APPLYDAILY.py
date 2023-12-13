import requests
import os

url = "https://www.north-plus.net/plugin.php"
params = {
    "H_name": "tasks",
    "action": "ajax",
    "actions": "job",
    "cid": "14",
    "nowtime": "1702389727027",
    "verify": "ca81e905"
}
cookie = os.environ.get("COOKIE")

headers = {
    "Cookie": cookie,
    "Sec-Ch-Ua": '"Chromium";v="109", "Not_A Brand";v="99"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "iframe",
    "Referer": "https://www.north-plus.net/plugin.php?H_name=tasks.html",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

response = requests.get(url, headers=headers, params=params)

print(response.text)
