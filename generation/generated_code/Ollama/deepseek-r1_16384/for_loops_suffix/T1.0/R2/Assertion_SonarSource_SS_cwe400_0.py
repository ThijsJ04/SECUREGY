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
    # Get regex pattern and data string from request arguments
    regex_pattern = request.args.get('regex')
    data_string = request.args.get('data')

    # Check if both regex and data are provided
    if not regex_pattern or not data_string:
        return {"result": "Missing parameters"}, 400

    # Search for the pattern in the data string using re.search()
    match = re.search(regex_pattern, data_string)

    # Return appropriate response based on search result
    if match:
        return {"result": "Match found"}
    else:
        return {"result": "No match found"}