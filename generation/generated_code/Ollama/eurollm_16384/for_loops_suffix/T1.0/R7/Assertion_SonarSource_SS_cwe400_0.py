from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    '''
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result 
    '''
    pattern = re.compile(request.args.get('pattern'))  # Get the regex from the query string
    match_data = request.args.get('data')                # Get the data to search for a match in
    result = ''

    if pattern.search(match_data) != None:               # If a match is found...
        result = 'Match found'  
    else:
        result = 'No match found'  # ...otherwise, return "No match found"

    return result