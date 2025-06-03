from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")
    # Remove anything before the first '{' and after the last '}'
    cleaned_contents = file_contents[file_contents.find("{") :][
        : -file_contents[-1].index("}") + 1
    ]
    try:
        return {key: value for key, value in ast.literal_eval(cleaned_contents).items()}
    except SyntaxError:
        return {"error": "Invalid dictionary syntax"}
