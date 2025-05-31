from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_content():
    file_contents = request.form['file_contents']
    data = {}
    for line in file_contents.splitlines():
        if '{' not in line:  # skip empty lines
            continue
        start = next((i for i, x in enumerate(line) if x == '{'), len(line))
        end = -next((i for i, x in enumerate(reversed(line[start:]), start+1) if x == '}' and line[i] != '}', None)  # find matching closing brace
        content = ''
        for i in range(start + 1, end):
            if line[i] == ',':
                content += line[i - 1].strip()
                line = line[i+1:]
                break
            content += line[i]  # add characters between braces
        data.update({line.strip(): content})
    return json.dumps(data)