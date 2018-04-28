#!/usr/bin/python
#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import requests
import sys
import os
import time
import random
from lxml import etree
from pymongo import MongoClient
from base64 import b64encode
from selenium.webdriver.common.action_chains import ActionChains
import hashlib
import commands
from PIL import Image

reload(sys)
sys.setdefaultencoding('utf-8')

def md5(str):
	m = hashlib.md5()
	m.update(str)
	return m.hexdigest()

def getcode():
	url = "http://api.dama2.com:7766/app/d2File"
	appID = "52178"
	type = "44"
	key = "966b14d646d0c90703b4db3b4b462d3a"
	user = "weihc"
	password = "wei4480560"
	u = md5(user)
	p = md5(password)
	u_p = u + p 
	tmp = md5(u_p)
	tmp_k = key + tmp
	pwd = md5(tmp_k)
	f = open("code.jpg","rb")
	content = f.read()
	fileDataBase64 = b64encode(content)
	tmp = key + user + content
	sign = md5(tmp)[0:8]
	f.close()
	payload = {"appID":appID,"user":user,"pwd":pwd,"type":type,"fileDataBase64":fileDataBase64,"sign":sign}
	r = requests.post(url
		,data=payload)
	code = r.json()['result']
	return code
	
def name_generator(url):
	r = requests.get(url)
	r = etree.HTML(r.text)
	name = r.xpath('//*[@id="details"]/div[2]/div[2]/div/div[1]/h3/text()')[0]
	birthday = r.xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[6]/dd/text()')[0]
	print name
	print birthday
	#ru_email(name,birthday)

