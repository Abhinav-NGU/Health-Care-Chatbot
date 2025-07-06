# AI-Powered Health Care Chatbot

## Overview

This project is an **AI-powered Health Care Chatbot** with a modern, user-friendly interface built using **Vue.js** for the frontend and **Django** for the backend API. The chatbot provides general health advice and information, and runs fully offline using a local AI model via **Ollama**.

---

## How to Use

### 1. Clone the Repository

Download or clone the project to your computer:

```bash
git clone https://github.com/Abhinav-NGU/Health-Care-Chatbot.git
```

---

### 2. Install Requirements

- **Python dependencies:**  
  In the project folder, run:
  ```bash
  pip install -r requirements.txt
  ```

- **Node.js dependencies for Vue.js:**  
  In the `Chatbotvue` folder, run:
  ```bash
  npm install
  ```
  This will install all frontend dependencies listed in `package.json`.

- **Install Axios (for API requests):**  
  Still in the `Chatbotvue` folder, run:
  ```bash
  npm install i
  ```
  Axios is used by the Vue.js frontend to communicate with the Django API.

---

### 3. Set Up Ollama (Local AI Model)

- Download and install Ollama from [https://ollama.com/](https://ollama.com/)
- In your terminal, run:
  ```bash
  ollama pull gemma3:4b
  ollama run gemma3:4b
  ```
- Make sure Ollama is running at `http://localhost:11434`

---

### 4. Start the Servers

- **Start Django API:**
  ```bash
  python manage.py runserver
  ```
- **Start Vue.js Frontend:**
  ```bash
  cd Chatbotvue
  npm run dev
  ```

---

### 5. Chat With the Bot

- Open your browser and go to the link shown in the terminal (usually `http://localhost:5173` for Vue).
- You’ll see a clean, modern chat interface where you can ask health-related questions.

---

## Features

- **Modern Chat UI:** Built with Vue.js for a smooth and responsive experience.
- **API-Driven:** All chat messages are handled through a Django API.
- **Offline AI:** Uses Ollama to run the AI model locally—no internet needed for chat.
- **Healthcare Focus:** Designed for general health advice, symptom checking, and tips.
- **Privacy First:** No chat history is shown to the user for a clean and private experience.

---

## Future Plans

- User accounts and login
- Remembering user health preferences
- More personalized advice
- Easy model switching

---

**Enjoy your private, AI-powered health care assistant!**
