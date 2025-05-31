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
    if request.is_json:
        req_data = request.get_json()
        regex = req_data.get('regex', '')
        data_text = req_data.get('data', '')
    else:
        regex = request.values.get('regex', '')
        data_text = request.values.get('data', '')

    if not regex or not data_text:
        return "No match found"

    try:
        pattern = re.compile(regex)
    except re.error:
        return "No match found"

    if pattern.search(data_text):
        return "Match found"
    else:
        return "No match found"