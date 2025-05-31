from flask import request
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    '''
    Get regex and data from request, search for regex in data, 
    and return the result as "Match found" or "No match found".
    '''
    regex = request.args.get('regex')  # Get regex from URL query parameters
    data = request.args.get('data')  # Get data from URL query parameters

    if regex and re.search(regex, data):
        return f"Match found in '{data}' using the regex: {regex}"
    else:
        return "No match found"