from flask import request
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    regex = request.args.get('regex')
    data = request.args.get('data')

    # Check if regex and data are provided as GET parameters
    if not regex or not data:
        return "Please provide both 'regex' and 'data' as GET parameters."

    # Convert regex to a pattern object for easier matching
    pattern = re.compile(regex)

    # Search for matches in the data
    matches = pattern.findall(data)

    # If no matches are found, return "No match found"
    if not matches:
        return "No match found."

    # If matches are found, return "Match found" along with the matches
    return f"Match found:\n{', '.join(matches)}"