from config import *
def text_to_speech(text: str):
    language = "en"
    
    speech = gTTS(text=text, lang=language)
    filename = "audio.mp3"
    speech.save(filename)
    
    playsound.playsound("audio.mp3")
    
    
    
