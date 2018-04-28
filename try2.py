import re

string = 'adsfasd123456'
s = re.search(r'([\d]{', string).groups()
print(s)
