from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents")
    if not file_contents:
        return {"error": "No file contents provided"}, 400

    # Remove anything before the first '{' and after the last '}'
    cleaned_json = file_contents[file_contents.find("{") :].strip()

    try:
        return (
            {cleaned_json}
            if cleaned_json.isjson()
            else {"error": "Invalid JSON format"}
        )
    except ValueError as e:
        return {"error": str(e)}
