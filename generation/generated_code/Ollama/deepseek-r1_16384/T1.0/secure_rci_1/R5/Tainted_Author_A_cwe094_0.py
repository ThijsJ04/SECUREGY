from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")

    start_brace = file_contents.find("{")
    if start_brace == -1:
        return jsonify({"error": "No opening brace found"})

    end_brace = file_contents.rfind("}")
    if end_brace == -1:
        return jsonify({"error": "No closing brace found"})

    cleaned_content = file_contents[start_brace + 1 : end_brace]

    try:
        result_dict = eval(cleaned_content)
        return jsonify(result_dict)
    except Exception as e:
        return jsonify({"error": str(e)})
