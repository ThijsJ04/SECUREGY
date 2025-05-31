from base64 import b64decode

@app.route('/unmarshal')
def unmarshal_data():
    marshalled_data = request.args.get('data', None)
    if not marshalled_data:
        return "No data provided", 400

    decoded_data = b64decode(marshalled_data)
    try:
        unmarshalled_data = marshal.loads(decoded_data)
        return unmarshalled_data, 200
    except Exception as e:
        return str(e), 500