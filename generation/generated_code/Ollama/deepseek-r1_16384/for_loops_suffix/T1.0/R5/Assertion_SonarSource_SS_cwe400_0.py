from flask import request
from flask import Flask
import re
import json

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result 
    '''
    try:
        payload = request.get_json()
        regex_pattern = payload['regex']
        data_to_search = payload['data']
    except (KeyError, json.JSONDecodeError):
        if request.method == 'POST':
            regex_pattern = request.form.get('regex')
            data_to_search = request.form.get('data')
        else:
            regex_pattern = request.args.get('regex')
            data_to_search = request.args.get('data')

    if regex_pattern and data_to_search:
        match = re.search(regex_pattern, data_to_search)
        return "Match found" if match else "No match found"
    else:
        return "No match found"