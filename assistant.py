from flask import Flask, request, jsonify
import speech_recognition as sr
import pyttsx3
from assistant_functions import simple_assistant
# from flowgpt import Checker, Resultscrapper, SendMessage, Websiteopener, waitfortheanswer

recognizer = sr.Recognizer()


#! THIS IS THE MAIN FILE WITH VOICE ASSISTANT


def get_voice_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)

    try:
        print("Recogizing....")
        query = r.recognize_google(audio, language="en")
        print(f"==> Ujjawal : {query}")
        return query.lower()

    except:
        return ""


def audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language="en")
        print(text)
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio"
    except sr.RequestError:
        return "Request error occurred"


def speak(text):
    engine = pyttsx3.init()
    Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    engine.setProperty('voice', Id)
    print("")
    print(f"==> Personal AI : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()


def text_to_audio(text, output_text_file, output_audio_file):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_audio_file)
    engine.runAndWait()

    with open(output_text_file, "w") as text_file:
        text_file.write(text)


def main():
    print("AI Assistant: Hello! How can I assist you?")
    #! VIA FILE OPERATED
    input_audio_file = 'play.wav'
    output_text_file = 'responses/output_text.txt'
    output_audio_file = 'responses/output_audio.wav'

    recognized_text = audio_to_text(input_audio_file)
    assistant_reply = simple_assistant(recognized_text)
    text_to_audio(assistant_reply, output_text_file, output_audio_file)

    #! VOICE COMMAND OPPERATED
    # Websiteopener()
    # Checker()
    # while True:
    #     command = get_voice_command()
    #     if command == None:
    #         pass
    #     response = simple_assistant(command)
    #     speak(response)
    #     if command.lower() in ["exit", "bye"]:
    #         break
    #         # SendMessage(Query=command)
    #         # waitfortheanswer()
    #         # Text = Resultscrapper()


if __name__ == "__main__":
    main()
