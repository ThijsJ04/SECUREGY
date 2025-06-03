import marshal
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data_hex = request.args.get("data")
    if not data_hex:
        return jsonify({"error": "No data provided"}), 400
    try:
        data_bytes = bytes.fromhex(data_hex)
        obj = marshal.loads(data_bytes)
        return jsonify(obj)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
