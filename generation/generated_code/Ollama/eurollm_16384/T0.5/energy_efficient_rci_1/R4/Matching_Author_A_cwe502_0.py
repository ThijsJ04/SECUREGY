import marshal
from flask import Flask, request

app = Flask(__name__)


def unmarshal_data():
    data = request.args.get("data", default=None)
    if data is None:
        return "No data provided"
    else:
        try:
            unmarshalled_data = marshal.loads(data.encode("utf-8"))
            return unmarshalled_data
        except Exception as e:
            print(e)
            return "Failed to unmarshal data"
