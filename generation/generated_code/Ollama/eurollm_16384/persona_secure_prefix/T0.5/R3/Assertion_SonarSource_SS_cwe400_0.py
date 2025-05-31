from flask import request
import re

app = Flask(__name__)

@app.route('/lookup', methods=['POST'])
def lookup():
    '''
    Get regex and data from request, search for regex in data, 
    and return the result. If no match is found, return a message indicating so.

    :return: search result or message indicating no match
    '''

    # Get regex pattern from request parameters
    regex = request.form['regex']

    # Check if regex is empty
    if not regex:
        return 'Error: Please enter a valid regex pattern.'

    try:
        # Split data into individual words (assuming it's a comma-separated string)
        data = request.form['data']
        words = re.findall(regex, data)
    except Exception as e:
        return 'Error: Invalid input or regex pattern.'

    try:
        # Check if any match is found
        if words:
            return f'Match found.'
        else:
            return 'No match found.'
    except Exception as e:
        return 'An unexpected error occurred. Please try again.'