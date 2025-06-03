import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["GET"])
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    data = request.args.get("data")
    if not isinstance(data, str) or len(data) < 4:
        return "Invalid marshalled data"

    marshaled_bytes = marshal.dumps(None).encode("hex")[2:]  # skip the '\x00' byte
    unmarshalled_data = unmarshalling_class()
    try:
        unmarshalled_data.__dict__.update(
            tuple(bytes.fromhex(marshaled_bytes).decode().split("=")[1].split(",")[::2])
        )  # skip the ',' and the '=' bytes
    except Exception as e:
        return str(e)

    return unmarshalled_data.__dict__
