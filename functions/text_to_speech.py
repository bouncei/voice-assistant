# from config import *
import pyttsx3
def speak():
    """
        Gets text input from the user and converts it to audio.
    """
    engine = pyttsx3.init()
    engine.say("Hello my boss.")
    
    engine.runAndWait()
    
    
    
speak()