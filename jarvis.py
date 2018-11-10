import time
import sys
import atexit
from os import system
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages")
sys.path.append("/usr/local/lib/python3.6/site-packages")
import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.playback import play
from pynput.mouse import Button, Controller
import pyautogui as p
import webbrowser
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def callback(r, audio):
    global JarvisOn
    global driver
    try:
        speech = recognise(audio)
        for i in speech:
            if str(i) == "Jarvis":
                JarvisOn = True
                if checkBrowser():
                    window, youtubeUsed, status = youtubeRunning()
                if youtubeUsed:
                    if status == 1:
                        driver.switch_to_window(window)
                        elem = driver.find_element_by_id('movie_player')
                        elem.click()
                        #p.moveTo(528, 374)
                        #time.sleep(0.5)
                        #mouse.click(Button.left, 1)
    except:
        print("Jarvis not initialised")

def talk(overYoutube=False):
    with sr.Microphone() as source:
        if overYoutube == False:
            audio = r.listen(source, phrase_time_limit=6)
        else:
            try:
                audio = r.listen(source, phrase_time_limit=2)
            except:
                print("Nothing said")
                audio = None
    return audio

def recognise(audio):
    speech = r.recognize_google(audio)
    speech = speech.split()
    return speech
                
def adjust():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.dynamic_energy_threshold = True
        r.dynamic_energy_adjustment_damping = 0.15
        r.pause_threshold = 0.5

def youtubeRunning():
    global youtubeUsed
    global driver
    status = None
    for i in driver.window_handles:
        driver.switch_to_window(i)
        title = driver.title.split()
        for j in title:
            if str(j).lower() == "youtube":
                youtubeUsed = True
                window = i
                status = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
                return window, youtubeUsed, status
            else:
                youtubeUsed = False
            print(youtubeUsed)
    return window, youtubeUsed, status

                
def checkBrowser():
    global driver
    browserOpen = False
    try:
        if len(driver.window_handles) == 0:
            print("No Chrome running")
        else:
            browserOpen = True
    except:
        print("No Chrome running")
    return browserOpen
    

def youtubeScrapper(x):
    global youtubeUsed
    global driver
    if checkBrowser():
        window, youtubeUsed, status = youtubeRunning()
        if youtubeUsed == False:
            driver.execute_script("window.open('');")
        else:
            driver.switch_to_window(window)
    else:
        driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/results?search_query="+x)
    driver.set_window_size(1280, 800)
    driver.maximize_window()
    driver.switch_to_window(driver.current_window_handle)
    try:
        myElem = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@class="yt-lockup yt-lockup-tile yt-lockup-video clearfix"]')))
        elem = driver.find_element_by_xpath('//*[@class="yt-lockup yt-lockup-tile yt-lockup-video clearfix"]')
        elem.click()
    except TimeoutException:
        print("Page did not load in time")
    #p.moveTo(394, 310)
    #time.sleep(1)
    #mouse.click(Button.left, 2)
    youtubeUsed = True

def begining():
    print("Speak")
    adjust()
    while JarvisOn == False:
        if checkBrowser():
            if youtubeUsed:
                print("here")
                audio = talk(overYoutube=True)
                callback(r, audio)
        else:
            audio = talk()
            callback(r, audio)
    main()

def main(audio=None, justRan=False):
    global JarvisOn
    JarvisOn = False
    count = 0
    if justRan == False:
        play(song[:1000])
        system('say -v Tom Yes, how can I help?')
        audio = talk()
        main(audio=audio, justRan=True)
    speech = recognise(audio)
    for i in speech:
        if str(i).lower() == "youtube":
            search = " ".join(speech[count+1:])
            system('say -v Tom Doing it now')
            youtubeScrapper(search)
        count += 1
    begining()

JarvisOn = False
youtubeUsed = False
mouse = Controller()
song = AudioSegment.from_wav("/Users/SagarJaiswal/Desktop/Siri_Sound_Effect_HD_.wav")
r = sr.Recognizer()
m = sr.Microphone()
r.energy_threshold = 400
adjust()
begining()