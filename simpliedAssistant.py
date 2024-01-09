from flask import Flask, request, jsonify, send_file
import speech_recognition as sr
import pyttsx3
from assistant_functions import simple_assistant

app = Flask(__name__)

recognizer = sr.Recognizer()


@app.route('/process_audio', methods=['POST'])
def process_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    audio_file = request.files['file']
    if audio_file.filename == '':
        return jsonify({'error': 'No selected file'})

    if audio_file:
        audio_file.save('responses/input.wav')

    return jsonify({'message': 'Audio received successfully'})


@app.route('/get_reply', methods=['GET'])
def get_reply():
    recognized_text = audio_to_text('responses/input.wav')
    assistant_reply = simple_assistant(recognized_text)
    text_to_audio(assistant_reply, 'responses/output_text.txt',
                  'responses/output_audio.wav')

    response = {
        'text': assistant_reply,
        'audio_url': 'http://127.0.0.1:5000/get_audio'
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
    engine.save_to_file(text, output_audio_file)
    engine.runAndWait()

    with open(output_text_file, "w") as text_file:
        text_file.write(text)


if __name__ == "__main__":
    app.run(debug=True)
