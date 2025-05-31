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
    # Extract regex and data from request arguments
    regex = request.args.get('regex')
    data = request.args.get('data')

    # Check if both parameters are provided
    if not regex or not data:
        return "Invalid request"

    # Escape the regex to prevent injection attacks
    safe_regex = re.escape(regex)

    # Perform the search
    if re.search(safe_regex, data):
        return "Match found"
    else:
        return "No match found"