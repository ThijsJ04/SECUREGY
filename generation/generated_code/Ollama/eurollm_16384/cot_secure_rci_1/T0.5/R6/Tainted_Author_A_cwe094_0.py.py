from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def contents_dict():
    data = request.args.get('data')  # Assuming 'data' is the key for the JSON string
    if not data:
        return "Missing required argument: 'data'"

    try:
        content = json.loads(data)
        return str(content)
    except ValueError as e:
        return f"Invalid JSON: {e}"