from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents')
    if not file_contents:
        return "Error: No data provided.", 400

    # Remove whitespaces and comments
    file_contents = file_contents.strip().replace('\n', ' ').replace('\r', ' ') \
                                .replace('{#', '{').replace('#}', '}') \
                                .replace('{//', '{').replace('//}', '}')

    # Find the index of opening brace and closing brace, then slice the string
    open_brace = file_contents.find('{')
    close_brace = file_contents[::-1].find('}') + len(file_contents) - 1

    if open_brace == -1 or close_brace == -1:
        return "Error: Invalid JSON format.", 400

    # Evaluate the string as a dictionary
    try:
        content_dict = eval(file_contents[open_brace:close_brace])
    except Exception as e:
        return f"Error: {str(e)}", 400

    return content_dict