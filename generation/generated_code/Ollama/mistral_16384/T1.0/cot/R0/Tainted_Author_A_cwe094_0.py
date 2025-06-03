from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents")
    if not file_contents:
        return jsonify({"error": "No file contents provided."}), 400

    # remove whitespace and comments before the first '{'
    cleaned_start = re.sub(r"\s*\{|\/\*.*\*/", "{", file_contents, flags=re.DOTALL)

    # remove whitespace and comments after the last '}'
    cleaned_end = re.sub(r"}\s*|\*.*\*/\s*$", "}", cleaned_start, flags=re.DOTALL)

    try:
        content_dict = eval(cleaned_end)
        return jsonify(content_dict)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
