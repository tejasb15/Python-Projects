import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            return "Not Understand"

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',170)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':

        speechtx("Welcome to Voice Assistant...")

        while True:

            data1 = sptext().lower()

            if 'your name' in data1:
                sname = "My Name is David"
                speechtx(sname)

            elif 'my name' in data1:
                myname = "Your Name is Tejas."
                speechtx(myname)

            elif 'time' in data1:
                time1 = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time1)

            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/")

            elif 'my portfolio' in data1:
                webbrowser.open('https://tejasbportfolio.netlify.app/')

            elif 'joke' in data1:
                joke_1 = pyjokes.get_joke(language='en',category="neutral")
                print(f"Joke :- {joke_1}")
                speechtx(joke_1)

            elif 'play song' in data1:
                address = 'D:/Music/Bollywood Songs/'
                listsong = os.listdir(address)
                print(listsong)
                os.startfile(os.path.join(address,listsong[1]))

            elif 'exit' in data1:
                speechtx('Thank you...')
                break

            else:
                d = "Not Found Data"
                speechtx(d)

            time.sleep(3)
