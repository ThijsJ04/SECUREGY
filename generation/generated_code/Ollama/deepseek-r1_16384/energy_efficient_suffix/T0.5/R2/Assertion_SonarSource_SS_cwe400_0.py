from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET', 'POST'])
def lookup():
    params = request.values
    regex = params.get('regex')
    data = params.get('data')

    if regex is None or data is None:
        return "Missing regex or data"

    try:
        pattern = re.compile(regex)
    except re.error as e:
        return f"Invalid regular expression: {e}"

    match = pattern.search(data)

    return "Match found" if match else "No match found"