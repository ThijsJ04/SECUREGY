import marshal, binascii
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data_hex = request.args.get("data", default="", type=str)
    if data_hex:
        data = binascii.unhexlify(data_hex)
        return marshal.loads(data)
