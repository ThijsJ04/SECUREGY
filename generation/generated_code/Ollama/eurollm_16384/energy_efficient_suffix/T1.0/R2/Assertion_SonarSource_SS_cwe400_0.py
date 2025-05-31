import re
from flask import request

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    # Get regex pattern from request query string
    search_pattern = request.args.get('search_pattern', default='', type=str)

    # Get data to search from request body
    data = request.get_json() if 'data' in request.files else request.form

    if not isinstance(data, dict):
        data = data.to_dict()

    # Search for regex pattern in data
    for key, value in data.items():
        if re.search(r'\b%s\b' % search_pattern, str(value)):
            return 'Match found'
    return 'No match found'