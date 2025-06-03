import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["GET"])
def unmarshal_data():
    data = request.get_json()  # Get the JSON payload from the request
    key = "data"
    try:
        # Unmarshal the data using marshal
        decompressed_data = marshal.loads(request.data[key])
        return {key: decompressed_data}
    except KeyError as e:
        return str({"error": f"Failed to unmarshal data. Invalid JSON structure."}), 400
