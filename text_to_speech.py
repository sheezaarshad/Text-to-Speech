import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Setting properties
engine.setProperty('rate', 200)  # Speed of speech
engine.setProperty('volume', 1)  # Maximum volume
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

# Text to be converted into speech
text = "Hello! This is an example of converting text to speech using Python."

# Convert text to speech
engine.say(text)

# Run the speech engine
engine.runAndWait()

print("Text-to-speech conversion done successfully.")
