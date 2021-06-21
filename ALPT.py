from gtts import gTTS
import pyttsx3
import speech_recognition as sr
from pygame import mixer
import random
import selenium 
import webbrowser
import os
from tkinter import *
import tkinter as tk
import time 
import datetime
import pywhatkit as k
import RPi.GPIO as gpio
from time import sleep
import sys
import pyautogui as pag
from pynput.keyboard import Controller 
import wikipedia
import keyboard

name =  'MG'
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(12 , gpio.OUT,initial=gpio.HIGH)

terminal = 'exo-open --launch TerminalEmulator'
discord = 'https://discord.com/channels/@me'
imager = 'rpi-imager'
firefox = '/usr/lib/firefox-esr/firefox-esr'
visual = '/usr/share/code/code --no-sandbox --unity-launch'
screenshot = 'xfce4-screenshooter'
logout = 'xfce4-session-logout'
shutdown ='/home/pi/Desktop/ALPHA.py'
bluetooth = 'blueman-manager'
appstore = '/home/pi/pi-apps/gui'
hardware = '/home/pi/.local/share/applications/arduino-arduinoide.desktop'
whatsapp = '/home/pi/WhatsAppWeb/WhatsAppWeb'
settings = '/usr/share/desktop-directories/xfce-settings.directory'

# VOICE OF ALPHA

def alpha(audio1):
   
    Alp = pyttsx3.init()
    voices = Alp.getProperty('voices')
    Alp.setProperty('voice', 'english_rp+m1')
    rate = Alp.getProperty('rate')
    Alp.setProperty('rate', 140)
    Alp.say(audio1)
    print(audio1)
    Alp.runAndWait()


# VOICE OF LOGIC

def logic(audio1):
   
    log = pyttsx3.init()
    voices = log.getProperty('voices')
    log.setProperty('voice', 'english_rp+m3')
    rate = log.getProperty('rate')
    log.setProperty('rate', 140)
    log.say(audio1)
    print(audio1)
    log.runAndWait()

#VOICE OF PARROT

def talk(audio1):
    for line in audio1.splitlines():
        text_to_speech = gTTS(text=audio1, lang='en-uk')
        text_to_speech.save('audio1.mp3')
        mixer.init()
        mixer.music.load("audio1.mp3")
        mixer.music.play()
    print(audio1)

#VOICE OF TETRA

def hey(audio):
    for line in audio.splitlines():
        text_to_speech = gTTS(text=audio, lang='en-uk')
        text_to_speech.save('audio.mp3')
        mixer.init()
        mixer.music.load("audio.mp3")
        mixer.music.play()
    print(audio)

def mc():
    #Initialize the recognizer
    #The primary purpose of a Recognizer instance is, of course, to recognize speech. 
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 0.5
        #wait for a second to let the recognizer adjust the  
        #energy threshold based on the surrounding noise level 
        r.adjust_for_ambient_noise(source, duration=2)
        #listens for the user's input
        audio = r.listen(source)
        print("thinking...")
    try:
        command = r.recognize_google(audio)
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = mc()
        command = command.lower()

    return command


def app():
    a = mc()
    os.startfile(a)
  
def bots():

    def yta():
        talk("what should i do")
        com = mc().lower()
        if 'pause' in com:
            pag.press('space bar')
        elif 'mute' in com:
            pag.press('m')
        elif 'skip forward' in com:
            pag.press('j')            
        elif 'skip back' in com:
            pag.press('l')
        elif 'bar' in com:
            pag.press('/')
        elif 'captions' in com:
            pag.press('c')
        elif 'screen' in com:
            pag.press('f')
        elif 'player' in com:
            pag.press('i')

        talk("done")
    while True:
        command = mc().lower()


##################################################################################################
##################################################################################################

