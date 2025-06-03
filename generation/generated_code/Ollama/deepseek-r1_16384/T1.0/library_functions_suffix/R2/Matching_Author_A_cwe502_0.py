import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data_hex = (
        request.args.get("data")
        or request.form.get("data")
        or (request.json.get("data") if request.is_json else None)
    )
    if not data_hex:
        return jsonify({"error": "No data provided"}), 400
    try:
        unmarshalled_data = bytes.fromhex(data_hex)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    return Response(unmarshalled_data, content_type="application/octet-stream")
