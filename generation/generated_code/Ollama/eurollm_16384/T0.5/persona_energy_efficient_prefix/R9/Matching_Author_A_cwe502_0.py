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
    data = request.args["data"]  # get the marshalled data from the request
    unmarshalled_data = marshal.loads(data)  # unmarshal the data using marshal.loads()
    return unmarshalled_data
