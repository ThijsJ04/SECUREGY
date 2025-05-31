 from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)
    if not file_contents:
        return 'No data provided.', 400

    # Remove whitespace and newlines
    cleaned_contents = file_contents.replace('\n', '').replace(' ', '')

    # Find indexes of the first and last brace (curly bracket)
    opening_brace_index = cleaned_contents.find('{')
    closing_brace_index = cleaned_contents.rfind('}')

    if opening_brace_index == -1 or closing_brace_index == -1:
        return 'Invalid JSON format.', 400

    # Extract the part between braces and evaluate it as a dictionary
    json_string = cleaned_contents[opening_brace_index:closing_brace_index + 1]
    try:
        return json.loads(json_string), 200
    except ValueError:
        return 'Invalid JSON format.', 400