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
    regex_pattern = request.args.get('regex', '')
    data_to_search = request.args.get('data', '')

    # Perform regex search in an energy-efficient manner using the re module
    if re.search(regex_pattern, data_to_search):
        return "Match found"
    else:
        return "No match found"