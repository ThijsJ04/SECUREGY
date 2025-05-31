import marshal
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    data_hex = request.args.get('data', '')
    data_bytes = bytes.fromhex(data_hex)
    return Response(data_bytes, content_type='application/octet-stream')