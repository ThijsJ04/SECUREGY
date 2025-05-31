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
    regex = request.args.get('regex', '.*')  # default to matching anything if not provided

    # Use re.escape() to safely handle special regex characters in the input
    pattern = re.compile(re.escape(regex))

    # Get data from query parameter (you might want to use form or json parsing here)
    data = request.args.get('data', '')

    # Perform search operation
    if pattern.search(data):
        return "Match found"
    else:
        return "No match found"