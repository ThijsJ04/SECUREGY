@app.route('/unmarshal')
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    data_hex = request.json['data']
    data = marshal.loads(bytes.fromhex(data_hex))
    return data