@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    payload = request.get_json()  # Assuming JSON is sent in the POST request
    serialized_payload = marshal.dumps(payload)  # Convert the payload to a string
    data = request.headers.get('data', '')  # Get the value of the key 'data' from the headers
    if not data:  # If no 'data' header is found
        return "No data provided"
    else:
        try:
            unmarshalled_payload = marshal.loads(data)  # Unmarshal the data by converting it back to bytes
            print("Unmarshalled payload: ", unmarshalled_payload)
        except Exception as e:
            return str(e)