import marshal
from flask import Flask, request

app = Flask(__name__)


def unmarshal_data():
    """
    This function assumes that the marshalled data is received in the request using 'data' as the key.
    It then converts the marshaled bytes to a native Python object and returns it.
    """
    data = request.get_json()  # Assuming JSON is being sent
    unmarshalled_data = marsh.load(
        data["data"]
    )  # Unmarshal the data from JSON using pickle
    return unmarshalled_data
