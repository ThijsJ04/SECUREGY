import marshal
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data")
    if not data:
        return jsonify({"error": "Data parameter not found"}), 400
    try:
        bytes_data = bytes.fromhex(data)
        result = marshal.loads(bytes_data)
        return jsonify(result)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Unmarshalling failed: {str(e)}"}), 500
