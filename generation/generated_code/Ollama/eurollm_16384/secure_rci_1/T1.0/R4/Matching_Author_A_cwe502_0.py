@app.route('/unmarshal')
def unmarshal_data():
    data = request.get_json()
    if 'data' not in data:
        return "Error: Invalid JSON response", 400
    data = data['data']

    # Unmarshal the data
    with open('data.m', 'wb') as f:
        f.write(data)
    unmarshalled_data = marshal.load(open('data.m'))
    return unmarshalled_data, 201