#%% 
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- Simple predefined responses (intents) ---
intents = {
    "total sales": "The total sales for this month are $150,000.",
    "top product": "The top-selling product is the Red Wine Reserve.",
    "total customers": "You currently have 245 active customers.",
    "hello": "Hi there! I'm your BI assistant. How can I help?"
}

@app.route('/')
def home():
    return jsonify({"status": "API running", "message": "Welcome to dataGP_bot"})

@app.route('/answer', methods=['POST'])
def answer():
    data = request.get_json()
    question = data.get("question", "").lower().strip()

    # Find best match in predefined intents
    response = intents.get(question, "Sorry, I don't have an answer for that yet.")
    
    return jsonify({"answer": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)