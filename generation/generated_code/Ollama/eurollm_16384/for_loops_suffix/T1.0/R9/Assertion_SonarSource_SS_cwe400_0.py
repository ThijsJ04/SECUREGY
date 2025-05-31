from flask import request
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    regex = request.args.get('regex')  # Get regex from query string
    data = request.args.get('data')    # Get data to search

    if not re.search(regex, data):
        return 'No match found'
    else:
        match_groups = re.findall(regex, data)
        print(f"Match found with groups {match_groups}")
        return f"Match found with groups {match_groups}"