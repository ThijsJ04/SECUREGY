import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data")
    if not data:
        return "No data provided", 400
    try:
        unmarshalled = bytes.fromhex(data)
    except ValueError:
        return "Invalid hex data", 400
    return unmarshalled


if __name__ == "__main__":
    app.run(debug=True)
