from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    content = request.values.get('file_contents')
    if not content:
        return {}
    start = content.find('{')
    end = content.rfind('}')
    if start == -1 or end == -1:
        return {}
    extracted_content = content[start:end+1]
    try:
        data = eval(extracted_content)
    except:
        return {}
    return data