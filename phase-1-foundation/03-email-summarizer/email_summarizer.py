import os
import time
from pathlib import Path
from dotenv import load_dotenv
from google import genai

env_path = Path(__file__).parent.parent / '01-python-api-basics' / '.env'
load_dotenv(env_path)

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("No key found in .env")


def process_email(subject, body):
    """Send email to Gemini for summarization and prioritization"""
    prompt = f"""
    Analyze this email and return:
    1. A one-sentence summary
    2. Priority level (High/Medium/Low)
    
    Subject: {subject}
    Body: {body[:500]}  # Truncate to avoid token limits
    
    Format your response exactly as:
    Summary: [your summary]
    Priority: [High/Medium/Low]
    """
    
    try:
        chat = client.chats.create(model="gemini-3.5-flash-lite")
        response = chat.send_message(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"
