import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data_hex = request.form.get("data")
    data_bytes = bytes.fromhex(data_hex)
    unmarshalled = marshal.loads(data_bytes)
    return str(unmarshalled)
