import marshal
from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data")
    data_bytes = bytes.fromhex(data)
    unmarshalled_data = marshal.loads(data_bytes)
    return make_response(unmarshalled_data)
