from flask import request
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    regex = request.args.get('regex')
    data = request.args.get('data')

    if regex and data:
        match = re.search(regex, data)
        if match:
            return "Match found"
        else:
            return "No match found"
    else:
        return "Please provide a regex pattern and some text to search."