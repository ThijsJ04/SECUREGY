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
    data = request.args.get("data")  # or request.form.get('data') if form data

    # Convert hex string to bytes
    unmarshalled_data = bytes.fromhex(data)

    # Return the unmarshalled data as a response
    return marshal.dumps(unmarshalled_data)


if __name__ == "__main__":
    app.run(debug=True)
