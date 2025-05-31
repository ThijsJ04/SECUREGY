from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)

    if not file_contents:
        return jsonify({"error": "Missing 'file_contents' parameter."}), 400

    # Remove any characters before the first '{' and after the last '}'
    cleaned_content = file_contents.strip('{}').strip()

    if not cleaned_content:
        return jsonify({"error": "Invalid JSON data."}), 400

    try:
        # Evaluate the content to a dictionary
        result = eval(cleaned_content)
        if isinstance(result, dict):
            return jsonify(result), 200
        else:
            return jsonify({"error": "Invalid JSON data."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400