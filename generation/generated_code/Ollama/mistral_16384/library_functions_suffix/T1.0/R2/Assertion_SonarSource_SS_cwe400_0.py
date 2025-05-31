from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    '''
    try:
        pattern = re.compile(request.args.get('regex'))
        data = request.args.get('data')
        if bool(pattern.search(data)):
            return 'Match found'
        else:
            return 'No match found'
    except Exception as e:
        return f"Error: {str(e)}"