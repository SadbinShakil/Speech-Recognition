from cmath import e
import datetime
from email.mime import audio
from email.utils import make_msgid
from logging import exception
from logging.config import listen
import sre_compile
from unicodedata import name
import pyttsx3
import wikipedia
import os
import webbrowser
import smtplib
import speech_recognition as sr




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("HI, i am jarvis,,how can i help you,")
speak("AND WHAT SHOULD I CALL YOU")

name = input("What's your name ? ")
gender =input(''' What's your gender
 press(f) for female
 and (m) for male''' " ")
if gender.lower() == "f":
    author ="mam"
else:
    author="sir"
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print("Time: ",hour)
    if hour < 11:
        speak("Good morning," + author)
    elif 11 < hour < 16 :
        speak('Good noon ,' + author)
    elif 16 <= hour <19 :
        speak("good afternoon," + author)
    else :
        speak("good night," + author)



# def takecommand():
#     r =sr.Recognizer()
#     with sr.Microphone as source:
#         print("Listening...")
#         # r.pause_threshold = 1
#         r.pause_threshold = 0.8
#         audio = r.listen(source,timeout=2,phrase_time_limit=5)
    

#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio,language="en-in")
#         print(f"User said :{query}")
#     except Exception as e:
#         speak("Say that again please...")
#         return"none"
#     return query



def takeCommand():
    # It takes microphones recognition from the user and returns String output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please")
        return "None"
    return query


if __name__=="__main__":
    takeCommand()

  
wishMe()





