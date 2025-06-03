import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshaled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    data = request.get_json()["data"]  # Get the marshaled data from the request
    unmarshalled_data = marshal.loads(data)  # Unmarshal the data using marshal.loads()
    return unmarshalled_data
