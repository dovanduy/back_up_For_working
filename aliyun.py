import os
import requests
import re
import random
import time
import math
import operator
from functools import reduce
from PIL import Image
import os
import threading
from pymongo import MongoClient
import sys


def input_phonenum(phonenum):

    ''' It was like the function name. '''

    x = 1130
    y = 285
    if random.choice(status) == 1:
        x -= random.random()*50
        y -= random.random()*10
    else:
        x += random.random()*50
        y += random.random()*10

    os.system('xdotool mousemove {} {} click 1'.format(x, y))
    time.sleep(random.random()*3)
    for i in phonenum:
        os.system('xdotool type "{}"'.format(i))
        time.sleep(random.random())


def move():

    '''this is used for move the slider.  '''

    x = 920+random.random()*10
    os.system('xdotool mousemove {} 350'.format(x))
    os.system('xdotool mousedown 1')
    time.sleep(random.randint(10,15)/10+random.random()*2)
    y = 350

    while x < 1200:
        length = random.random()*random.random()*45
        x += length
        symble = random.choice(status)
        # if symble == 1:
        y -= random.random()
        # else:
        #     y -= random.random()

        os.system('xdotool mousemove {} {}'.format(x, y))

    os.system('xdotool mouseup 1')


########################################
#
# pixel recongnition.
# 
# if confirm was wrong, refresh it.
#
########################################


def refresh():

    '''this is used for refresh the confirm part.'''

    x = 1045 
    y = 345
    if random.choice(status) == 1:
        x -= random.random()*5
        y -= random.random()
    else:
        x += random.random()*5
        y += random.random() 

    os.system("xdotool mousemove {} {} click 1".format(x, y))


def left_part(argu):

    ''' To finish some left work. '''

    time.sleep(1)
    if argu == 0:
        os.system("xdotool mousemove 900 410 click 1")

    time.sleep(1)
    x = 990
    y = 450
    if random.choice(status) == 1:
        x -= random.random()*5
        y -= random.random()
    else:
        x += random.random()*5    
        y += random.random()
    os.system("xdotool mousemove {} {} click 1".format(x, y))


def input_phone_code(code):

    ''' it is just like the function name'''

    x = 960 
    y = 425
    if random.choice(status) == 1:
        x -= random.random()*40
        y -= random.random()*5
    else:
        x += random.random()*40    
        y += random.random()*5
    os.system('xdotool mousemove {} {} click 1'.format(x, y))
    time.sleep(random.random())
    for i in code:
        os.system('xdotool type "{}"'.format(i))
        time.sleep(random.random())

    time.sleep(random.random())
    x = 965 
    y = 510
    if random.choice(status) == 1:
        x -= random.random()*40
        y -= random.random()*5
    else:
        x += random.random()*40    
        y += random.random()*5
    os.system('xdotool mousemove {} {} click 1'.format(x, y))    


def input_emailAdress(email,pwd):

    ''' input something'''

    # input emailAdress
    x = 1000 
    y = 343
    if random.choice(status) == 1:
        x -= random.random()*40
        y -= random.random()*5
    else:
        x += random.random()*40    
        y += random.random()*5
    os.system('xdotool mousemove {} {} click 1'.format(x, y))
    time.sleep(random.random()*3)
    for i in email:
        os.system('xdotool type "{}"'.format(i))
        time.sleep(random.random())
    
    # input password
    x = 1000 
    y = 475
    if random.choice(status) == 1:
        x -= random.random()*40
        y -= random.random()*5
    else:
        x += random.random()*40    
        y += random.random()*5
    os.system('xdotool mousemove {} {} click 1'.format(x, y))
    time.sleep(random.random()*3)
    for i in pwd:
        os.system('xdotool type "{}"'.format(i))
        time.sleep(random.random())
    
    # input pwd again
    x = 1000 
    y = 535
    if random.choice(status) == 1:
        x -= random.random()*40
        y -= random.random()*5
    else:
        x += random.random()*40    
        y += random.random()*5
    os.system('xdotool mousemove {} {} click 1'.format(x, y))
    time.sleep(random.random()*3)
    for i in pwd:
        os.system('xdotool type "{}"'.format(i))
        time.sleep(random.random())


    time.sleep(3)
    # submit.
    x = 990 
    y = 600 
    if random.choice(status) == 1:
        x -= random.random()*40
        y -= random.random()*5
    else:
        x += random.random()*40    
        y += random.random()*5
    os.system('xdotool mousemove {} {} click 1'.format(x, y))
    time.sleep(random.random()*3)
    os.system('xdotool mousemove {} {} click 1'.format(x, y))
    time.sleep(random.random()*5)

    
