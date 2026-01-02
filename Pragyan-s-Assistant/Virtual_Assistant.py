import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import pywhatkit

# Initialize recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 200)  # Increase speech rate for faster output

# Calibrate for ambient noise (set duration to 1 second for quicker startup)
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)

def speak(text):
    print("Jarvis (speaking):", text)
    engine.say(text)
    engine.runAndWait()

def listen_with_retry(timeout=5, phrase_time_limit=5, retries=3):
    """
    Attempts to capture speech input multiple times.
    Returns recognized text (in lowercase) or an empty string if nothing is captured.
    """
    for attempt in range(retries):
        with sr.Microphone() as source:
            print(f"Jarvis (listening)... Attempt {attempt + 1}")
            try:
                audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                text = r.recognize_google(audio).lower()
                print("You said:", text)
                return text
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start.")
            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print("Request error:", e)
    return ""

def process_command(command):
    """
    Processes the given command.
    Returns True if the command is an exit command, else False.
    """
    command = command.strip()
    # Pre-defined website commands
    if command.startswith("open youtube"):
        speak("Opening YouTube. Working on it...")
        webbrowser.open("https://www.youtube.com")
    elif command.startswith("open google"):
        speak("Opening Google. Working on it...")
        webbrowser.open("https://www.google.com")
    elif command.startswith("open facebook"):
        speak("Opening Facebook. Working on it...")
        webbrowser.open("https://www.facebook.com")
    # Generic "open" command for any website
    elif command.startswith("open"):
        website = command.replace("open", "", 1).strip()
        if website:
            # If website doesn't contain a dot, assume it's a .com domain
            if '.' not in website:
                website = website.replace(" ", "")
                url = "https://www." + website + ".com"
            else:
                if not website.startswith("http"):
                    url = "https://" + website
                else:
                    url = website
            speak("Opening " + website + ".")
            webbrowser.open(url)
        else:
            speak("Please say the name of the website.")
    elif command.startswith("search"):
        query = command.replace("search", "", 1).strip()
        if query:
            speak("Searching for " + query + ". Please wait.")
            webbrowser.open("https://www.google.com/search?q=" + query)
            speak("Here are the search results for " + query)
        else:
            speak("Please say what you want me to search for.")
    # Play any song using pywhatkit (supports any song)
    elif command.startswith("play"):
        song = command.replace("play", "", 1).strip()
        if song:
            speak("Playing " + song + ". Enjoy!")
            pywhatkit.playonyt(song)
        else:
            speak("Please say the name of the song.")
    elif command in ("exit", "stop"):
        speak("Goodbye!")
        return True
    else:
        speak("Command not recognized, please try again.")
    return False

def main():
    # One-time activation with the wake word "mika"
    speak("Hello, say 'mika' to activate.")
    wake_text = listen_with_retry()
    if "mika" in wake_text:
        speak("Welcome sir. This model is built by Pragyan Dhakal to provide you with a virtual assistant service. You can search for anything, open any website, and play any YouTube video on your device. So,How may I assist you today?")
        # Continuously listen for commands without needing the wake word again
        while True:
            command = listen_with_retry()
            if not command:
                speak("I did not catch that. Please try again.")
                continue
            if process_command(command):
                break
    else:
        speak("Wake word not detected. Exiting.")

if __name__ == "__main__":
    main()