def unmarshal_data():
    data = request.args.get('data')
    if data is None or len(data) % 2 != 0:
        return "Invalid input", 400

    hex_bytes = bytes.fromhex(data)
    unmarshalled_data = marshal.loads(hex_bytes)
    return unmarshalled_data