import tkinter as tk
from tkinter import ttk
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
win=tk.Tk()
win.title('PIA')
# submit=ttk.Button(win,text='Start',command=action)
win.mainloop()
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour == 0 and hour <12:
        speak("Good Morning!")
    elif hour>=12 and hour < 16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Swati Raman")
    speak("I am PIA . Please tell me how may I help you?")
def takeCommand():
    # It takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
        print("Wait....")
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        speak("Mam You said")
        speak(query)
        print("User said: ",query)
    except Exception as e:
        print(e)
        print("Say that again please ....")
        return "None"
    return query
wishMe()
while True:
    query=takeCommand().lower()
    if 'wikipedia' in query:
        speak('Searching Wikipedia....')
        query=query.replace('wikipedia',"")
        results=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif 'youtube' in query:  
        webbrowser.open('youtube.com')
    elif 'stackoverflow' in query:
        webbrowser.open('stackoverflow.com')
    elif 'google' in query:
        webbrowser.open('google.com')
    elif 'music' in query or 'songs' in query:
        music_dir='C:/Users/Lenovo/Desktop/music'
        songs=os.listdir(music_dir)
        x=random.randint(0,len(songs)-1)
        os.startfile(os.path.join(music_dir,songs[x]))
    elif 'time' in query:
        a=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Mam the time is {a}")
    elif 'vs code' in query or 'visual studio' in  query:
        os.startfile('"C:/Users/Lenovo/AppData/Local/Programs/Microsoft VS Code/Code.exe"')
    elif 'chrome' in query:
        os.startfile('"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"')
    elif 'sleep' in query or  'close' in query:
        speak('Ok bye mam . Have a nice day')
        break
    else:
        speak('As mam you have not asked before so I didn\'t thought about it')