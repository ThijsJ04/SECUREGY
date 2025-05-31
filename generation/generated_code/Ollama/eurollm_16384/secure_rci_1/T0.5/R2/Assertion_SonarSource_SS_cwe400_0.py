from flask import request
import re

app = Flask(__name__)

@app.route('/lookup', methods=['POST'])
def lookup():
    regex_data = request.json.get('regex')
    data = request.json.get('data')

    if not regex_data or not data:
        return 'No input provided.'

    match = re.search(regex_data, data)
    if match:
        return f'Match found in "{data}" at position {match.start()}'
    else:
        return 'No match found.'