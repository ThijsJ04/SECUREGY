from flask import request, jsonify
import ast

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    data = {"message": "", "content": None}

    # Get file contents from the request
    file_contents = request.json["file_contents"]

    # Remove anything before the first '{' and after the last '}'
    try:
        ast_tree = ast.parse(file_contents)
        eval_tree = eval(str(ast_tree), {}, {})
        data["content"] = eval_tree
    except Exception as e:
        data["message"] = str(e)

    # Return the evaluated content or error message
    data["result"] = (
        jsonify(data)
        if "content" in data
        else jsonify({"message": "Error evaluating content."})
    )
    return data, 200
