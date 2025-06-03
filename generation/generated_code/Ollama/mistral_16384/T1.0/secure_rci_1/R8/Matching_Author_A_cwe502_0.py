import marshal
from flask import Flask, request

app = Flask(__name__)


def unmarshal_data():
    marshalled_data = request.args.get("data", None)
    if marshalled_data is None or len(marshalled_data) % 2 != 0:
        return None, 400

    try:
        unmarshalled_data = marshal.loads(bytearray.fromhex(marshalled_data))
    except Exception as e:
        return None, 400

    return unmarshalled_data, 200
