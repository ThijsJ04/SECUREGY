import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    hex_str = request.args.get('data', '')
    if not hex_str.strip():
        return 'No data provided', 400
    try:
        byte_data = bytes.fromhex(hex_str)
    except ValueError as e:
        return f'Invalid hexadecimal string: {e}', 400
    return byte_data