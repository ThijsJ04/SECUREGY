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
    # Extract regex pattern and data from form inputs
    regex_pattern = request.form.get('regex')
    data_string = request.form.get('data')

    # Search for the regex in the data string
    if re.search(regex_pattern, data_string):
        return "Match found"
    else:
        return "No match found"