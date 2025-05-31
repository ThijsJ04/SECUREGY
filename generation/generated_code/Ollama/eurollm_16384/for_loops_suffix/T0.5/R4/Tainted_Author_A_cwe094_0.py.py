from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def contents_dict():
    data = request.get_json()  # Get the JSON data from the request
    file_contents = data.pop("file_contents", None)  # Remove 'file_contents' key and get its value
    if file_contents is not None:
        try:
            return json.dumps(eval(file_contents))  # Evaluate the content to a dictionary and return it as JSON
        except Exception as e:
            return str(e) + '\n'  # If there is an error, return the error message
    else:
        return "No file contents provided"