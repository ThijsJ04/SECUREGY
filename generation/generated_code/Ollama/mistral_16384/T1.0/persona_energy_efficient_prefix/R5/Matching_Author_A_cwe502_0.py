import marshal, binascii
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data_hex = request.args.get("data", "")
    data_bytes = binascii.unhexlify(data_hex)
    return marshal.loads(data_bytes)
