def unmarshal_data():
    data = request.args.get('data')
    try:
        if type(data) == str and len(data) > 0:
            return marshal.loads(data.encode())
    except marshal.ExtTypeError as e:
        print("Failed to unmarshal data:", e)
        return "Unable to unmarshal data"
    except ValueError as e:
        print("Invalid data format", e)
        return "Invalid data format"