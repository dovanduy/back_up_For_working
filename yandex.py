from uiautomator import Device
import time
import os
import requests
import re
import random
import time
import sys
from pymongo import MongoClient
from uiautomator import JsonRPCError


conn = MongoClient('mongodb://192.168.1.66:27017/')
db = conn.yandex
yandex = db.account
d = Device('4d51746e')
d.press('home')
d.press('home')


try:         
    if d(text="确定").exists:
        d(text="确定").click()
    #d.press('menu')
    #d(text="设置").click()
    d(text="设置").click()
    time.sleep(1)
    d(text="其他连接方式").click()
    time.sleep(2)
    d(text="飞行模式").click()
    time.sleep(2)
    d(text="飞行模式").click()
    time.sleep(2)
    #os.system('adb -s 4d51746e shell settings put global airplane_mode_on 1')
    #os.system('adb -s 4d51746e shell settings put global airplane_mode_on 0')
    d.press('home')
    # d(text="手机查看器").click()
    # time.sleep(1)
    # d(text="一键改机").click()
    # time.sleep(1)
    # d.press('home')
    os.system("adb -s 4d51746e uninstall ru.yandex.mail")
    time.sleep(1)
    os.system("adb -s 4d51746e install /home/administator/下载/ru.yandex.mail_43964.apk")
    # time.sleep(3)
    d(text="Mail").click()
    time.sleep(2)
    if d(textContains="拒绝").exists:
        d(textContains="拒绝").click()
    time.sleep(1)
    d(text="Register").click()
    text = requests.get('https://www.fakenamegenerator.com/gen-male-us-us.php', timeout=20).text
    name = re.search('''<div class="address">
                                        <h3>([\w\W]+?)</h3>''', text).groups()[0]
    nameGroup = re.match('([\w]+) ([\w\W]+)', name).groups()
    firname = nameGroup[0]
    lastname = nameGroup[1]
    lastname = re.sub('([\w]+)\. ([\w]+)', r'\1\2', lastname)
    
    password = ''
    # a list for makeing password.
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(12):
        password += random.choice(words)

    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    username = ''
    for i in range(8):
        username += random.choice(words)
    for i in range(4):
        username += random.choice(num)

    request_token = requests.get('http://api.ema666.com/Api/userLogin?uName=wangzeming666&pWord=123456789&Developer=Cnp%2bioCFjIENLUVatRXU6g%3d%3d',timeout=10)
    token = re.match(r'([\w\W]+?)&', request_token.text).group(1)
    print(token)
    number = requests.get('http://api.ema666.com/Api/userGetPhone?ItemId=58216&token={}&PhoneType=0'.format(token),timeout=10)
    phonenum = re.match(r'([\d]+);', number.text).group(1)
    # phonenum = '13121312780'
    print(phonenum)
    phonenum86 = '+86'+phonenum
    d(text="First name").set_text(firname)
    time.sleep(1)
    d(text="Last name").set_text(lastname)
    time.sleep(1)
    d(text="Username").set_text(username)
    time.sleep(1)
    d(resourceId="ru.yandex.mail:id/am_account_password").set_text(password)
    time.sleep(1)
    d(resourceId="ru.yandex.mail:id/am_account_password_retype").set_text(password)
    time.sleep(1)
    d(text="Phone number").set_text(phonenum86)
    d.swipe(400,800,400,500)
    time.sleep(2)
    d(text="Next").click()    

    try:
        code = ''
        time.sleep(5)
        codestr = requests.get('http://api.ema666.com/Api/userSingleGetMessage?token={}&itemId=58216&phone={}'.format(token,phonenum), timeout=10).text
        print(codestr)
        code = re.search(r'([\d]{6}|[\d]{5}|[\d]{4})', codestr).group(1)
    except AttributeError:
        count_time = time.time()
        while (time.time() - count_time) < 55:
            time.sleep(5)
            try:
                # if (time.time() - count_time) > 60:
                    # d(text='Resend').click()
                codestr = requests.get('http://api.ema666.com/Api/userSingleGetMessage?token={}&itemId=58216&phone={}'.format(token,phonenum), timeout=10).text
                print(codestr)
                code = re.search(r'([\d]{6}|[\d]{5})', codestr).group(1)
                break
            except AttributeError:
                continue
    if code == '':
        print('验证码平台出错')
        raise Exception
    d(resourceId="ru.yandex.mail:id/am_phone_confirmation").set_text(code)
    time.sleep(2)
    d(text="Next").click()
    if code:
        yandex.insert({"userName":username+'@yandex.com', "passwords":password, "used":0})
        time.sleep(10)
    python3 = sys.executable
    os.execl(python3, python3, * sys.argv)

except (JsonRPCError,Exception,BaseException, requests.exceptions.RequestException) as e:
    print(e)
    
    python3 = sys.executable
    os.execl(python3, python3, * sys.argv)