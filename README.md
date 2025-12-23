## 🎥 Demo Video

👉 **[Experience GemVoice AI in Action 🚀](https://drive.google.com/file/d/1wasBdTYn5Ss-pPvBbqr_DZ6AGxH4EeJd/view?usp=drivesdk)**

---

🎙️🧠 GemVoice – An AI-Powered Voice Assistant using Google Gemini

GemVoice is a voice-controlled desktop assistant built using Python and powered by Google Gemini AI. It enables hands-free interaction by understanding spoken commands, performing automation tasks, retrieving real-time information, and generating intelligent conversational responses.

The assistant runs locally and communicates entirely through voice for a smooth and intuitive user experience.

---

🔍 Overview

GemVoice functions as a smart personal assistant designed for desktop environments. It listens for voice commands, analyzes user intent using Python logic and AI models, and responds through natural-sounding speech.

The project combines voice recognition, AI-driven reasoning, and system automation into a single modular application.

---

🚀Features

🔊 Voice Activation
- Activated using the keyword “Jarvis”
- Confirms activation with “Yaa”
- Continuously listens for commands

🌐 Website Automation
Supports commands such as:
- `open google`
- `open youtube`
- `open facebook`
- `open linkedin`

Opens the requested website instantly in the default browser.

🎵 Music Playback
- Custom music library implemented using Python dictionary
- Example:
  - `play bulleya` → opens the song on YouTube

📰 News Reading
- Fetches top headlines using News API
- Reads news aloud on command
- `stop` → stops speech immediately

🌦 Weather Information
- Command: `tell me weather`
- Prompts for city name
- If recognized → provides city-specific weather
- If not recognized → defaults to current location and announces:  
  “Speech not recognized. Using current location.”

⏰ Alarm / Clock Access
- Command: `open alarm`
- Opens the system clock or alarm application

💬 WhatsApp Automation
- Command: `open whatsapp`
- Requests phone number via voice
- Opens WhatsApp chat with the specified number
- If number is not recognized → asks for manual input

🤖 AI Conversational Mode
- Handles general questions using **Google Gemini AI**
- Example queries:
  - `what is coding`
  - `explain programming`
  - `tell me about python`
- Responses are generated contextually and spoken aloud
- `stop` → interrupts speech output

 👋 Exit Command
- `bye` → confirms and exits the assistant gracefully

---

🛠️ Technology Stack

- Python  
- SpeechRecognition  
- PyAudio  
- pyttsx3 (Text-to-Speech)  
- webbrowser  
- Requests  
- Google Gemini API  
- News API  
- Weather API  

---

🔧 System Workflow

1️⃣ Voice Input 🎤  
   Captured using microphone and SpeechRecognition.

2️⃣ Speech-to-Text
   Converts spoken input into text.

3️⃣ Command Processing 
   Determines whether the request is automation, API-based, or AI-driven.

4️⃣ API & AI Handling
   - News and weather fetched via APIs  
   - Intelligent responses generated using Google Gemini

5️⃣ Action Execution
   Performs system tasks or responds with speech.

6️⃣ Text-to-Speech Output 🔊  
   Converts responses into voice using pyttsx3.

---

▶️ Running the Application

1. Clone the repository  
2. Install required Python dependencies  
3. Configure API keys in a `.env` file  
4. Run the main Python script  
5. Interact using voice commands  

---

✅ Summary

GemVoice is a fully functional AI-powered voice assistant that integrates speech recognition, desktop automation, and Google Gemini AI to deliver an intelligent and hands-free user experience.
