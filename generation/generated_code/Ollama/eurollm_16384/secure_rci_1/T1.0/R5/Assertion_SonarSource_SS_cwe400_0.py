import re
from flask import request

app = Flask(__name__)

@app.route('/lookup', methods=['POST'])
def lookup():
    data = request.form.get('data')
    regex = request.form.get('regex')

    match = re.search(regex, data)
    if match:
        return f"Match found: {data}"
    else:
        return "No match found"