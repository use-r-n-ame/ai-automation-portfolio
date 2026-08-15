import requests
# import json
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY") # my api key stored inside

# if no api
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=API_KEY) 

chat = client.chats.create(model="gemini-3.5-flash-lite")

response = chat.send_message(
    "Categorize this text as 'Complaint', 'Inquiry', or 'Praise': My order arrived broken"
)

print(response.text)