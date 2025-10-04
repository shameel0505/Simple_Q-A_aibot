Q&A Chatbot

Project Overview

This is a simple AI-powered chatbot built as part of an internship assignment. The bot allows users to type questions and receive concise, human-readable answers using the Google Gemini API.

The project demonstrates not just coding, but also my learning journey, problem-solving, and experimentation with AI tools.
How It Works
	•	Users type a question in a command-line interface or the Streamlit front-end.
	•	The bot sends the question to Google Gemini and returns a clear, concise, human-readable response.
	•	The bot maintains conversation context, so multi-turn dialogues feel natural.

⸻

 My Journey

First Attempt: OpenAI API
	•	I initially tried building this chatbot using OpenAI’s free tier.
	•	It worked, but I quickly ran into token restrictions, which made it difficult to maintain longer conversations or handle detailed queries.

 Switching to Google Gemini
	•	I researched alternatives and found Google Gemini via their Python SDK.
	•	Gemini allowed longer context, better multi-turn conversations, and fast responses.
	•	I configured the model with generation settings to keep answers concise, informative, and human-like.

 Learning & Experimenting
	•	I Googled documentation, watched tutorials, and used ChatGPT as a coding partner to figure out API usage, error handling, and chat session management.
	•	I experimented with different system instructions to make the bot friendly, concise, and informative.
	•	I learned how to handle conversation history and maintain state across multiple turns.

 Going Beyond the Minimum
	•	Added a Streamlit front-end to make the chatbot interactive and user-friendly.
	•	Implemented session-based chat history so the bot remembers the conversation context.
	•	Ensured the bot can gracefully handle exits and empty inputs.

⸻

##  Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/shameel0505/Simple_Q-A_aibot
   cd Simple_Q-A_aibot
   ```

2. **Install dependencies**

   ```bash
   pip install google-generativeai
   ```

3. **Add your API key**
   - Create a file named `api.py` in the same folder.  
   - Add your key like this:
   ```python
   gapi = "YOUR_GOOGLE_GEMINI_API_KEY"
   ```

4. **Run the chatbot**
   - **Command-line version**
     ```bash
     python gemini.py
     ```

---

##  Example Conversation
```
Bot: Hello, how can I help you?
You: What is photosynthesis?
Bot: Photosynthesis is how plants make food using sunlight, water, and carbon dioxide. 
     Imagine a plant as a little chef mixing ingredients to make sugar!
```

