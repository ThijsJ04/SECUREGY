from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval", methods=["GET"])
def contents_dict():
    if "file_contents" not in request.files:
        return jsonify({"error": "Invalid Request Data"}), 400
    try:
        data = request.json["file_contents"]
        result = eval(
            data
        )  # eval function is unsafe, use exec for safer alternative if you are using Python 3
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(result)
