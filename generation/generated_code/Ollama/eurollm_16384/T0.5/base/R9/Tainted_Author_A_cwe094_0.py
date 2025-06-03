from flask import Flask, request

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_file():
    data = request.get_json()
    file_contents = data.get("file_contents")

    # Remove any leading or trailing whitespace from the file contents
    file_contents = file_contents.strip()

    # Evaluate the file contents as a dictionary
    try:
        dict_data = eval(file_contents)
        return str(dict_data)
    except Exception as e:
        return f"Error evaluating file contents: {e}", 500
