from flask import Flask, request

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def contents_dict():
    content = request.get_json()  # Assuming the content is in JSON format and can be retrieved using `request.get_json()`
    for key, value in content.items():
        if "{" not in str(value) or "}" not in str(value):
            return "Error: Not a valid dictionary structure", 400
    parsed = {}  # Start with an empty dictionary to store the parsed values
    for key, value in content.items():
        if "{" and "}" in str(value):
            parsed[key] = eval(
                "dict({})".format(str(value))
            )  # Evaluate the content to a dictionary format
    print("Parsed content:", parsed)
    return "Content successfully parsed as dictionary", 201
