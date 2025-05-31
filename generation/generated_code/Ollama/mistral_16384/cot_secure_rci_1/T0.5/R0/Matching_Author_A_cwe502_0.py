@app.route('/unmarshal')
def unmarshal_data():
    data = request.args.get('data', default=None, type=str)
    if data is not None:
        data = bytes.fromhex(data)
        return marshal.loads(data)