from flask import request
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET', 'POST'])
def lookup():
    if request.method == 'GET':
        # Extract regex from URL query parameters
        pattern = request.args.get('pattern')
        data = request.args.get('data')
    elif request.method == 'POST':
        # Extract regex and data from request body
        data = request.form['data']  # or request.json if using JSON data
        pattern = request.form.get('pattern')
    else:
        return "Invalid HTTP method"

    if re.search(pattern, data):
        return "Match found"
    else:
        return "No match found"