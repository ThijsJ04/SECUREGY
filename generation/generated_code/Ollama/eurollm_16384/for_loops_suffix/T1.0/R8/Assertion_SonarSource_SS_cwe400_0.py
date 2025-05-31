import re
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    # Get regex and data from request
    regex = request.args.get('regex')
    data = request.get_json() if 'data' in request.args else request.args.get('data')

    # Search for regex in data
    if regex:
        match = re.search(regex, data)
        print("Match found")
        return "Match found"
    else:
        return "No match found"