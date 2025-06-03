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
    data = request.get("data")  # get the marshaled data
    data_bytes = (
        b"unmarshalled here".encode()
    )  # your marshalled data, let's say it's in string format
    request.set("data", data_bytes)  # set unmarshalled data back to request object

    return None  # no content returned by default (could be changed if needed)
