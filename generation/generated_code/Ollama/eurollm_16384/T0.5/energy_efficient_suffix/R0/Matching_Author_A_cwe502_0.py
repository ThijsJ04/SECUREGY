import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    key = request.args.get("key")  # Get the key from the request query parameters
    data_hex = request.form.get(
        key
    )  # Get the marshalled data from the form (if any) or query parameters

    if data_hex:
        unmarshalled_data = marshal.loads(
            data_hex.encode("utf-8")
        )  # Unmarshal the data by converting it from hex to bytes
        return unmarshalled_data, 200, {"message": "Data successfully unmarshalled"}
    else:
        return "", 400, {"error": "No marshalled data provided"}
