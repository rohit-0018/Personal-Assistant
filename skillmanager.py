import re 
import os
from googlesearch import search
import webbrowser 
import wikipedia as wiki
from termcolor import cprint
from is_connected import is_connected
import text_to_speech as tts
from helper_function import hear_for_task


skillset = ['file','music','email','search','window','personal_detail','whatsapp','tweeter','instagram','facebook']
operation = ['open','close','search','find','who','what']
personal = ['my','i','mine']
receiver_list = [{'rohit':'rohitpersonal1998@gmail.com'},{'sahil':'sahilkhurrana19061998@gmail.com'}]
class operations:
	def email_skill(self,text):
		if('send' in text):
			# try:
			port = 465  # For SSL
			smtp_server = "smtp.gmail.com"
			sender_email = "senders email i.e yours"  # Enter your address
			receiver_email = None
 # --------------------------Dont give this password to any body without destroying it--------
			password =	'Give your password dude'
			res = re.search('send email to (.+)',text)
			if(res is not None):
				receiver = res.group(1)
				# for i in receiver_list:
				# 	receiver = [a for a in i.keys() if(rcvr in a) ]
				# else:
				# 	tts.voice_message('Who is the receiver')
				# 	receiver = hear_for_task()	
			else:
				tts.voice_message('Who is the receiver')
				receiver = hear_for_task()

			if(receiver  is not None):
				cprint('receiver is','yellow')
				print(receiver)
				# for i in receiver_list:
				receiver_key = [[a for a in i.keys() if(a in receiver)] for i in receiver_list]
				key = receiver_key[0]
				print('key is ----------',key)
				for i in receiver_list:
					try:
						receiver_email = i[key[0]]
						break
					except:
						pass
				import smtplib, ssl
				# receiver_email = i[receiver_key[0]]
				if(receiver_email is None):
					tts.voice_message('receiver not in the list enter his email')
					# cprint("Enter email-id for %s",'yellow',receiver)
					receiver_email = input()
					receiver_list.append({receiver:receiver_email})
					# receiver_list.append(new_rec)
				# cprint('Prepairing email for %s: ','green',receiver_email)
				tts.voice_message('what is the message')
				cprint("Enter the message",'yellow')
				message = input()
				try:
					context = ssl.create_default_context()
					with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
					    server.login(sender_email, password)
					    server.sendmail(sender_email, receiver_email, message)
					    tts.voice_message("Sir you email has been sent you can recheck it in inbox")
				except:	
					tts.voice_message('Sir you are offline so nothing can be done')
			else:
				tts.voice_message('You are offline sir nothing can be done')	
				#  call welcome or some another function
		# elif('open' in text):
		# 	webbrowser.open('gmail.com') #open email
		else:
			status = is_connected()
			if(status == True):
				try:
					webbrowser.open('https://www.gmail.com')			
					tts.voice_message('Your default email service is open for you')
					cprint('Your default email service is open for you','green')
				except:
					tts.voice_message('somthing went wrong')
					cprint('Something went wrong','red')
			else:
				tts.voice_message('You are offline sir so we cannot proceed')
				cprint('You are offline sir so we cannot proceed','red')

			# else just open emailing servce
	def close_skill(self,text):
		tts.voice_message('This operation cannot be performed rightnow')
		cprint('This operation cannot be performed','red')
	def open_social_media(self,s_media,task):
		if('facebook' in s_media):
			print('opening facebooks')
		elif('instagram' in s_media):
			print('opening instagram')
		elif('whatsapp' in s_media):
			print('opening whatsapp')
	def play_music(self,task):
		# print('In play music function ---------------------------------------------')
		try:
			print('task----------------',task)
			task = ' '.join(task)
			task+=' video'
			result = search(task,num = 10,start = 0,stop = 10)
			link = ''
			for i in result:
				if('youtube' in i):
					link = i
					break
				else:
					tts.voice_message('sir there is no such song on the internet')
			tts.voice_message('opening your song sir')
			cprint('Opening...','red',attrs = ['blink'])
			webbrowser.open(link)
		except:
			match = re.search('(play)(me)?(music)?(.*)',task)
			print(match.groups())
			if(match.groups()[3] is not None):
				match = match.groups()[3].replace('video','')
				# match
			else:
				match = ""
			# print(match.groups()[3])
			if(is_connected()):
				tts.voice_message('I am sorry sir something went wrong so cannot play'+match)
				cprint('Cannot play'+match,'red')
			else:
				tts.voice_message('sir there is no internet connection so cannot play'+match)
				cprint('Cannot play'+match,'red')
				cprint("your task was :-- '"+task+"'",'red')

	def google_search(self,task):
		res = search(task,num = 1,start = 0,stop = 1)
		tts.voice_message('getting your google search')
		webbrowser.open(res[0])


	def random_page(self,task):
		print('You will get the best possible result')
	def close_skill(self,text):
		print('all tabs will be closed')
	def wiki_Search(self,text):
		try:
			tts.voice_message('Searching for you query sir')
			cprint('Searching on wikipedia','red',attrs = ['blink'])
			response = wiki.page(text)
			text = response.content[0:200]
			text = text.replace('\n',' ')
			tts.voice_message(text)
		except:
			tts.voice_message('Cannot search on wikipedia because you are offline')
			cprint('Cannot search on wikipedia because you are offline','red')
	def tell_time(self):
		import datetime
		# tts.voice_message('telling the time now')
		now = datetime.datetime.now()
		tts.voice_message('Current time is %d hours %d minutes'%(now.hour, now.minute))
