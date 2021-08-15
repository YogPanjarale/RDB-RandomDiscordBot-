import pyttsx3
import sys
from time import sleep
import pyautogui as p
def alpha(audio1):   
    Alp = pyttsx3.init()
    voices = Alp.getProperty('voices')
    Alp.setProperty('voice', 'english_rp+f4')
    rate = Alp.getProperty('rate')
    Alp.setProperty('rate', 140)
    Alp.say(audio1)
    print(audio1)
    Alp.runAndWait()
sleep(20)
p.write('mg@1612')
sleep(1)
p.press('enter')
sleep(1)
alpha("logging in")
sleep(1)
sys.exit()
