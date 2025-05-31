import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    hex_string = request.args.get('data')
    if not hex_string:
        return 'Data parameter is required', 400
    try:
        bytes_data = bytes.fromhex(hex_string)
    except ValueError as e:
        return f'Invalid hex string: {e}', 400
    return bytes_data