################################################
#
# pixel recongnition.
#
# if emailAdress has existed, then handle this.
#
################################################


##########################################
#
# get phone number and recive the code.
#
##########################################



########################################
#
# pixel recongnition.
# 
# if phone number repeat, get new one.
#
########################################


def test_drop_block():
    im = GrabWindow(894, 329, 1196, 365)
    if compare_picture(im, 'drop_the_block_error.png') == 0:
        return 1
    else:
        # maybe you need compare it with the picture be named with 'drop_the_block_right.png'
        return 0


def test_phonenum():
    im = GrabWindow(894, 471, 1200, 500)
    if compare_picture(im, 'phone_number_OK.png') == 0:
        return 0
    else:
        # maybe you need compare it with the picutre be named with 'phone_number_OK.png'
        return 1


def test_email():
    im = GrabWindow(894, 624, 1200, 650)
    if compare_picture(im, 'email_repeat_error.png') == 0:
        return 1
    else:
        # there is not a picture can be used for compare that is right.  
        return 0


def change_ip(ip, port=17125, pwd=1234, way='rc4-md5'):
    # kill the old ss connection and start a new one.  
    os.system("kill -9 `ps -ef| grep sslocal | awk '{print $2}'`")
    time.sleep(random.random())
    t1 = threading.Thread(target=lambda :os.system('sslocal -s {} -p {} -k {} -m {} > sslog'.format(ip, port, pwd, way)))
    t1.start()
    time.sleep(5)
    print('ss has been changed!')


def GrabWindow(x1,y1,x2,y2):
    # grab the full of window.
    os.system("scrot -e 'cp $f picture.png'")
    # crop an area of picture that you needed.
    im = Image.open('picture.png')
    box = (x1, y1, x2, y2)
    im = im.crop(box)
    return im


def compare_picture(im, picture):
    # the second argu is a road of picure that you want read from your local sdcard.
    pass
    pass
    im1 = im.histogram()
    picture = Image.open(picture)
    im2 = picture.histogram()
    '''sqrt:计算平方根，reduce函数：前一次调用的结果和sequence的下一个元素传递给operator.add
    operator.add(x,y)对应表达式：x+y
    这个函数是方差的数学公式：S^2= ∑(X-Y) ^2 / (n-1)
    '''
    result = math.sqrt(reduce(operator.add, list(map(lambda a,b:(a-b)**2, im1, im2)))/len(im1))
    #result的值越大，说明两者的差别越大；如果result=0,则说明两张图一模一样
    print(result)
    if result > 0:
        return 0
    if result == 0:
        return 1
    ####################################
    #
    # test it and write your coding.
    #
    ####################################


def clear_cookies():

    os.system('xdotool mousemove 1900 70 click 1')
    time.sleep(0.5)
    os.system('xdotool mousemove 1700 365 click 1')
    time.sleep(0.5)
    os.system('xdotool mousemove 1500 430 click 1')
    time.sleep(1)
    os.system('xdotool mousemove 1200 785 click 1')
    time.sleep(1)
    os.system('xdotool mousemove 150 35 click 1')
    time.sleep(1)
    # os.system('xdotool key F5')
    # time.sleep(0.5)
    os.system('xdotool mousemove 300 70 click 1')
    time.sleep(0.5)
    os.system('xdotool type "https://mailsso.mxhichina.com/aliyun/register?lang=zh_CN"')
    time.sleep(0.5)
    os.system('xdotool key Return')


