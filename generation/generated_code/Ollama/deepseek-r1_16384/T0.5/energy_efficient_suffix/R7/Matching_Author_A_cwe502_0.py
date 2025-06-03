import marshal
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data")
    byte_data = bytes.fromhex(data)
    result = marshal.loads(byte_data)
    return jsonify(result)
