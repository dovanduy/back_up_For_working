from uiautomator import Device
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


d = Device('6b862e8')
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

print(username)
d.press('home')
# 更改机器码
d.press('home')
d(text="changer").click()
d(text="Random").click()
d.press('home')
# 卸载fb
os.system('adb -s 6b862e8 uninstall com.facebook.katana')
# 安装fb
os.system('adb -s 6b862e8 install /home/administator/facebook-163-0-0-43-91.apk')
# 切换ip代理

# d(resourceId="com.github.shadowsocks:id/edit").click()
# d(resourceId="com.github.shadowsocks:id/action_delete").click()
# d(text='是').click()
# with open('ssArgu', 'r') as f:
# 	ssdict = json.loads(f.read())
# ss = sslist.pop()

# with open('ssArgu', 'w') as f:
# 	f.write(sslist)# 从数据库中读取最近没有使用的ss信息
# d = Device('6b862e8')
# d(description="添加配置文件").click()
# d(text="手动设置").click()
#d.click(606, 1111)
db = conn.ssArgu
ss = [i for i in db.ss.find().sort('times', 1)][0]
# 设置信号量
ss['times'] = ss['times'] + 1
db.ss.update({'ip':ss['ip']}, ss)
ip = ss['ip']
#port = ss["port"]
#pwd = ss['password']
#way = ss['way']	
d(textContains='shadow').click()
time.sleep(1)
d(resourceId="com.github.shadowsocks:id/fab").click()
time.sleep(2)
d(resourceId="com.github.shadowsocks:id/edit").click()
d(text="Server").click()
time.sleep(2)
d.click(660, 1100)
time.sleep(1)
d(resourceId="android:id/edit").set_text(ip)
d(text="OK").click()
#d(text="Remote Port").click()
#d(resourceId="android:id/numberpicker_input").set_text(port)
#d(text="OK").click()
#d(text="Password").click()
#d(resourceId="android:id/edit").set_text(pwd)
#d(text="OK").click()
#d(text="Encrypt Method").click()
#time.sleep(1)
#d.swipe(200, 140, 200, 1200)
#d(text=way).click()
d(resourceId="com.github.shadowsocks:id/action_apply").click()
#time.sleep(1)
#d(resourceId="com.github.shadowsocks:id/container").click()
d(resourceId="com.github.shadowsocks:id/fab").click()
time.sleep(2)
d.press('home')
# 注册fb
d(text="Facebook").click()
time.sleep(15)
#d(textContains="拒绝").click()
#d(text="邮箱或手机号").set_text(username)
#d(resourceId="com.facebook.katana:id/(name removerd)").set_text(password)
#d(text="登录").click()
d(text="Create New Facebook Account").click()
# d(text='暂时使用英语').click()
d(textContains="Deny").click()	
# d(text="继续").click()
time.sleep(1)
d(text="Next").click()
firstname, lastname = re.match('([A-Z]{1}[a-z]+)([A-Za-z]+)', username).groups()
# d(resourceId="com.facebook.katana:id/(name removed)").set_text(lastname)
# d(resourceId="com.facebook.katana:id/(name removed)").set_text(firstname)
# d(text="姓名").click()
time.sleep(1)
d(text="Last Name").set_text(lastname)
time.sleep(1)
d(text="First Name").set_text(firstname)
time.sleep(1)
d(text='Next').click()
time.sleep(1)
num = [str(i) for i in range(10)]
year = '19' + random.choice(['8', '9']) + random.choice(num)
month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
day = [i for i in range(1, 31)]
time.sleep(1)
d(resourceId='android:id/numberpicker_input')[2].set_text(year)
time.sleep(1)
d(resourceId='android:id/numberpicker_input')[0].set_text(random.choice(month))
time.sleep(1)
# d(resourceId='android:id/numberpicker_input')[0].set_text(random.choice(month))
d(resourceId='android:id/numberpicker_input')[1].set_text(random.choice(day))
time.sleep(1)
# d(text="继续").click()
d(text="Next").click()
time.sleep(1)
# d(text="女").click()
# d(text="继续").click()
d(text="Female").click()
time.sleep(1)
d(text="Next").click()
time.sleep(1)
d(text="Sign Up With Email Address").click()
time.sleep(1)
d(description="Email Address").set_text(username)
time.sleep(1)
d(text="Next").click()
time.sleep(1)
time.sleep(1)
# d(resourceId="com.facebook.katana:id/(name removed)")[9].set_text('123')
d(text="Password")[1].set_text(password)
time.sleep(1)
# d(textContains="123").set_text(password)
d(text="Next").click()
time.sleep(1)
d(text="Sign up without uploading my contacts").click()
time.sleep(20)
d(text="Not Now").click()
time.sleep(2)
d.press('home')
d.press('home')
# 卸载邮箱
# 安装邮箱
os.system("adb -s 6b862e8 uninstall ch.protonmail.android")
os.system("adb -s 6b862e8 install /home/administator/下载/ch.protonmail.android_430.apk")
# 登录邮箱
d(text="ProtonMail").click()
time.sleep(1)
d(text="Sign In").click()
time.sleep(1)
d(text="Username").set_text(username)
time.sleep(1)
# d(text="next").click()
d(resourceId="ch.protonmail.android:id/password").set_text(password)
#d(text="Next").click()
#d(text="YES")
d(text="Sign In").click()
time.sleep(1)
#d(text="OK").click()
d(text="close tour").click()
time.sleep(1)
d(text="OK").click()
time.sleep(1)
# 验证注册
# d.click(350,230)
try:
	d(textContains="is your Facebook confirmation").click()
except JsonRPCError as e:
	print(e)
	d.click(400, 240)
	time.sleep(1)
d(text="Display Images").click()
time.sleep(3)
try:
	d(descriptionContains="Confirm Your Facebook Account Link").click()
except JsonRPCError as e:
	print(e)
	d.click(250, 950)
	time.sleep(2)

try:
	d(text="Facebook").click()
except JsonRPCError as e:
	print(e)
	d.click(300, 830)
	time.sleep(1)
	d(text="Facebook").click()
time.sleep(5)
# d(text="以后在说").click()
# 存入数据库
fb.insert({"username" : username, "password" : password})
time.sleep(15)
# 重启程序
python3 = sys.executable
os.execl(python3, python3, * sys.argv)