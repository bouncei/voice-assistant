from config import *

    

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
            
            # if "Joshua" in said:
            #     print("working perfectly")
            
            
            print(said)
            
        except Exception as e:
            print("Exception: ", str(e))
            print("Something went wrong")
            
    return said

