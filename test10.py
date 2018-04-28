from uiautomator import device as d
import os
import re
import time


text = 'nk84w92f9326@ieasyfeed.com'
d.click(350, 565)
time.sleep(0.5)
# get emailname
os.system('adb shell input text "{}"'.format(text))
d.click(350, 655)
time.sleep(0.5)
d.click(350, 655)
time.sleep(0.5)
# get password
text = 'lingxiuguigu'
os.system('adb shell input text "{}"'.format(text))
time.sleep(1)
d(description="Login").click()
time.sleep(10)
d.dump('string')
with open('string', 'r') as f:
	string = f.read()

code = re.findall('([\d]{6}|[\d]{5}) is your', string)[0]


