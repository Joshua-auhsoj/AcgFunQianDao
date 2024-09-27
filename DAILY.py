import requests
import os
import json
import xml.etree.ElementTree as ET

# 获取 cookie 值
cookie_value = os.getenv('COOKIE')
cookies = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookie_value.split('; ')}

# 请求头
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Referer': 'https://acgfun.moe/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

# 发送请求
response = requests.get(
    'https://acgfun.moe/plugin.php?id=k_misign:sign&operation=qiandao&format=global_usernav_extra&formhash=b21898d7&inajax=1&ajaxtarget=k_misign_topb',
    cookies=cookies,
    headers=headers,
)

# 打印原始响应
#print(response.text)

# 解析 XML 数据
root = ET.fromstring(response.content)
message = root.text.strip()

# 输出签到结果
print(f"签到状态: {message}")
