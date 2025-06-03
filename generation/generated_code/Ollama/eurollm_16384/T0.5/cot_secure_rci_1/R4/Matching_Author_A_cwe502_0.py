from flask import request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    try:
        unmarshalled_data = request.get_json()[
            "data"
        ]  # assuming JSON is used for marshalling
        print(unmarshalled_data)
    except KeyError as e:
        print("No 'data' key found in the request.")
