## Let's Walk You Through Something I Created in My Sem-1 🚀
### Python Voice Assistant (Shinchan) 

This is a Python-based voice assistant named "Shinchan" that performs various tasks using voice commands. The assistant can greet the user, fetch information from Wikipedia, open websites like YouTube and Google, play music, check the time, and launch applications like Visual Studio Code. The project utilizes several libraries such as `pyttsx3` for text-to-speech, `speech_recognition` for recognizing voice commands, `wikipedia` for fetching summaries, and `webbrowser`/`os` for handling browser and file interactions.

---

### Features
- **Speech Recognition**: Listens to the user's voice commands.
- **Text-to-Speech**: Responds audibly using `pyttsx3`.
- **Wikipedia Search**: Fetches summaries of topics.
- **Web Browser Control**: Opens websites like YouTube, Google, and Stack Overflow.
- **Music Player**: Plays music from a specified directory.
- **Time Inquiry**: Tells the current time.
- **App Launching**: Opens applications like Visual Studio Code.

---

### How It Works
1. The assistant greets based on the time of day.
2. It listens for voice commands using the microphone.
3. Depending on the command, it performs tasks like:
   - Fetching Wikipedia summaries.
   - Opening popular websites.
   - Playing music from a local directory.
   - Telling the current time.
   - Launching specific applications.

---

### Setup Instructions
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/voice-assistant-shinchan.git
    ```

2. Install dependencies:
    ```bash
    pip install pyttsx3 SpeechRecognition wikipedia
    ```

3. Run the script:
    ```bash
    python shinchan.py
    ```

---

### Example Commands
- "Search [topic] on Wikipedia"
- "Open YouTube"
- "Play music"
- "What time is it?"
- "Open Visual Studio Code"

---

Feel free to customize the code and extend functionality as needed!
