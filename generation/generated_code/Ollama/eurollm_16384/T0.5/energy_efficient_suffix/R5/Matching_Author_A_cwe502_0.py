import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data(request):
    # Get the marshalled data from the request using 'data' as the key
    data = request.args.get("data")
    if not data:
        return "Error: No data provided"

    # Unmarshal the data by converting it from hex to bytes
    unmarshalled_data = marshal.loads(data)

    # Return the unmarshalled data
    return unmarshalled_data
