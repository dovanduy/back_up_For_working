from uiautomator import Device
import time


ssdict = 'ssArgu':{
	{
		'ip': '96.8.118.207',
		'port': '8005',
		'password': 'shijihetu520',
		'way': 'AES-256-CTR'
	},

	{
		'ip': '96.8.118.208',
		'port': '8005',
		'password': 'shijihetu520',
		'way': 'AES-256-CTR'
	},
	
	{
		'ip': '96.8.118.209',
		'port': '8005',
		'password': 'shijihetu520',
		'way': 'AES-256-CTR'
	},
	
	{
		'ip': '96.8.118.210',
		'port': '8005',
		'password': 'shijihetu520',
		'way': 'AES-256-CTR'
	},


	{
		'ip': '52.8.151.88',
		'port': '8688',
		'password': 'shijihetu520',
		'way': 'AES-256-CTR'
	},

	{
		'ip': '96.8.118.211',
		'port': '7005',
		'password': 'shijihetu520',
		'way': 'BF-CFB'
	},

	{
		'ip': '96.8.118.212',
		'port': '7005',
		'password': 'shijihetu520',
		'way': 'BF-CFB'
	},

	{
		'ip': '96.8.118.213',
		'port': '7005',
		'password': 'shijihetu520',
		'way': 'BF-CFB'
	},
	
	{
		'ip': '96.8.118.214',
		'port': '7005',
		'password': 'shijihetu520',
		'way': 'BF-CFB'
	},
	
	{
		'ip': '96.8.118.215',
		'port': '7005',
		'password': 'shijihetu520',
		'way': 'BF-CFB'
	},
	
	{
		'ip': '24.238.46.81',
		'port': '7005',
		'password': 'shijihetu520',
		'way': 'AES-256-CTR'
	},
	
	{
		'ip': '35.168.192.218',
		'port': '7005',
		'password': 'shijihetu520',
		'way': 'AES-256-CTR'
	},
	
	{
		'ip': '35.171.173.179',
		'port': '7005',
		'password': 'shijihetu520',
		'way': 'AES-256-CTR'
	},
	
	{
		'ip': '35.173.23.234',
		'port': '7005',
		'password': 'shijihetu520',
		'way': 'AES-256-CTR'
	},
	
	{
		'ip': '35.173.63.0',
		'port': '7005',
		'password': 'shijihetu520',
		'way': 'AES-256-CTR'
	},
	
}

for i in sslist:
	ip = i['ip']
	port = i["port"]
	password = i['password']
	way = i['way']	
	d = Device('6b862e8')
	d(description="添加配置文件").click()
	d(text="手动设置").click()
	d(text="服务器").click()
	time.sleep(1)
	d.click(660, 1100)
	d(resourceId="android:id/edit").set_text(ip)
	d(text="确定").click()
	d(text="远程端口").click()
	d(resourceId="android:id/numberpicker_input").set_text(port)
	d(text="确定").click()
	d(text="密码").click()
	d(resourceId="android:id/edit").set_text(password)
	d(text="确定").click()
	d(text="加密方法").click()
	d(text=way).click()
	d(resourceId="com.github.shadowsocks:id/action_apply").click()

