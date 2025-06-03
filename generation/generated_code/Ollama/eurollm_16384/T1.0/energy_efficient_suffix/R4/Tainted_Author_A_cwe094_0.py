from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    try:
        with open(request.args.get("file_contents"), "r") as file:
            json_or_yaml = file.read()
    except FileNotFoundError:
        return {"error": "File not found."}, 404

    try:
        parsed_content = (
            yaml.safe_load(json_or_yaml)
            if "file_contents" in request.args
            else json.loads(json_or_yaml)
        )  # Use yaml if file_contents exists, otherwise use json
        return {**parsed_content, "error": ""}, 200
    except Exception as e:
        print("An error occurred: {}".format(str(e)))
        return {"error": str(e)}, 500
