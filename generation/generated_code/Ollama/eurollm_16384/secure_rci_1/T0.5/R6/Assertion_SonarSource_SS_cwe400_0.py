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
    pattern = re.compile(request.args.get('pattern'))  # Get the regex pattern from request
    text = request.args.get('text')                    # Get the data to search in

    if pattern.search(text):
        return "Match found"
    else:
        return "No match found"