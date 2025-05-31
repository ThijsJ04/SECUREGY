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
    regex = re.compile(request.args.get('regex'))  # Compile the given regular expression
    data = request.args.get('data')  # Get the data to search in
    match = regex.search(data)  # Search for a match
    return "Match found" if match else "No match found"