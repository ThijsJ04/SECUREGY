@app.route('/unmarshal')
def unmarshal_data():
    try:
        data = json.loads(request.get_json())
        return data
    except ValueError as e:
        # Handle the case where no JSON payload is found
        return str(e)