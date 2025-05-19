import os
from groq import Groq

# Create the Groq client
GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

# Set the system prompt
system_prompt = {
    "role": "system",
    "content":
    "You are a helpful assistant. You reply with very short answers."
}

# Initialize the chat history
chat_history = [system_prompt]

MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

while True:
  # Get user input from the console
  user_input = input("You: ")

  # Append the user input to the chat history
  chat_history.append({"role": "user", "content": user_input})

  response = client.chat.completions.create(model=MODEL,
                                            messages=chat_history,
                                            max_tokens=100,
                                            temperature=1.2)
  # Append the response to the chat history
  chat_history.append({
      "role": "assistant",
      "content": response.choices[0].message.content
  })
  # Print the response
  print("Assistant:", response.choices[0].message.content)

