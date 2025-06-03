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
    start = file_contents.find("{")
    end = file_contents.rfind("}")

    if start == -1 or end == -1:
        return jsonify({})

    content_str = file_contents[start + 1 : end]
    try:
        data_dict = eval(content_str)
    except:
        return jsonify({})

    return jsonify(data_dict)
