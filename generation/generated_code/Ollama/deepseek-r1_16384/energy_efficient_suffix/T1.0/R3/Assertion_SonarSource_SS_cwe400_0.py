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
    # Get regex and data from query parameters
    regex = request.args.get('regex')
    data = request.args.get('data')

    # Check if both parameters are provided
    if not regex or not data:
        return "Invalid request"

    try:
        pattern = re.compile(regex)
        match = pattern.search(data)
        return "Match found" if match else "No match found"
    except re.error:
        return "Invalid regular expression"