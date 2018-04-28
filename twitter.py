# twitter.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
import os
import requests
import re
import random
import time
from pymongo import MongoClient
import sys


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
prousers = [i['userName'] for i in prolist]
# 从proton邮箱列表中选出未注册过的帐号
index = -1
for i in prousers:
	index += 1
	if i not in twusers:
		username = i
		password = prolist[index]['passwords']
		break




# profile = webdriver.FirefoxProfile() # add proxy
# profile.set_preference('network.proxy.type', 1)
# profile.set_preference('network.proxy.socks', '127.0.0.1')
# profile.set_preference('network.proxy.socks_port', 1080)
# profile.set_preference('network.proxy.socks_remote_dns', True)
# profile.update_preferences()
# driver = webdriver.Firefox(profile)
# driver = webdriver.Chrome()
# driver.delete_all_cookies()
# driver.implicitly_wait(10)
print(username)
print(password)
a = input('aaaaaa')
# driver.get("https://twitter.com/")
# time.sleep(2)
# os.system('xdotool mousemove 1609, 623 click 1 ')
# for i in username:
# 	driver.find_element_by_xpath('//*[@id="doc"]/div/div[1]/div[1]/div[2]/form/div[1]/input').send_keys(i)
# # 	os.system('xdotool type '+i)
# 	time.sleep(random.random()/5)
# # os.system('xdotool mousemove 1607 708 click 2 ')
# time.sleep(10)
# try:
# 	for i in password:
# 		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/form/div[2]/input').send_keys(i)
# # 		os.system('xdotool type '+i)
# 		time.sleep(random.random()/5)
# except ElementNotInteractableException as e:
# 	print(e)
# 	driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/form/div[2]/input').click()

# time.sleep(random.random())
# driver.find_element_by_xpath('//*[@id="doc"]/div/div[1]/div[1]/div[2]/form/div[3]/button').click()
# try:
# 	driver.find_element_by_xpath('//*[@id="doc"]/div/div[1]/div[1]/div[2]/form/div[3]/button').click()
# except (ElementNotInteractableException, ElementNotVisibleException):
# 	pass

# try:
# 	driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/form/div[3]/button').click()
# except (ElementNotInteractableException, ElementNotVisibleException):
# 	pass
# time.sleep(random.random())
# time.sleep(10)
# try:
# 	if driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/form/div[1]/div[1]').text == '请输入有效的邮箱地址。':
# 		pro.remove({"userName": username})
# 		driver.close()
# 		python3 = sys.executable
# 		os.execl(python3, python3, * sys.argv)
# except NoSuchElementException as e:
# 	print(e)

# for i in re.match('[\w]+', username).group():
# 	driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/form/div[4]/div[1]/input').send_keys(i)
# 	time.sleep(random.random()/5)
# time.sleep(random.random())
# driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/form/div[4]/button').click()
# time.sleep(random.random())
# driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div[3]/div[2]/a').click()
# time.sleep(random.random())
# driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div[3]/div[2]/a').click()
# time.sleep(random.random())
# driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div/a').click()
# time.sleep(random.random())
# driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/button').click()
# time.sleep(random.random())
# driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/a').click()
# time.sleep(random.random())
# driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/button').click()
# time.sleep(random.random())
# driver.find_element_by_xpath('/html/body/div[41]/div/div[3]/button').click()
# time.sleep(random.random())
# driver.find_element_by_xpath('/html/body/div[38]/div[2]/div[3]/div[1]/div[1]/button').click()
# time.sleep(random.random())
# driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div/div/button').click()
# time.sleep(random.random())

driver = webdriver.Chrome()
driver.delete_all_cookies()
driver.implicitly_wait(10)
driver.get('https://protonmail.com/')
driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul/li[7]/a').click()
time.sleep(random.random())
driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
time.sleep(random.random())
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
time.sleep(random.random())
driver.find_element_by_xpath('//*[@id="login_btn"]').click()
time.sleep(random.random())

try:
	obj = driver.find_element_by_xpath('//*[@id="conversation-list-columns"]/section/div[1]/div[2]/div[1]/h4').click()
	# if re.serch('Confirm Your Twitter ... ', obj.text) exist
	# then click()
except NoSuchElementException as e:
	print(e)
	time.sleep(5)
	obj = driver.find_element_by_xpath('//*[@id="conversation-list-columns"]/section/div[1]/div[2]/div[1]/h4').click()

driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/element-view/div/section/div/article/div[2]/div[3]/div/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table[1]/tbody/tr/td[2]/table/tbody/tr[8]/td/table/tbody/tr/td/a').click()
time.sleep(5)
driver.quit()
tw.insert({"userName" : username, "password" : password})


# reboot
python3 = sys.executable
os.execl(python3, python3, * sys.argv)