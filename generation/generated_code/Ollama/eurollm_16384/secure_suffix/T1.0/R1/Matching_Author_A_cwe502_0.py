@app.route('/unmarshal')
def unmarshal_data():
    data = request.args.get('data', default=None)
    if not data or 'details' in data:
        return "", 400

    # Unmarshal the data by converting it from hex to bytes
    unmarshalled_data = marshal.loads(data)
    return unmarshalled_data