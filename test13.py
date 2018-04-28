import os
import sys
import time

time.sleep(1)
print(1)
python3 = sys.executable
os.execl(python3, python3, * sys.argv)
