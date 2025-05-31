from flask import request
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    regex_pattern = request.args.get('regex')
    data = request.args.get('data')
    if regex_pattern:
        if re.search(regex_pattern, data):
            return f"Match found in '{data}' with regex pattern '{regex_pattern}'.", 200
        else:
            return "No match found in '{}' with regex pattern '{}'.".format(data, regex_pattern), 404
    else:
        return "Missing required parameters. Please provide a regex and data.", 400