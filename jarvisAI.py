import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id) used to check the voice is working or not
engine.setProperty('voice',voices[0].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishME():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!!!")
    else:
        speak("Good Evening!!!") 

    speak("I am shinchan,How can i make your day better")           

def  takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am here waiting for u....")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("trying bro.....")
        query =r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n" )

    except Exception as e:
        print("can u please say again...")
        return "None" 
    return query
     





if __name__ =="__main__":
    wishME()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching Wikipedia')
            query = query.replace("wikipeida","")
            result = wikipedia.summary(query,)
            speak("According to Wikipedia")
            #print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'hi shinchan' in query:
            speak("hiiii i am shinchan how are is how ia ur day")    
        elif 'open stackoverflow' in query:
            webbrowser.open("google.com") 
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs =os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Dear,the time is {strTime} ") 
        elif 'open code' in query:
            codepath= "C:\\Users\\korra\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"   
            os.startfile(codepath)








    
        
    

