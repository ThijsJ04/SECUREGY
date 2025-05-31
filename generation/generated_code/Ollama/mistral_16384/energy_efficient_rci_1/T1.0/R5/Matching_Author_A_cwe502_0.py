from marshal import loads
@app.route('/unmarshal')
def unmarshal_data():
    data = request.args.get('data', None)
    if data:
        try:
            hex_str = data[2:].lstrip("0x")  # Remove '0x' prefix if present
            byte_array = bytes.fromhex(hex_str)
            return loads(byte_array)  # Return the unmarshalled data
        except ValueError as e:
            return str(e), 400  # Return an error message and a status code if unmarshalling fails