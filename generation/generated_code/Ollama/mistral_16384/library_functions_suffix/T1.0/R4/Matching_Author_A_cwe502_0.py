@app.route('/unmarshal')
def unmarshal_data():
    data = request.args.get('data', None)
    if data is not None and len(data) > 0:
        unmarshalled_data = marshal.loads(bytes.fromhex(data))
        return unmarshalled_data
    else:
        return "Invalid data"