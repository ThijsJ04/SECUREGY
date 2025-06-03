import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data")
    if not data:
        return "No data provided"
    try:
        unmarshalled = bytes.fromhex(data)
        return unmarshalled
    except ValueError as e:
        return f"Error decoding hex: {e}", 400


if __name__ == "__main__":
    app.run(debug=True)
