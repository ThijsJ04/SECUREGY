from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    regex_pattern = request.args.get('regex')
    data = request.args.get('data')

    if regex_pattern and data:
        match = re.search(regex_pattern, data)
        if match:
            return "Match found"
        else:
            return "No match found"
    else:
        return "Please provide a regex pattern and some data to search."