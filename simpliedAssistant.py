import speech_recognition as sr
import pyttsx3
from pydub import AudioSegment
from assistant_functions import simple_assistant
from flask import Flask, request, jsonify, send_file

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
    assistant_reply = simple_assistant(recognized_text)
    text_to_audio(assistant_reply, 'responses/output_text.txt',
                  'responses/output_audio.wav')

    response = {
        'text': assistant_reply,
        'audio_url': 'https://us2002.pythonanywhere.com/get_audio'
    }

    return jsonify(response)


@app.route('/get_audio', methods=['GET'])
def get_audio():
    audio_file_path = 'responses/output_audio.wav'
    return send_file(audio_file_path, as_attachment=True)


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


def text_to_audio(text, output_text_file, output_audio_file):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.save_to_file(text, output_audio_file)
    engine.runAndWait()

    with open(output_text_file, "w") as text_file:
        text_file.write(text)


def convert_to_wav(input_file, output_file):
    audio = AudioSegment.from_file(input_file)
    audio.export(output_file, format="wav")


if __name__ == "__main__":
    app.run(debug=True)
