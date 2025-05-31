from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def contents_dict():
    data = request.get_json()  # Get JSON data from the request

    # Remove unwanted characters before and after the first '{' and last '}'
    filtered_data = data['file_contents'].strip('{{').strip('}}')

    # Evaluate the filtered content to a dictionary
    try:
        result = eval(filtered_data)
        return result
    except Exception as e:
        return str(e), 500  # Return error message and status code 500