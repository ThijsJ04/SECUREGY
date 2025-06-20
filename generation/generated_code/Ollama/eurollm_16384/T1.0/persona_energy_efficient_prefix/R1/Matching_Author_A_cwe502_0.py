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
    data = request.args.get("data")  # get the data from the request
    try:
        unmarshaled_data = marshal.loads(data)  # load the data using marshal
        return unmarshaled_data
    except Exception as e:
        print(f"Error unmarshaling data: {e}")
        return "Failure", 500
