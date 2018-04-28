import threading
import time
import os
import sys

def foo():
	print('start')
	time.sleep(10)
	print('over')

def boo():
	print('gg')
	time.sleep(3)
	boo()
thread_list = []
for i in range(10):
	thread_list.append(threading.Thread(target=foo,))
	thread_list.append(threading.Thread(target=boo,))
for i in thread_list:
	i.start()
for i in thread_list:
	i.join()

print("it's over")

