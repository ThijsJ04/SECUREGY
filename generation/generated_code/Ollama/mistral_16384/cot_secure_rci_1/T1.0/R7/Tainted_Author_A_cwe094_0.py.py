from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents')
    if file_contents:
        # Remove anything before the first '{' and after the last '}'
        cleaned_content = file_contents[file_contents.find('{'):]
        cleaned_content = cleaned_content[:cleaned_content.rfind('}') + 1]
        return eval(cleaned_content)