import marshal, base64
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.json["data"]
    decoded_data = base64.b64decode(data)
    return marshal.loads(decoded_data)
