from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Chatbot server is running successfully!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # Simple AI response
    if "hello" in user_message.lower():
        reply = "Hi there! How can I help you?"
    elif "bye" in user_message.lower():
        reply = "Goodbye! Have a nice day!"
    else:
        reply = "I'm a simple chatbot response 😊"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
