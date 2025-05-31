import re
from flask import request

app = Flask(__name__)

@app.route('/lookup', methods=['POST'])
def lookup():
    '''
    Get regex and data from POST request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result 
    '''
    post_data = request.get_json()  # assuming the request is JSON-encoded

    regex = re.compile(post_data['regex'])
    for item in post_data['items']:
        if regex.search(str(item)):
            return "Match found"
    return "No match found"