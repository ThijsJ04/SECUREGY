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
    # Get regex pattern and data from query parameters
    regex_pattern = request.args.get('regex', '')
    data_to_search = request.args.get('data', '')

    try:
        # Compile the regular expression pattern
        pattern = re.compile(regex_pattern)

        # Search for the pattern in the data
        if pattern.search(data_to_search):
            return "Match found"
        else:
            return "No match found"
    except re.error:
        # Handle invalid regular expression patterns
        return "Invalid regular expression"
    except Exception as e:
        # Handle other unexpected errors
        return f"Internal server error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)