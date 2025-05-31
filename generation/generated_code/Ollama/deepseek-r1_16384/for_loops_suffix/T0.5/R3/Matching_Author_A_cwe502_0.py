import marshal
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    data_hex = request.args.get('data')
    unmarshalled_data = bytes.fromhex(data_hex)
    return make_response(unmarshalled_data, 200, {'Content-Type': 'application/octet-stream'})