#ALPHA COMMANDS - (SYSTEM RELATED)

        if 'hello' in command:
            hello = mc()
            if 'alpha' in hello:
                alpha("busy")
            elif 'logic' in hello:
                logic("give me a command sir")
            elif 'tetra' in hello:
                hey("hi there")
            elif 'parrot' in hello:
                talk("Im here")     
            else:
                hey("excuse")
                logic("what?")
                alpha("please repeat")
                hey("say it slowly")
        elif 'update' in command:
            alpha("okay , updating")
            sleep(0.1)
            currentMouseX, currentMouseY = pag.position()
            pag.moveTo(37,15)
            pag.click()
            sleep(0.1)
            pag.moveTo(50,70)
            pag.click()
            sleep(10)
            pag.write("sudo apt update && sudo apt upgrade -y")
            sleep(1)
            pag.press('enter')
        elif 'guys' in command:
            hey("hi")
            logic("hello")
            alpha("ready")
            hey("lets do this") 
        elif 'application' in command:
            talk("which application?")
            launch =mc()
            if 'terminal' in launch:
                alpha("launching " + launch)
                os.startfile(terminal)
            elif 'disk' in launch:
                alpha("launching " + launch)
                os.startfile(imager)
            elif 'discord' in launch:
                alpha("launching " + launch)
                webbrowser.open_new(discord)
            elif 'screenshot' in launch:
                alpha("taking screenshot , open the correct window")
                sleep(3)
                ss = pag.screenshot()
                alpha("what should i save it as ?")
                ss.save('/home/pi/Desktop/backup/')
            elif 'firefox' in launch:
                alpha("launching " + launch)
                os.startfile(firefox)
            elif 'shutdown computer' in launch:
                alpha("launching " + launch)
                sleep(0.1)
                pag.moveTo(1630,15)
                pag.click()
                sleep(0.1)
                pag.moveTo(1630,45)
                pag.click()
            elif 'logout computer' in launch:
                alpha("launching " + launch)
                sleep(0.1)
                pag.moveTo(1630,15)
                pag.click()
                sleep(0.1)
                pag.moveTo(1630,45)
                pag.click()    
            elif 'restart computer' in launch:
                alpha("launching " + launch)
                sleep(0.1)
                pag.moveTo(1630,15)
                pag.click()
                sleep(0.1)
                pag.moveTo(1630,45)
                pag.click()                           
            elif 'visual' in launch:
                alpha("launching " + launch)
                os.startfile(visual)
            elif 'app store' in launch:
                alpha("launching " + launch)
                os.startfile(appstore)
            elif 'bluetooth' in launch:
                alpha("launching " + launch)
                sleep(0.1)
                pag.moveTo(1630,15)
                pag.click()
                sleep(0.1)
                pag.moveTo(1630,45)
                pag.click()
            elif 'hardware' in launch:
                alpha("launching " + launch)
                sleep(0.1)
                pag.moveTo(1630,15)
                pag.click()
                sleep(0.1)
                pag.moveTo(1630,45)
                pag.click()
            elif 'whatsapp' in launch:
                alpha("launching " + launch)
                app(whatsapp)
            elif 'settings' in launch: 
                alpha("launching " + launch)
                sleep(0.1)
                pag.moveTo(1630,15)
                pag.click()
                sleep(0.1)
                pag.moveTo(1630,45)
                pag.click()           

        elif "discord bot" in command:
            alpha('starting up MGSB')
            sleep(2)
            pag.keyDown('ctrl')
            pag.press('enter')
            pag.keyUp('ctrl')
            sleep(3)
            pag.write("cd Desktop")
            pag.press('enter')
            sleep(2)
            pag.write("cd m")
            pag.press("enter")
            sleep(2)
            pag.write("python3 main.py")
            pag.press("enter")
        elif 'sleep' in command:
            alpha("shutting down")
            break

##################################################################################################
##################################################################################################

#PARROT COMMANDS - (WEB SURFING)
    
        elif 'google' in command:
            talk("what should i search?")
            google = mc()
            k.search(google)

        elif 'search youtube' in command:
            talk("what should i search?")
            win = Tk()
            win.geometry("100x100")
            win.configure(background='cyan')
            win.title('YOUTUBE SEARCH')
            #Fname = Label(win , text = 'Email Recipient').place(x=20,y=5)
            yt = StringVar()
            entry_frame = Entry(win ,width=25,textvariable=yt).place(x=100,y=50)
            mainloop()
            a = yt.get()
            y = mc().lower()
            k.playonyt(y)
            k.playonyt(a)

        elif "website" in command:
            talk("which website?")
            web1 = mc().lower()
            talk('okay sir launching ..')
            web = 'https://www.' + web1 + '.com'
            webbrowser.open(web)
            talk("launched succesfully")

        elif 'search wikipedia' in command:
            talk("what should i search for?")
            wiki = mc().lower()
            b = k.info(wiki,2)
            talk('this is what i found')
 
        elif 'tools' in command:
            yta()
        
        
##################################################################################################
##################################################################################################

#LOGIC COMMANDS - (HARDWARE)

        elif 'light' in command:
            logic("turning on the light")
            gpio.setup(12 , gpio.OUT,initial=gpio.HIGH)
        elif 'led' in command:
            logic("turning off the light")
            gpio.setup(12 , gpio.OUT,initial=gpio.LOW)

##################################################################################################
##################################################################################################

#TETRA COMMANDS - (GAMES)   

        elif 'rand' in command:
            win = Tk()
            win.geometry("300x300")
            win.configure(background='cyan')
            win.title('RANDOM NUMBER')
            #Fname = Label(win , text = 'Email Recipient').place(x=20,y=5)
            fn = IntVar()
            sn = IntVar()
            entry_frame = Entry(win ,width=15,textvariable=fn).place(x=100,y=20)
            entry_frame = Entry(win ,width=15,textvariable=sn).place(x=100,y=50)
            mainloop()
            a = fn.get()
            b = sn.get()
            c = a+1
            d = b-1
            s = random.randint(c,d)
            hey(f"the number is {s}")

if __name__ == "__main__":
    alpha("ready for your commands")  
    while True:
        start = mc()
        if "wake up" in start:
            alpha("hello sir , waking up parrot ,logic and tetra")
            bots()
        elif 'shut' in start:
            alpha("okay sir , see you soon")
            sys.exit()
        else:
            alpha("can u repeat that")
