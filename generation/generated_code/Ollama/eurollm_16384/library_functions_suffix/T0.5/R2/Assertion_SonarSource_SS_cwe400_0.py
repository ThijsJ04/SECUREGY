import re
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    regex_input = request.args.get('regex')
    data_input = request.args.get('data')

    match = re.search(regex_input, data_input)

    if match:
        return f"Match found"
    else:
        return "No match found"