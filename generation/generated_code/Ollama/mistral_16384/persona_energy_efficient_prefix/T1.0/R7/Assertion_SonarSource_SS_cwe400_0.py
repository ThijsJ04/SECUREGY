import re
from flask import request, Flask

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    regex_pattern = re.compile(request.args.get('regex'))
    data = request.args.get('data')
    if re.search(regex_pattern, data):
        return "Match found"
    else:
        return "No match found"