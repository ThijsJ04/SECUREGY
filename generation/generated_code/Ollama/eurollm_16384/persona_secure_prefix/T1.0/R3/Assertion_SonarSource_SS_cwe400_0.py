import re
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    search_regex = request.args.get('search')  # get regex from query string
    matching_data = request.args.get('data')   # get data to search in

    if re.search(search_regex, matching_data):
        return f"Match found"
    else:
        return f"No match found"