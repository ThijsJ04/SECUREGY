import re
from flask import request, jsonify
app = Flask(__name__)

# Function to look up a regex pattern in the input data
def lookup(pattern, text):
    if not re.search(pattern, text):
        return "No match found"
    else:
        return "Match found"

@app.route('/lookup', methods=['POST'])
def lookup_data():
    data = request.get_json()  # assuming JSON data is being sent in the request body
    regex = re.compile(data["regex"], re.IGNORECASE)  # compile regex pattern as a regular expression object
    result = lookup(regex, data["text"])  # pass the regex and text to be searched for match
    return jsonify({"message": result})