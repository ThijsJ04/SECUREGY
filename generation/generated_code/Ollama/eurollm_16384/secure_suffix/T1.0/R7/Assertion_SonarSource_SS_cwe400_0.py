from flask import request
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    """
    Search for a regex pattern within the request data and return the result.
    """
    search_regex = re.compile(request.args.get('search_regex'))  # get the regex from the query string
    match = search_regex.search(request.data) if 'data' in request else None  # search for the regex in data and return match or None

    if match:
        return f"Match found!"
    else:
        return "No match found."