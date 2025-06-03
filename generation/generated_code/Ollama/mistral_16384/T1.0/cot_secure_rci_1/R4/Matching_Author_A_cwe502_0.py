from marshal import loads


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    data = request.args.get("data")
    if data:
        # Convert the hex string to bytes first
        data_bytes = bytes.fromhex(data)
        # Then unmarshal the bytes to a Python object
        return loads(data_bytes)
