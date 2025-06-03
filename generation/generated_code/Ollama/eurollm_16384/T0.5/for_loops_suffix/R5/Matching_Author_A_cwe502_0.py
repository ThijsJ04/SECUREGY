import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    data = request.get_json()  # Assuming JSON is the expected format

    # Unmarshal the data from marshaled bytes to a dictionary
    unmarshalled_data = marshal.loads(
        data["data"].encode("hex"),
        object_hook=lambda d: dict((k, v) for k, v in d.items()),
    )

    return unmarshalled_data
