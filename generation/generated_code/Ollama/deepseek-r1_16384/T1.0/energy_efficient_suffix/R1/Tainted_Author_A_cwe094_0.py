from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.args.get("file_contents") or request.form.get("file_contents")
    if not data:
        return jsonify({"error": "No file_contents provided"}), 400

    start = data.find("{")
    end = data.rfind("}")
    if start == -1 or end == -1:
        return jsonify({"error": "Invalid format"}), 400

    content = data[start + 1 : end]
    try:
        result = eval(content)  # Be cautious with using eval in production
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
