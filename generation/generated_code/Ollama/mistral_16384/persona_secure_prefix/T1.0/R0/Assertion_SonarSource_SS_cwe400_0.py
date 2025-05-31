import re
from flask import request, Flask

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    regex = re.compile(request.args.get('regex'))  # create a compiled regular expression object from the provided regex
    data = request.args.get('data')                # get the provided data as string
    match = regex.search(data)                     # search for the regex pattern in the data

    if match:
        return "Match found"
    else:
        return "No match found"