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
    regex = request.args.get('regex', '').strip()
    data = request.args.get('data', '').strip()

    if not regex or not data:
        return "No match found"

    try:
        pattern = re.compile(re.escape(regex))
        if pattern.search(data):
            return "Match found"
        else:
            return "No match found"
    except re.error:
        return "Invalid regular expression"