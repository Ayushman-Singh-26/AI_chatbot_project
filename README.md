# 🎤 AI Voice Assistant using Python

## 📌 Overview
This project is a Python-based AI Voice Assistant that can perform various tasks using voice commands. It integrates speech recognition, text-to-speech, and external APIs to automate everyday actions like opening websites, playing music, fetching news, and generating AI responses.

---

## 🚀 Features
- 🎤 Voice command recognition  
- 🌐 Open popular websites (Google, YouTube, LinkedIn, etc.)  
- 🎵 Play songs from a custom music library  
- 📰 Fetch latest news using News API  
- 🤖 Generate AI-based responses using Hugging Face API  
- 🔊 Text-to-speech output  

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **Libraries:**  
  - SpeechRecognition  
  - pyttsx3  
  - requests  
- **APIs Used:**  
  - Hugging Face Inference API  
  - News API  

---

## 📂 Project Structure
```
AI_chatbot_project/
│── main.py              # Main application logic
│── client.py            # API interaction (Hugging Face)
│── musiclibrary.py      # Custom music links
│── README.md            # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```
git clone https://github.com/Ayushman-Singh-26/Al_chatbot_project
cd Al_chatbot_project
```

### 2️⃣ Install dependencies
```
pip install -r requirements.txt
```

*(If requirements.txt is not available, install manually:)*
```
pip install SpeechRecognition pyttsx3 requests
```

### 3️⃣ Add your API Keys
Replace the placeholders in the code with your own API keys:
```
HUGGING_FACE_API_KEY = "YOUR_API_KEY"
NEWS_API_KEY = "YOUR_API_KEY"
```

---

## ▶️ How to Run
```
python main.py
```

Say **"computer"** to activate the assistant, then give commands like:
- "Open Google"  
- "Play millionaire"  
- "Give me news"  

---

## 💡 Future Improvements
- Add GUI interface (Tkinter / PyQt)  
- Improve NLP for better understanding  
- Add more automation features  
- Integrate with smart home devices  

---

## 📸 Demo
Add screenshots or a demo video here to showcase your project.

---

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## 📬 Contact
If you have any feedback or suggestions, feel free to connect with me on LinkedIn.

---

## ⭐ Acknowledgements
- Hugging Face for AI models  
- Open-source Python libraries  

---

## 📄 License
This project is open-source and available under the MIT License.