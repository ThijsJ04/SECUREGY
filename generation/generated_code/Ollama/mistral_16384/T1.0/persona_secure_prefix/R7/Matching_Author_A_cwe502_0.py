import marshal
from flask import Flask, request

app = Flask(__name__)


def unmarshal_data():
    data = request.args.get("data")
    if not data:
        return "Error: No data provided", 400
    hex_data = data.encode()
    try:
        return marshal.loads(hex_to_bytes(hex_data))
    except Exception as e:
        return f"Error: {str(e)}", 500


def hex_to_bytes(hex_string):
    bytes_list = (int(hex_string[i : i + 2], 16) for i in range(0, len(hex_string), 2))
    return bytes(bytes_list)
