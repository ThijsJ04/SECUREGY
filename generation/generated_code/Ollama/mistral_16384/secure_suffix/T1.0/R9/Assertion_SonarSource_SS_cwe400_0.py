from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    regex = request.args.get('regex', '')  # get regex from query params
    data = request.args.get('data', '')   # get data from query params

    if re.search(regex, data):
        return "Match found"
    else:
        return "No match found"