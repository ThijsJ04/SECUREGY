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
    bytes_data = bytes.fromhex(data_hex)
    unmarshalled_data = marshal.loads(bytes_data)
    return jsonify(unmarshalled_data)


if __name__ == "__main__":
    app.run(debug=True)
