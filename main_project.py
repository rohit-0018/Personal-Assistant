import os
import random 
import speech_recognition as sr
import re
# import pyttsx3 as tta # for test to audio/speech
import text_to_speech as tts
import graphic_module as ghm
from termcolor import cprint
# import operations
from skillmanager import skmapper # skmapper is a class

class Scarlet_assistant:
    name = ""
    email = ""
    age  = ""
    skill_set = ['email','music','file','window']
    greeting_message = ['Welcome again sir','you got it','happy to serve','command me again','looks good','what\'s your query']
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age
    def __init__(self):
        print("Welcome Rohit")
    # Test url is needed for this function
    def is_connected(self):
        res = os.system('ping -c 1 google.com')
        if(res == 0):
            return True
        else:
            return False


            
    def personal_detail_creator(self,colum,data):
        with open('personal_details.txt','a+') as personal_detail:
            personal_detail.write(self.colum+':'+self.data+',')


    def hear_for_task(self):
        # #Sample rate is how often values are recorded
        sample_rate = 48000
        #Chunk is like a buffer. It stores 2048 samples (bytes of data)
        #here.
        #it is advisable to use powers of 2 such as 1024 or 2048
        chunk_size = 2048
        # #Initialize the recognizer
        r = sr.Recognizer()
        with sr.Microphone( sample_rate = sample_rate,  chunk_size = chunk_size) as source:
        #wait for a second to let the recognizer adjust the
        #energy threshold based on the surrounding noise level
            r.adjust_for_ambient_noise(source)
            ghm.display_speak() #This method is frm graphic module and displays mic and speak string
            audio = r.listen(source)
            cprint("Stopped listening",'green')    
            try:
                text = r.recognize_google(audio)
                print ("--------------You ordered me to perform : " + text )
                return text
            #error occurs when google could not understand what was said

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")

            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

    

    def erase_data_frm_file(file_name):
        with open(file_name+'.txt','w+') as eraser:
            eraser.write(" ")
        print("++++++++++++++++++++++++ Data has been erased ++++++++++++++++++++++++++")
# ----------------Starting the assistant from here ---------------------
    count = 1
    def welcome_func(self):
        status = self.is_connected()
        if(status == False):
            tts.voice_message("You are offline for better experiece go online")
            print("You are offline for better experince go online")
            # task = self.hear_for_task()
        else:
            if(self.count == 1):
                tts.voice_message("Welcome Mr Rohit what can i do for you")
            else:
                i = random.randint(0,5)
                stri = self.greeting_message[i]
                tts.voice_message(stri)
            task = self.hear_for_task()
            if(task == None):
                tts.voice_message('Some thing went wrong sir try again')
                self.welcome_func()
            else:
                s = skmapper()
                if('exit' in task):
                    return False
                else:
                    # self.welcome_func()            
                    s.language_analysis(task)
                    self.count+=1 
                    # return True
                    self.welcome_func()
            # skmapper(task) # This function will perform skill mapping tasks and call the associated function








# if __name__ == "__main__":
    # s1 = Scarlet("rohit","21","rohitpersonal1998@gmail.com")
    # s1.personal_detail_creator("rohit","st")
    # erase_data_frm_file("personal_details")
t = Scarlet_assistant()
t.welcome_func()




print("Thank you for using me!!!!!!!!!!!!!")
