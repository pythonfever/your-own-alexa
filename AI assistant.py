import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import pyjokes
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine. setProperty("rate", 158)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'tell me about ' in command:
        person = command.replace('tell me about ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'open youtube' in command:
            webbrowser.open("youtube.com")

    elif 'open google' in command:
            webbrowser.open("google.com")

    elif 'open facebook' in command:
            webbrowser.open("facebbok.com") 

    elif 'open instagram' in command:
            webbrowser.open("instagram.com") 

    elif 'open c drive' in command:
            codePath = "C:\\"
            os.startfile(codePath)

    elif 'open d drive' in command:
            codePath = "d:\\"
            os.startfile(codePath)
    
    elif 'open e drive' in command:
            codePath = "e:\\"
            os.startfile(codePath)

    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()