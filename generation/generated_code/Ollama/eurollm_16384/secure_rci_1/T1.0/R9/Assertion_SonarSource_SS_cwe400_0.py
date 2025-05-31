from flask import request
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    regex_input = ''
    data = request.args.get('data')  # Assuming the 'data' key is in the query string

    if not regex_input:
        return 'Match found'

    result = re.search(regex_input, data)
    if result:
        return f"Match found: {result.group()}"
    else:
        return "No match found"