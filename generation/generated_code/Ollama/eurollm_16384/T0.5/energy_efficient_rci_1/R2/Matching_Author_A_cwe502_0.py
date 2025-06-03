import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.get_json()  # Assuming JSON is being sent in the request body
    if "data" not in data:
        return "No data found", 400

    data = data["data"]

    # Unmarshal the data from bytes to a Python object (e.g., dictionary, list, etc.)
    unmarshalled_data = marshal.loads(data)  # marshal is used for unmarshalling

    return unmarshalled_data, 200
