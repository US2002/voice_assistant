import speech_recognition as sr
from pydub import AudioSegment
from flask import Flask, request, jsonify
from assistant_functions import simple_assistant
from flowgpt import Resultscrapper, SendMessage, Websiteopener, waitfortheanswer

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Ujjawal the Creator of this Voice Assistant!\nYou can contact me on\nLinkedin: ujjawalsoni2002\nMail: ujjawal.soni2002@gmail.com\nWebsite: https://us2002.github.io/Links-and-Websites/Website/index.html'


@app.route('/check')
def check():
    return 'Server is working fine!'


@app.route('/help')
def help():
    return '/process_audio : For taking Audio file as input!\n/get_reply : For receveing reply of the Audio file you sent\n/get_audio : For receving reply as an audio file of the Audio file you sent'


recognizer = sr.Recognizer()


@app.route('/process_audio', methods=['POST'])
def process_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    audio_file = request.files['file']
    if audio_file.filename == '':
        return jsonify({'error': 'No selected file'})

    if audio_file:
        audio_file.save('responses/input.aac')
        convert_to_wav('responses/input.aac', 'responses/input.wav')

    return jsonify({'message': 'Audio received successfully'})


@app.route('/get_reply', methods=['GET'])
def get_reply():
    recognized_text = audio_to_text(
        'responses/input.wav')
    #!FOR SIMPLE ASSISTANT
    assistant_reply = simple_assistant(recognized_text)
    response = {
        'text': assistant_reply,
        'recevied': recognized_text
    }

    return jsonify(response)


@app.route('/get_flow_reply', methods=['GET'])
def get_flow_reply():
    recognized_text = audio_to_text(
        'responses/input.wav')
    #!FOR SIMPLE ASSISTANT
    # assistant_reply = simple_assistant(recognized_text)
    #!FOR FLOWGPT
    Websiteopener()
    SendMessage(Query=recognized_text)
    waitfortheanswer()
    assistant_reply = Resultscrapper()
    response = {
        'text': assistant_reply,
        'recevied': recognized_text
    }

    return jsonify(response)


def audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language="en")
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio"
    except sr.RequestError:
        return "Request error occurred"


def convert_to_wav(input_file, output_file):
    audio = AudioSegment.from_file(input_file)
    audio.export(output_file, format="wav")


if __name__ == "__main__":
    app.run(debug=True)
