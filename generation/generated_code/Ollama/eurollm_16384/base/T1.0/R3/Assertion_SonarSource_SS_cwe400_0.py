import re
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result 
    '''
    pattern = request.args.get('pattern')  # Get the regex pattern from the query string
    data = request.args.get('data')       # Get the data to search for the pattern

    match_found = re.search(pattern, data) 
                                              # Search for the pattern in the data using regular expressions

    if match_found:
        return f'Match found'   # If a match is found, return "Match found"
    else:
        return 'No match found'  # If no match is found, return "No match found"