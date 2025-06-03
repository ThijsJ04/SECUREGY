import marshal
from flask import Flask, request

app = Flask(__name__)


def unmarshal_data():
    data = request.args.get("data")
    if data:
        data_bytes = bytes.fromhex(data)
        return marshal.loads(data_bytes)
