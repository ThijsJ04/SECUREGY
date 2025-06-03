import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.json["data"]
    return bytes.fromhex(data)