def get_phonenum(token):
    
    number = requests.get('http://api.ema666.com/Api/userGetPhone?ItemId=61&token={}&PhoneType=0'.format(token),timeout=60)
    phonenum = re.match(r'([\d]+);', number.text).group(1)
    print(phonenum)
    return phonenum


def recive_phone_code(token, phonenum):
    t = time.time()
    while (time.time() - t) < 60:
        time.sleep(5)
        try:
            codestr = requests.get('http://api.ema666.com/Api/userSingleGetMessage?token={}&itemId=61&phone={}'.format(token,phonenum), timeout=60).text
            print(codestr)
            code = re.search(r'([\d]{6})', codestr).group(1)
            break
        except Exception:
            pass
    return code


def first_step(argu=0):
    phonenum = get_phonenum(token)
    input_phonenum(phonenum)
    time.sleep(random.random()*5)
    move()
    time.sleep(random.random()*10)
    while test_drop_block() == 0:
        refresh()
        time.sleep(random.random()*5)
        move()
        time.sleep(random.random()*5)
    left_part(argu)
    return phonenum


def clear_phonenum_input():
    x = 1130 
    y = 285
    os.system('xdotool mousemove {} {} click 1'.format(x, y))
    os.system('xdotool mousemove {} {} click 1'.format(x, y))
    time.sleep(random.random())
    os.system('xdotool key BackSpace')


def clear_email_input():
    x = 1000 
    y = 343
    if random.choice(status) == 1:
        x -= random.random()*100
        y -= random.random()*5
    else:
        x += random.random()*100
        y += random.random()*5
    os.system('xdotool mousemove {} {} click 1'.format(x, y))
    os.system('xdotool mousemove {} {} click 1'.format(x, y))
    time.sleep(random.random())
    os.system('xdotool key BackSpace')


def make_account():
    pwd = ''
    email = ''
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(12):
        pwd += random.choice(words)
        email += random.choice(words)
        for i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            words.append(i)
    return pwd, email    


def get_ip():
    db = conn.ssArgu
    ss = [i for i in db.tt.find().sort('times', 1)][0]
    # 设置信号量
    ss['times'] = ss['times'] + 1
    ip = ss['ip']
    db.tt.update({'ip':ss['ip']}, ss)
    return ip


def insert_account(email, pwd):

    db = conn.emailAccount
    aliyun = db.aliyun
    aliyun.insert({"username":email, "password":pwd})


if __name__ == '__main__':
    conn = MongoClient('mongodb://192.168.1.66:27017/')
    ip = get_ip()
    change_ip(ip)
    status = [1,0,0]
    request_token = requests.get('http://api.ema666.com/Api/userLogin?uName=wangzeming666&pWord=123456789&Developer=Cnp%2bioCFjIENLUVatRXU6g%3d%3d',timeout=60)
    token = re.match(r'([\w\W]+?&)', request_token.text).group(1)
    print(token)
    clear_cookies()
    time.sleep(10)
    phonenum = first_step()
    time.sleep(5)
    while test_phonenum() == 0:
        clear_phonenum_input()
        phonenum = first_step(argu=1)
        time.sleep(5)
        # print('True')

    code = recive_phone_code(token, phonenum)
    input_phone_code(code)
    time.sleep(4)
    pwd, email = make_account()
    input_emailAdress(email, pwd)
    while test_email() == 0:
        clear_email_input()
        pwd, email = make_account()
        input_emailAdress(email, pwd)
    
    insert_account(email, pwd)
    print('done!')
    python3 = sys.executable
    os.execl(python3, python3, * sys.argv)
    