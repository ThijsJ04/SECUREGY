from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    if request.is_json:
        regex_pattern = request.json.get('regex')
        data_to_search = request.json.get('data')
    else:
        regex_pattern = request.values.get('regex')
        data_to_search = request.values.get('data')

    if not regex_pattern or not data_to_search:
        return "Parameters missing"

    if re.search(regex_pattern, data_to_search):
        return "Match found"
    else:
        return "No match found"