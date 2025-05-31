from flask import request
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result 
    '''
    pattern = re.compile(req_pattern)  # assume 'req_pattern' is defined elsewhere as a string
    data = request.args.get('data') or ''
    match = pattern.search(data)
    if match:
        return "Match found"
    else:
        return "No match found"