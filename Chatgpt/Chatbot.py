from gtts import gTTS
from playsound import playsound
import os
import openai
import speech_recognition as sr
from time import sleep
openai.api_key = "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"
r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("Listening....")
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        text = r.recognize_google(audio_data)
        print(text)




    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    message=str(message.strip())
    print(message)


    language = 'en'  
    obj = gTTS(text=message, lang=language, slow=False)
    print("Making Audio....")
    obj.save("say.mp3")
    print("Playing Audio....")
    playsound("say.mp3")
    sleep(2)
    print("Deleting Audio....")
    os.remove("say.mp3")










