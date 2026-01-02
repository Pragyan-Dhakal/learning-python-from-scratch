# import speech_recognition as sr
# import webbrowser
# import pyttsx3

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()
# def speak (text):
#     engine.say (text)
#     engine.runAndWait()

# if __name__=="__main__":
#     speak ("Hello sir, How can I help you.")

 



import speech_recognition as sr
import pyttsx3
import webbrowser
import time

# Initialize recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Calibrate for ambient noise
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)

def speak(text):
    # Provide console feedback and speak out loud
    print("Jarvis (speaking):", text)
    engine.say(text)
    engine.runAndWait()

def listen(timeout=3, phrase_time_limit=4):
    with sr.Microphone() as source:
        print("Jarvis (listening)...")
        try:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            text = r.recognize_google(audio).lower()
            print("You said:", text)
            return text
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return ""
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print("Request error:", e)
            return ""

# Initial greeting
speak("Hello, say 'Jarvis' to activate.")

while True:
    # Continuously listen for the wake word "jarvis"
    wake_text = listen()
    if "jarvis" in wake_text:
        speak("You are welcome sir. This model is made by Pragyan Dhakal to provide you with a virtual assistant. How can I help you?")
        command = listen()
        
        if "open youtube" in command:
            speak("Opening YouTube. Working on it...")
            webbrowser.open("https://www.youtube.com")
        elif "open google" in command:
            speak("Opening Google. Working on it...")
            webbrowser.open("https://www.google.com")
        elif "open facebook" in command:
            speak("Opening Facebook. Working on it...")
            webbrowser.open("https://www.facebook.com")
        elif "search" in command:
            # Extract the query from the command
            query = command.replace("search", "", 1).strip()
            if query:
                speak("Searching for " + query + ". Please wait.")
                webbrowser.open("https://www.google.com/search?q=" + query)
                speak("Here are the search results for " + query)
            else:
                speak("Please say what you want me to search for.")
        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break
        else:
            speak("Command not recognized, please try again.")




