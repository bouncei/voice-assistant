from gtts import gTTS
import os
import playsound

def text_to_speech(text: str):
    language = "en"
    
    speech = gTTS(text=text, lang=language)
    filename = "audio.mp3"
    speech.save(filename)
    
    playsound.playsound("audio.mp3")
    
    
    
text_to_speech("My name is Irene. I am sexy and I know it.")
