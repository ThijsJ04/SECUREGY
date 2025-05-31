from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    content = request.headers.getlist("file_contents")[0]
    cleaned_content = content[content.find('{'):].strip()
    return jsonify(eval(cleaned_content))