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

    # Compile the regex pattern with DOTALL and MULTILINE flags
    pattern = re.compile(regex, flags=re.DOTALL | re.MULTILINE)

    # Search for the pattern in the data
    if pattern.search(data):
        return "Match found"
    else:
        return "No match found"