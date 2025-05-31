from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    regex_pattern = request.args.get('regex', type=str)
    data_to_search = request.args.get('data', type=str)

    if not regex_pattern or not data_to_search:
        return "Either regex or data is missing"

    if re.search(regex_pattern, data_to_search):
        return "Match found"
    else:
        return "No match found"

# Example usage with curl:
# $ curl "http://localhost:5000/lookup?regex=hello&data=Hello%20world"