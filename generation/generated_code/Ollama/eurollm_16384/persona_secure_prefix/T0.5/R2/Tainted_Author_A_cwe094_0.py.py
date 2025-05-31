from flask import Flask, request

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_request():
    file_contents = request.form["file_contents"]  # Assuming file contents is a form field
    data = {}
    for line in file_contents.splitlines():
        if '{' in line:
            key, value = line.split('}')[-1].strip().split('{')[0].strip()
            data[key] = eval(value) if 'eval' not in request.form else None
    return jsonify(data)