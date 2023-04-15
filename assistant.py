import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import requests
import random
from bs4 import BeautifulSoup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Reminder():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Ak")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! Ak")   

    else:
        speak("Good Evening! Ak")  

    speak("I am Cheeku Sir. Please tell me how may I help you")       

def microphone():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('singhanubhav8122000@gmail.com', 'ASH8122004@123')
    server.sendmail('singhanubhav8122000@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    Reminder()
    while True:
    #if 1:
        query = microphone().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=ardtvdR28SQ")
                    elif b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=pI0IJrnit8I")
                    elif b==3:
                        webbrowser.open("https://www.youtube.com/shorts/fnQfJ4zISdo")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open robotic' in query:
            webbrowser.open("https://www.frontiersin.org/journals/robotics-and-ai/research-topics")   


        elif 'play music' in query:
            music = 'F:\DOWNLOADS\Bepanah Pyaar - Payal Dev 320 Kbps.mp3'
            os.startfile(music)
        
        elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")
        elif "schedule my day" in query:
                    tasks = []
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = microphone().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open vs' in query:
            vs = "C:\\Users\\lenovo\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vs)
        
        elif "temperature" in query:
            search = "temperature in punjab"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")

        elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

        elif 'email to Ashish' in query:
            try:
                speak("What should I say?") 
                content = Reminder()
                to = "anubhav8122000@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Ak bhai. I am not able to send this email")  

        elif "shut down system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break 

