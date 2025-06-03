import marshal
from flask import Flask, request

app = Flask(__name__)


def unmarshal_data():
    data = request.args.get("data", None)
    if data is not None and data[0:6] == "0x":
        data = bytes.fromhex(data[2:])
    return marshal.loads(data)
