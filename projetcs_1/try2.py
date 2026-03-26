import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import json
from transformers import pipeline
from transformers import GPT2LMHeadModel, GPT2Tokenizer

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "your api"

# Initialize the GPT-2 text generator
generator = pipeline('text-generation', model='gpt2')

def speak(text):
    engine.say(text)
    engine.runAndWait()


model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def aiprocess(command):
    inputs = tokenizer.encode(command, return_tensors="pt")
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

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

    elif "play" in c.lower():
        song = c.lower().replace("play", "").strip()  # Handles multiple words in the song name
        if song:
            link = musiclibrary.music.get(song, None)
            if link:
                webbrowser.open(link)
                speak(f"Playing {song}")
            else:
                speak(f"Sorry, I couldn't find {song} in the music library.")
        else:
            speak("Please specify a song to play.")

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
        output = aiprocess(c)  # Directly call the aiprocess to speak the AI response
        speak(output)
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
            speak("Sorry, I couldn't understand that. Could you please repeat?")
