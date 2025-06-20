import marshal
from flask import Flask, request

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
        return jsonify({"error": "No data provided"}), 400
    try:
        byte_data = bytes.fromhex(data)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    return Response(byte_data, content_type="application/octet-stream")
