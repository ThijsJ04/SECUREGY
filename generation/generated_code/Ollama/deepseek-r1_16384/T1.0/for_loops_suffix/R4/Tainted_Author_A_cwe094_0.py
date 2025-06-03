from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    file_contents = request.args.get("file_contents", "")
    start_idx = file_contents.find("{")
    end_idx = file_contents.rfind("}")
    if start_idx == -1 or end_idx == -1:
        return jsonify({})
    expr = file_contents[start_idx + 1 : end_idx]
    try:
        result = eval(expr)
        return jsonify(result)
    except:
        return jsonify({"error": "invalid expression"}), 400
