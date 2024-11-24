# AI-Powered Health Care Chatbot

## Instructions to Set Up and Use

Follow these steps to set up and run the **Health Care Chatbot** on your local machine:

### 1. Clone the Repository
You can clone the repository using one of the following methods:
- Using Git:
  ```bash
  git clone https://github.com/Abhinav-NGU/Health-Care-Chatbot.git
  ```
- Or download it manually as a ZIP file from the repository page.

### 2. Install Required Python Modules
Navigate to the project directory and install all the required Python modules using the `requirements.txt` file. Run the following command:
```bash
pip install -r requirements.txt
```

### 3. Ensure a Stable Internet Connection
Even though the chatbot runs locally, a stable and reliable internet connection is required for seamless operation.

### 4. Obtain an API Key from GroqCloud
1. Log in to [GroqCloud](https://console.groq.com).  
2. Navigate to the **API Keys** section and generate a new API key.  
3. **Important:** Keep this key secure and do not share it with others to maintain security.  
4. Copy the API key (a unique hash-like string).

### 5. Configure the `.env` File
1. Locate the `.env` file in the project directory.  
2. Find the following line:
   ```
   GROQ_API_KEY = None
   ```
3. Replace `None` with your API key. It should look like this:
   ```
   GROQ_API_KEY = your_api_key_here
   ```

### 6. Run the Application
Once the setup is complete, start the server by running the following command:
```bash
python manage.py runserver
```

### 7. Access the Chatbot
Open the local link displayed in the terminal (usually `http://127.0.0.1:8000`) in your web browser. You should be directed to the chatbot interface.

---

## Model Information
This chatbot leverages **Llama-3.1-70B-Versatile**, a state-of-the-art large language model (LLM) hosted on GroqCloud. 

### Customizing the Model
If you wish to use a different model, you can modify the chatbot's configuration:
1. Open the `llm_manager.py` file in the project directory.
2. Locate the following code snippet:
   ```python
   LLMManager._instance = ChatGroq(
       temperature=0,
       groq_api_key=settings.GROQ_API_KEY,
       model_name="llama-3.1-70b-versatile"
   )
   ```
3. Update the `model_name` parameter with the desired model name from GroqCloud's available options.  
   For example:
   ```python
   model_name="new-model-name"
   ```

This allows you to switch to another model that better suits your requirements.

### Use Case
The chatbot is specifically designed for healthcare-related conversations, providing AI-powered assistance for various health care scenarios. Future updates will continue to enhance its capabilities and focus.

---

Stay tuned for updates as we refine and improve this chatbot!
