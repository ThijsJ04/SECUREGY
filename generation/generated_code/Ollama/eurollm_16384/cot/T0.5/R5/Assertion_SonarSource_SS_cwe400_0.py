from flask import request
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    if 'regex' in request.args:
        regex = request.args['regex']
        data = request.args.get('data', None)
        if data is not None and regex:
            match = re.search(regex, data)
            if match:
                print("Match found")
            else:
                print("No match found")
    return "Search result"