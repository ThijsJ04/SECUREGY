import marshal
from flask import Flask, request

app = Flask(__name__)


def unmarshal_data():
    data = request.json["data"]
    hex_data = bytes.fromhex(data)
    return marshal.loads(hex_data)
