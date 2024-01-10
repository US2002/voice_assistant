# Simplified Voice Assistant

## Description

This simplified voice assistant, implemented in Python, utilizes speech recognition and text-to-speech conversion to interact with users via audio input. It provides various functionalities and communicates through defined API endpoints.

## Files

- `simplifiedAssistant.py`: Python file containing the Flask-based server setup, audio processing functions, and API endpoints for audio processing and interaction.
- `assistant_functions.py`: Python file with functions related to the assistant's responses based on intents.

## API Endpoints

### `/`

- **Description**: Home endpoint displaying contact information.
- **Method**: `GET`
- **Response**: Display contact details and creator information.

### `/check`

- **Description**: Endpoint to check server status.
- **Method**: `GET`
- **Response**: Confirms server status.

### `/help`

- **Description**: Endpoint providing information about available API endpoints.
- **Method**: `GET`
- **Response**: Lists available API endpoints and their purposes.

### `/process_audio`

- **Description**: Accepts an audio file, processes it, and saves it for further handling.
- **Method**: `POST`
- **Request Parameters**: `file` (Audio file)
- **Response**: Message indicating successful audio processing.

### `/get_reply`

- **Description**: Fetches AI-generated replies based on processed audio.
- **Method**: `GET`
- **Response**: AI-generated reply text along with an audio URL to retrieve the audio reply.

### `/get_audio`

- **Description**: Endpoint to download the AI-generated audio reply.
- **Method**: `GET`
- **Response**: Returns the AI-generated audio file as an attachment.

## Usage

1. Ensure required Python libraries are installed (`speech_recognition`, `pyttsx3`, `pydub`, `Flask`).
2. Run the `simplifiedAssistant.py` file to start the Flask server.
3. Access the defined API endpoints to interact with the voice assistant.

## How to Contribute

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make changes and submit a pull request.

## Authors

- [Ujjawal Soni/DIT University](https://github.com/us2002)
