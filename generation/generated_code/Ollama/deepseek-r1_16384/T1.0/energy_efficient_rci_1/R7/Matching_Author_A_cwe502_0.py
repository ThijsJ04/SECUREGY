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
    data_hex = request.args.get("data")
    if data_hex:
        try:
            return marshal.loads(bytes.fromhex(data_hex))
        except Exception as e:
            return str(e), 400
    else:
        return "No data provided", 400


if __name__ == "__main__":
    app.run(debug=True)
