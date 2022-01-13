from config import *
from functions.text_to_speech import speak
from functions.speech_to_text import get_audio
from functions.date_from_speech import get_events, service, get_date

if __name__ == "__main__":
    # speak("My name is Irene. I am sexy and I know it.")
    # get_audio()
    
    # get_events(3, service)
    
    text = get_audio().lower()
    print(get_date(text))
    

    
    
    