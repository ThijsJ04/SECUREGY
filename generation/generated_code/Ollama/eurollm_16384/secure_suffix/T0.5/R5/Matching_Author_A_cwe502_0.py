@app.route('/unmarshal')
def unmarshal_data():
    data = request.get_json()  # Get JSON data from the request
    if 'data' in data:
        marshalled_data = data['data']
        try:
            unmarshalled_data = marshal.loads(marshalled_data)
            return unmarshalled_data
        except Exception as e:
            print("Error unmarshalling data:", str(e))
    else:
        return "No 'data' key found in JSON request."