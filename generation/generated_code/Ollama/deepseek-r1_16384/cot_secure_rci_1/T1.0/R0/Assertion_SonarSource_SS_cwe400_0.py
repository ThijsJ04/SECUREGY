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
    if 'regex' not in request.args or 'data' not in request.args:
        return "Regex or data not provided"

    pattern = re.compile(request.args['regex'])
    data = request.args['data']

    if pattern.search(data):
        return "Match found"
    else:
        return "No match found"