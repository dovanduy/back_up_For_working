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

try:
	# get email account
	conn = MongoClient('mongodb://192.168.1.66:27017/')
	db = conn.emailAccount
	tw = db.twitter
	twaccount = tw.find()

	# 获取已注册的fb用户列表
	twusers = [i['userName'] for i in twaccount]

	# 获取proton邮箱帐号列表
	db = conn.proemail
	pro = db.account
	prolist = [i for i in pro.find()]
	prousers = [i['userName'] for i in prolist[::-1]]

	# 从proton邮箱列表中选出未注册过的帐号
	index = len(prolist)
	a = 0
	for i in prousers:
		index -= 1
		if i not in twusers:
			username = i
			password = prolist[index]['passwords']
			a += 1
			if a > 9:
				break
	print(username)
	print(password)

	d = Device('0123456789ABCDEF')

	# # change ip
	# db = conn.ssArgu
	# ss = [i for i in db.tt.find().sort('times', 1)][0]

	# # 设置信号量
	# ss['times'] = ss['times'] + 1
	# db.tt.update({'ip':ss['ip']}, ss)
	# ip = ss['ip']

	# os.system('adb -s 0123456789ABCDEF shell am start -n com.github.shadowsocks/com.github.shadowsocks.Shadowsocks')
	# time.sleep(1)

	# d(className='android.widget.ImageButton').click()
	# time.sleep(2)
	# d(text="服务器").click()
	# time.sleep(1)
	# d.long_click(200, 450)
	# os.system('adb -s 0123456789ABCDEF shell input keyevent 67')
	# time.sleep(1)
	# os.system("adb -s 0123456789ABCDEF shell input text '{}'".format(ip))
	# time.sleep(1)
	# d(text="确定").click()
	# time.sleep(1)
	# d(className='android.widget.ImageButton').click()

	# remove twitter
	os.system('adb -s 0123456789ABCDEF uninstall com.twitter.android')

	# install twitter
	os.system('adb -s 0123456789ABCDEF install /home/administator/twitter.apk')
	time.sleep(5)

	# start twitter
	os.system('adb -s 0123456789ABCDEF shell "su -c" am start -n com.twitter.android/.DispatchActivity')
	d.watcher("fbui_tooltip").when(resourceId="com.yulong.android.seccenter:id/alertdlg_forbid").click(resourceId="com.yulong.android.seccenter:id/alertdlg_forbid")
	d.watchers.run()
	time.sleep(8)
	try:
		d(text="等待").click()
		time.sleep(3)
	except JsonRPCError:
		pass
	# get name of chinese
	# with open('tw.txt', 'r') as f:
	# 	namelist = f.readlines()

	# name = re.match('[\w]+', namelist[0]).group()
	

	# sign up
	d(text="注册").click()
	# d(resourceId="com.twitter.android:id/name_entry").click()
	# os.system("adb -s 0123456789ABCDEF shell am broadcast -a ADB_INPUT_TEXT --es msg '{}'".format(enname))
	enname = re.match('[\w]+', username).group()
	print(enname)
	os.system('adb -s 0123456789ABCDEF shell input text "{}"'.format(enname))
	time.sleep(4)
	d(text="下一步").click()
	if d(textContains="使用电子邮件注册").exists:
		ui = d(textContains="使用电子邮件注册").info
		x = ui["bounds"]["left"]
		y = ui["bounds"]["top"]
		d.click(x,y)
	d.click(300, 320)
	# d(resourceId="com.twitter.android:id/email_entry").click()
	os.system("adb -s 0123456789ABCDEF shell input text {}".format(username))
	time.sleep(4)
	# d(resourceId="com.twitter.android:id/cta").click()
	d(text="下一步").click()
	time.sleep(7)
	# d(resourceId="com.twitter.android:id/password_entry")
	os.system("adb -s 0123456789ABCDEF shell input text {}".format(password))
	time.sleep(4)
	d(text="下一步").click()
	time.sleep(2)
	d(text="暂时不用").click()
	time.sleep(2)
	d(text="我确定").click()
	# d(text="跳过").click()
	# d(resourceId="android:确定").click()
	# d.long_press(300, 350)
	randomName = str(int(random.random()*10)) + enname[:9] + str(int(random.random()*10))
	print(randomName)
	d.long_click(200, 350)
	os.system('adb -s 0123456789ABCDEF shell input keyevent 67')
	os.system('adb -s 0123456789ABCDEF shell input text "{}"'.format(randomName))
	time.sleep(3)
	d(text="下一步").click()
	time.sleep(2)
	d(textContains="现在开始").click()
	tw.insert({"userName" : username, "passwords" : password, "name": randomName})
	# here maybe quit account.
	#
	#
	#
	#
	#
	#
	#
	# !!!!!!!!!!!!!!!!!!!!!!!!!!!
	time.sleep(2)
	d(text="跳过").click()
	time.sleep(2)
	d(text="暂时跳过").click()
	time.sleep(5)
	d(textContains="关注")[1].click()
	time.sleep(5)
	if d(textContains="关注").exists:
		d(textContains="关注")[1].click()
	d(description="显示导航栏").click()
	time.sleep(2)
	d(text="设置和隐私").click()
	time.sleep(2)
	d(text="登出").click()
	time.sleep(2)
	d(text="确定").click()
	time.sleep(2)

	# the end of the program, remove the name that has been used.
	# with open('tw.txt', 'w') as f:
	# 	for i in namelist[1:]:
	# 		f.write(i)
