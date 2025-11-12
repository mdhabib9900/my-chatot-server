from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Chatbot is running!"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "")
    # simple AI response
    if "hello" in user_message.lower():
        reply = "Hi! How can I help you today?"
    else:
        reply = "I'm a lightweight chatbot!"
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
