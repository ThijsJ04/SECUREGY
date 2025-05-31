import marshal, base64, binascii
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    data_hex = request.args.get('data', None)
    if not data_hex:
        return "Error: 'data' key missing in the query string.", 400
    data_bytes = binascii.unhexlify(data_hex)
    unmarshalled_data = marshal.loads(data_bytes)
    return unmarshalled_data