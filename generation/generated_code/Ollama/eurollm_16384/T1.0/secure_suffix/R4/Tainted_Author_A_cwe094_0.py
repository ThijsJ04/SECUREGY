from flask import request, jsonify
import re

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_contents():
    file_content = request.files.get("file_contents")
    content_dict = eval(re.sub(r"^\s*|\s*$", "", file_content))
    return jsonify({"result": content_dict})
