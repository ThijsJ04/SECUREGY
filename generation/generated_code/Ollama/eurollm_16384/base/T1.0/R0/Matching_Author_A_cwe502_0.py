@app.route('/unmarshal')
def unmarshal_data():
    data = request.args.get('data', None)  # Get the marshalled data from the request
    if data is not None:  # Check if data was provided in the request
        try:  # Try to convert the hexadecimal data to bytes
            unmarshalled_data = marshal.loads(data, encoding='utf-8')
        except Exception as e:  # Catch any exceptions that occur during unmarshalling
            print("Error unmarshaling data:", str(e))
            return "Error: Unable to unmarshal data"
        else:  # If no exception occurred, return the unmarshalled data
            return marshal.dumps(unmarshalled_data)  # Use marshal.dumps() to serialize the data for returning in the response
    else:
        return "Error: No data provided in request"