import marshal
from flask import Flask, request

app = Flask(__name__)


def unmarshal_data():
    data = request.args.get("data")
    if data:
        hex_data = bytes.fromhex(data)
        return marshal.loads(hex_data)
    else:
        return "No data provided"
