from flask import Flask, request, jsonify
import ujson as json
import yaml

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    try:
        file_contents = request.data
        content = json.loads(json.dumps({'type': file_contents, 'contents': file_contents}), object_hook=lambda d: dict(d))["contents"]
        if "YAML" in file_contents or "YAML" == content[0]:
            return jsonify(yaml.safe_load_all(file_contents)[1])
        else:
            return jsonify({"error": f"Unsupported content type '{file_contents}'"})
    except Exception as e:
        return jsonify({"error": str(e)})