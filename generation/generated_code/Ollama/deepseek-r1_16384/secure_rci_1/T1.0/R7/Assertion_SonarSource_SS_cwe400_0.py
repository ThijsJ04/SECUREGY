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
    # Get JSON data from request
    data = request.get_json()

    # Extract regex and text to search
    regex = data.get('regex')
    text_to_search = data.get('data')

    if not regex or not text_to_search:
        return jsonify({'error': 'Regex or data is missing'}), 400

    # Search for regex in text
    match = re.search(regex, text_to_search)

    if match:
        return jsonify({'result': 'Match found'}), 200
    else:
        return jsonify({'result': 'No match found'}), 200

if __name__ == "__main__":
    app.run(debug=True)