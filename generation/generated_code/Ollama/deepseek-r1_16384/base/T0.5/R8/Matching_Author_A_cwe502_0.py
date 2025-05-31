import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    data = request.args.get('data')
    if not data:
        return "No data provided"
    try:
        bytes_data = bytes.fromhex(data)
        return Response(bytes_data, mimetype='application/octet-stream')
    except ValueError as e:
        return f"Error: {e}"