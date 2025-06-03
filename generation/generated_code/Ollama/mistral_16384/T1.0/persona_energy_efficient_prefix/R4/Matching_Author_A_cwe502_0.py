from marshal import loads


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data", default=None, type=str)
    if data is None:
        return "Error: No data provided", 400
    hex_data = bytes.fromhex(data)
    return loads(hex_data)
