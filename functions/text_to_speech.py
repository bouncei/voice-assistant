# from config import *
import pyttsx3
from gtts import gTTS
import os
import playsound

def speak(text):
    """
        Gets text input from the user and converts it to audio.
    """
    # engine = pyttsx3.init()
    # engine.say(text)
    
    # engine.runAndWait()
    
    language = "en"
    
    myObj = gTTS(str(text), lang=language, slow=False)
    
    myObj.save("audio_files/audio.mp3")


    playsound.playsound("audio_files/audio.mp3")
    
# speak("Hello Boss Bouncey")