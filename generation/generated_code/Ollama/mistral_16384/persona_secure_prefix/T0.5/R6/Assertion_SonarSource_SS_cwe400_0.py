import re
from flask import request, Flask

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    regex = re.compile(request.args.get('regex'))
    data = request.args.get('data')
    if regex.search(data):
        return "Match found"
    else:
        return "No match found"