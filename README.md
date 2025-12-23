🎙️ **GemVoice AI – Intelligent Voice Assistant**

🔗 MVP – Experience GemVoice AI Live
- **GitHub Repository (Working Project):** [Explore the Code & Run Your Own Assistant](https://github.com/Pranita-Zalli/GemVoice-AI-Intelligent-Voice-Assistant)
- **3-Minute Demo Video:** [See GemVoice AI in Action 🚀](https://drive.google.com/file/d/1wasBdTYn5Ss-pPvBbqr_DZ6AGxH4EeJd/view?usp=drivesdk)

---

📌 Overview

GemVoice AI is a Python-based intelligent voice assistant that enables natural voice interaction to automate everyday
tasks and provide real-time information. It uses Google Gemini AI for intelligent responses and integrates multiple APIs 
for weather updates, news retrieval, and system-level automation.

---

🚀Key Features

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

🛠 Technology Stack

- Python  
- SpeechRecognition  
- PyAudio  
- pyttsx3 (Text-to-Speech)  
- webbrowser  
- Requests   
- WeatherStack API - real time weather data
- News API - Latest news headlines

---

🟢 Google Technologies Used (Mandatory)
- Google Gemini API (Generative Language API)

🤖 Google AI Tools Integrated
- Gemini AI (gemini-2.5-flash) – for generating intelligent, context-aware responses to user queries

---

🧠 Solution Description:

GemVoice AI is a Python-based intelligent voice assistant that uses Google Gemini AI to generate contextual responses and integrates real-time APIs for weather, news, and task automation. Users interact through voice commands to open applications, initiate WhatsApp chats, fetch weather updates, listen to news, and ask general questions. The assistant combines speech recognition, text-to-speech, AI integration, and system automation to deliver a responsive, hands-free user experience, demonstrating practical implementation of voice-based AI systems in real-world scenarios.

---

🚀 Installation & Setup

1️⃣ Clone the repository
    git clone https://github.com/Pranita-Zalli/GemVoice-AI-Intelligent-Voice-Assistant.git
    cd GemVoice-AI-Intelligent-Voice-Assistant
2️⃣ Install dependencies
    pip install -r requirements.txt
3️⃣ Configure Environment Variables

---

Create a .env file and add:

GEMINI_API_KEY=your_gemini_api_key
WEATHERSTACK_API_KEY=your_weatherstack_api_key
news_api=your_news_api_key

---

4️⃣ Run the project

python main.py

---

🔧 Voice Assistant Workflow

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

📌 Project Highlights

- Practical implementation of AI + voice systems
- Real-world API integration
- Modular and extensible project structure
- Focus on usability and automation

---
