
# Week 13 - Simple Gemini Chatbot

import os
from dotenv import load_dotenv
from google import genai
from google.genai import errors

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: Gemini API key not found.")
    print("Please check your .env file.")
    raise SystemExit(1)

# Connect to Gemini
client = genai.Client(
    api_key=api_key,
    http_options={"timeout": 60000}
)

print("\n================================")
print("       MY GEMINI CHATBOT")
print("================================")
print("You can start chatting with Gemini.")
print("Type 'exit' to stop the chatbot.")
print("--------------------------------")

try:
    while True:
        user_message = input("\nYou: ").strip()

        if user_message.lower() == "exit":
            print("\nGemini: Goodbye! Have a great day.")
            break

        if not user_message:
            print("Please enter a message.")
            continue

        try:
            print("\nGemini is thinking...", flush=True)

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=user_message
            )

            if response.text:
                print("\nGemini:", response.text)
            else:
                print("\nGemini returned an empty response.")

        except errors.APIError as error:
            print("\nGemini API Error:", error)

        except Exception as error:
            print("\nUnexpected Error:", error)

except KeyboardInterrupt:
    print("\n\nChatbot stopped.")

finally:
    client.close()
    print("Connection closed.")
