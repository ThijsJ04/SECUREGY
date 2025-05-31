from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.values.get('file_contents', '')
    if not file_contents:
        return jsonify({})

    content_start = file_contents.find('{')
    if content_start == -1:
        return jsonify({})

    content_end = file_contents.rfind('}')
    if content_end == -1 or content_end < content_start:
        return jsonify({})

    processed_content = file_contents[content_start:content_end + 1]

    try:
        result_dict = eval(processed_content)
        if isinstance(result_dict, dict):
            return jsonify(result_dict)
        else:
            return jsonify({})
    except Exception as e:
        return jsonify({})