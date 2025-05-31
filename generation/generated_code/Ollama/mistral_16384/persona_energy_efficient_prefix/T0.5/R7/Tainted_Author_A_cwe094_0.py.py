from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', '')
    cleaned_data = file_contents[1:-1] if cleaned_data.startswith("{") and cleaned_data.endswith("}") else ''
    return jsonify({'content': eval(cleaned_data)})