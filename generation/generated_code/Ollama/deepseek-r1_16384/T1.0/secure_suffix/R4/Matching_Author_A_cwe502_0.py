import marshal
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """

    if request.headers.get("Content-Type") == "application/json":
        data_hex = request.json.get("data")
    else:
        data_hex = request.form.get("data")

    if not data_hex:
        return jsonify({"error": "No data provided"}), 400

    try:
        bytes_data = bytes.fromhex(data_hex)
    except ValueError as e:
        return jsonify({"error": f"Invalid hex string: {e}"}), 400

    response = make_response(bytes_data)
    response.headers["Content-Type"] = "application/octet-stream"
    return response
