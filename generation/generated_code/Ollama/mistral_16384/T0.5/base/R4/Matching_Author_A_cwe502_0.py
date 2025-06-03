import marshal, base64
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data", None)
    if not data:
        return "Error: No data provided.", 400

    decoded_data = base64.b64decode(data)
    try:
        unmarshalled_data = marshal.loads(decoded_data)
    except Exception as e:
        return f"Error while unmarshalling data: {str(e)}", 500

    return unmarshalled_data
