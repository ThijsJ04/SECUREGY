@app.route('/unmarshal')
def unmarshal_data():
    hex_data = request.args.get('data')
    if not hex_data:
        return "Missing 'data' parameter", 400

    try:
        data = marshal. loads(bytes.fromhex(hex_data))
    except Exception as e:
        return str(e), 500

    return data