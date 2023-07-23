# Description: This is a virtual assistant program that gets the date, current time, responds back with a random greeting, and returns the information.

#pip install pyaudio
#pip install SpeechRecognition
#pip install gTTS
#pip install wikipedia

#import the libraries
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

# Ignore any warning messages we get from the program
warnings.filterwarnings('ignore')

# Record audio and return it as a string
def recordAudio():
    #Record the audio
    r = sr.Recognizer() #Creating a recognizer object

    #Open the microphone and start recording
    with sr.Microphone() as source:
        print('say something')
        audio = r.listen(source)

    # Use googles speech recognition
    data = ''
    try:
        data = r.recognize_google(audio) 
        print('You said: ' + data)
    except sr.UnknownValueError: 
        print('Google speech could not understand the audio')
    except sr.RequestError as e: 
        print('Request results from google service error' + e)

    return data
 
recordAudio()