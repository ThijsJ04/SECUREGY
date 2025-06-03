import marshal, base64
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    then unmarshal the bytes into Python object(s).
    Return the unmarshalled data.
    """
    data = request.args.get("data")
    decoded_data = base64.b64decode(data)
    unmarshaled_data = marshal.loads(decoded_data)
    return str(
        unmarshaled_data
    )  # or any other appropriate response depending on the expected data type
