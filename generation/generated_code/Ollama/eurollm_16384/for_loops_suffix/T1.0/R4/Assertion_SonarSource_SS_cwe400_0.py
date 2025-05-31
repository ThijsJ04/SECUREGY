from flask import request
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    regex_data = request.args.get('regex')
    data_string = request.args.get('data')

    if regex_data is None or data_string is None:
        return 'Error: Missing required arguments.'

    match = re.search(regex_data, data_string)
    if match:
        return f'Match found'
    else:
        return 'No match found'