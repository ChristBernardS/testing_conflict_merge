from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(
    model="Llama3",
    messages=[
        {
            "role": "user",
            "content": "Why is the sky blue?",
        },
    ],
)
print(response["message"]["content"][0])
print(response.message.content)
