import marshal
from flask import Flask, request, Response, jsonify

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    data = request.args.get('data')
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    try:
        bytes_data = bytes.fromhex(data)
        return Response(bytes_data, content_type='application/octet-stream'), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400