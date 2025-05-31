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
    pattern = request.args.get('pattern')  # get the regex pattern from query string
    data = request.args.get('data')  # get the data to search in

    if re.search(pattern, data):
        return f"Match found: '{data}' contains the pattern {pattern}."
    else:
        return "No match found."