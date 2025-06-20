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
        # Convert hex string to bytes
        data_bytes = bytes.fromhex(data)
        # Unmarshal the data
        result = loads(data_bytes)
        return result
