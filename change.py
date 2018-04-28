import json


ssdict = {
	'ss1': {
		'ip': '96.8.118.207',
		'port': '8005',
		'password': 'shijihetu520',
		'way': 'AES-256-CTR'
	},

	'ss2': {
		'ip': '96.8.118.208',
		'port': '8005',
		'password': 'shijihetu520',
		'way': 'AES-256-CTR'
	},
	
	'ss3': {
		'ip': '96.8.118.209',
		'port': '8005',
		'password': 'shijihetu520',
		'way': 'AES-256-CTR'
	},
	
	'ss4': {
		'ip': '96.8.118.210',
		'port': '8005',
		'password': 'shijihetu520',
		'way': 'AES-256-CTR'
	},


	'ss5': {
		'ip': '52.8.151.88',
		'port': '8688',
		'password': 'shijihetu520',
		'way': 'AES-256-CTR'
	},

	'ss6': {
		'ip': '96.8.118.211',
		'port': '7005',
		'password': 'shijihetu520',
		'way': 'BF-CFB'
	},

	'ss7': {
		'ip': '96.8.118.212',
		'port': '7005',
		'password': 'shijihetu520',
		'way': 'BF-CFB'
	},

	'ss8': {
		'ip': '96.8.118.213',
		'port': '7005',
		'password': 'shijihetu520',
		'way': 'BF-CFB'
	},
	
	'ss9': {
		'ip': '96.8.118.214',
		'port': '7005',
		'password': 'shijihetu520',
		'way': 'BF-CFB'
	},
	
	'ss10': {
		'ip': '96.8.118.215',
		'port': '7005',
		'password': 'shijihetu520',
		'way': 'BF-CFB'
	},
	
	'ss11': {
		'ip': '34.238.46.81',
		'port': '7005',
		'password': 'shijihetu520',
		'way': 'AES-256-CTR'
	},
	
	'ss12': {
		'ip': '35.168.192.218',
		'port': '7005',
		'password': 'shijihetu520',
		'way': 'AES-256-CTR'
	},
	
	# 'ss13': {
	# 	'ip': '35.171.173.179',
	# 	'port': '7005',
	# 	'password': 'shijihetu520',
	# 	'way': 'AES-256-CTR'
	# },
	
	'ss14': {
		'ip': '35.173.23.234',
		'port': '7005',
		'password': 'shijihetu520',
		'way': 'AES-256-CTR'
	},
	
	'ss15': {
		'ip': '35.173.63.0',
		'port': '7005',
		'password': 'shijihetu520',
		'way': 'AES-256-CTR'
	},
	
}

with open('a.json', 'w') as f:
	f.write(json.dumps(ssdict))
