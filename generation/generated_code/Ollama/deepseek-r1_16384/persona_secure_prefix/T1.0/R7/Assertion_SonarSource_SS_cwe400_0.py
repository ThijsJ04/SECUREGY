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
    # Get regex pattern from query parameters or form data
    regex = request.args.get('regex') or request.form.get('regex')
    # Get data string from query parameters or form data
    data = request.args.get('data') or request.form.get('data')

    try:
        # Compile the regex pattern
        pattern = re.compile(regex)
        # Search for the pattern in the data
        if pattern.search(data):
            return "Match found"
        else:
            return "No match found"
    except Exception as e:
        # Handle any regex compilation errors or other exceptions
        return f"Error processing request: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)