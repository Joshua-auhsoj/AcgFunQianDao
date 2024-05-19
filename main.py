import os
import subprocess
import re
import asyncio
from telegram import Bot

process_1 = subprocess.Popen(['python', 'DAILY.py'], stdout=subprocess.PIPE)
output_1, _ = process_1.communicate()
process_2 = subprocess.Popen(['python', 'BALANCE.py'], stdout=subprocess.PIPE)
output_2, _ = process_2.communicate()


response_text1 = output_1.decode()
response_text2 = output_2.decode()



print(response_text1)
print(response_text1)


bot_token = os.environ.get('BOTTOKEN')
chat_id = os.environ.get('USERID')

# 创建 Bot 实例

bot = Bot(token=bot_token)


# 发送消息
async def send_message():
    await bot.send_message(chat_id=chat_id, text=response_text1)


# 运行异步函数
asyncio.run(send_message())
