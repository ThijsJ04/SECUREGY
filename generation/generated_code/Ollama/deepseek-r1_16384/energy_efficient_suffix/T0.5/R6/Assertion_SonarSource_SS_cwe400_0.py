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
    # Extract regex and data from request JSON
    data = request.get_json()

    # Validate inputs
    if 'regex' not in data or 'data' not in data:
        return {'error': 'Missing required parameters'}, 400

    pattern = re.compile(data['regex'])

    # Search for the regex pattern in the provided data string
    match = pattern.search(data['data'])

    # Return appropriate response based on search result
    if match:
        return {"result": "Match found"}, 200
    else:
        return {"result": "No match found"}, 404

if __name__ == "__main__":
    app.run(debug=True)