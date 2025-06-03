from flask import Flask, request
import ast  # Using ast.literal_eval for safe evaluation

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    content = request.args.get("file_contents", "")
    if not content:
        return {}
    first_brace = content.find("{")
    last_brace = content.rfind("}")
    if first_brace == -1 or last_brace == -1:
        return {}
    dict_str = content[first_brace : last_brace + 1]
    try:
        # Using ast.literal_eval for safe evaluation of dictionary
        result_dict = ast.literal_eval(dict_str)
        if isinstance(result_dict, dict):
            return result_dict
        else:
            return {}
    except (ValueError, SyntaxError):
        return {}


if __name__ == "__main__":
    app.run(debug=True)
