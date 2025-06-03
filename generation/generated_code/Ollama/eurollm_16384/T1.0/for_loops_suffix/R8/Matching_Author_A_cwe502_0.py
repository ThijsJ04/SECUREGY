import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    try:
        # Get the key from the request path (it should be 'data')
        data_key = request.path.split("/")[1] if "/" in request.path else None
    except Exception as e:
        return str(e), 500

    try:
        # Get the marshalled data from the request
        marshalled_data = (
            request.get_json().get("{}".format(data_key))
            if "{" in request.get_json()
            else request.args.get(data_key)
        )
    except Exception as e:
        return str(e), 501

    try:
        # Unmarshal the data by converting it from hex to bytes
        data = marshal.loads(bytes.fromhex(marshalled_data))
    except Exception as e:
        return str(e), 406

    return data, 200  # return the unmarshalled data with HTTP response status 200
