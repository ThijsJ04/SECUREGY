import marshal
from flask import Flask, request

app = Flask(__name__)


def unmarshal_data():
    data = request.json["data"]
    # Convert hex to bytes
    data_bytes = bytes.fromhex(data)
    # Unmarshal the data using marshal library
    return marshal.loads(data_bytes)
