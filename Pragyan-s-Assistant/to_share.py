import streamlit as st
import pyttsx3
import webbrowser
import pywhatkit

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 200)  # Increase speech rate for faster output

def speak(text):
    """Function to speak text output using pyttsx3."""
    st.write(f"Jarvis (speaking): {text}")
    engine.say(text)
    engine.runAndWait()

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
            if '.' not in website:
                website = website.replace(" ", "")
                url = "https://www." + website + ".com"
            else:
                if not website.startswith("http"):
                    url = "https://" + website
                else:
                    url = website
            speak(f"Opening {website}.")
            webbrowser.open(url)
        else:
            speak("Please say the name of the website.")
    elif command.startswith("search"):
        query = command.replace("search", "", 1).strip()
        if query:
            speak(f"Searching for {query}. Please wait.")
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Here are the search results for {query}")
        else:
            speak("Please say what you want me to search for.")
    elif command.startswith("play"):
        song = command.replace("play", "", 1).strip()
        if song:
            speak(f"Playing {song}. Enjoy!")
            pywhatkit.playonyt(song)
        else:
            speak("Please say the name of the song.")
    elif command in ("exit", "stop"):
        speak("Goodbye!")
        return True
    else:
        speak("Command not recognized, please try again.")
    return False

# Streamlit interface
st.title("Virtual Assistant")

# One-time activation with a keyword
st.write("Say 'mika' to activate.")
user_input = st.text_input("Enter your command:")

if user_input:
    if "mika" in user_input.lower():
        speak("Welcome sir. This model is built by Pragyan Dhakal to provide you with a virtual assistant service. You can search for anything, open any website, and play any YouTube video on your device. How may I assist you today?")
        
        # Continuously listen for commands
        command_input = st.text_input("Enter your command below:")
        if command_input:
            if process_command(command_input):
                st.write("Session ended.")
    else:
        speak("Wake word not detected.")
