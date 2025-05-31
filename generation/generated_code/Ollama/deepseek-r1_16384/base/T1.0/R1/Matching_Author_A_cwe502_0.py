import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    data = request.form.get('data', '')
    try:
        unmarshalled_bytes = bytes.fromhex(data)
    except ValueError:
        return 'Invalid hex string'
    return unmarshalled_bytes