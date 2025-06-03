import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data(request):
    data = request.get_json()  # Assuming JSON data is sent in the request
    unmarshalled_data = marshal.loads(
        data["data"].encode("hex"), object_hook=lambda o: bytes([o])
    )[0]
    return unmarshalled_data
