from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_function():
    data = request.get_json()
    file_contents = data.get("file_contents")
    if file_contents is None:
        return 'Error: Missing "file_contents" key in JSON payload', 400

    # Remove anything before the first '{' and after the last '}'
    cleaned_contents = ""
    for line in file_contents.split("\n"):
        line = line.strip()
        if line:  # Skip empty lines
            if line[0] == "{":
                cleaned_contents += line + "\n"
            elif line[-1] == "}":
                cleaned_contents += line + "\n"
            else:
                cleaned_contents += line
    file_contents = cleaned_contents[:-2]  # Remove the trailing newline characters

    try:
        content = eval(file_contents)
        return json.dumps({"content": content})
    except Exception as e:
        return str(e), 500


if __name__ == "__main__":
    app.run()
