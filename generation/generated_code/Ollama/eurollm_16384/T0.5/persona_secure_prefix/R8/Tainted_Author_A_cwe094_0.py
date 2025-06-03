from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def contents_dict():
    file_contents = request.get_json()
    data = file_contents.pop("data")  # Assuming 'data' is the key for the content

    # Remove any extra whitespace and newline characters from the content
    cleaned_content = data.strip().replace("\n", "")

    # Evaluate the content as a dictionary
    eval_result = eval(cleaned_content)

    return jsonify({"result": eval_result})
