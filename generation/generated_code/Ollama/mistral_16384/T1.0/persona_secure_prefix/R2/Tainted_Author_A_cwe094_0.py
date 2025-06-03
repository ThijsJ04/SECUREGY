from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", type=str)
    if file_contents:
        cleaned_contents = file_contents[1:-1]  # Remove first '{' and last '}'
        try:
            return jsonify(eval(cleaned_contents))
        except Exception as e:
            return str(e), 500
