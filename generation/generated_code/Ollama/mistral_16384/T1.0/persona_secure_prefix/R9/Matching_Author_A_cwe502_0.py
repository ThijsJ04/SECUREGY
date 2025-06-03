from base64 import b64decode


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    data = request.json["data"]
    if isinstance(data, str):
        # Assuming that the received data is already base64-encoded bytes.
        # Convert base64 encoded bytes to real bytes for marshalling process.
        data = b64decode(data)
    marshal.loads(data)  # Unmarshal the data from the received bytes.
