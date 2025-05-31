@app.route('/unmarshal')
def unmarshal_data():
    data = request.args.get('data', default=None)  # Retrieve the marshalled data from the request
    if not isinstance(data, str):  # Check if the data is a string (marshalled as hex)
        return "Error: Invalid data type"
    else:
        try:
            unmarshalled_data = marshal.loads(data.encode('utf-8'))  # Unmarshal the data using the `marshal` module
            return str(unmarshalled_data)  # Convert the unmarshalled data to a string for easier processing
        except Exception as e:
            return "Error: Unable to unmarshal data" + str(e)