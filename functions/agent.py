from datetime import datetime
from resources.res import *
import speech_recognition as sr

def speak(text):
    """
    Talk

    :param text:
    :return: Talks inputted text
    """
    engine.say(text)
    engine.runAndWait()

    return

def Command():
    """
    Ask user for input and listen to it

    :return:
    """

    listener = sr.Recognizer()

    with sr.Microphone() as source:

        audio = listener.listen(source)
        engine.runAndWait()

        try:
            #Initialize to English, but for further development make language detection
            command = listener.recognize_google(audio,language='en_US')

        except:
            speak("Sorry, I am still in Beta Phase. Please say that again")
            return "None"
        return command

def greet():
    """
    Greet user

    :return: None
    """

    #Use datetime library
    hour=datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")