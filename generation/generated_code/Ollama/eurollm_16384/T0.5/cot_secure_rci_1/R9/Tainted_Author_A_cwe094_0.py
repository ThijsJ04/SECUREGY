import json


@app.route("/eval")
def contents_dict():
    try:
        # Get the JSON data from the request
        data = request.get_json()  # or request.files.get('file').read().decode('utf-8')
    except Exception as e:
        return str(e)

    # Remove whitespace and newline characters before the first '{' and after the last '}'
    data = data.strip()

    # Evaluate the resulting string as a Python dictionary using eval()
    try:
        parsed_data = eval(data)
        return json.dumps(parsed_data, indent=2)  # pretty-print the result
    except Exception as e:
        return str(e)
