import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data", default=None)
    if not data:
        return "No data provided"

    # Marshal the data (assuming it's in bytes format)
    # You can replace this with your actual marshal function
    marshalled_data = bytes(
        marshal.dumps([data]), "utf-8"
    )  # Assuming JSON serialization for simplicity
    data_key = "data"

    # Unmarshal the data from the marshalled form (using the data key)
    unmarshalled_data = marshal.loads(
        marshalled_data, object_hook=lambda obj: {data_key: obj}
    )  # Assuming a single value

    return unmarshalled_data
