from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Chatbot server is live and running!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json(force=True)
    user_message = data.get("message", "")

    # simple logic
    if "hello" in user_message.lower():
        reply = "Hi! How can I assist you today?"
    elif "bye" in user_message.lower():
        reply = "Goodbye 👋"
    else:
        reply = "I'm a simple chatbot running on Flask!"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
