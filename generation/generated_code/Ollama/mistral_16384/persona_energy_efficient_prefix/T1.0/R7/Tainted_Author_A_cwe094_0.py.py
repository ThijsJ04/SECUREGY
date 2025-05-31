from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    data = request.files['file_contents']
    content = data.read().decode('utf-8')
    start = content.find('{') if '{' in content else 0
    end = content.rfind('}') if '}' in content else len(content)
    cleaned_content = content[start:end+1]
    return jsonify(eval(cleaned_content))