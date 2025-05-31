from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)
    if not file_contents:
        return jsonify({"error": "No 'file_contents' provided."}), 400

    start_index = file_contents.find('{') + 1
    end_index = file_contents.rfind('}')

    if start_index == -1 or end_index == -1:
        return jsonify({"error": "Invalid JSON format."}), 400

    try:
        parsed_json = eval(file_contents[start_index:end_index])
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    return jsonify(parsed_json)