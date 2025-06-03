import marshal
from flask import Flask, request, Response

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data")
    unmarshalled_data = bytes.fromhex(data)
    return Response(unmarshalled_data)