def ru_email(name, birthday):
	useragent = ["Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 MicroMessenger/6.5.8 NetType/2G Language/zh_CN","Mozilla/5.0 (iPhone 5SGLOBAL; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.4.1 Mobile/14E304 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1"]
	ip_num = random.randint(0,1)
	flag = False
	a = name.split(" ")
	first_name = a[0]
	last_name = a[2]
	mail = first_name + "." + a[1] + last_name
	b = birthday.split(" ")
	year = b[2]
	month_before = b[0]
	month = month_change(str(month_before))
	day = b[1].split(",")[0]
	profile = webdriver.FirefoxProfile() # add proxy
	profile.set_preference("general.useragent.override", useragent[0])
	profile.set_preference('network.proxy.type', 1)
	#profile.set_preference('network.proxy.http','58.181.39.182')
	#profile.set_preference('network.proxy.http_port', 80)
	profile.set_preference('network.proxy.socks', '127.0.0.1')
	profile.set_preference('network.proxy.socks_port', 1080)
	profile.set_preference('network.proxy.socks_remote_dns', True)
	#profile.set_preference('network.proxy.ssl', '183.89.95.29')
	#profile.set_preference('network.proxy.ssl_port', 8080)
	# Proxy auto login
	#profile.add_extension('firebug.xpi')
	#profile.add_extension('FireXPath.xpi')
	#profile.add_extension('closeproxy.xpi')
	#credentials = '{shijihetu}:{shijihetu}'
	#credentials = b64encode(credentials.encode('ascii')).decode('utf-8')
	#profile.set_preference('extensions.closeproxyauth.authtoken', credentials)
	profile.update_preferences()
	driver = webdriver.Firefox(profile)
	#driver = webdriver.Firefox()
	driver.delete_all_cookies()
	driver.get("https://account.mail.ru/signup/simple")
	time.sleep(random.randint(2,5)) 
	handle = driver.current_window_handle
	# 切换标签页，获取密码
	js = 'window.open("https://security.mail.ru/#passgen")'
	driver.execute_script(js)
	handles = driver.window_handles
	for i in handles:
		if i != handle:
			driver.switch_to_window(i)
	while True:
		try:
			driver.find_element_by_xpath("//*[@id='create']/span[1]").click()
			flag = True
		except NoSuchElementException:
			time.sleep(random.randint(2,5))
		if flag:
			break
	time.sleep(random.randint(2,5))
	passwd = driver.find_element_by_xpath("//*[@id='total-code']").get_attribute("value")
	driver.close()
	driver.switch_to_window(handle)
	first_name_elem = driver.find_element_by_xpath(
		".//*[@id='app-canvas']/div/div/div/div[1]/div[2]/form/div[3]/div/div/div[1]/div/div[2]/div[1]/input")
	first_name_elem.send_keys(first_name)
	time.sleep(random.randint(2,5)) 
	last_name_elem = driver.find_element_by_xpath(
		".//*[@id='app-canvas']/div/div/div/div[1]/div[2]/form/div[3]/div/div/div[2]/div/div[2]/div[1]/input")
	last_name_elem.send_keys(last_name)
	time.sleep(random.randint(2,5))
	day_elem = driver.find_element_by_xpath('//*[@id="app-canvas"]/div/div/div/div[1]/div[2]/form/div[4]/div/div[2]/div[1]/div[1]/div[2]/div[1]').click()
	time.sleep(random.randint(2,5))
	driver.find_element_by_class_name('b-dropdown__list').find_elements_by_class_name(
		'b-dropdown__list__item__text')[int(day) - 1].click()
	month_elem = driver.find_element_by_xpath(
		'//*[@id="app-canvas"]/div/div/div/div[1]/div[2]/form/div[4]/div/div[2]/div[1]/div[1]/div[2]/div[2]').click()
	time.sleep(random.randint(2,5))
	driver.find_element_by_xpath(
		'//*[@id="app-canvas"]/div/div/div/div[1]/div[2]/form/div[4]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]').find_elements_by_class_name(
		'b-dropdown__list__item__text')[month].click()
	year_elem = driver.find_element_by_xpath(
		'//*[@id="app-canvas"]/div/div/div/div[1]/div[2]/form/div[4]/div/div[2]/div[1]/div[1]/div[2]/div[3]').click()
	time.sleep(random.randint(2,5))
	driver.find_element_by_xpath(
		'//*[@id="app-canvas"]/div/div/div/div[1]/div[2]/form/div[4]/div/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]').find_elements_by_class_name(
		'b-dropdown__list__item__text')[2017 - int(year)].click()

	sex_elem = driver.find_element_by_xpath(
		'//*[@id="app-canvas"]/div/div/div/div[1]/div[2]/form/div[5]/div/div[2]/div[1]/div[1]/div[3]/label/span/input').click()
	mail_elem = driver.find_element_by_xpath(
		".//*[@id='app-canvas']/div/div/div/div[1]/div[2]/form/div[6]/div/div[2]/div[1]/div/div[1]/span[3]/input")
	time.sleep(random.randint(2,5))
	mail_elem.send_keys(mail)
	passwd_id = driver.find_element_by_xpath(
		".//*[@id='app-canvas']/div/div/div/div[1]/div[2]/form/div[8]/div/div[1]/label").get_attribute("for")
	passwd_elem = driver.find_element_by_xpath(".//*[@id='{}']".format(passwd_id))
	time.sleep(random.randint(2,5))
	passwd_elem.send_keys(passwd)
	print passwd
	time.sleep(random.randint(2,5))
	passwd_again_elem = ""
	while True:
		try:
			passwd_again_elem = driver.find_element_by_xpath('//*[@id="passwordRetry"]')
			break
		except NoSuchElementException:
			time.sleep(random.randint(2,5))
	passwd_again_elem.send_keys(passwd)
	try:
		driver.find_element_by_class_name("b-form-field__errors__error js-invalid_login_invalid_length js-error")
		mail_elem.clear()
		num = random.randint(100, 99999)
		mail = mail + str(num)
		mail_elem.send_keys(mail)
	except NoSuchElementException:
		pass
	time.sleep(random.randint(2,5))
	register_elem = driver.find_element_by_xpath(
		".//*[@id='app-canvas']/div/div/div/div[1]/div[2]/form/div[12]/div[1]/button")
	register_elem.click()
	time.sleep(random.randint(2,5))
	flag = 0
	try:
		driver.find_element_by_name("phone.phone")
		print 'need tel'
		driver.close()
	except NoSuchElementException:
		flag = 1
	'''
	try:
		assert "Ошибка сервера, попробуйте позже"  in driver.page_source
		print 'server error'
	except NoSuchElementException:
		flag = 1
	'''

	if flag == 1:
		code_elem = ''
		while True:
			try:
				code_elem = driver.find_element_by_xpath('//*[@id="app-canvas"]/div/div/div/div/div[3]/form/div[2]/div/div/div/div/div/input')
				break
			except NoSuchElementException:
				time.sleep(random.randint(2,5))

		time.sleep(random.randint(15,25))
		driver.save_screenshot("code1.png")
		code_element = driver.find_element_by_xpath('//*[@id="app-canvas"]/div/div/div/div[1]/div[3]/form/div[2]/div/div[1]/div[1]/div/img')
		location = code_element.location
		size = code_element.size
		box = (int(location["x"]),int(location["y"]),int(location["x"] + size["width"]),int(location["y"] + size["height"]))
		image = Image.open("code1.png")
		image = image.convert('RGB')
		newimg = image.crop(box)
		newimg.save("code.jpg")
		email = mail + '@mail.ru'
		info = {"first_name":first_name,"last_name":last_name,"passwd":passwd,"birthday":birthday,"email":email}
		#print info

		flag = 0
		while True:
			flag += 1
			if flag == 4:
				print 'already second,exit'
				driver.close()
				break
			code = getcode()
			code_elem.clear()
			code_elem.send_keys(code)
			time.sleep(random.randint(2,5))
			driver.find_element_by_xpath(".//*[@id='app-canvas']/div/div/div/div[1]/div[3]/form/div[5]/div[1]/button").click()
			time.sleep(random.randint(10,15))
			title = driver.title
			print title
			if title == "Почта@Mail.Ru":
				email = mail + '@mail.ru'
				info = {"first_name":first_name,"last_name":last_name,"passwd":passwd,"birthday":birthday,"email":email}
				print info
				insert_db_doc(info)	
				driver.close()
				flag2 = True
				print "END"
			else:
				print 'code error or server error'
				time.sleep(random.randint(5,7))

			'''
			try:
				driver.find_element_by_xpath(".//*[@id='app-canvas']/div/div/div/div[1]/div[3]/form/div[5]/div[1]/button")
				print 'code error or server error'
			except NoSuchElementException:
				email = mail + '@mail.ru'
				info = {"first_name":first_name,"last_name":last_name,"passwd":passwd,"birthday":birthday,"email":email}
				print info
				insert_db_doc(info)	
				driver.close()
				break
			'''
		'''
		email = mail + '@mail.ru'
		info = {"first_name":first_name,"last_name":last_name,"passwd":passwd,"birthday":birthday,"email":email}
		print info
		insert_db_doc(info)	
		driver.close()
		'''

