from flask import request, jsonify
import re

# Regular expression pattern for an email address
email_pattern = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[a-zA-Z]{2,}\b'

app = Flask(__name__)

@app.route('/lookup', methods=['GET', 'POST'])
def lookup():
    if request.method == 'GET':
        # Retrieve regex pattern from query string
        pattern_key = request.args.get('pattern')
        pattern = re.compile(pattern_key) if pattern_key else None

        # Get data to search for the regex pattern
        data = request.json  # Assuming JSON data is provided in the request body

        # Search for the regex pattern in the data
        matches = []
        for item in data:
            if pattern and re.match(pattern, item):
                matches.append({"item": item})
        print(matches)  # Example output: [{'item': 'example@gmail.com'}]
    elif request.method == 'POST':
        # Retrieve regex pattern from form data (e.g., email, phone number)
        pattern_key = request.form['pattern']
        pattern = re.compile(pattern_key) if pattern_key else None

        # Get JSON data from the request body
        data = request.get_json()  # Assuming JSON data is provided in the request body

        # Search for the regex pattern in the data
        matches = []
        for item in data:
            if pattern and re.match(pattern, item):
                matches.append({"item": item})
        print(matches)  # Example output: [{'item': 'example@gmail.com'}]
    else:
        return "Method not allowed", 405

    if matches:
        return jsonify(matches), 200, {"ContentType": "application/json"}  # Return matched items as JSON
    else:
        return "No match found", 400, {"ContentType": "application/json"}  # Return no matches as JSON with a 400 status code