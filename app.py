#%% 
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/answer', methods=['POST'])
def answer():
    data = request.get_json()
    question = data.get('question', '')
    if 'sales' in question.lower():
        return jsonify({"answer": "DAX: SUM(Sales[Total])"})
    return jsonify({"answer": "Sorry, I don’t understand."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)