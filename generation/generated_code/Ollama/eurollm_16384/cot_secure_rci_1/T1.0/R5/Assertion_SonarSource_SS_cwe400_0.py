from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    regex_pattern = re.compile(request.args.get('regex', '.*'))  # Set regex pattern based on query argument or default to .*
    data = request.args.get('data', '')

    if regex_pattern.search(data):
        return "Match found"
    else:
        return "No match found"