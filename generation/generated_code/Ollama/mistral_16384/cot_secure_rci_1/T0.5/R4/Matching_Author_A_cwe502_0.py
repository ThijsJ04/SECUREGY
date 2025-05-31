def unmarshal_data():
    data = request.args.get('data')
    if data:
        data_bytes = bytes.fromhex(data)
        return marshal.loads(data_bytes)