def unmarshal_data():
    data = request.args.get('data', None)
    if data is None or not data.startswith("0x"):
        return "Invalid hexadecimal data", 400

    try:
        hex_data = data[2:]
        byte_data = bytes.fromhex(hex_data)
        unmarshalled_data = marshal.loads(byte_data)
        return unmarshalled_data
    except Exception as e:
        return f"Error while unmarshalling data: {str(e)}", 500