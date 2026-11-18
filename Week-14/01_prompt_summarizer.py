
import os
import json
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types


# Load Gemini API key from Week-13 environment file
load_dotenv("Week-13/.env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found. Please check Week-13/.env")


# Create Gemini client
client = genai.Client(
    api_key=api_key,
    http_options={"timeout": 60000}
)


print("================================")
print("       AI TEXT SUMMARIZER")
print("================================")


# Ask user to select summary length
print("\nChoose summary length:")
print("1. Short")
print("2. Medium")
print("3. Detailed")

choice = input("\nEnter your choice (1/2/3): ")


# Define summary lengths
summary_lengths = {
    "1": "1 to 2 sentences",
    "2": "3 to 5 sentences",
    "3": "6 to 8 sentences"
}


try:

    if choice not in summary_lengths:
        print("Invalid choice! Please select 1, 2, or 3.")

    else:

        # Get text from user
        text = input("\nEnter text to summarize:\n")

        if not text.strip():
            print("Please enter some text to summarize.")

        else:

            selected_length = summary_lengths[choice]

            # Create prompt
            prompt = f"""
Act as an expert text summarizer and teacher.

Summarize the following text for a complete beginner.

Instructions:
1. Use simple English.
2. Follow the selected summary length strictly: {selected_length}.
3. Count the sentences before returning the summary.
4. Include exactly 3 key points.
5. Only include information from the original text.
6. Return valid JSON with these exact fields:
   - summary: a string
   - key_points: an array of 3 strings

Text:
{text}
"""

            # Generate response with automatic retry
            response = None

            for attempt in range(3):

                try:

                    print("\nGenerating summary...")

                    response = client.models.generate_content(
                        model="gemini-3.5-flash-lite",
                        contents=prompt,
                        config=types.GenerateContentConfig(
                            response_mime_type="application/json"
                        )
                    )

                    break

                except Exception as e:

                    if "503" in str(e) and attempt < 2:

                        wait_time = (attempt + 1) * 5

                        print(
                            f"\nGemini server is busy. "
                            f"Retrying in {wait_time} seconds..."
                        )

                        time.sleep(wait_time)

                    else:
                        raise

            # Process Gemini response
            if response and response.text:

                result = json.loads(response.text)

                print("\n========== SUMMARY ==========")
                print(result["summary"])

                print("\n========== KEY POINTS ==========")

                for point in result["key_points"]:
                    print(f"- {point}")

                print("\nJSON generated and parsed successfully!")

            else:
                print("Gemini returned an empty response.")


except json.JSONDecodeError:

    print("Could not parse Gemini's JSON response.")

except Exception as e:

    print(f"\nAn error occurred: {e}")

finally:

    client.close()
