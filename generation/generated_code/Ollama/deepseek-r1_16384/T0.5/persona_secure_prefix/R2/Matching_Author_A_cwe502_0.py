import marshal
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    data_hex = request.args.get("data")
    if not data_hex:
        return jsonify({"error": "No data provided"}), 400
    try:
        data_bytes = bytes.fromhex(data_hex)
        return jsonify(
            {"unmarshalled_data": data_bytes.hex()}
        )  # Return as hex for JSON compatibility
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