except JsonRPCError as e:
	print(e)
	db = conn.proemail
	pro = db.account
	pro.remove({"userName":username})
	# with open('tw.txt', 'w') as f:
	# 	for i in namelist[1:]:
	# 		f.write(i)
	python3 = sys.executable
	os.execl(python3, python3, * sys.argv)
# d(textContains="关注")[1].click()
# d(resourceId="com.twitter.android:id/skip").click()
# d(resourceId="com.twitter.android:id/lets_go").click()
# d(resourceId="android:id/button2").click()
# time.sleep(10)

# sign in the protonmail, confirm the account.
# 卸载邮箱
# 安装邮箱
# os.system("adb -s 0123456789ABCDEF uninstall ch.protonmail.android")
# os.system("adb -s 0123456789ABCDEF install /home/administator/下载/ch.protonmail.android_430.apk")
# # 登录邮箱
# os.system("adb -s 0123456789ABCDEF shell am start -n ch.protonmail.android/ch.protonmail.android.activities.SplashActivity")
# time.sleep(1)
# d(text="Sign In").click()
# time.sleep(1)
# d(text="Username").set_text(username)
# time.sleep(3)
# # d(text="next").click()
# # d(resourceId="ch.protonmail.android:id/password").set_text(password)
# d.click(200, 350)
# os.system('adb -s 0123456789ABCDEF shell input text "{}"'.format(password))
# #d(text="Next").click()
# #d(text="YES")
# d(text="Sign In").click()
# time.sleep(1)
# #d(text="OK").click()
# d(text="close tour").click()
# time.sleep(1)
# d(text="确定").click()
# time.sleep(1)
# # 验证注册
# # d.click(350,230)
# try:
# 	d(textContains="请确认你的 Twitter 账号。").click()
# except JsonRPCError as e:
# 	print(e)
# 	d.click(200, 160)
# 	time.sleep(1)
# d.click(200, 800)
# time.sleep(2)
# try:
# 	d(descriptionContains="").click()
# except JsonRPCError as e:
# 	print(e)
# 	d.click(250, 950)
# 	time.sleep(2)

# try:
# 	d(text="Twitter").click()
# except JsonRPCError as e:
# 	print(e)
# 	d(text="twitter").click()
# d(text="始终").click()
# time.sleep(5)
# # d(text="以后在说").click()
# # 存入数据库
# fb.insert({"username" : username, "password" : password})
# print('DONE!')
# 重启程序
python3 = sys.executable
os.execl(python3, python3, * sys.argv)













