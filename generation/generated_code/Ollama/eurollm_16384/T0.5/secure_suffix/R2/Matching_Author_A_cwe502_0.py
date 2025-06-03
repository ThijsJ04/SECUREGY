import marshal
from flask import Flask, request

app = Flask(__name__)


def unmarshal_data(request):
    try:
        # Get the marshalled data from the request using 'data' as the key
        data = request.get("data")
    except KeyError:
        return "Invalid request", 400

    # Unmarshal the data by converting it from hex to bytes
    try:
        unmarshalled_data = marshal.loads(data)
    except ValueError as e:
        return str(e), 500

    return unmarshalled_data, 200
