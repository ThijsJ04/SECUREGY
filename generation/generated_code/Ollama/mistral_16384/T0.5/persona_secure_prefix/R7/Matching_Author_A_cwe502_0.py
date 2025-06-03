from base64 import b64decode


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data", None)
    if data is not None and len(data) > 0:
        # Convert hex string to bytes
        data = b64decode(data)
        # Unmarshal the data using marshal module
        return marshal.loads(data)
