from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    regex = request.args.get("regex")  # Retrieve regex pattern from the request
    data = request.args.get("data")  # Retrieve data to search for the regex in

    if re.search(regex, data):
        return "Match found"
    else:
        return "No match found"