from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    content = request.args.get("file_contents")
    start = content.find("{")
    end = content.rfind("}")
    if start == -1 or end == -1:
        return jsonify({"error": "Invalid format"}), 400
    content_str = content[start + 1 : end]
    data_dict = eval(content_str)
    return jsonify(data_dict)


if __name__ == "__main__":
    app.run(debug=True)
