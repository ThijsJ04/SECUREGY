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
    # Extract regex and data from query parameters
    pattern = request.args.get('regex', '')
    text = request.args.get('data', '')

    if not pattern or not text:
        return 'Bad Request', 400

    try:
        match = re.search(pattern, text)
        if match:
            return 'Match found'
        else:
            return 'No match found'
    except re.error:
        return 'Invalid regex', 500

if __name__ == '__main__':
    app.run(debug=True)