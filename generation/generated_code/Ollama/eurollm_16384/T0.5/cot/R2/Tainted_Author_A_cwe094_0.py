from flask import Flask, request
import yaml  # or json depending on your file format

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", default="example.yaml")
    try:
        with open(file_contents, "r") as f:
            data = yaml.safe_load(f)  # or json.loads() for JSON files
    except FileNotFoundError:
        abort(404)
    return dict(data)
