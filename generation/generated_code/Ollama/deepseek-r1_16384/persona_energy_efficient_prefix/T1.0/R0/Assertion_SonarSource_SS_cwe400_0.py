from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup', methods=['POST'])
def lookup():
    regex = request.json.get('regex')
    data = request.json.get('data')

    if regex and data:
        if re.search(regex, data):
            return "Match found"
        else:
            return "No match found"
    return "Invalid input"

if __name__ == '__main__':
    app.run(debug=True)