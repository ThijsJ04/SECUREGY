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
    # Extract query parameters
    regex_pattern = request.args.get('regex', '')
    data_to_search = request.args.get('data', '')

    # Check if both parameters are provided
    if not regex_pattern or not data_to_search:
        return "Bad Request", 400

    # Perform the search
    if re.search(regex_pattern, data_to_search):
        return "Match found", 200
    else:
        return "No match found", 404