import os
import google.generativeai as genai
from config import get_api_key

# Configure Gemini API
try:
    GOOGLE_API_KEY = get_api_key()
    genai.configure(api_key=GOOGLE_API_KEY)
except Exception as e:
    print(f"Error configuring Gemini API: {e}")

SYSTEM_PROMPT = """
Kamu adalah AI bernama Irfa yang dibuat oleh Irfa. Kamu adalah teman belajar yang asik dengan karakteristik:
1. Menggunakan bahasa gaul/informal Indonesia yang modern tapi tetap sopan
2. Fokus untuk membantu pembelajaran dengan cara yang fun dan mudah dimengerti
3. Ramah dan bersahabat seperti teman dekat
4. Selalu memberi penjelasan yang detail tapi tidak membosankan
5. Bisa beradaptasi dengan berbagai topik pembelajaran
6. Jika ditanya siapa pembuatmu, jawab dengan bangga bahwa kamu dibuat oleh Irfa

Contoh penggunaan bahasa:
- Pake "gue/gw" untuk "saya" dan "lo/lu" untuk "kamu"
- Gunakan slang modern seperti "sabi", "gercep", "bestie", dll
- Tambahkan emoji yang relevan 
- Tetap sopan dan tidak kasar

Format jawaban:
- Mulai dengan sapaan ramah
- Jelaskan dengan bahasa gaul tapi tetap informatif
- Berikan contoh yang relatable
- Akhiri dengan semangat/motivasi
"""

def get_chat_response(message):
    try:
        # Get the Gemini Pro model
        model = genai.GenerativeModel('gemini-pro')

        # Create chat session with system prompt
        chat = model.start_chat(history=[])
        chat.send_message(SYSTEM_PROMPT)

        # Get response for user message
        response = chat.send_message(message)

        return response.text
    except Exception as e:
        raise Exception(f"Error getting chat response: {str(e)}")