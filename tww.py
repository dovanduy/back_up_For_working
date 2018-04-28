#!/usr/bin/python
#coding=utf-8
import os
from uiautomator import Device
from uiautomator import JsonRPCError
from pymongo import MongoClient
import commands
from multiprocessing import Pool
import random
import time
import logging
from logging import handlers
import sys

reload(sys)
# sys.setdefaultencoding( "utf-8" )
#第一步，创建一个logger
# debug_logger = logging.getLogger("process.debug")
# debug_logger.setLevel(logging.DEBUG)
# #第二步，创建一个handler，用于写入日志文件
# debug_logfile = './tw_register.log'
# debug_fh = logging.handlers.RotatingFileHandler(debug_logfile,mode='w',maxBytes=1024*1024*10,backupCount=100)
# debug_fh.setLevel(logging.DEBUG)
# #第三步，定义handler的输出格式
# formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s")
# debug_fh.setFormatter(formatter)
# #第四步，将logger添加到handler里面
# debug_logger.addHandler(debug_fh)





def tw_up_dev(device,doc):
	'''
	cmd = "adb -s {} install Twitter.apk".format(device)
	result = os.popen(cmd).read()
	if "Success" in result:
		pass 
	else:
		return 500
	'''
	cmd = 'adb -s {} shell "su -c" am start -n com.twitter.android/.DispatchActivity'.format(device)
	result = os.popen(cmd).read()
	if "Starting: Intent { cmp=com.twitter.android/.DispatchActivity }" in result:
		d = Device(device)
		if d.screen == "off":
			d.wakeup()
		d.watcher("fbui_tooltip").when(resourceId="com.yulong.android.seccenter:id/alertdlg_forbid").click(resourceId="com.yulong.android.seccenter:id/alertdlg_forbid")
		d.watchers.run()
		x = tw_register(d,device,doc)
		return x
	else:
		return 501


def tw_register(d,device,doc):
	print("tw_register")
	name = doc["name"]
	password = doc["password"]
	email = doc["email"]
	print(name)
	print(password)
	print(email)
	time.sleep(random.randint(2,5))
	# Get started
	if d(resourceId="com.twitter.android:id/cta_button").exists:	# click start
		d(resourceId="com.twitter.android:id/cta_button").click()
	time.sleep(random.randint(5,7))
	if d(resourceId="com.twitter.android:id/name_entry").exists:
		d(resourceId="com.twitter.android:id/name_entry").click()
	# 输入name
	# cmd = "adb -s {} shell input text '{}'".format(device,name)
	time.sleep(random.randint(2,5))
	if d.watchers.triggered:
		d.watchers.reset()
	cmd = "adb -s {} shell am broadcast -a ADB_INPUT_TEXT --es msg '{}'".format(device,name)
	os.system(cmd)
	time.sleep(random.randint(2,5))
	# Next
	if d(resourceId="com.twitter.android:id/cta").exists:
		d(resourceId="com.twitter.android:id/cta").click()
	# Use email 
	if d(resourceId="com.twitter.android:id/signup_options").exists:
		ui = d(resourceId="com.twitter.android:id/signup_options").info
		x = ui["bounds"]["left"]
		y = ui["bounds"]["top"]
		d.click(x,y)
	# 输入邮箱
	if d(resourceId="com.twitter.android:id/email_entry").exists:
		d(resourceId="com.twitter.android:id/email_entry").click()
		cmd = "adb -s {} shell input text '{}'".format(device,email)
		os.system(cmd)
	time.sleep(random.randint(7,9))
	# Next
	if d(resourceId="com.twitter.android:id/cta").exists:
		d(resourceId="com.twitter.android:id/cta").click()


#  ---------------------下面还没改完


	time.sleep(random.randint(2,5))
	#if d(resourceId="com.twitter.android:id/primary_text").exists:
	if d(resourceId="com.twitter.android:id/cta_button").exists:
		d(text="Sign up").click()
		debug_logger.info("Sign up")
		print("Sign up")
		#break
	'''
	else:
		time.sleep(random.randint(4,7))
		n += 1
		if n > 5:
			return 503
	'''
	time.sleep(random.randint(6,7))
	# 输入密码
	if d(resourceId="com.twitter.android:id/text_field").exists:
		print("password")
		d(resourceId="com.twitter.android:id/text_field").click()
		cmd = "adb -s {} shell input text '{}'".format(device,password)
		os.system(cmd)
	time.sleep(random.randint(2,5))
	if d(resourceId="com.twitter.android:id/cta_button").exists:
		d(text="Next").click()

	time.sleep(random.randint(7,8))

	if d(resourceId="com.twitter.android:id/button_negative").exists:
		d(text="Not now").click()
	time.sleep(random.randint(7,8))

	if d(resourceId="com.twitter.android:id/cta_button").exists:
		d(text="Skip for now").click()
	time.sleep(random.randint(7,8))

	if d(resourceId="com.twitter.android:id/cta_button").exists:
		d(resourceId="com.twitter.android:id/cta_button").click()

	time.sleep(random.randint(7,8))
	d.watchers.remove()
	if d(resourceId="com.twitter.android:id/moments").exists:
		return 200
	else:
		return 504
	

def get_devices():
	cmd = "adb devices | awk '{print $1}'"
	devices = os.popen(cmd).readlines()
	devices.pop()
	devices.pop(0)
	devices = [x.rstrip() for x in devices]
	return devices
	

def find_db_doc(col,sql):
	result = []
	docs = col.find(sql[0],sql[1])
	for doc in docs:
		result.append(doc)
	return result


def db_connect():
	client = MongoClient(host="192.168.1.66", port=27017) 
	db = client['app']
	col= db['tw']
	return col

def update_db_doc(col,sql):
	col.update(sql[0],sql[1])


def tw_register_main():
	code_list = []
	devices = get_devices()	
	col = db_connect()
	sql = [{"device":{"$exists":False}},{"_id":0}]
	docs = find_db_doc(col,sql)    #找到所有不包含device字段的doc,拿出来进行注册
	for device_index,device in enumerate(devices):
		if device in ["104b46b","1f54bac","be61d8","28f44d3","bb3009","208bbc9","ba506d"]:
			pass
		else:
			doc = docs[device_index]
			print(doc)
			print(device)
			x = tw_up_dev(device,doc)
			if x == 200:
				sql = [{"email":dco["email"]},{"$set":{"device":device}}]
				update_db_doc(col,sql)
			else:
				data = "device:{},doc:{}".format(device,doc)
				debug_logger.info(data)
			code = {}
			code["device"] = x
			code_list.append(code)
			debug_logger.info(code_list)
			print(code_list)




if __name__=='__main__':
	tw_register_main()
