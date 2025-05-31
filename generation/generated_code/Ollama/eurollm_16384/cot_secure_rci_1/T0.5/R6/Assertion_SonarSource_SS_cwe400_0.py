from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    regex = request.args.get('regex')  # Get the regex pattern from query parameters
    data = request.json if 'data' in request.args else request.args.get('data')  # Get the data to search (JSON or string)

    if not regex:
        return "Please provide a valid regex pattern", 400

    match = re.search(regex, data)
    if match:
        return f"Match found in '{data}' at position {match.start()}"
    else:
        return "No match found"