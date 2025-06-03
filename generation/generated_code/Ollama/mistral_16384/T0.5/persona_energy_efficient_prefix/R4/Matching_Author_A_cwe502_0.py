import marshal, base64
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data", None)
    if data is not None:
        data_bytes = base64.b64decode(data)
        return marshal.loads(data_bytes)
