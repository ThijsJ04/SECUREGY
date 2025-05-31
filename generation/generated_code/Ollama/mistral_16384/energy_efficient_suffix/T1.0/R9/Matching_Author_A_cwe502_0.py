from marshal import loads as unmarshal

@app.route('/unmarshal')
def unmarshal_data():
    hex_data = request.args.get('data')
    data = bytes.fromhex(hex_data)
    return unmarshal(data)