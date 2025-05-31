from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', default='', type=str)
    if not file_contents:
        return {"error": "No 'file_contents' provided."}, 400

    # Remove everything before the first '{' and after the last '}'
    clean_content = file_contents.strip('{}')
    start_index = clean_content.find('{')
    end_index = clean_content.rfind('}')

    if start_index == -1 or end_index == -1:
        return {"error": "Invalid JSON format."}, 400

    json_string = clean_content[start_index:end_index+1]
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        return {"error": f"Could not parse JSON data. {e}"}, 400