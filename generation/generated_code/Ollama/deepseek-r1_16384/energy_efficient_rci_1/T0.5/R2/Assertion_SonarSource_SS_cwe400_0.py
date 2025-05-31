from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result 
    '''
    regex_pattern = request.args.get('regex')
    data_string = request.args.get('data')

    if not regex_pattern or not data_string:
        return "Invalid request parameters"

    pattern = re.compile(regex_pattern)
    match = pattern.search(data_string)

    return "Match found" if match else "No match found"

if __name__ == '__main__':
    app.run(debug=True)