# Voice Assistant

This project provides a Python-based tool to create an interactive Voice Assistant. It integrates Speech Recognition for understanding user commands and Speech Synthesis for responding. The assistant offers utilities like time retrieval, opening websites, telling jokes, and playing music from a predefined playlist.

<div style="text-align:center;">
  <img src="./Voice Assistant thumbnail.jpg" alt="Voice Assistant Project Thumbnail" width="500px" height="auto">
</div>

## Features

- **Speech Recognition**: Processes voice commands using Google Speech Recognition API.
- **Speech Synthesis**: Generates voice responses using pyttsx3.
- **Utilities**:
  - Tells the current time.
  - Opens YouTube and portfolio links.
  - Tells jokes using `pyjokes`.
  - Plays songs from a predefined playlist.
- **User Interaction**: Pre-configured responses for user queries.

## Requirements

To run this project, you'll need Python 3.x and the following libraries:

- `pyttsx3` : Text-to-speech conversion library
- `speech_recognition` : Library for recognizing speech input
- `webbrowser` : Standard library to open web pages
- `datetime` : Standard library for date and time manipulation
- `pyjokes` : Library for generating programming jokes
- `os` : Standard library for interacting with the operating system
- `time` : Standard library for time-related tasks

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tejasb15/Python-Projects.git
   cd Python-Projects
   ```

2. Install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Or, if you're only installing the required libraries individually:

   ```bash
   pip install pyttsx3
   ```

   ```bash
   pip install speech_recognition
   ```

   ```bash
   pip install pyjokes
   ```

3. No additional dependencies are required, as Python’s `webbrowser`,`datetime`,`os`,`time` module is part of the standard library.

## Usage

1. Open the project directory:

   ```bash
   cd Python-Projects/Voice Assistant
   ```

2. Run the script:

   ```bash
   python Voice_Assistant.py
   ```

3. Interact with the assistant by speaking commands such as:
   - "What is your name?"
   - "What time is it?"
   - "Tell me a joke."
   - "Open YouTube."
   - "Play a song."

## Example

- **User**: "What is your name?"
- **Assistant**: "My Name is David."

- **User**: "Tell me a joke."
- **Assistant**: "Why don’t scientists trust atoms? Because they make up everything!"

## References

This project uses the following Python module:

- [Google Speech Recognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3 Documentation](https://pypi.org/project/pyttsx3/)
- [pyjokes Documentation](https://pypi.org/project/pyjokes/)

## Author

**Tejas Bharambe**  
Full Stack Developer | AWS Enthusiast  
[GitHub](https://github.com/tejasb15) | [LinkedIn](https://www.linkedin.com/in/tejasb15/)
