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

    regex = request.args.get('regex')  # Get the regex from the request
    data = request.args.get('data')    # Get the data from the request

    if re.search(regex, data):         # Check if there's a match using re.search
        return "Match found"
    else:                              # If not, return "No match found"
        return "No match found"