import marshal, base64
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    data_hex = request.args.get('data', None)
    if data_hex is None:
        return "Error: 'data' not provided.", 400
    data_bytes = base64.b64decode(data_hex)
    return marshal.loads(data_bytes)