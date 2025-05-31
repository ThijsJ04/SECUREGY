 from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)

    if not file_contents:
        return "Missing 'file_contents' parameter", 400

    # Remove whitespaces, tabs and newlines from start and end
    file_contents = file_contents.strip()

    # Find the position of the first '{' and last '}' (if any)
    first_bracket_pos = file_contents.find('{')
    last_bracket_pos = file_contents.rfind('}')

    if first_bracket_pos == -1 or last_bracket_pos == -1:
        return "Invalid JSON format", 400

    # Extract the part between the brackets and evaluate as a dictionary
    content = file_contents[first_bracket_pos:last_bracket_pos+1]
    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        return str(e), 400