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
    # Extract regex and data from the form request
    regex = request.form.get('regex')
    data = request.form.get('data')

    if not regex or not data:
        return "No data provided"

    try:
        pattern = re.compile(regex)
        match = pattern.search(data)
        if match:
            return "Match found"
        else:
            return "No match found"
    except re.error:
        return "Invalid regular expression"