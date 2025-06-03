import json


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", default=None)
    if not file_contents:
        return "No content provided", 400
    try:
        data = json.loads(file_contents)  # Load the JSON data
        return '{"data": {}'.format(**data), 200
    except json.JSONDecodeError as e:
        return str(e), 400
