from uiautomator import Device
import time


d = Device('6b862e8')
d.swipe(350, 1000, 350, 100)
d.dump('aaa')
d.swipe(350, 1000, 350, 100)
time.sleep(1)
d.swipe(350, 1000, 350, 800)
d.dump('bbb')
