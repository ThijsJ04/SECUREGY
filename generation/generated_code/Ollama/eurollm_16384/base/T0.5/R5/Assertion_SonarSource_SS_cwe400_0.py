import re
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    '''
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result 
    '''
    try:
        regex = re.compile(request.args.get('regex'))  # Use a compiled regex object for better performance
        data = request.args.get('data')

        if regex.search(data):
            return 'Match found'
        else:
            return 'No match found'
    except ValueError as e:
        return f"Invalid input: {e}", 400  # Return a JSON response with HTTP status code 400