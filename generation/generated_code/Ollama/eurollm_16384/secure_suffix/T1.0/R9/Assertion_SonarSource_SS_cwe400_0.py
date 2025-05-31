import re
from flask import request, abort

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    """
    Look up a string with regex in the data.

    Args: 
        - GET parameters: regex, data
        - URL path: /lookup

    Returns: 
        str - "Match found" or "No match found" if regex is not found in data
    """
    try:
        regex = request.args.get('regex')  # Get the regex pattern from URL query parameters
        data = request.args.get('data')  # Get the data string to search with regex
    except KeyError as e:  # If 'regex' or 'data' is not provided in URL
        return "Missing or invalid input: Please provide 'regex' and 'data' parameters", 400

    if not re.search(regex, data):  # Search for regex pattern in the data string
        return "No match found"
    else:
        return "Match found"