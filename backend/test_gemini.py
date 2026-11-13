import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

load_dotenv(Path(__file__).resolve().parent / ".env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("Gemini API key not found!")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model=os.getenv("GEMINI_MODEL", "gemini-3.8-flash"),
    contents="Explain what an array is in programming in two simple sentences."
)

print("Gemini API connection successful!")
print(response.text)
