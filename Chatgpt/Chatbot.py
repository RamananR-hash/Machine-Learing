from gtts import gTTS
from playsound import playsound
import os
import openai
import speech_recognition as sr
r = sr.Recognizer()
from time import sleep
openai.api_key = ""#enter your api here


with sr.Microphone() as source:
    print("Listening")
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    text = r.recognize_google(audio_data)
    print(text)

    
prompt = text

completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

message = completions.choices[0].text
message=str(message.strip())


print(message)
tts=message

language = 'en'  
obj = gTTS(text=tts, lang=language, slow=False)   
obj.save("say.mp3")   
playsound("say.mp3")
sleep(2)
os.remove("say.mp3")
try:
    os.remove("say.mp3")
except:
    pass

