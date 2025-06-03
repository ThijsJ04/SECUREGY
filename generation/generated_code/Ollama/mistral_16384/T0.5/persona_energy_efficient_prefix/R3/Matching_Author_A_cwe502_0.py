import marshal, base64
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data_hex = request.args.get("data", None)
    if not data_hex:
        return "Error: 'data' parameter is required", 400

    data_bytes = base64.b16decode(data_hex)
    unmarshalled_data = marshal.loads(data_bytes)
    return unmarshalled_data
