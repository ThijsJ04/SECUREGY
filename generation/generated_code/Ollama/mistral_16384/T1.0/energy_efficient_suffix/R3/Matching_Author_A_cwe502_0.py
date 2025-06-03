from marshal import loads


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes, then to object.
    Return the unmarshalled data.
    """
    data = request.json["data"]  # get data from the request
    decoded_data = bytes.fromhex(data)  # convert hex string to bytes
    return loads(decoded_data)  # unmarshal the data
