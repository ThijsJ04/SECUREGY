def unmarshal_data():
    data = request.args.get('data')
    if data is None:
        return "Error: No data provided.", 400

    # Convert hex string to bytes
    byte_data = bytes.fromhex(data)

    # Unmarshal the data using marshal.loads()
    unmarshalled_data = marshal.loads(byte_data)

    return unmarshalled_data