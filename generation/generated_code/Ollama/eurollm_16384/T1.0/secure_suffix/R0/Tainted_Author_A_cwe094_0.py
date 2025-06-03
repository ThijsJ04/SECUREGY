from flask import Flask, request
import ast

app = Flask(__name__)


def eval_ast(node):
    try:
        return ast.literal_eval(node)
    except (SyntaxError, ValueError, TypeError) as err:
        print("Failed to evaluate the expression:", node)
        print("Exception:", err)
        return {}  # Return an empty dictionary if the expression can't be evaluated


@app.route("/eval", methods=["POST"])
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    post_data = request.get_json()  # Assuming JSON is sent in the request body
    file_contents = post_data["file_contents"]

    if file_contents:
        try:
            data = eval_ast(file_contents)
            return jsonify({"result": data})  # Return the result as JSON
        except Exception as err:
            return jsonify(
                {"error": str(err)}
            )  # Return an error message if evaluation fails
    else:
        return jsonify(
            {"error": "No file_contents found in request"}
        )  # Return an error message for missing data
