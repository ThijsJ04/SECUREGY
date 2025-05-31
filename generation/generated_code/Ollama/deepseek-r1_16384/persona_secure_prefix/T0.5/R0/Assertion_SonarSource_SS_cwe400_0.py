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
    pattern = request.args.get('pattern', '')
    data = request.args.get('data', '')

    # Validate input parameters
    if not pattern:
        return {"error": "Pattern parameter is required"}, 400

    try:
        re.compile(pattern)
    except re.error as e:
        return {"error": f"Invalid regex pattern: {str(e)}"}, 400

    if re.search(pattern, data):
        return {"result": "Match found"}
    else:
        return {"result": "No match found"}