from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET', 'POST'])
def lookup():
    '''
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result 
    '''
    try:
        # Try to get regex and data from JSON if available
        regex = request.json['regex']
        data = request.json['data']
    except KeyError:
        # Fall back to query parameters or form data
        regex = request.values.get('regex', '', type=str)
        data = request.values.get('data', '', type=str)

    # Compile the regex pattern
    try:
        pattern = re.compile(regex)
    except re.error:
        return "Invalid regex pattern"

    # Search for the pattern in data
    if pattern.search(data):
        return "Match found"
    else:
        return "No match found"