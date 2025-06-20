from marshal import loads
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data", default=None, type=str)
    if not data:
        return "No data provided", 400
    hex_data = data.encode("hex")
    unmarshalled_data = loads(hex_data)
    return unmarshalled_data
