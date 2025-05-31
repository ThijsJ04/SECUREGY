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

    # Extract the regular expression from the request
    regex_str = request.args.get('regex')

    # If no regex is provided, return an error message
    if not regex_str:
        return "Error: No regex provided."

    # Extract the data from the request
    data_str = request.args.get('data')

    # If no data is provided, return an error message
    if not data_str:
        return "Error: No data provided."

    # Compile the regular expression
    regex = re.compile(regex_str)

    # Search for the regular expression in the data
    match = regex.search(data_str)

    if match:
        return "Match found"
    else:
        return "No match found"