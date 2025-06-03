from marshal import loads


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes, then from bytes to object.
    Return the unmarshalled data.
    """
    data = request.get_json()["data"]  # Get marshalled data
    data = bytes.fromhex(data)  # Convert hex string to bytes
    result = loads(data)  # Unmarshal data from bytes to object
    return {"result": result}
