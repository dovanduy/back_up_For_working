import requests
import re
import random
import time
import sys
import json
from pymongo import MongoClient
from uiautomator import JsonRPCError
from uiautomator import device as d

d.press('home')
d.press('home')
# 卸载邮箱
# 安装邮箱
#os.system("adb uninstall ch.protonmail.android")
#os.system("adb install /home/administator/下载/ch.protonmail.android_430.apk")
# 登录邮箱
d(text="ProtonMail").click()
#d(text="Sign In").click()
#d(text="Username").set_text('DavidACampos@protonmail.com')
#d(text="next").click()
#d(resourceId="ch.protonmail.android:id/password").set_text('6iz0m8j2ehvu')
#d(text="Next").click()
#d(text="YES")
#d(text="Sign In").click()
#d(text="OK").click()
#d(text="close tour").click()
#d(text="OK").click()
# 验证注册
d(textContains="is your Facebook confirmation").click()
d(text="Display Images").click()
d(description="Action Required: Confirm Your Facebook Account Link").click()
d(text="Facebook").click()
d(text="以后在说").click()
# 存入数据库
fb.insert({"username" : username, "password" : password})
# 重启程序
python3 = sys.executable
os.execl(python3, python3, * sys.argv)
