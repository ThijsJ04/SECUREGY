import marshal
from flask import request

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    data = request.form["data"]  # Assuming you have a form where users can input data

    unmarshalled_data = marshal.loads(data)  # Unmarshal the data using marshal library

    return "Successfully unmarshalled", 200, {"unmarshalled_data": unmarshalled_data}
