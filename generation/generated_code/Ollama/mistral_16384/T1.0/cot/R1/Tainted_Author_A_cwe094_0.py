from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", type=str)

    # Remove anything before the first '{' and after the last '}'
    cleaned_contents = file_contents[
        file_contents.find("{") : -file_contents[-1:].index("}")
    ]

    try:
        return jsonify(eval(cleaned_contents))
    except Exception as e:
        return str(e)
