from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", None)

    if not file_contents:
        return "Missing required parameter 'file_contents'", 400

    # Remove anything before the first '{' and after the last '}'
    cleaned_contents = file_contents.strip("{}").strip()

    try:
        # Evaluate the content to a dictionary
        result = eval(cleaned_contents)

        if not isinstance(result, dict):
            return "The provided JSON string is not valid", 400

        return result
    except Exception as e:
        return str(e), 400
