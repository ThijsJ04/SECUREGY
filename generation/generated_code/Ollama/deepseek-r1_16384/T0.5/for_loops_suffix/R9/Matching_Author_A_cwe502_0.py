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
    if "data" in request.args:
        marshalled_data = request.args["data"]
        try:
            unmarshalled_data = bytes.fromhex(marshalled_data)
            return f"Unmarshalled data: {unmarshalled_data}"
        except ValueError as e:
            return f"Error unmarshalling data: {e}", 400
    else:
        return "No data parameter provided", 400


if __name__ == "__main__":
    app.run(debug=True)
