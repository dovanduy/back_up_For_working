#from uiautomator import device as d
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
# from uiautomator.builtins import Exception, BaseException


d = Device('6b862e8')
conn = MongoClient('mongodb://192.168.1.66:27017/')
db = conn.proemail
proton = db.account
d.press('home')
d.press('home')
d.press('home')
try:         
    #d.press('menu')
    #d(text="设置").click()
    d(text="设置").click()
    time.sleep(1)
    d(text="其他连接方式").click()
    time.sleep(1)
    d(text="飞行模式").click()
    time.sleep(2)
    d(text="飞行模式").click()
    time.sleep(2)
    #os.system('adb -s 6b862e8 shell settings put global airplane_mode_on 1')
    #os.system('adb -s 6b862e8 shell settings put global airplane_mode_on 0')
    # d.press('home')
    # d(text="手机查看器").click()
    # time.sleep(1)
    # d(text="一键改机").click()
    # time.sleep(1)
    d.press('home')
    os.system("adb -s 6b862e8 uninstall ch.protonmail.android")
    os.system("adb -s 6b862e8 install /home/administator/protonmail.apk")
    d(descriptionContains="ProtonMail").click()
    time.sleep(1)
    d(text="Create Account").click()
    time.sleep(1)
    d(resourceId="ch.protonmail.android:id/expand_free").click()
    time.sleep(1)
    d(text="Select").click()
    text = requests.get('https://www.fakenamegenerator.com/gen-male-us-us.php', timeout=60).text
    name = re.search('''<div class="address">
                                        <h3>([\w\W]+?)</h3>''', text).groups()[0]
    nameGroup = re.firname = re.match('([\w]+) ([\w\W]+)', name).groups()
    firname = nameGroup[0]                                                                                                                                          
    lastname = nameGroup[1]
    lastnameNoPoint = re.sub('([\w]+)\. ([\w]+)', r'\1\2', lastname)
    emailpart = firname + lastnameNoPoint
    password = ''
    # a list for makeing password.
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(12):
        password += random.choice(words)

    emailaccount = emailpart+"@protonmail.com"
    d(resourceId="ch.protonmail.android:id/username").set_text(emailpart)
    d.click(660, 1220)
    d(resourceId="ch.protonmail.android:id/sign_up").click()
    time.sleep(1)
    #d(text="Password").click()
    d(resourceId="ch.protonmail.android:id/password").set_text(password)     
    d(resourceId="ch.protonmail.android:id/confirm_password").set_text(password)
    time.sleep(1)
  
    d.click(660, 1220)
    d(resourceId="ch.protonmail.android:id/generate_keypair").click()
    d.click(665, 805)
    d(resourceId="ch.protonmail.android:id/cont").click()
    d(resourceId="ch.protonmail.android:id/phone_verification").click()
    time.sleep(2)
    d.click(400,550)
    time.sleep(2)
    num = random.random() * 100
    d.swipe(400+num, 900-num, 600+num, 200-num)
    num = random.random() * 100
    d.swipe(400+num, 900-num, 600+num, 200-num)
    num = random.random() * 100
    d.swipe(400+num, 900-num, 600+num, 200-num)
    num = random.random() * 100
    d.swipe(400+num, 900-num, 600+num, 200-num)
    num = random.random() * 100
    d.swipe(400+num, 900-num, 600+num, 200-num)
    num = random.random() * 100
    d.swipe(400+num, 900-num, 600+num, 500-num)
    #d.swipe(400+num, 900-num, 600+num, 200-num)
    #d.swipe(400+num, 900-num, 600+num, 200-num)
    #d.swipe(400+num, 900-num, 600+num, 200-num)
    #d.swipe(400+num, 900-num, 600+num, 200-num)
    time.sleep(1)
    d(text="China").click()
    request_token = requests.get('http://api.ema666.com/Api/userLogin?uName=wangzeming666&pWord=123456789&Developer=Cnp%2bioCFjIENLUVatRXU6g%3d%3d',timeout=60)
    token = re.match(r'([\w\W]+?)&', request_token.text).group(1)
    print(token)
    number = requests.get('http://api.ema666.com/Api/userGetPhone?ItemId=49740&token={}&PhoneType=0'.format(token),timeout=60)
    phonenum = re.match(r'([\d]+);', number.text).group(1)
    print(phonenum)
    d(resourceId="ch.protonmail.android:id/phone_number").set_text(phonenum)
    time.sleep(1)
    d.click(660, 1220)
    time.sleep(1)
    d.click(660, 1220)
    time.sleep(1)
    d.click(670, 800)
    d(text="Send Verification Code").click()
    try:
        code = ''
        time.sleep(5)
        codestr = requests.get('http://api.ema666.com/Api/userSingleGetMessage?token={}&itemId=49740&phone={}'.format(token,phonenum), timeout=60).text
        print(codestr)
        code = re.search(r'([\d]{6}|[\d]{5}|[\d]{4})', codestr).group(1)
    except AttributeError:
        count_time = time.time()
        while (time.time() - count_time) < 60:
            time.sleep(5)
            try:
                codestr = requests.get('http://api.ema666.com/Api/userSingleGetMessage?token={}&itemId=49740&phone={}'.format(token,phonenum), timeout=60).text
                print(codestr)
                code = re.search(r'([\d]{6}|[\d]{5})', codestr).group(1)
                break
            except AttributeError:
                continue
    if code == '':
        print('验证码平台出错')
        raise Exception('unrecive phone code.')
    d(resourceId="ch.protonmail.android:id/verification_code").set_text(code)
    time.sleep(1)
    d.click(660, 1220)
    time.sleep(1)
    d(text="Continue").click()
    time.sleep(40)
    d(text="Display Name").click()
    d.click(660, 1220)
    time.sleep(2)
    d.click(660, 1220)
    time.sleep(2)
    d.swipe(400, 1120, 400, 500)
    d(text="Go to my inbox").click()
    d(text="Yes").click()
    d(text="close tour").click()
    d(text="确定").click()
    # d.press('menu')
    #with open(emailaccount+str(time.time()), 'w') as f:
        #f.write(password)
    proton.insert({"userName":emailaccount, "passwords":password, "used":0})
    # d(text="设置").click()
    # d(text="飞行模式").click()
    # time.sleep(2)
    # d(text="飞行模式").click()
    # time.sleep(1)
    # d.press('menu')
    # d(text="手机修改器").click()
    # d(text="随机").click()
    # d.press('home')
    # os.system("adb uninstall ch.protonmail.android")
    # os.system("adb install /home/administator/下载/ch.protonmail.android_430.apk")
    python3 = sys.executable
    os.execl(python3, python3, * sys.argv)

except (JsonRPCError,Exception,BaseException, requests.exceptions.RequestException) as e:
    print(e)
    with open('error_log', 'r') as f:
        old = f.read()

    with open('error_log', 'w') as f:
        f.write(old)
        f.write(str(e)+'\n')
 
    # d.press('menu')
    # d(text="设置").click()
    # d(text="飞行模式").click()
    # time.sleep(2)
    # d(text="飞行模式").click()
    # time.sleep(1)
    # d.press('menu')
    # d(text="手机修改器").click()
    # d(text="随机").click()
    # d.press('home')
    # os.system("adb uninstall ch.protonmail.android")
    # os.system("adb install /home/administator/下载/ch.protonmail.android_430.apk")    

    python3 = sys.executable
    os.execl(python3, python3, * sys.argv)

    python3 = sys.executable
    os.execl(python3, python3, * sys.argv)
