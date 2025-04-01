import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class GeminiChat:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-pro")
        self.chat = self.model.start_chat(history=[])

    def ask(self, message: str) -> str:
        try:
            response = self.chat.send_message(message)
            return response.text
        except Exception as e:
            return f"Error: {e}"
