import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data_hex = request.args.get("data")
    if not data_hex:
        return "No data provided", 400
    try:
        data_bytes = bytes.fromhex(data_hex)
    except ValueError as e:
        return f"Invalid hex string: {e}", 400
    return data_bytes


if __name__ == "__main__":
    app.run(debug=True)
