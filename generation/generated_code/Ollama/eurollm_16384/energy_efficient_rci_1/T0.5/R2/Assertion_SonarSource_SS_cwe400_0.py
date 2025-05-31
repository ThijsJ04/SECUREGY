from flask import request
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    '''
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result 
    '''
    pattern = re.compile(request.args.get('pattern'))  # get the regex pattern from request args
    data = request.args.get('data')  # get the dataset from request args

    if bool(pattern.search(data)):
        return 'Match found'
    else:
        return 'No match found'