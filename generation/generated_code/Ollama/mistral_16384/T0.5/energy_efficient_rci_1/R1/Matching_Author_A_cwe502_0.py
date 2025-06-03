import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data", None)
    if data is not None:
        try:
            hex_data = bytes.fromhex(data)
            return marshal.loads(hex_data)
        except Exception as e:
            return str(e), 500
    else:
        return "No data provided", 400
