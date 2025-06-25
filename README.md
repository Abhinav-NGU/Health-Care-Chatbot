# AI-Powered Health Care Chatbot

## Instructions to Set Up and Use

Follow these steps to set up and run the **Health Care Chatbot** on your local machine using **Ollama**:

---

### 1. Clone the Repository

You can clone the repository using one of the following methods:

* Using Git:

  ```bash
  git clone https://github.com/Abhinav-NGU/Health-Care-Chatbot.git
  ```
* Or download it manually as a ZIP file from the repository page.

---

### 2. Install Required Python Modules

Navigate to the project directory and install all the required Python modules using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

### 3. Install Ollama (Local LLM)

This chatbot runs **fully offline** using a locally hosted LLM via **Ollama**.
Follow these steps to install Ollama:

* Visit the official site: [https://ollama.com/](https://ollama.com/)
* Download and install Ollama according to your operating system.
* You can also refer to YouTube tutorials for detailed installation steps if needed.

After installing, open your terminal and run:

```bash
ollama pull gemma3:4b
ollama run gemma3:4b
```

Make sure the Ollama server is running at `http://localhost:11434`.

---

### 4. Run the Application

Once Ollama is running, start the Django server:

```bash
python manage.py runserver
```

---

### 5. Access the Chatbot

Open the local link displayed in the terminal (usually `http://127.0.0.1:8000`) in your web browser. You should be directed to the chatbot interface.

---

## Model Information

This chatbot currently uses the **Gemma 3:4B model via Ollama**.

### 🔄 Changing the Model (Dynamic Setup in Future Updates)

The chatbot is designed to make switching models easy in the future.

If you want to change the model:

1. Pull the new model using Ollama:

   ```bash
   ollama pull [new_model_name]
   ```
2. Open the `llm_manager.py` file.
3. Find the following code:

   ```python
   class LLMManager:
       _instance = None

       @staticmethod
       def get_instance():
           if LLMManager._instance is None:
               LLMManager._instance = Ollama(
                   model="gemma3:4b",  # Use the model you've pulled locally
                   temperature=0.0,
                   base_url="http://localhost:11434"  
               )
           return LLMManager._instance
   ```
4. Replace `model="gemma3:4b"` with the name of your newly pulled model.

This process will be made dynamic in future updates to allow model selection from the UI.

---

## Use Case

The chatbot is specifically designed for **healthcare-related conversations**, providing AI-powered assistance for general health advice, symptom checking, and quick health tips.
⚙️ Future updates will continue to refine the experience and expand its capabilities.

---

## 🚀 Planned Future Updates

* ✅ **User Login Page:**
  Personal user accounts to save individual health preferences and improve the user experience.

* ✅ **Temporary Memory:**
  Store temporary health issues (like short-term diseases or recent symptoms) for better session-based assistance.

* ✅ **Permanent Memory:**
  Save permanent user information such as allergies, chronic illnesses, and long-term conditions for more personalized care.

* ✅ **Private Chat History:**
  Chat history will not be shown directly to the user to prioritize a clean and comforting user experience. History management can be added based on future feedback.

---

Stay tuned for more updates as this chatbot continues to evolve!
Your health, privacy, and comfort remain our top priority.
