def unmarshal_data():
    data = request.args.get('data', None)
    if data is not None:
        data = bytes.fromhex(data)
        return marshal.loads(data)
    else:
        return None