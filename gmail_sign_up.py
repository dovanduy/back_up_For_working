# gmail_sign_up.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
import os
import requests
import re
import random
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
# clear cookies and open the url.  
driver.delete_all_cookies()
driver.get('https://protonmail.com/signup')
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[5]/div[1]/div[1]/div/div[3]/i[1]').click()
driver.find_element_by_xpath('//*[@id="freePlan"]').click()
# get name that has faked.  
text = requests.get('https://www.fakenamegenerator.com/gen-male-us-us.php').text
name = re.search('''<div class="address">
                                        <h3>([\w\W]+?)</h3>''', text).groups()[0]
nameGroup = re.firname = re.match('([\w]+) ([\w\W]+)', name).groups()
firname = nameGroup[0]
lastname = nameGroup[1]
lastnameNoPoint = re.sub('([\w]+)\. ([\w]+)', r'\1\2', lastname)
emailpart = firname + lastnameNoPoint

time.sleep(10)
for i in emailpart:
	driver.find_element_by_xpath('//*[@id="username"]').send_keys(i)
	time.sleep(random.random()/5)
password = ''
# a list for makeing password.
words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(12):
    password += random.choice(words)
emailAccount = emailpart+"@gmail.com"
time.sleep(1)
print("password: ", password)
for i in password:
	driver.find_element_by_xpath('//*[@id="password"]').send_keys(i)
	time.sleep(random.random()/5)
for i in password:
	driver.find_element_by_xpath('//*[@id="passwordc"]').send_keys(i)
	time.sleep(random.random()/5)
for i in (emailAccount):
	driver.find_element_by_xpath('//*[@id="notificationEmail"]').send_keys(i)
	time.sleep(random.random()/5)
# 检测名字是否有重复
time.sleep(random.random())
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/form/footer/button').click()
time.sleep(10)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/form/div/div/div[3]/label/div').click()
request_token = requests.get('http://api.ema666.com/Api/userLogin?uName=wangzeming666&pWord=wangzeming&Developer=Cnp%2bioCFjIENLUVatRXU6g%3d%3d',timeout=60)
token = re.match(r'([\w\W]+?&)', request_token.text).group(1)
print(token)
number = requests.get('http://api.ema666.com/Api/userGetPhone?ItemId=49740&token={}&PhoneType=0&notPrefix=170|177|171'.format(token),timeout=60)
phonenum = re.match(r'([\d]+);', number.text).group(1)
print(phonenum)
time.sleep(1)
for i in ('+86'+phonenum):
	driver.find_element_by_xpath('/html/body/div[2]/div/div/div/form/div/div/div[7]/form/div[1]/div/input').send_keys(i)
	time.sleep(random.random())
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/form/div/div/div[7]/form/div[2]/button').click()
try:
    code = ''
    time.sleep(5)
    codestr = requests.get('http://api.ema666.com/Api/userSingleGetMessage?token={}&itemId=49740&phone={}'.format(token,phonenum)).text
    print(codestr)
    code = re.search(r'([\d]{6})', codestr).group(1)
except AttributeError:
    count_time = time.time()
    while (time.time() - count_time) < 60:
        time.sleep(5)
        try:
            codestr = requests.get('http://api.ema666.com/Api/userSingleGetMessage?token={}&itemId=49740&phone={}'.format(token,phonenum)).text
            print(codestr)
            code = re.search(r'([\d]{6})', codestr).group(1)
            break
        except AttributeError:
            continue
if code == '':
    print('验证码平台出错')
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/form/div/div/div[7]/div/div[1]/input').send_keys(code)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/form/div/div/p[3]/button').click()
time.sleep(20)
try:
    driver.find_element_by_xpath('/html/body/div[1]/form/div[1]/div[2]/section[2]/div[1]/div[2]/ul/li[2]/a').click()
except NoSuchElementException:
    print('不能选中fb跳转链接')
time.sleep(10)
driver.switch_to_window(driver.window_handles[1])

with open('C://Users/Administrator/Desktop/protonaccount.txt', 'r') as f:
	oldemail = f.read()

with open('C://Users/Administrator/Desktop/protonaccount.txt', 'w') as f:
	for i in oldemail:
		f.write(i)
		f.write(emailAccount+'\n')
		f.write(password+'\n')
time.sleep(20)
situation = 0
try:
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]/a').click()

    ssituation = 1
except ElementNotInteractableException:
    count_time = time.time()
    while (time.time() - count_time) < 300:
        time.sleep(10)
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]/a').click()
            situation = 1
            break
        except ElementNotInteractableException:
            continue
except NoSuchElementException:
	driver.find_element_by_xpath('/html/body/div[1]/form/div[1]/div[2]/section[2]/div[1]/div[2]/ul/li[2]/a').click()                               
if situation == 0:
    print('网络原因，浏览器无法加载页面。')

time.sleep(5)

for i in firname:
    driver.find_element_by_xpath('//*[@id="u_0_m"]').send_keys(i)
    time.sleep(random.random()/5)
for i in lastname:
	driver.find_element_by_xpath('//*[@id="u_0_o"]').send_keys(i)
	time.sleep(random.random()/5)
emailAccount = emailpart + '@protonmail.com'
for i in emailAccount:
	driver.find_element_by_xpath('//*[@id="u_0_r"]').send_keys(i)
	time.sleep(random.random()/5)
for i in emailAccount:
	driver.find_element_by_xpath('//*[@id="u_0_u"]').send_keys(i)
	time.sleep(random.random()/5)
for i in password:
	driver.find_element_by_xpath('//*[@id="u_0_y"]').send_keys(i)
	time.sleep(random.random()/5)
month_options = driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/form/div[1]/div[6]/div[2]/span/span/select[2]/option')[1:]
random.choice(month_options).click()
time.sleep(random.random())
day_options = driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/form/div[1]/div[6]/div[2]/span/span/select[1]/option')[1:-1]
random.choice(day_options).click()
time.sleep(random.random())
year_options = driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/form/div[1]/div[6]/div[2]/span/span/select[3]/option')[20:40]
random.choice(year_options).click()
time.sleep(random.random())
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[1]/label').click()
driver.find_element_by_xpath('//*[@id="u_0_14"]').click()
time.sleep(5)
driver.switch_to_window(driver.window_handles[0])
driver.find_element_by_xpath('/html/body/div[1]/form/div[2]/button').click()
try:
    code = ''
    message = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/section/div[1]/div[2]/div[1]/h4/span[2]').text
    code = re.match('[\d]{5}', message)
except AttributeError:
    count_time = time.time()
    while (time.time() - count_time) < 300:
        time.sleep(5)
        try:
            message = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/section/div[1]/div[2]/div[1]/h4/span[2]').text
            code = re.match('[\d]{5}', message)
            break
        except AttributeError:
            continue
if code == '':
    print('未知原因无法接到邮件验证')

with open('C://Users/Administrator/Desktop/fbaccount.txt', 'r') as f:
    old = f.read()

with open('C://Users/Administrator/Desktop/fbaccount.txt', 'w') as f:
    for i in old:
        f.write(i)
    print(emailAccount)
    f.write(emailAccount+'\n')
    f.write(password+'\n')