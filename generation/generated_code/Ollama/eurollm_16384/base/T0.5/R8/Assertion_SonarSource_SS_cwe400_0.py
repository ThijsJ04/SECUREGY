from flask import request
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    '''
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result 
    '''
    regex = request.args.get('regex')  # Get the regex pattern from query string or POST data
    data = request.args.get('data', default=None)  # Get the data to search for the regex

    if regex and data:
        match_found = re.search(regex, data) is not None
        return f"Match found {' ' if match_found else ''}no match found"
    else:
        return "Invalid input. Please provide a regex pattern and data to search."