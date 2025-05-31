import pickle

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    data = request.get_data(key='data')  # Get the marshalled data from the request using 'data' as the key
    unmarshalled_data = pickle.loads(data)  # Unmarshall the data and return it
    return unmarshalled_data, 200