from flask import request
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    regex = request.args.get('regex')  # get regex from query string
    data = request.args.get('data')  # get data to search in

    if not regex or not data:  # check if both are provided
        return 'No match found', 400  # return error if missing values

    match = re.search(regex, data)  # search for regex in data using re module
    if match:  # if match is found
        return f'Match found at position {match.start()}'
    else:
        return 'No match found', 400  # return error if no match is found