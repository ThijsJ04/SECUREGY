from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    regex_str = request.args.get('regex')  # Get the regex from the URL query string
    data = request.args.get('data')       # Get the data from the URL query string

    if not regex_str or not data:         # Check if both regex and data are provided
        return 'No match found'

    match = re.search(regex_str, data)  # Search for the regex in the data using regular expressions
    if match:                            # Return "Match found" if a match is found, otherwise return "No match found"
        return 'Match found'
    else:
        return 'No match found'