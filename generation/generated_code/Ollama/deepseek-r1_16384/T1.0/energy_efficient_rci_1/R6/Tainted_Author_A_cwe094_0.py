from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    data = request.get_json()
    file_contents = data.get("file_contents", "")
    start_index = file_contents.find("{")
    end_index = file_contents.rfind("}")

    if start_index == -1 or end_index == -1:
        return {}

    content_to_evaluate = file_contents[start_index : end_index + 1]

    try:
        # Using ast.literal_eval for safer evaluation
        import ast

        result_dict = ast.literal_eval(content_to_evaluate)
        if isinstance(result_dict, dict):
            return result_dict
        else:
            return {}
    except (ValueError, SyntaxError, TypeError) as e:
        print(f"Error evaluating content: {e}")
        return {}
