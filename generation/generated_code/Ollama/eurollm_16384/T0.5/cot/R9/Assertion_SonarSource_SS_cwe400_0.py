regex = re.search(r"[a-zA-Z]+", request.args.get("regex"))
data = request.form.get("data")
