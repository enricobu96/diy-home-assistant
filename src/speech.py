import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os
from pydub import AudioSegment, playback

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("temp.mp3")
    sound = AudioSegment.from_mp3("temp.mp3")
    playback.play(sound)
    os.remove("temp.mp3")

def speech_to_text(lang='en'):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    text = ''
    try:
        text = r.recognize_google(audio, language=lang)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return text