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

    try:
        # Extract the regex pattern and data from the request
        regex = request.args.get('regex')
        data = request.args.get('data')

        # Check if either regex or data is missing from the request
        if not (regex or data):
            return 'Either regex or data must be provided', 400
    except:  # General exception for cases where the regex and/or data are missing or invalid
        return 'Invalid request parameters. Please provide a valid regex pattern and data', 400

    # Use re.match to check if the regex pattern exists within the data
    try:
        if not bool(re.match(regex, data)):
            return 'No match found'
        else:
            return 'Match found'
    except:  # General exception for cases where the regex and/or data are invalid or there's an error during matching
        return 'Invalid input. Please check your regex pattern and data', 400