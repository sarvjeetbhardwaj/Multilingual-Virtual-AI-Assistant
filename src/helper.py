import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS


def voice_input():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening.....')
        audio = r.listen(source)

    try:
        text=r.recognize_google(audio)
        print("you said: ", text)
        return text
    except sr.UnknownValueError:
        print("sorry, could not understand the audio")
    except sr.RequestError as e:
        print("could not request result from google speech recognition service: {0}".format(e))

def llm_model(user_text):
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

    model = genai.GenerativeModel('gemini-2.0-flash')
    
    response=model.generate_content(user_text)
    
    result=response.text
    
    return result

def text_to_speech(text):
    tts=gTTS(text=text, lang="en")
    tts.save("speech.mp3")