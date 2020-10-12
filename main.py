import os
import time
import playsound
import gaana
import speech_recognition as sr
from gtts import gTTS

# initial code
def speak (text):
    tts = gTTS(text = text, lang= "en")
    filename = "text.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    print("Bot is listening")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception : "+str(e))

    return said



text = get_audio()

if "hello" in text:
    speak("Hi, Anshu how can I help you today")

if "your name" in text:
    speak("My name is anshu")

if "my name" in text:
    speak("I dont know your name")

