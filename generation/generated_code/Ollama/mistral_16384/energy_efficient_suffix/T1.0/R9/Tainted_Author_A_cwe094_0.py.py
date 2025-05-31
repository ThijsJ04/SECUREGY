 from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    data = request.args.get('file_contents', default=None)

    if not data:
        return jsonify({"error": "No data provided"}), 400

    cleaned_data = data[data.index('{') : data.rindex('}') + 1]

    try:
        result = eval(cleaned_data)
        if isinstance(result, dict):
            return jsonify(result)
        else:
            return jsonify({"error": "Expected a dictionary but received another type"}), 400
    except SyntaxError as e:
        return jsonify({"error": f"Invalid JSON syntax: {str(e)}"}), 400