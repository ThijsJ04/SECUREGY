from flask import Flask, request, jsonify
import base64
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    data = request.headers.get('file_contents')
    if not data:
        return jsonify({'error': 'Missing "file_contents" header.'}), 400

    decoded_data = base64.b64decode(data).decode()
    start = decoded_data.find('{') + 1
    end = decoded_data.rfind('}')
    content = decoded_data[start:end]

    try:
        return jsonify(json.loads(content))
    except json.JSONDecodeError as e:
        return jsonify({'error': f"Invalid JSON syntax: {e}"}), 400