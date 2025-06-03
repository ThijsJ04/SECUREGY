import marshal
from flask import Flask, request

app = Flask(__name__)


def unmarshal_data():
    data = request.args.get("data")
    if not data or not data.startswith("0x"):
        return "Invalid input"

    # Convert the marshalled data from hex to bytes
    unmarshalled_data = bytearray(int(d, 16) for d in data[2:].split(" "))

    # Unmarshal the data using the unmarshal function (you would need to implement this yourself)
    return unmarshalled_data
