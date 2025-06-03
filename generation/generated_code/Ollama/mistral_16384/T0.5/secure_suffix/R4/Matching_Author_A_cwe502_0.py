import marshal
from flask import Flask, request

app = Flask(__name__)


def unmarshal_data():
    data = request.args.get("data")
    if not data:
        return "Error: No data provided", 400

    # Convert hex string to bytes
    data_bytes = bytearray.fromhex(data)

    try:
        unmarshalled_data = marshal.loads(data_bytes)
    except Exception as e:
        return f"Error: Failed to unmarshal data. {str(e)}", 500

    return unmarshalled_data
