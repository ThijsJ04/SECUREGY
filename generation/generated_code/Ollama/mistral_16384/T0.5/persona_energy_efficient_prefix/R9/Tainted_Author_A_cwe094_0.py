from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", None)

    if not file_contents:
        return "Error: No 'file_contents' provided.", 400

    # Remove any characters before the first '{' and after the last '}'
    cleaned_content = file_contents[file_contents.find("{") :]
    cleaned_content = cleaned_content[: cleaned_content.rfind("}") + 1]

    try:
        return jsonify(eval(cleaned_content)), 200
    except Exception as e:
        return str(e), 500
