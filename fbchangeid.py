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
	prolist = [i for i in pro.find()][::-1]
	prousers = [i['userName'] for i in prolist]
	# get new fbaccount db information.
	db = conn.fbaccount
	fb = db.new
	fbaccount = fb.find()
	# if len([i for i in fbaccount]) == 0:
	fbuserslist = [i for i in fbaccount]
	for i in fbuserslist:
		fbusers.append(i['email'])

	# 从proton邮箱列表中选出未注册过的帐号
	# for another phone
	num = 0
	index = -1
	for i in prousers:
		index += 1
		if i not in fbusers:
			num += 1
			username = i
			password = prolist[index]['passwords']
			if num == 3:
				break

	print(username)
	print(password)
	d.press('home')
	# 更改机器码
	# d.press('home')
	# time.sleep(1)
	# d(text="changer").click()
	# time.sleep(2)
	# d(text="Random").click()
	# time.sleep(1)
	# d.press('home')
	d(text="XPrivacy").click()
	time.sleep(3)
	d.click(650, 100)
	time.sleep(1)
	d.swipe(700, 1000, 700, 500)
	d(text="Settings").click()
	time.sleep(1)
	d(text="Randomize now").click()
	time.sleep(1)
	d.swipe(350, 1000, 350, 100)
	d.dump('aaa')
	d.swipe(350, 1000, 350, 100)
	time.sleep(1)
	d.swipe(350, 1000, 350, 800)
	d.dump('bbb')
	d(text="OK").click()

	list = [17, 20, 23, 26, 31, 36, 39, 42, 45, 48, 55, 66, 69]
	with open('aaa', 'r') as f:
		string = f.read()

	with open('bbb', 'r') as f:
		string = string + f.read()

	argudict = {}
	for i in list:
		text = re.search('index="{}"[\w\W]+?text="([\w\W]+?)"'.format(i+1), string).groups()[0]
		value = re.search('index="{}"[\w\W]+?text="([\w\W]+?)"'.format(i+2), string).groups()[0]
		argudict[text] = value

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
	d.press('home')
	db = conn.ssArgu
	ss = [i for i in db.ts.find().sort('times', 1)][0]
	# 设置信号量
	ss['times'] = ss['times'] + 1
	ip = ss['ip']
	db.ts.update({'ip':ss['ip']}, ss)
	#port = ss["port"]
	#pwd = ss['password']
	# way = ss['way']	
	d(textContains='shadow').click()
	time.sleep(1)
	d(resourceId="com.github.shadowsocks:id/fab").click()
	time.sleep(2)
	d(resourceId="com.github.shadowsocks:id/edit").click()
	time.sleep(1)
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
	# time.sleep(1)
	# d(text="Encrypt Method").click()
	# time.sleep(1)
	# d.swipe(200, 140, 200, 1200)
	time.sleep(1)
	# d(text=way).click()
	# time.sleep(1)
	d(resourceId="com.github.shadowsocks:id/action_apply").click()
	#time.sleep(1)
	#d(resourceId="com.github.shadowsocks:id/container").click()
	d(resourceId="com.github.shadowsocks:id/fab").click()
	time.sleep(5)
	
	d.press('home')
	# 注册fb
	d(text="Facebook").click()
	time.sleep(15)
	if d(text="CONTINUE").exists:
		d(text="CONTINUE").click()
	#d(textContains="拒绝").click()
	#d(text="邮箱或手机号").set_text(username)
	#d(resourceId="com.facebook.katana:id/(name removerd)").set_text(password)
	#d(text="登录").click()
	d(text="Create New Facebook Account").click()
	# d(text='暂时使用英语').click()
	try:
		d(textContains="Deny").click()	
	except JsonRPCError:
		pass
	# d(text="继续").click()
	time.sleep(1)
	d(text="Next").click()
	firstname, lastname = re.match('([A-Z]{1}[a-z]+)([A-Za-z]+)', username).groups()
	# firstname, lastname = 'Stephon', 'Alan'
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
	day = [str(i) for i in range(1, 31)]
	month = random.choice(month)
	day = random.choice(day)
	time.sleep(1)
	d(resourceId='android:id/numberpicker_input')[2].set_text(year)
	time.sleep(1)
	d(resourceId='android:id/numberpicker_input')[0].set_text(month)
	time.sleep(1)
	# d(resourceId='android:id/numberpicker_input')[0].set_text(random.choice(month))
	d(resourceId='android:id/numberpicker_input')[1].set_text(day)
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
	if d(text="Try Again").exists:
		d(textContains="Try Again").click()
	
	time.sleep(20)
	if d(text="Not Now").exists:
		d(text="Not Now").click()
		time.sleep(1)
	else:
		d.click(500, 800)
		time.sleep(1)
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
	time.sleep(3)
	if d(text="Sign In").exists:
		d(text="Sign In").click()
	time.sleep(5)
	
	if d(textContains="Deny").exists:
		d(textContains="Deny").click()	
		time.sleep(2)
	#d(text="OK").click()
	d(text="close tour").click()
	time.sleep(1)
	if d(text="OK").exists:
		d(text="OK").click()
	time.sleep(1)
	# 验证注册
	# d.click(350,230)#
	#
	#
	# d.click(50,125)
	# time.sleep(1)
	# d(text="Spam").click()
	# time.sleep(2)
	#
	#
	#
	if d(textContains="is your Facebook confirmation").exists:
		d(textContains="is your Facebook confirmation").click()
		time.sleep(2)
	# except JsonRPCError as e:
		# print(e)\
	else:
		d.click(400, 220)
		time.sleep(2)
	if d(text="Display Images").exists:
		d(text="Display Images").click()
	time.sleep(3)
	if d(descriptionContains="Confirm Your Facebook Account Link").exists:
		d(descriptionContains="Confirm Your Facebook Account Link").click()
		time.sleep(2)
	# except JsonRPCError as e:
		# print(e)
	else:
		d.click(250, 950)
		time.sleep(2)

	if d(text="Facebook").exists:
		d(text="Facebook").click()
	# except JsonRPCError as e:
		# print(e)
	else:	
		time.sleep(1)
		d.click(50,105)
		time.sleep(2)
		d.click(50,125)
		time.sleep(2)
		d(text="Spam").click()
		time.sleep(2)
		if d(textContains="is your Facebook confirmation").exists:
			d(textContains="is your Facebook confirmation").click()
			time.sleep(2)
		# except JsonRPCError as e:
			# print(e)\
		else:
			d.click(400, 220)
			time.sleep(2)
		if d(text="Display Images").exists:
			d(text="Display Images").click()
		time.sleep(3)
		if d(descriptionContains="Confirm Your Facebook Account Link").exists:
			d(descriptionContains="Confirm Your Facebook Account Link").click()
			time.sleep(2)
		# except JsonRPCError as e:
			# print(e)
		else:
			d.click(250, 950)
			time.sleep(2)

		d(text="Facebook").click()

	time.sleep(5)
	# d(text="以后在说").click()
	# 存入数据库
	print(year,month,day)
	db = conn.fbaccount
	fb = db.new
	argudict["email"] = username
	argudict["passwd"] = password
	argudict["birthday"] = "{}".format(year+'-'+month+'-'+day)
	argudict["gender"] = "Female"
	argudict["page"] = "Null"
	argudict["first_name"] = firstname
	argudict["last_name"] = lastname
	argudict['device_argu'] = 'True'
	fb.insert(argudict)
	# time.sleep(random.random()*600)

except JsonRPCError as e:
	print(e)
	pro.remove({"userName":username})
	python3 = sys.executable
	os.execl(python3, python3, * sys.argv)
# 重启程序
python3 = sys.executable
os.execl(python3, python3, * sys.argv)