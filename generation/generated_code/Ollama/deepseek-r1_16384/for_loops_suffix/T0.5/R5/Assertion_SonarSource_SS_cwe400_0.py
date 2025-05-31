from flask import request
from flask import Flask
import re
import json

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result 
    '''
    # Extract regex pattern from query parameters
    regex = request.args.get('regex')

    # Determine the content type to extract data
    if request.headers.get('Content-Type') == 'application/json':
        data = json.loads(request.data)
    else:
        data = request.args.get('data', '')

    # Perform regex search
    if re.search(regex, str(data)):
        return "Match found"
    else:
        return "No match found"