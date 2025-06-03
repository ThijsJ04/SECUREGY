from marshal import loads
import base64


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data", None)
    if data is not None and isinstance(data, str):
        decoded_data = base64.b64decode(data)
        return loads(decoded_data)
