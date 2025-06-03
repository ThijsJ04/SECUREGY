import marshal
from flask import Flask, request

app = Flask(__name__)


def unmarshal_data():
    data = request.args.get(
        "data"
    )  # Get the marshalled data from the request as 'data' key

    if data:
        unmarshalled_data = marshal.loads(
            data
        )  # Unmarshal the data by converting it from hex to bytes
        return unmarshalled_data
    else:
        return "No data provided"
