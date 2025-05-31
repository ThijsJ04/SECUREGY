from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    regex = request.args.get('regex', '')
    data = request.args.get('data', '')
    match = re.search(regex, data)
    return "Match found" if match else "No match found"

# (The code above implements the required functionality by extracting 'regex' and 'data' from query parameters and using Python's `re` module to perform the search. If a match is found, it returns "Match found"; otherwise, it returns "No match found".)