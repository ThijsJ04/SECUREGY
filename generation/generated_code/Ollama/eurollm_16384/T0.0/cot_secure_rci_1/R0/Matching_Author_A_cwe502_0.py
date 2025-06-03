import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data", default=None)
    if data is None:
        return "No data provided"

    # Convert the hexadecimal value to bytes
    unmarshalled_data = int(data, 16).tobytes()

    return unmarshalled_data
