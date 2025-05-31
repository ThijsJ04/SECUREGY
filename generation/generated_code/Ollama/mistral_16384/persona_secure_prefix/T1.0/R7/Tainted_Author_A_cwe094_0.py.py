from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents')
    if file_contents:
        # remove anything before the first '{' and after the last '}'
        clean_content = file_contents[file_contents.find('{'):]
        clean_content = clean_content[:clean_content.rfind('}') + 1]
        try:
            # evaluate the cleaned content as a dictionary
            return json.loads(clean_content)
        except ValueError:
            return {"error": "Invalid JSON"}