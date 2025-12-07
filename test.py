from ollama import chat
from ollama import ChatResponse

generate: ChatResponse = chat(
    model="Llama3",
    messages=[
        {
            "role": "user",
            "content": "Why is the sea taste salty?",
        },
    ],
)
print(generate["message"]["content"])
print(generate.message.content)

