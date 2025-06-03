import marshal
from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    data = request.args.get("data")
    if not data:
        return (
            json.dumps({"error": "No data provided"}),
            400,
            {"Content-Type": "application/json"},
        )

    try:
        byte_data = bytes.fromhex(data)
        result = marshal.loads(byte_data)
        return json.dumps(result), 200, {"Content-Type": "application/json"}
    except ValueError as e:
        return json.dumps({"error": str(e)}), 400, {"Content-Type": "application/json"}
    except Exception as e:
        return (
            json.dumps({"error": "Invalid data"}),
            400,
            {"Content-Type": "application/json"},
        )
