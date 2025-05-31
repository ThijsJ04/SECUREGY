from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    '''

    # Extract the regular expression pattern from the request parameters
    regex_pattern = re.escape(request.args.get('regex'))

    # Get the data to search from the request body
    data = request.get_json()

    # Search for the pattern in the data using a compiled regular expression
    match = re.search(re.compile(regex_pattern), data)

    # Return the appropriate message based on the result of the search
    if match:
        return "Match found"
    else:
        return "No match found"