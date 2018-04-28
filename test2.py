from uiautomator import device as d
import time
import os
import requests
import re
import random
import time
import sys
import json
from pymongo import MongoClient
from uiautomator import JsonRPCError


# d = Device('6b862e8')
# with open('account', 'r') as f:
# 	proton = f.read()
# 	prodict = json.loads(proton)
# 读取邮箱帐号
conn = MongoClient('mongodb://192.168.1.66:27017/')
db = conn.fbaccount
fb = db.emailAccount
fbaccount = fb.find()
# 获取已注册的fb用户列表
fbusers = [i['username'] for i in fbaccount]
# 获取proton邮箱帐号列表
db = conn.proemail
pro = db.account
prolist = [i for i in pro.find()]
prousers = [i['userName'] for i in prolist]
# 从proton邮箱列表中选出未注册过的帐号
index = -1
for i in prousers:
	index += 1
	if i not in fbusers:
		username = i
		password = prolist[index]['passwords']
	break


os.system("adb uninstall ch.protonmail.android")
os.system("adb install /home/administator/下载/ch.protonmail.android_430.apk")
# 登录邮箱
d(text="ProtonMail").click()
d(text="Sign In").click()
d(text="Username").set_text(username)
#d(text="next").click()
d(resourceId="ch.protonmail.android:id/password").set_text(password)
#d(text="Next").click()
#d(text="YES")
d(text="Sign In").click()
#d(text="OK").click()
d(text="close tour").click()
d(text="OK").click()
# 验证注册
d(textContains="is your Facebook confirmation").click()
d(text="Display Images").click()
d(description="Action Required: Confirm Your Facebook Account Link").click()
d(text="Facebook").click()
d(text="以后在说").click()
# 存入数据库
fb.insert({"username" : username, "password" : password})
