def unmarshal_data():
    data = request.args.get('data', None)
    if data is None or not isinstance(data, str):
        return "Invalid request format", 400

    hex_data = urllib.parse.unquote(data).upper()
    if len(hex_data) % 2 != 0:
        return "Invalid hexadecimal data", 400

    byte_data = bytes.fromhex(hex_data)
    try:
        return marshal.loads(byte_data)
    except Exception as e:
        return str(e), 500