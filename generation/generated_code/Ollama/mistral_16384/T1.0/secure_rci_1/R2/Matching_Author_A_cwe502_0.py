import marshal
from flask import Flask, request

app = Flask(__name__)


def unmarshal_data():
    hex_data = request.args.get("data")
    bytes_data = marshal.unhex2abyte(hex_data)
    return bytes_data
