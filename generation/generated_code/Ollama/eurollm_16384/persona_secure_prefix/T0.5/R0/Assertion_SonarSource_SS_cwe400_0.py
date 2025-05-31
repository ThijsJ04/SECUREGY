import re
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    '''
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result 
    '''
    try:
        # Get regex from request parameters
        pattern = re.compile(request.args.get('pattern'))

        # Get data from request body (JSON) or query string (key=value pairs)
        data = {} if 'data' not in request.args else {k: v for k, v in request.args['data'].items()}

        # Search for regex in data
        for key, value in data.items():
            if pattern.search(value):
                return f"Match found in '{key}' with value: {value}"
    except Exception as e:
        return str(e)