import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty ('voice',voices[0].id)

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("GOOD MORNING ")

    elif hour>=12 and hour<=18:
        speak("GOOD AFTERNOON ")

    elif hour>=18 and hour<=23:
        speak("GOOD EVENING ")

    else:
        speak("GOOD NIGHT  SWEET DREAMS")


    speak("I M AR ASSISTANT ,PLEASE TELL ME HOW CAN I HELP YOU")


def takeCommand():
    #micrphone command

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold =0.5
        audio = r.listen(source) 


    try:
        print("Recognising....")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n",)

    except Exception as e:
        #print(e)

        print("can u please repeat it again....")
        return "None"
    return query                        

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



if __name__ == "__main__":
    wishMe()
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak('searching wikipedia....')
        query=query.replace("wikipedia","")
        results= wikipedia.summary (query ,sentences=2)
        speak("Accoding to Wikipedia")
        speak(results)
        print(results)


    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in  query:
        webbrowser.open("google.com")
    elif 'open instagram' in query:
        webbrowser.open("instagram.com")
    elif 'open twitter' in query:
        webbrowser.open("twitter.com")

    elif 'the time'in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Baby!,THE TIME IS  {strTime}")  

    elif 'open whatsapp' in query:
        path='C:\\ Users\\sony\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp'
        os.startfile(path)
