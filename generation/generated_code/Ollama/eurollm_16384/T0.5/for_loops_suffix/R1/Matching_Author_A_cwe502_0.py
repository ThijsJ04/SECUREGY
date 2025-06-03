import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    and return the unmarshalled data.
    """
    key = request.form[
        "data"
    ]  # Assuming the marshalled data is sent in a form field named 'data'
    with open(f"{app.root_path}/temp/unmarshaled_{key}.txt", "wb") as f:
        f.write(marshal.loads(key))
    return marshal.dumps(key)  # Return the unmarshalled data as a string
