import google.generativeai as genai
from api import gapi
genai.configure(api_key=gapi)
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.5-flash",
  generation_config=generation_config,
  system_instruction="""You are an AI assistant that answers user questions in a command-line interface.When a user types a question, provide a clear, informative, and human-readable answer. 
Keep your responses concise, easy to understand, and directly relevant to the question. 
Do not include long explanations unless necessary. 
Use examples or analogies only when they help clarify the answer. 
Avoid unnecessary commentary and keep the interaction focused on solving the user’s query.""",
)

chat_session = model.start_chat(
    history=[]
)

print("Bot: Hello, how can I help you?")

while True:

    user_input = input("You: ")
    if user_input.lower() in ['exit','quit','bye']:
        response = chat_session.send_message(user_input)
        model_response = response.text
        print(f'Bot: {model_response}')
        break
    response = chat_session.send_message(user_input)

    model_response = response.text

    print(f'Bot: {model_response}')


    chat_session.history.append({"role": "user", "parts": [user_input]})
    chat_session.history.append({"role": "model", "parts": [model_response]})

