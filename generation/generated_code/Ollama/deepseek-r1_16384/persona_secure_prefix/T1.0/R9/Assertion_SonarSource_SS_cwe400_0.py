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
    # Extract regex and data from the request form
    regex = request.form.get('regex', '')
    data = request.form.get('data', '')

    # Check if both parameters are provided
    if not regex or not data:
        return "Missing parameters"

    try:
        # Perform regex search
        if re.search(regex, data):
            return "Match found"
        else:
            return "No match found"
    except re.error:
        # Handle invalid regex pattern
        return "Invalid regex"