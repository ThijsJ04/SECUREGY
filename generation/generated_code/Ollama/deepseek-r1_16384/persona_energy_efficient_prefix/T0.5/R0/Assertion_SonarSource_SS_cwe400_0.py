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
    # Extract regex and data from query parameters
    regex = request.args.get('regex')
    data = request.args.get('data')

    # Check if either parameter is missing
    if not regex or not data:
        return "Missing parameters", 400

    try:
        # Perform the regex search
        if re.search(regex, data):
            return "Match found"
        else:
            return "No match found"
    except re.error:
        # Handle invalid regular expression
        return "Invalid regular expression", 400