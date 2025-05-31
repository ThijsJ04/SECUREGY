from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    regex = request.args.get('regex')
    data = request.args.get('data')
    if re.search(regex, data):
        return "Match found"
    else:
        return "No match found"

# (The code is complete and ready to be used.)