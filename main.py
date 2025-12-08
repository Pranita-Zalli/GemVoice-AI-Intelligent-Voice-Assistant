import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import musicLibrary
import requests
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # loads .env file

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
news_api_key=os.getenv("news_api")
recognizier=sr.Recognizer()
news=news_api_key

def speak(text):
    engine=pyttsx3.init()
    engine.setProperty('rate', 150)   
    engine.say(text)
    engine.runAndWait()
    engine.stop()

#Gemini Processs
def aiProcess(command):
    client = OpenAI(
        api_key=GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/" 
    )

    completion = client.chat.completions.create(
        model="gemini-2.5-flash", # 3. Change the model name to a compatible Gemini model
        messages=[
            {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general like Alexa and Google Cloud"},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content


#Processs the command given by user
def processCommand(c):

    # -------------------------------------------------
    # 1. BYE CONDITION (MUST BE FIRST)
    # -------------------------------------------------
    if "bye" in c or "jarvis bye" in c:
        speak("Bye, have a great day!")
        return "exit"   # for breaking main loop safely
    


    # -------------------------------------------------
    # 2. OPEN WHATSAPP APP ON WINDOWS
    # -------------------------------------------------
    elif "open whatsapp" in c:
        speak("Opening WhatsApp.")
        os.startfile(r"C:\Users\%pzalli%\AppData\Local\WhatsApp\WhatsApp.exe")
        return

    # -------------------------------------------------
    # 3. YOUR NORMAL COMMANDS
    # -------------------------------------------------
    elif "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        songs=c.lower().split(" ")[1] #command= play bulley songs=["play","bulley"] so song bulley[1] will play
        link=musicLibrary.music[songs]
        webbrowser.open(link)

    # -------------------------------------------------
    # 4. NEWS READING WITH STOP
    # -------------------------------------------------
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?category=general&apiKey={news}")

        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])

            if not articles:
                speak("No news found.")
                return

            speak("Reading latest news. Say stop anytime to stop me.")

            for art in articles:
                title = art.get("title", "")
                
                # Skip empty titles
                if not title.strip():
                    continue
                print("Speaking:", art['title'])
                speak(title)

                #LISTEN FOR STOP AFTER EACH HEADLINE
                with sr.Microphone() as source:
                    recognizier.adjust_for_ambient_noise(source, duration=0.5)
                    try:
                        print("Listening for stop command...")   # DEBUG
                        audio = recognizier.listen(source, timeout=2, phrase_time_limit=2)
                        c = recognizier.recognize_google(audio).lower()
                        print("Heard:", c,"\n")   # DEBUG

                        if "stop" in c or "enough" in c or "pause" in c:
                            speak("Okay, stopping the news.")
                            break

                    except:
                        # Nothing said → just move to next headline
                        continue
    

    # -------------------------------------------------
    # 5. DEFAULT: GEMINI AI WITH STOP LISTENING
    # -------------------------------------------------
    else:
    # Get Gemini output
        output = aiProcess(c)

        # Split Gemini response into sentences
        sentences = output.split(".")

        speak("Okay.")

        for sentence in sentences:
            s = sentence.strip()
            if not s:
                continue

            # Speak one sentence at a time
            speak(s)

            # --- LISTEN FOR STOP AFTER EACH SENTENCE ---
            with sr.Microphone() as source:
                recognizier.adjust_for_ambient_noise(source, duration=0.5)

                try:
                    print("Listening for stop command...")
                    audio = recognizier.listen(source, timeout=2, phrase_time_limit=2)
                    c = recognizier.recognize_google(audio).lower()
                    print("Heard:", c)

                    if "stop" in c or "pause" in c or "enough" in c:
                        speak("Okay, stopping now.")
                        break

                except:
                    # If user says nothing → continue to next sentence
                    continue


# -------------------------------------------------
# Main Programs Starts From here
# -------------------------------------------------
if __name__== "__main__" :
    speak("Initializing Jarvis......")
    r = sr.Recognizer()
    while True:
        #Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        # r = sr.Recognizer()
           
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            print("Detected word:",word)
            print("Recognizing....")
            if(word.lower().strip() == "jarvis" ):
                speak("Yaa")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active.....")
                    # audio = r.listen(source)
                    audio = r.listen(source)
                    command=r.recognize_google(audio)

                    result = processCommand(command)

                    #If processCommand returned "exit", break the loop
                    if result == "exit":
                        break


        except sr.WaitTimeoutError:
            print("Timed out")
        except Exception as e:
            print("Error; {0}".format(e)+"Speak Jarvis..")

