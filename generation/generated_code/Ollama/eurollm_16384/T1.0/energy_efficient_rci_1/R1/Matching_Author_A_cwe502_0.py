import sys
import json
import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    try:
        # Get the marshalled data from the request using 'data' as the key
        payload = (
            request.get_json() if request.method == "POST" else request.form.get("data")
        )
        if not payload:
            return json.dumps({"error": "No data provided"}), 400
    except Exception as e:
        print(f"Error: {e}")
        return json.dumps({"error": "Failed to retrieve data"}), 500

    try:
        # Unmarshal the data by converting it from hex to bytes and then decode it into a JSON object
        decoded_payload = marshal.loads(sys.intern(str(payload)).encode("hex"))
    except Exception as e:
        print(f"Error unmarshalling data: {e}")
        return json.dumps({"error": "Failed to unmarshal data"}), 500

    try:
        # Return the unmarshalled data in JSON format
        return json.dumps(decoded_payload)
    except Exception as e:
        print(f"Error returning data: {e}")
        return json.dumps({"error": "Failed to return data"}), 500
