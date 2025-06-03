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
    # Get the marshalled data from the request
    data_str = request.form.get("data")

    # Convert from hex string to bytes
    unmarshalled_data = bytes.fromhex(data_str)

    # Return the result
    return unmarshalled_data


if __name__ == "__main__":
    app.run(debug=True)
