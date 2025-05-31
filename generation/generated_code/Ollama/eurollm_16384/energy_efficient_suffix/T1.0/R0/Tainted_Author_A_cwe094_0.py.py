from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def contents_dict():
    file_contents = request.args.get("file")
    data = file_contents[file_contents.find("{") + 1:file_contents.rfind("}")]  # Remove the first '{' and last '}'
    if "." in data:
        try:
            content = json.loads(data)
            return str(content)
        except:
            return "Error"
    else:
        content = eval(data)  # Evaluate the content as a dictionary
        return str(content)