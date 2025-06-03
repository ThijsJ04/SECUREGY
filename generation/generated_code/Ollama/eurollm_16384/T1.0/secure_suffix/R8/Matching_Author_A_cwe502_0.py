import json
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    # Use `request.get_json()` to get the marshaled data as a JSON object
    data = request.get_json()

    if not isinstance(data, dict):
        return "Error: Invalid JSON response", 400

    # Try to unmarshal the data from bytes using `load` and then convert it back to a dictionary
    try:
        decoded_data = json.loads(
            json.dumps(data, ensure_ascii=False)
        )  # or use marshal.loads(b64encode(json.dumps(data, ensure_ascii=False)).decode())
        return decoded_data
    except Exception as e:
        return f"Error unmarshaling data: {e}", 500
