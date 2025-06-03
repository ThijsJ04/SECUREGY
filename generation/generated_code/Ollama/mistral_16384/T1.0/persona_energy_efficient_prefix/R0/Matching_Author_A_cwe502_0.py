import marshal, base64
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get(
        "data"
    )  # Get the marshalled data from the request using 'data' as the key
    encoded_data = base64.b64decode(data)  # Convert the data from hex to bytes
    return marshal.loads(
        encoded_data
    )  # Unmarshal the data by converting it from bytes back into its original Python object
