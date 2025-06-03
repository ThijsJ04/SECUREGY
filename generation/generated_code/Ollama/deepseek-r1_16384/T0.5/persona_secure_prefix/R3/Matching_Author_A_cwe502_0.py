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
    data_str = request.args.get("data", "")
    try:
        data_bytes = bytes.fromhex(data_str)
        result = marshal.load(data_bytes)
        return str(result)
    except Exception as e:
        return f"Error unmarshalling data: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True)
