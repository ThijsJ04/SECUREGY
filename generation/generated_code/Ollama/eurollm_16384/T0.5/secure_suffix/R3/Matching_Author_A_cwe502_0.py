from flask import request
import marshal

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    data = request.get_json()  # Get the JSON data from the request
    unmarshalled_data = marshal.loads(
        data["data"].encode()
    )  # Unmarshal the data using 'data' as the key
    return unmarshalled_data
