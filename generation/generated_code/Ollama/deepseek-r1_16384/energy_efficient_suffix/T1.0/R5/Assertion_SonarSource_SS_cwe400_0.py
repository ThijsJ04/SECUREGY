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
    # Extract regex pattern and data from query parameters
    regex_pattern = request.args.get('regex')
    data = request.args.get('data', '')

    # Check if both parameters are provided
    if not regex_pattern or not data:
        return "Both regex and data are required."

    try:
        # Search for the regex pattern in each line of data
        for line in data.split('\n'):
            if re.search(regex_pattern, line):
                return "Match found"
        return "No match found"
    except re.error:
        return "Invalid regular expression."