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
    try:
        if request.is_json:
            regex = request.json['regex']
            string_to_search = request.json.get('string', '')
        else:
            # Try form data
            if 'regex' in request.form:
                regex = request.form['regex']
            else:
                # Try query parameters
                regex = request.args.get('regex')
                string_to_search = request.args.get('string', '')

        if not regex or not string_to_search:
            return "Missing required parameters", 400

        match = re.search(regex, string_to_search)
    except KeyError:
        return "Invalid request format", 400
    except re.error as e:
        return f"Invalid regular expression: {str(e)}", 400

    if match:
        return "Match found"
    else:
        return "No match found"