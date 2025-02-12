import os
from flask import Flask, render_template, request, jsonify
from chat import get_chat_response
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "rahasia_irfa_banget")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        message = request.json.get('message', '')
        if not message:
            return jsonify({'error': 'Pesan kosong nih bestie!'}), 400

        response = get_chat_response(message)
        return jsonify({'response': response})
    except Exception as e:
        logging.error(f"Error in chat endpoint: {str(e)}")
        return jsonify({'error': 'Waduh error nih bestie, coba lagi ya!'}), 500
