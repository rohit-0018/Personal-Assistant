import speech_recognition as sr
import graphic_module as ghm
from termcolor import cprint
import text_to_speech as tts
from is_connected import is_connected
def hear_for_task():
    # #Sample rate is how often values are recorded
    sample_rate = 48000
    #Chunk is like a buffer. It stores 2048 samples (bytes of data)
    #here.
    #it is advisable to use powers of 2 such as 1024 or 2048
    chunk_size = 2048
    # #Initialize the recognizer
    status = is_connected()
    if(status == True):
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
    else:
        # tts.voice_message('we are offline for better experience come online')
        return