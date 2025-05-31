from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents')
    if file_contents:
        # Remove whitespaces and find the first '{' and last '}' indexes
        cleaned_file_contents = file_contents.strip().replace(' ', '')
        start_index = cleaned_file_contents.find('{')
        end_index = cleaned_file_contents.rfind('}')

        # Slice the string and evaluate the substring as a JSON object
        content_dict = eval(cleaned_file_contents[start_index:end_index+1])
        return jsonify(content_dict)
    else:
        return "Error: No data provided.", 400