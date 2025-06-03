import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.get_json().get("data", "")
    if not data:
        return {"error": "No data provided"}, 400
    try:
        unmarshalled_data = bytes.fromhex(data)
        return {"result": unmarshalled_data.hex()}
    except ValueError:
        return {"error": "Invalid hexadecimal string"}, 400
