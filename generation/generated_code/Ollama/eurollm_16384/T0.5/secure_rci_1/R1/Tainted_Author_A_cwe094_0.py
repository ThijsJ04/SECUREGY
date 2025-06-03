from flask import Flask, request

app = Flask(__name__)


@app.route("/eval", methods=["GET"])
def eval_file():
    data = request.args.get("file_contents")
    if not data:
        return "Please provide a file contents to evaluate."

    # Remove anything before the first '{' and after the last '}'
    content = data[data.find("{") + 1 : -1]

    # Try to evaluate the content as a dictionary
    try:
        dict_content = eval(content)
        return str(dict_content)
    except Exception as e:
        return f"Error evaluating {content}: {str(e)}"
