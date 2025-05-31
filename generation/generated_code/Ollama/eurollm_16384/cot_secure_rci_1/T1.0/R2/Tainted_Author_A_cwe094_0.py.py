from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def contents_dict():
    data = request.get_json()  # Get the JSON data from the POST request
    if not data:
        return {"error": "No data provided"}, 400

    try:
        content = eval(data['file_contents'])  # Evaluate the content as a dictionary
        return {"result": content}
    except Exception as e:
        return {"error": str(e)}, 500