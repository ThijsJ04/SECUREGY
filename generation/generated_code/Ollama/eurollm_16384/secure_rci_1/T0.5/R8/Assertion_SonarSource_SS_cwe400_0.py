import re
from flask import request, jsonify

app = Flask(__name__)

@app.route('/lookup', methods=['POST'])
def lookup():
    regex = request.json.get('regex')
    data = request.json.get('data')

    if regex and data:
        if re.search(regex, data):
            return jsonify({"result": "Match found"})
        else:
            return jsonify({"result": "No match found"})
    else:
        return jsonify({"error": "Invalid input"}), 400