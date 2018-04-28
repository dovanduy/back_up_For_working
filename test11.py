from uiautomator import Device
import time
import os
import requests
import re
import random
import time

d = Device('6b862e8')
os.system("adb -s 6b862e8 uninstall cn.mailchat")
os.system("adb -s 6b862e8 install /home/administator/下载/MailChat_Setup.apk")
d.press('home')
time.sleep(1)
d(text="MailChat").click()
time.sleep(2)
d(text="Others").click()
time.sleep(1)
d(resourceId="cn.mailchat:id/actv_account_email").set_text('x53my1656l15@ieasyfeed.com')
time.sleep(1)
d(resourceId="cn.mailchat:id/et_account_password").set_text('lingxiuguigu')
time.sleep(1)
d(resourceId="cn.mailchat:id/bt_login").click()
time.sleep(5)
d(resourceId="cn.mailchat:id/bt_sure").click()
time.sleep(5)
d(textContains="is your Facebook").click()
time.sleep(5)
d.click(400, 500)
d.click(400, 500)

