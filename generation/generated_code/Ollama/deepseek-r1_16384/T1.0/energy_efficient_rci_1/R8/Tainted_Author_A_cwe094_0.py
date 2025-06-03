from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")

    # Extract content between first '{' and last '}'
    start = file_contents.find("{")
    end = file_contents.rfind("}")
    if start == -1 or end == -1:
        return {}
    content = file_contents[start + 1 : end]

    try:
        data_dict = json.loads(content)
        return data_dict
    except json.JSONDecodeError:
        return {}


if __name__ == "__main__":
    app.run()
