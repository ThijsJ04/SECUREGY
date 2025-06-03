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
    # Extract hex data from request parameters
    hex_data = request.args.get("data") or request.form.get("data")

    # Convert hex string to bytes
    data_bytes = bytes.fromhex(hex_data)

    # Unmarshal the bytes using marshal module
    result = marshal.load(data_bytes)

    # Return the unmarshalled data as JSON response
    return {"unmarshalled_data": result}


if __name__ == "__main__":
    app.run(debug=True)
