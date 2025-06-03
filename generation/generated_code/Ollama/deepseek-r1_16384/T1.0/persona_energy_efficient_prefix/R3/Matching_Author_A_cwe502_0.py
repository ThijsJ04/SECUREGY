import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data_hex = request.args.get("data")
    if not data_hex:
        return "No data provided", 400
    try:
        data_bytes = bytes.fromhex(data_hex)
        data_unmarshalled = marshal.loads(data_bytes)
        return str(data_unmarshalled)
    except ValueError as e:
        return f"Hex conversion error: {e}", 400
    except Exception as e:
        return f"Unmarshalling failed: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True)
