import requests

URL = "http://localhost:11434/api/chat"

def chat(prompt):
    response = requests.post(URL, json = {
        "model": "llama3.2",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    })

    return response.json()["message"]["content"]

print("Local LLM Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    reply = chat(user_input)
    print("Bot: ", reply)
