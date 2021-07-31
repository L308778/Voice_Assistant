import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices') #Initialize voice
voice = voices[0]