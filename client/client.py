import requests
import time
url1="http://server:5000/"
while(1):
	x=requests.post(url1)
	print(x.headers)
	time.sleep(5)
