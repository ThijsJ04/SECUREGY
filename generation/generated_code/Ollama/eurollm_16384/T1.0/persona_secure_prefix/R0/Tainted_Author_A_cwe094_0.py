import re
from flask import Flask, request

app = Flask(__name__)


@app.route("/eval", methods=["GET"])
def contents_dict():
    data = request.args.get("file_contents")
    if not data:
        return "File content not provided."

    # Remove everything before the first '{' and after the last '}'
    cleaned_data = re.sub(r"(?<!^)(?!$)[\{\}]", "", data)

    try:
        dict_data = eval(cleaned_data, {}, {})
        return str(dict_data)
    except Exception as e:
        return f"An error occurred while evaluating the dictionary. Error: {str(e)}"
