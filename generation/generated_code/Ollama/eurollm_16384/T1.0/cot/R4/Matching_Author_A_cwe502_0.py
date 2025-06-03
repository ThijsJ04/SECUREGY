import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.get_json()  # Assuming the data is sent as JSON in the request body
    unmarshalled_data = marshal.loads(data["data"].encode())
    return "Successfully unmarshaled: {0}".format(unmarshalled_data)
