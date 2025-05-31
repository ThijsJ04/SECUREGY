from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result 
    '''
    # Extract regex pattern and data from request
    data = request.json.get('data', '')
    regex_pattern = request.json.get('regex', '')

    if not data or not regex_pattern:
        return {"error": "Missing 'data' or 'regex' in request"}, 400

    try:
        # Compile the regex pattern
        pattern = re.compile(regex_pattern)

        # Search for the pattern in data
        match = pattern.search(data)

        if match:
            return {"result": "Match found"}
        else:
            return {"result": "No match found"}

    except re.error:
        return {"error": "Invalid regex pattern"}, 400