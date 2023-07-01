import speech_recognition as sr
import pyttsx3
import webbrowser
from nltk.tokenize import word_tokenize

# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print("User:", query)
        return query
    except Exception as e:
        print(e)
        return ""

# Function to process user's command and provide a response
def process_command(command):
    tokens = word_tokenize(command.lower())

    if "hello" in tokens:
        speak("Hello! How can I assist you?")
    elif "search" in tokens:
        query = ' '.join(tokens[tokens.index("search") + 1:])
        url = f"https://www.google.com/search?q={query}"
        speak(f"Searching for {query} on Google.")
        webbrowser.open(url)
    elif "goodbye" in tokens:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand your command.")

# Main program loop
if __name__ == "__main__":
    while True:
        speak("How can I assist you?")
        command = listen()
        process_command(command)
