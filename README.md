# RJHome签到
## 源代码来自只会用BurpSuite的我和神通广大的ChatGPT
### 感谢[能把Curl转换成各种语言的神奇网站](https://curlconverter.com/),感谢万能的[ChatGPT](https://poe.com/ChatGPT),感谢优秀的渗透工具[BurpSuite](https://portswigger.net/burp)，感谢大毛病不多，小毛病不断的浏览器[Chromium](https://www.chromium.org/chromium-projects/)及[Google Chrome](https://www.google.com/chrome/)
## 使用方法
1.支持TelegramBot推送，将**USERID**和**BOTTOKEN**和添加到**Action Secrets**，两者分别为用户的ChatID（可以找Userinfobot索要），BotToken（可以找BotFather索要）  
2.将**COOKIE**添加到**Action Secrets**  
3.添加了定时任务，会在每天北京时间凌晨一点运行  
4.低调使用，避免迭代  
5.COOKIE值示例  
```plaintext
_ga=值; _gid=值; eb9e6_cknum=值D; eb9e6_ck_info=值; eb9e6_winduser=值D; eb9e6_readlog=值; eb9e6_ol_offset=值; eb9e6_lastpos=值; _gat=1; _ga_3G0BZEH5V0=值; eb9e6_lastvisit=值
```
两端无引号，值间用分号隔开，从Chrome抓请求获取，或者将请求复制后摘取  
## 开发过程
1.启动Chrome，登陆网站  
2.使用F12抓包，进行一次签到 
3.查看并复制请求，粘贴到翻译网站获得Python代码，复制其中“Cookie”字段的值，询问ChatGPT获得将Cookie转化为请求格式的代码  
4.将两段代码融合，并加上从系统变量提取Cookie的代码，即可完成两个个执行脚本之一，另一个脚本以此类推完成   
5.询问ChatGPT得到GitHubAction配置文件，放置于“.github/workflows”文件夹内  
6，将项目上传GitHub  
## 以上内容完成于23/12/13，19:32    
抽空完成了整个项目，现在可以正常使用了

