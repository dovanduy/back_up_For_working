import os
import time
import threading

t1 = threading.Thread(target=lambda :os.system('sslocal -c /etc/shadowsocks.json'))
t1.start()
time.sleep(10)
os.system("kill -9 `ps -ef| grep shadowsocks| awk '{print $2}'`")
print('done!')
