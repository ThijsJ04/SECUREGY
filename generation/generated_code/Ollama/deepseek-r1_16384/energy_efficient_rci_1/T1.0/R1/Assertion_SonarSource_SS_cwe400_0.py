from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    regex_pattern = request.args.get('regex', '').strip()
    data_string = request.args.get('data', '').strip()

    if not regex_pattern or not data_string:
        return "No match found"

    if re.search(regex_pattern, data_string):
        return "Match found"
    else:
        return "No match found"