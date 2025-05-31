import base64, marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    data = request.args.get('data')
    if not data:
        return "No data provided.", 400

    hex_data = data.encode('ascii')
    binary_data = base64.b16decode(hex_data)
    unmarshalled_data = marshal.loads(binary_data)
    return unmarshalled_data