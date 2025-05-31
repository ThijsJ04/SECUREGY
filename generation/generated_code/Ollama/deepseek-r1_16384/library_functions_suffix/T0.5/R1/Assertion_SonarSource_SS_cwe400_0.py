from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    regex_pattern = request.args.get('regex', '')
    data_to_search = request.args.get('data', '')
    match = re.search(regex_pattern, data_to_search)
    return "Match found" if match else "No match found"

if __name__ == "__main__":
    app.run(debug=True)