class skmapper:
	def language_analysis(self,text):
		o = operations()
		# text = list(set(text.split(' ')))
		text = text.lower()
		if('email' in text):
			o.email_skill(text)
				# tts.voice_message('Sorry please repeat for the task')
				# task = scarlet.hear_for_task()
				# language_analysis(task)
		elif('time' in text or 'Time' in text):
			o.tell_time()
		elif('close' in text or 'Close' in text):
			tts.voice_message("sorry sir cannot perform closing tasks because i am having some issues")
			# response = hear_for_task()
			# language_analysis(response)
			# o.close_skill(text)
		elif('facebook' in text or 'Facebook' in text):
			webbrowser.open('https://www.facebook.com/profile.php?id=100043900563772',autoraise = True)
			 #create a social media function
		elif('instagram' in text or 'Instagram' in text):
			# o.open_social_media('instagram',text)
			# webbrowser.open('',autoraise = True)
			tts.voice_message('Your instagram is blocked sir so cannot open it')
		elif('twitter' in text or 'Twitter' in text):
			# o.open_social_media('twitter',text)
			webbrowser.open('https://twitter.com/home',autoraise = True)
		elif('play' in text or 'Play' in text):
			o.play_music(text)   
		# elif('search' in text):
		# 	o.google_search(text)
		# elif ('news' in text):
		# 	# try:
		# 		from urllib.request import urlopen
		# 		from bs4 import BeautifulSoup as soup
		# 		news_url="https://news.google.com/news/rss"
		# 		Client=urlopen(news_url)
		# 		xml_page=Client.read()
		# 		Client.close()
		# 		soup_page=soup(xml_page,"xml")
		# 		news_list=soup_page.findAll("item")
		# 		for news in news_list[:15]:
		# 			tts.voice_message(news.title.text.encode('utf-8'))
		# 	# except:
				# tts.voice_message("Sorry sir something went wrong so cannot tell you the news")
		elif 'joke' in text:
			import requests
			res = requests.get('https://icanhazdadjoke.com/',headers={"Accept":"application/json"})
			if res.status_code == requests.codes.ok:
				tts.voice_message(str(res.json()['joke']))
			else:
				tts.voice_message('oops!I ran out of jokes')
		elif('open' in text ):
			tts.voice_message("Is this a file or folder")
			response = hear_for_task()
			if('yes' in response):
				tts.voice_message('You got it')
				search_file_folder(text)
			else:
				tts.voice_message('sorry')
				a = hear_for_task()
				language_analysis(a)
		else:
			ser = re.search('(who is)?(tell me about)?(.*)',text)
			# print('searching has been initiated++++++++++++++++++++++',ser)
			if(ser.group(3) is not None):
				o.wiki_Search(ser.group(3))
			else:
				result = search(text,num = 2, start = 0, stop= 1)
				for i in result:
					webbrowser.open(i,new = 2,autoraise= True)
				# if('yes' in response):
			# 	tts.voice_message('You got')
			# 	search_file_folder(text.remove('open')
			# else:
			# 	tts.voice_message('sorry sir i don\'t understand please repeat')
			# 	language_analysis(hear_for_task())

# s = skmapper()
# s.language_analysis('tell me a joke')
# print(receiver_list)
# open file
# open whatsapp
# open social network
# email
# search online
# play music from youtube
# close skill
