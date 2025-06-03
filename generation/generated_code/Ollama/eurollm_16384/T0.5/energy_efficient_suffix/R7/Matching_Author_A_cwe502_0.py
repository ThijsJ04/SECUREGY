import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data(request):
    data = request.get("data")
    if not data or len(data) == 0:
        return "No data provided", 400

    unmarshalled_data = marshal.loads(data.encode())
    return unmarshalled_data, 200
