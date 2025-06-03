import marshal
from flask import Flask, request

app = Flask(__name__)


def unmarshal_data():
    data = request.json["data"]
    # Convert hex to bytes
    decoded_data = marshal.loads(bytes.fromhex(data))
    return decoded_data
