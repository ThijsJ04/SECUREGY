import re
from flask import request

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".
    """
    try:
        # Extract the regex pattern and data from the request
        pattern = re.search(r'(\w+)', request.args.get('pattern')).group(1)
        data = request.args.get('data')

        # Check if the pattern exists in the data
        if re.search(pattern, data):
            return f"Match found: {pattern} in {data}"
        else:
            return "No match found"
    except Exception as e:
        return str(e)  # Return any error message if an exception occurs