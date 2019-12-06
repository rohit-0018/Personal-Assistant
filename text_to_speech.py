import pyttsx3
from gtts import gTTS 
from playsound import playsound
import os 
  
def is_connected():
	try:
		res = os.system('ping -c 1 google.com')
	except:
		pass
	if(res==0):
		return True
	else:
		return False

def voice_message(text):
	status = is_connected()
	if(status):
		language = 'en'
		myobj = gTTS(text=text, lang=language, slow=False) 
		myobj.save("recording.mp3") 
		playsound('recording.mp3')
		os.remove("recording.mp3")
	else:
		engine = pyttsx3.init()
		engine.setProperty("rate",150) # 150 words perminute default was 200 
		# engine.setProperty("vloume",0.5)
		# print(engine.getProperty('volume'))
		# engine.say('You are offline sir please come online')
		engine.say(text)
		engine.runAndWait()

# # voice_message("hello aman")			
# def convert_online_and_play(text):
# 	language = 'en'
# 	myobj = gTTS(text=text, lang=language, slow=False) 
# 	myobj.save("recording.mp3") 
# 	playsound('recording.mp3')
# 	os.remove("recording.mp3")
# 	print("status Ok")

# def convert_offline_and_play(text):
# 	engine = pyttsx3.init()
# 	engine.setProperty("rate",120) # 120 words perminute default was 200 
# 	# engine.setProperty("vloume",0.5)
# 	print(engine.getProperty('volume'))
# 	engine.say(text)
# 	engine.runAndWait()
# 	print("status ok")