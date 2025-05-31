from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_content = request.form.get('file_contents', '')
    start_index = file_content.find('{')
    end_index = file_content.rfind('}')
    content_to_eval = file_content[start_index+1:end_index]
    result = eval(content_to_eval)
    return result

if __name__ == '__main__':
    app.run(debug=True)