# from flask import Flask, request, jsonify
# from chatbot import generate_response

# app = Flask(__name__)
# chat_history = []

# @app.route('/chat', methods=['POST'])
# def chat():
#     global chat_history
#     user_input = request.json.get("message", "")
#     if not user_input:
#         return jsonify({"error": "Message cannot be empty"}), 400
    
#     response, chat_history = generate_response(user_input, chat_history)
#     return jsonify({"response": response})

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify
from chatbot import generate_response

app = Flask(__name__)
chat_history = []  # Store chat history globally

@app.route('/chat', methods=['POST'])
def chat():
    """Handles user messages and generates chatbot responses."""
    global chat_history
    user_input = request.json.get("message", "")
    
    if not user_input:
        return jsonify({"error": "Message cannot be empty"}), 400

    response, chat_history = generate_response(user_input, chat_history)
    return jsonify({"response": response})

@app.route('/clear_chat', methods=['POST'])
def clear_chat():
    """Clears the chat history from the backend."""
    global chat_history
    chat_history = []  # Reset chat history
    return jsonify({"message": "Chat history cleared successfully."})

if __name__ == '__main__':
    app.run(debug=True)
