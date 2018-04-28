a = [1,2,3,4]
try:
	for i in range(10):
		print(a[i])
except Exception as e:
	with open('try', 'w') as f:
		f.write(str(e))
