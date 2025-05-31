from flask import request
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    '''
    Get regex and data from request, search for regex in data, and return result.
    '''
    pattern = re.compile(re.escape(request.args.get('pattern')))
    match = None

    if 'data' in request.args:
        data = request.args['data']
        match = pattern.search(data)
    elif 'text' in request.args:
        text = request.args['text']
        match = pattern.search(text)

    return {'found': bool(match)}