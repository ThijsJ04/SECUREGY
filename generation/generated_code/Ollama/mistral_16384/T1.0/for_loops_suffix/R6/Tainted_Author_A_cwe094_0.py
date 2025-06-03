from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents")

    # Remove anything before the first '{' and after the last '}'
    clean_file_contents = file_contents[
        file_contents.find("{") : -1 * file_contents[-1:].index("}")
    ]

    # Return the content by evaluating it to a dictionary
    return jsonify(eval(clean_file_contents))
