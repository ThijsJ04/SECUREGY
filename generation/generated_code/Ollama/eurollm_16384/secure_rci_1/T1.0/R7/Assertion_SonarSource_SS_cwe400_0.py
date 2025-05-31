from flask import request
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    regex = request.args.get('regex') or '^.*$'  # Default to any string for now
    data = request.args.get('data', default='')

    if not regex:
        return "Match found"

    match = re.search(regex, data)
    if match:
        return "Match found"
    else:
        return "No match found"