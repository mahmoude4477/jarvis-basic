
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0])

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    hour = int(datetime.datetime.now().hour)
    if 12>hour>=0:
        speak("Good morning")
    elif 18>hour>=12:
        speak("good after noon")
    else:
        speak("good evening")
    speak("i am jarvis sir. Please tell me how may i help you")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as sou:
        print("listsing")
        r.pause_threshold = 1
        ad = r.listen(sou)
    try:
        print("Recoqring")
        qu = r.recognize_google(ad,language="en-us")
        print(f"user said:{qu}\n")
    except Exception as e:
        print("say that again") 
        return "None"
    return qu
def sendEmail(to,content):
    server = smtplib.SMTP("smtp@gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("your email@gmail.com","your passwd")
    server.sendmail("your email@gmail",to,content)
    server.close()
wish()
while 1:
    qu = takeCommand().lower()
    if 'wikipedia' in qu and len(qu) != 9 :
        try:
            speak("Searching wikipedia...")
            qu = qu.replace("wikipedia","")
            results = wikipedia.summary(qu, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        except:
            print("can not search")
    elif 'open youtube' in qu:
        webbrowser.open("youtube.com")

