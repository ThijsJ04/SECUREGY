from flask import request, jsonify
import re

app = Flask(__name__)

@app.route('/lookup', methods=['POST'])
def lookup():
    '''
    Get regex and data from request body, search for regex in data, 
    and return the result as JSON.

    If no match is found, return a 404 status code with a JSON object indicating "No match found".

    :return: JSON response with search result or error message
    '''

    try:
        # Get regex and data from request body
        data = request.json['data']
        regex = re.compile(request.json['regex'])

        # Check if regex matches any item in the data
        for item in data:
            if regex.search(item):
                return jsonify({'result': 'Match found'})
    except Exception as e:
        return jsonify({'error': str(e)})
    else:
        return jsonify({'result': 'No match found'})