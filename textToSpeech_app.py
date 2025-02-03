import streamlit as st
import pyttsx3

def text_to_speech(text, rate, volume, voice_index):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_index].id)
    engine.say(text)
    engine.runAndWait()

# Streamlit UI
st.set_page_config(page_title="Text-to-Speech App", page_icon="🔊", layout="centered")
st.title("🔊 Text-to-Speech Converter")
st.markdown("### Convert your text into realistic speech with adjustable settings.")

# Input text
text = st.text_area("Enter the text you want to convert to speech:", "Hello! This is an example of converting text to speech using Python.")

# Speech settings
rate = st.slider("Select Speech Rate:", min_value=100, max_value=300, value=200, step=10)
volume = st.slider("Select Volume:", min_value=0.0, max_value=1.0, value=1.0, step=0.1)

# Voice selection
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice_options = [f"{i + 1}. {voice.name}" for i, voice in enumerate(voices)]
voice_choice = st.selectbox("Choose Voice:", voice_options)
voice_index = int(voice_choice.split('.')[0]) - 1

# Convert text to speech
if st.button("🔊 Convert to Speech"):
    if text.strip():
        text_to_speech(text, rate, volume, voice_index)
        st.success("✅ Speech conversion completed!")
    else:
        st.error("❌ Please enter some text to convert.")

# Footer
st.markdown("---")
st.markdown("💡 Created with ❤️ using Python & Streamlit")
