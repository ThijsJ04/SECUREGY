from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval", methods=["GET"])
def contents_dict():
    data = request.args.get("file_contents")  # Get the data from the request
    if not data:
        return "Error: No file content provided."

    output_data = eval(data) if data else None
    return jsonify(output_eval=json.dumps(output_data))
