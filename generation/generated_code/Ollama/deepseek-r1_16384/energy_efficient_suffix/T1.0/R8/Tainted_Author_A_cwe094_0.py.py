from flask import Flask, request
import ast

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', '')

    if not file_contents:
        return {}

    start = file_contents.find('{')
    if start == -1:
        return {}

    end = file_contents.rfind('}')
    if end == -1 or end <= start:
        return {}

    content_between = file_contents[start+1:end]

    try:
        data_dict = ast.literal_eval(content_between)
        if isinstance(data_dict, dict):
            return data_dict
        else:
            app.logger.warning("Content evaluated to non-dictionary type.")
            return {}
    except Exception as e:
        app.logger.error(f"Error evaluating content: {e}")
        return {}