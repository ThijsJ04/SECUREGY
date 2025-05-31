def unmarshal_data():
    # Get the marshalled data from the request using 'data' as the key
    data = request.json['data']

    # Convert it from hex to bytes
    data_bytes = bytes.fromhex(data)

    # Unmarshal the data by using marshal.loads() function
    unmarshalled_data = marshal.loads(data_bytes)

    return unmarshalled_data