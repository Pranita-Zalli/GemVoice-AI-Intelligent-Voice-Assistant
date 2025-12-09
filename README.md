🧠 Jarvis AI Assistant – Voice Controlled Desktop Assistant (Python)

A smart AI-powered voice assistant built using Python, capable of performing tasks like opening websites, playing songs, reading news, and answering general knowledge questions using Gemini API — all through your voice commands.

✨ Overview

Jarvis AI Assistant is a Python-based voice command application that works similar to Alexa.
It listens to your voice, processes your requests, and responds using text-to-speech.
It also includes smart features like news reading, music playback, and AI conversational abilities.

This project demonstrates strong skills in Python, APIs, automation, AI integration, and speech processing.

🚀 Features
🔊 Voice Recognition
Activates when you say “Jarvis”
Responds with: “Yaa”

🌐 Website Automation
Commands like:
“open google”
“open youtube”
“open facebook”
“open linkedin”

Jarvis opens the website instantly.

🎵 Music Library
Custom music library created using Python dict datatpe
Example:
“Play Bulleya” → plays music on YouTube

📰 News Reader (NewsAPI)
“Tell me news” → Reads top headlines
“Stop” → Stops reading immediately

🤖 AI Conversational Mode (Gemini API)
Ask anything:
“What is coding?”
“Explain programming.”
“Tell me about Python.”

Jarvis responds with accurate AI-generated information.
You can say “stop” anytime to stop the speech.

👋 Exit Command

“Bye” → Jarvis replies:
“Okay, bye. Have a great day!”

🛠️ Tech Stack
Python
SpeechRecognition
PyAudio
pyttsx3
webbrowser
Requests (for APIs)
Google Gemini API
News API

🔧 How It Works
Jarvis AI works in a simple, modular flow:

1️⃣ Voice Input
Listens using microphone & SpeechRecognition library
Activates when hearing “Jarvis” and sayes "Yaa"

2️⃣ Speech-to-Text
Your speech is converted into text by STT engine

3️⃣ Command Processing
The text command is analyzed in Python.
Examples:
"open google" → opens Google
"play bulleya" → plays YouTube music
"tell me news" → fetches headlines
"what is coding" → calls Gemini API

4️⃣ API Integration
News API → fetch latest headlines
Gemini API → generate intelligent responses

5️⃣ Perform Action
Executes task: open browser, play song, read news, answer Q&A.

6️⃣ Text-to-Speech Output
Uses pyttsx3 to speak responses back to the user.

7️⃣ Stop/Exit
"stop" → stops speaking
"bye" → exits assistant

🚀 Future Enhancements
  1. Weather Reporting: Using Weather API.
  2. Alarm & Reminder System: Set alarms with voice.
  3. WhatsApp & Email Automation: Send messages or emails using voice.
  4. GUI Desktop Version: A graphical interface for Jarvis.
  5. Task Scheduling: Manage events & reminders.
