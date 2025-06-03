import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data", "")
    try:
        unmarshalled = bytes.fromhex(data)
        return (
            unmarshalled.decode()
        )  # Assuming the result is a string; adjust as needed
    except ValueError:
        return "Invalid hexadecimal data", 400


if __name__ == "__main__":
    app.run(debug=True)
