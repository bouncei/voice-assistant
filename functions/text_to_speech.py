from config import *

def speak(text: str):
    """
        Gets text input from the user and converts it to audio.
    """
    engine = pyttsx3.init()
    engine.say(text)
    
    engine.runAndWait()
    
    
    
