from base64 import b64decode


def unmarshal_data():
    data = request.json[
        "data"
    ]  # Assuming the marshalled data is sent as a JSON object with 'data' key
    hex_string = data.encode("hex")  # Encode string to bytes for hex values
    return marshal.loads(
        b64decode(hex_string)
    )  # Decode hex strings to bytes and unmarshal the data
