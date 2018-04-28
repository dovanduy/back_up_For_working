from uiautomator import Device
import time
import os


username = 'teukowwg7430@yandex.com'
password = 'qihuy014warg'
d = Device('6b862e8')
d(text="Mail").click()
time.sleep(1)
d(textContains="Deny").click()
time.sleep(1)
d(text="Username").set_text(username)
time.sleep(1)
d.click(280, 350)
os.system('adb -s 6b862e8 shell input text "{}"'.format(password))
time.sleep(1)
d(text="Sign in").click()
time.sleep(8)
d(text="Continue to inbox").click()
time.sleep(3)
d(text="No, thanks").click()
time.sleep(1)
d(textContains="is your Facebook").click()
time.sleep(5)
if d(descriptionContains="Confirm Your Facebook Account Link").exists:
	d(descriptionContains="Confirm Your Facebook Account Link").click()
	time.sleep(2)
else:
	d.click(400, 610)
	time.sleep(2)
d(text="Facebook").click()
time.sleep(5)
