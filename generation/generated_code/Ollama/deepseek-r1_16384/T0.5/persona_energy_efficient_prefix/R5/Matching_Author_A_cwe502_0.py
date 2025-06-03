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
    # Extract the marshalled data from the request parameters
    data = request.args.get("data")

    # Convert the hex string to bytes
    unmarshalled_data = bytes.fromhex(data)

    # Return the unmarshalled data as a JSON response
    return {"result": unmarshalled_data.decode()}


if __name__ == "__main__":
    app.run(debug=True)
