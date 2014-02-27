



import time


p = {}



def get_time():
	def t():
		return time.time()
	return t

def get():
	return time.time()



p ['time'] = get

for i in range(10):
	time.sleep(1)
	print p['time']()