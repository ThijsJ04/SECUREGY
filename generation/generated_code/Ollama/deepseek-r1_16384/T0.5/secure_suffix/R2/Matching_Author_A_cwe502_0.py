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
    data_str = request.args.get("data")
    if not data_str:
        return jsonify({"error": "No data provided"}), 400
    try:
        data_bytes = bytes.fromhex(data_str)
        result = marshal.loads(data_bytes)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
