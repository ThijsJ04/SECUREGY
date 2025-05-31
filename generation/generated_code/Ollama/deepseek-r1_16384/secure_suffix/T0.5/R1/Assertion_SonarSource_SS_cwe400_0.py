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
    # Extract regex pattern and data from request form
    regex_pattern = request.form.get('regex')
    data_to_search = request.form.get('data', '')

    if not regex_pattern or not data_to_search:
        return "Missing parameters"

    try:
        pattern = re.compile(regex_pattern)
        if re.search(pattern, data_to_search):
            return "Match found"
        else:
            return "No match found"
    except re.error:
        return "Invalid regular expression"