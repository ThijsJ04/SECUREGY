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
    regex_pattern = request.args.get('regex')
    search_data = request.args.get('data')

    if not regex_pattern or not search_data:
        return "No match found"

    try:
        pattern = re.compile(re.escape(regex_pattern))
        return "Match found" if pattern.search(search_data) else "No match found"
    except re.error:
        return "No match found"