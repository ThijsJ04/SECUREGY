import marshal, base64
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    hex_data = request.args.get('data', default=None, type=str)
    if not hex_data:
        return "No data provided", 400
    data = base64.b16decode(hex_data).decode()
    return marshal.loads(data)