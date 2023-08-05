# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 01:18:44 2023

@author: sahin
"""
import pyttsx3
import speech_recognition as sr
import openai
openai.api_key = 'PUT YOUR CHATGPT API KEY HERE'
messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

#text to speak
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold=1
        audio=r.listen(source,timeout=5,phrase_time_limit=6)
        speak("okay sir")
    try:
        print("recognizing....")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception:
        speak("say that again please sir..")
        return 'none'
    return query
while True:
    message = takecommand()
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        
            
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )   
    reply = chat.choices[0].message.content
    speak(reply)
    '''print(f"ChatGPT: {reply}")'''
    messages.append({"role": "assistant", "content": reply})
    
     
