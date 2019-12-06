import os
# try :	
# 	url = "https://www.google.com"
# 	urllib.request.urlopen(url)
# 	status = "Connected"
# except :
# 	status = "Not connect"
# print (status)


def is_connected():
	res = os.system('ping -c 1 google.com')
	if(res==False):
		return True
	else:
		return False

# status = is_connected("google.com")
# print(status)