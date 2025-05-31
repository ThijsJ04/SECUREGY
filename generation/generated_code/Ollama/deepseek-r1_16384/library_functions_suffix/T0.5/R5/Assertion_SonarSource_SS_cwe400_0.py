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
    # Get regex pattern and data from request parameters
    regex = request.args.get('regex', '')
    data = request.args.get('data', '')

    # Check if either regex or data is missing
    if not regex or not data:
        return "Missing required parameters"

    try:
        # Compile the regular expression pattern
        pattern = re.compile(regex)

        # Search for the pattern in data
        match = pattern.search(data)

        # Return result based on whether a match was found
        return "Match found" if match else "No match found"
    except re.error:
        return "Invalid regular expression"

if __name__ == '__main__':
    app.run(debug=True)