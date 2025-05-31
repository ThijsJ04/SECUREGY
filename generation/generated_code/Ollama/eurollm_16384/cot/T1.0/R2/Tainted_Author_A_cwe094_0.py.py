from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def eval_file():
    content = request.args.get('file_contents', default='No file provided')
    if not content:
        return 'Please provide a file'

    try:
        contents = content[1:-1]  # remove everything before the first '{' and after the last '}'
        parsed_content = eval(contents)
        return str(parsed_content)
    except Exception as e:
        return f"An error occurred: {e}"