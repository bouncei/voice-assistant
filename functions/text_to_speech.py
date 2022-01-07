from config import *

def speak(text: str):
    """
        Gets text input from the user and converts it to audio.
    """
    language = "en"
    
    speech = gTTS(text=text, lang=language)  # Speech Object
    filename = "audio.mp3" 
    speech.save(filename)  # Saves the audio
    
    playsound.playsound("audio.mp3") # Play audio file using the playsound libary
    
    
    
