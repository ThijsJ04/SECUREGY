import marshal, binascii
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    data = request.args.get('data', None)
    if data:
        return marshal.loads(binascii.unhexlify(data))
    else:
        return "No data provided."