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
    if request.method != 'GET':
        return 'Method not allowed', 405

    regex = request.args.get('regex')
    data = request.args.get('data')

    if not regex or not data:
        return 'Bad request', 400

    try:
        pattern = re.compile(regex)
        match = pattern.search(data)
        if match:
            return "Match found"
        else:
            return "No match found"
    except re.error:
        return 'Invalid regular expression', 400