import os
import subprocess
import re
import asyncio
from telegram import Bot

bot_token = os.environ.get('BOTTOKEN')
chat_id = os.environ.get('USERID')

# 创建 Bot 实例
bot = Bot(token=bot_token)


async def send_message():
    # 调用子进程并获取输出
    try:
        output_1 = subprocess.check_output(['python', 'DAILY.py']).decode()
        output_2 = subprocess.check_output(['python', 'BALANCE.py']).decode()
        botmessage =output_1 + output_2
        print(botmessage)

        # 发送消息
        await bot.send_message(chat_id=chat_id, text=botmessage)

    except subprocess.CalledProcessError as e:
        print("子进程调用错误:", e)

    except Exception as e:
        print("发生其他异常:", e)


# 运行异步函数
asyncio.run(send_message())
