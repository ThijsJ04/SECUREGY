@app.route('/first_name')
def echo_name():
    data = request.args.get("first_name", default="World")
    return f"Greetings, {escape(data)}!"