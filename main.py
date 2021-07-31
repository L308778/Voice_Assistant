#Import modules
from functions.agent import *
from resources.res import *

#Import all other packages
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException

# Define Chromeoptions (Block notifications, Define Driver)
chromeOptions = Options()
chromeOptions.add_argument("--disable-notifications")

print(" - ID: %s" % voice.id)
print(" - Name: %s" % voice.name)
print(" - Languages: %s" % voice.languages)
print(" - Gender: %s" % voice.gender)
print(" - Age: %s" % voice.age)


counter = 0
sleeper = 0

if __name__=='__main__':

    while True:
        if counter > 1:
            speak("Do you need anything else")
            decision = Command().lower()
        else:
            speak("How can I assist?")
            counter += 1
        command = Command().lower()

        if command == 0:
            speak("Please give me a command or you can require my services at another time")
            continue

        elif "shut up" in command or "bye" in command or "stop" in command:
            speak('Have a good day')
            break

        elif 'wikipedia' in command:
            speak('What do you want to search for')
            command = Command()
            results = wikipedia.summary(command, sentences=3)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in command:
            speak("What do you want to search for?")
            command = Command()
            webbrowser.open_new_tab("https://www.youtube.com" + "/results?search_query=" + command)
            time.sleep(3)

        elif 'open google' in command.lower() or "search" in command.lower() or "google" in command.lower():
            speak("What do you want to search for")
            search = Command()
            url = "https://www.google.com/search?q=" + search
            webbrowser.open_new_tab(url)
            speak("Google chrome is open now with your search keyword")
            time.sleep(3)

        elif "shazam" in command:

            url = "https://shazam.p.rapidapi.com/auto-complete"

            querystring = {"term": "kiss the", "locale": "en-US"}

            headers = {
                'x-rapidapi-key': "a1b64bde3amsh6864fe68856e57ap1dc5f0jsn4eae796bffcd",
                'x-rapidapi-host': "shazam.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            print(response.text)


        elif 'open gmail' in command.lower():
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Google Mail open now")
            time.sleep(3)

        elif "weather" in command.lower():

            #Use template from geeks
            #API Key generated
            api_key="2fc2871d628098b478fe9671a803b117"
            #Initialize Base URL
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            #Ask user for the specific city by reusing the command function
            speak("What city are you thinking of?")
            city_name=Command()
            print(city_name)
            complete_url=base_url+"appid="+api_key+"&q="+city_name+"&units=metric"
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak("Temperature is " + str(current_temperature) + "degree celsius")
                speak("The humidity in percentage is " + str(current_humidiy) + "percent")
                speak("The current state of the weather is" + str(weather_description))
                print(" Temperature in celsius unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
            else:
                speak(" City Not Found ")

        elif 'time' in command.lower():
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak("the time is {}".format(time))

        elif 'ask' in command or 'ask something' in command or "question" in command:
            speak('Please ask')
            question=Command()
            app_id="5V7P2V-UPH67HRG4J"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'news' in command or "headlines" in command:
            speak("Which digital print do you want to read?")
            news = Command()
            if "economist" in Command().lower():
                news = webbrowser.open_new_tab("https://www.economist.com/")
                speak('Here are some headlines from the Economist')

            elif "bbc" in Command().lower():
                news = webbrowser.open_new_tab("https://www.bbc.com/")
                speak('Here are some headlines from the BBC')

            elif "cnn" in Command().lower():
                news = webbrowser.open_new_tab("https://edition.cnn.com/")
                speak('Here are some headlines from the CNN')

            time.sleep(3)
        #buggy

        elif 'who are you' in command or 'who made you' in command:
            speak("I was developed by Leo Platzer to help people")

        elif 'name' in command:
            speak("My name is Pypy")

        elif "turn off" in command or "turn down" in command:
            speak("Your computer will shut down")
            subprocess.call(["shutdown", "/l"])

        elif "reflect" in command:
            speak("I am listening")
            reflection = ""
            while len(Command()) > 0:
                if "stop" in Command().lower():
                    break
                else:
                    reflection += Command()
            with open('my_result.txt', mode='w') as file:
                file.write("Recognized text:")
                file.write("\n")
                file.write(reflection)
            print("Exporting process completed!")
            print(reflection)

time.sleep(3)