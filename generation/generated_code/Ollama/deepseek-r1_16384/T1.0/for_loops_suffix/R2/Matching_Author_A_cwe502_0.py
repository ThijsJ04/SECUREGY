import marshal
from flask import Flask, request
from flask import jsonify

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data")
    data_bytes = bytes.fromhex(data)
    unmarshalled_data = marshal.loads(data_bytes)
    return jsonify(unmarshalled_data)
