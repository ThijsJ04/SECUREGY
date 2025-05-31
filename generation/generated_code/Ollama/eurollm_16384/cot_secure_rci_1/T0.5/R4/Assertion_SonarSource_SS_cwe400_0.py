from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    regex = re.search(r'\d+', request.args).group()  # Extract regex pattern from request data (in this case, it's a simple number)
    data = request.args.get('data')  # Extract the data to be searched for the regex pattern
    if re.search(regex, data):
        return "Match found"
    else:
        return "No match found"