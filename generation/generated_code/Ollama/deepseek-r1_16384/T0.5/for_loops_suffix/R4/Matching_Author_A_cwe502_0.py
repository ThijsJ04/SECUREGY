import marshal
from flask import Flask, request, jsonify, Response

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data")
    if not data:
        return jsonify({"error": "No data provided"}), 400
    try:
        unmarshalled_data = bytes.fromhex(data)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    return Response(unmarshalled_data, content_type="application/octet-stream")
