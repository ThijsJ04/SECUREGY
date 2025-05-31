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
    # Extract regex pattern and data string from the request
    if request.is_json:
        regex_pattern = request.json.get('regex', '')
        data_str = request.json.get('data', '')
    else:
        regex_pattern = request.args.get('regex', '')
        data_str = request.args.get('data', '')

    # Perform regex search
    try:
        pattern = re.compile(regex_pattern)
        match = pattern.search(data_str)
        return "Match found" if match else "No match found"
    except re.error:
        # Handle invalid regular expression
        return "Invalid regular expression", 400