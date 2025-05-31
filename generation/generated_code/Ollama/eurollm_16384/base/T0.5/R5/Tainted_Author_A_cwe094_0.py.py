from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def contents_dict():
    file_contents = request.args.get('file_contents')  # Get the data from the request using 'file_contents'.
    content = file_contents[1:-1]  # Remove anything before the first '{' and after the last '}'.
    try:
        data = json.loads(content)  # Evaluate it to a dictionary.
        return json.dumps(data, indent=4)  # Return the content by evaluating it to a dictionary.
    except ValueError as e:
        return str(e), 500  # If the content is not valid JSON, return an error response.