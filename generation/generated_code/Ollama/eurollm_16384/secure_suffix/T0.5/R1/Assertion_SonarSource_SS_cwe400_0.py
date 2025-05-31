from flask import request
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    regex_input = request.args.get('regex')
    data_input = request.args.get('data')

    # Regular expression pattern to match the given input
    if re.search(regex_input, data_input):
        return f"Match found: '{regex_input}' matched in '{data_input}'."
    else:
        return "No match found."