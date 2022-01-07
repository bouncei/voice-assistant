from config import *
from functions.text_to_speech import speak
import random

Reply = ["Boss B's my one and only name - use as often as you'd like! ",
         "The name is Boss B - easy to remember!", "They call me Boss B, and by 'they,' I mean everyone! ",
         "I just go by 'Boss B.'It feels right! ",
         "I stick with a single name: 'Boss B.' " 
        ]
    

def get_audio():
    """
        Getting Input From Users Throgh The Microphone Using The Pyaudio and Speech Recognition libaries.
         
    """
    r = sr.Recognizer() # Recognizer Object: Creates a new Recognizer instance, which represents a collection of speech recognition functionality.
    
    with sr.Microphone() as source:  #Creates a new Microphone instance, which represents a physical microphone on the computer. 
        print("Speak...")

        audio = r.listen(source)
        said = ""
        
        
        try:
            print("Ready... ")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source,duration=1)
            said = r.recognize_google(audio) #Performs speech recognition on audio_data
            
            if "what is your name" or "what's your name" in said:
                response = random.choice(Reply)
                speak(response)
            
            
           
            
            print(said + " : ", response)
            
        except Exception as e:
            print("Exception: ", str(e))
            print("Something went wrong")
            
    return said

