from flask import request
import re

app = Flask(__name__)

@app.route('/lookup', methods=['POST'])
def lookup():
    regex_input = request.json['regex'] if 'regex' in request.json else None
    data_input = request.json['data'] if 'data' in request.json else None

    if regex_input and data_input:
        result = re.search(regex_input, str(data_input))
        print(result)  # Uncomment this line to see the match result in console
        return {
            'found': 'Match found', if result else 'No match found',
        }
    else:
        raise ValueError("Both regex and data are required")