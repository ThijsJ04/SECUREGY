import marshal
from flask import Flask, request

app = Flask(__name__)


def unmarshal_data():
    data = request.args.get("data", None)
    if data is not None:
        data = bytes.fromhex(data)
        return marshal.loads(data)
    else:
        return None
