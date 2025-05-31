@app.route('/unmarshal', methods=['GET'])
def unmarshal_data():
    data = request.args.get('data')
    if not data:
        return 'No data provided.'

    try:
        data = bytes.fromhex(data)
        # Add some logic to process the unmarshalled data here...
        # For example, you can print it or store it in a database...
        return f'Unmarshalled data: {data}'
    except ValueError as e:
        return str(e)