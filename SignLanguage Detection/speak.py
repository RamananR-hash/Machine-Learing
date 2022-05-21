from gtts import gTTS  
  
# This module is imported so that we can  
# play the converted audio  
import os
from playsound import playsound  
  

def Speak(text_val):
    text_val=str(text_val)
    language = 'en'  
    obj = gTTS(text=text_val, lang=language, slow=False)   
    obj.save("say.mp3")   
    playsound("say.mp3")
    os.remove("say.mp3")
    try:
        os.remove("say.mp3")
    except:
        pass

