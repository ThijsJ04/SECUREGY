from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup', methods=['POST'])
def lookup():
    try:
        if not request.is_json:
            return "Invalid request format. JSON required.", 400

        data = request.json
        regex = data.get('regex')
        search_data = data.get('data')

        if not regex or not search_data:
            return "Missing parameters in request", 400

        pattern = re.compile(regex)

        if re.search(pattern, search_data):
            return "Match found", 200
        else:
            return "No match found", 200

    except re.error:
        return "Invalid regular expression", 400
    except Exception as e:
        return f"Internal server error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)