def insert_db_doc(info):
	client = MongoClient(host="192.168.1.66", port=27017) 
	db = client['app']
	col= db['fb']
	col.insert(info)

def month_change(month):
	if month == "January":
		return 0
	if month == "February":
		return 1
	if month == "March":
		return 2
	if month == "April":
		return 3
	if month == "May":
		return 4
	if month == "June":
		return 5
	if month == "July":
		return 6
	if month == "August":
		return 7
	if month == "September":
		return 8
	if month == "October":
		return 9
	if month == "November":
		return 10
	if month == "December":
		return 11

#https://c.mail.ru/c/6?1513075104242 ru邮箱注册验证码地址
if __name__=='__main__':
	url = "http://www.fakenamegenerator.com/gen-male-us-us.php"	
	name_generator(url)
	'''
	while True:
		ip_proxy = ["96.8.118.107","192.210.205.107","192.210.205.108","96.8.118.106","172.245.170.163"]
		for ip in ip_proxy:
			cmd = "sslocal -s {} -p 8688 -b 127.0.0.1 -l 1080 -k shijihetu520 -m aes-256-cfb -d start".format(ip)
			result = commands.getoutput(cmd)
			url = "http://www.fakenamegenerator.com/gen-male-us-us.php"	
			name_generator(url)
			time.sleep(3600)
			cmd = "sslocal -s {} -p 8688 -b 127.0.0.1 -l 1080 -k shijihetu520 -m aes-256-cfb -d stop".format(ip)
			result = commands.getoutput(cmd)
	'''
