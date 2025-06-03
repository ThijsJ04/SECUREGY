import marshal
from flask import Flask, request, jsonify, Response

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data")
    if not data:
        return jsonify({"error": "Data parameter is missing"}), 400
    try:
        data_bytes = bytes.fromhex(data)
        return Response(data_bytes, mimetype="application/octet-stream")
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
