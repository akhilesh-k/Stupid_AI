import aiml
import os
import time, sys
import pyttsx
import warnings
import Tkinter

mode = "text"
if len(sys.argv) > 1:
    if sys.argv[1] == "--voice" or sys.argv[1] == "voice":
        try:
            import speech_recognition as sr
            mode = "voice"
        except ImportError:
            print("\nYou need to install SpeechRecognition Sir.\nQuitting.\nStarting text mode\n")

terminate = ['bye','buy','shutdown','exit','quit','gotosleep','goodbye']

def offline_speak(jarvis_speech):
    engine = pyttsx.init()
    engine.say(jarvis_speech)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("How can I help you Sir: ")
        audio = r.listen(source)
    try:
        print r.recognize_google(audio)
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        offline_speak("I am sorry! I could not understand. Would you like to repeat?")
        return(listen())
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")

# kernel now ready for use
while True:
    if mode == "voice":
        response = listen()
    else:
        response = raw_input("Talk to C.R.A.Z.Z.O : ")
    if response.lower().replace(" ","") in terminate:
        break
    jarvis_speech = kernel.respond(response)
    print "C.R.A.Z.Z.O. Speaks: " + jarvis_speech
    offline_speak(jarvis_speech)
    
