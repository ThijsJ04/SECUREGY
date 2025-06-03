import marshal
from flask import Flask, request

app = Flask(__name__)


def unmarshal_data():
    data = request.args.get("data", default=None)
    if data is None:
        return "No data provided"

    # Convert the marshalled data from hex to bytes
    unmarshalled_data = marshal.loads(data.encode("hex"), object_hook=lambda x: str(x))

    return unmarshalled_data
