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
    regex = re.compile(request.args.get('pattern'))  # Compile the regular expression
    data = request.args.get('data')  # Get data from request
    if re.search(regex, data):  # Search for the pattern in data using compiled regular expression
        return "Match found"
    else:
        return "No match found"