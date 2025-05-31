@app.route('/unmarshal')
def unmarshal_data():
    data = request.args.get('data', default='default value', type=str)  # Get marshalled data from the request
    if data and isinstance(data, str):
        try:
            unmarshalled_data = marshal.loads(data.encode('utf-8'))
            return unmarshalled_data
        except Exception as e:
            print(e)
            return {"error": "Failed to unmarshal data"}
    else:
        return {"error": "Invalid or missing marshalled data"}