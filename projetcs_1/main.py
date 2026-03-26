import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import json

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "d5c0e344c6c6468889fcaff914f08eef"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    API_KEY = 'your api key'
    MODEL_ID = 'gpt2'

    url = f"https://api-inference.huggingface.co/models/{MODEL_ID}"

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "inputs": command
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        generated_text = result[0]['generated_text']
        speak(generated_text)  # Speak the generated text directly
    else:
        print(f"Error: {response.status_code}")
        print(f"Details: {response.text}")
        speak("Sorry, I could not process your request.")  # Speak error message

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
        speak("Opening Instagram")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")
        speak("Opening WhatsApp")
    elif "open twitter" in c.lower():
        webbrowser.open("https://twitter.com")
        speak("Opening Twitter")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music.get(song, None)
        if link:
            webbrowser.open(link)
            speak(f"Playing {song}")
        else:
            speak(f"Sorry, I couldn't find {song} in the music library.")

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for article in articles:
                speak(article["title"])
        else:
            speak("Sorry, I couldn't fetch the news at the moment.")
    
    else:
        aiprocess(c)  # Directly call the aiprocess to speak the AI response

if __name__ == "__main__":
    speak("Initializing computer....")
    while True:
        r = sr.Recognizer()
        print("Recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if word.lower() == "computer":
                speak("Yes, how can I assist you?")
                with sr.Microphone() as source:
                    print("Computer is listening...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(f"Command received: {command}")
                    processcommand(command)

        except Exception as e:
            print(f"Error: {e}")
