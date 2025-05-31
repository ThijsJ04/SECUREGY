from flask import request
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    regex_pattern = request.args.get('regex')  # Get the regex pattern from the query string
    data = request.args.get('data')  # Get the data to search in

    if regex_pattern and data:
        match = re.search(regex_pattern, data)
        if match:
            return f"Match found at position {match.start()} with length {len(match.group())}"
        else:
            return "No match found"
    else:
        return "Invalid input. Please provide a regex pattern and some data to search in."