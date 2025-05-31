from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)
    if not file_contents:
        return "", 400

    # Remove any characters before the first '{' and after the last '}'
    cleaned_contents = file_contents.strip('{}').strip()

    # Evaluate the content as a dictionary
    try:
        result = eval(cleaned_contents)
        if isinstance(result, dict):
            return result
        else:
            raise ValueError("The evaluated content is not a dictionary.")
    except Exception as e:
        return str(e), 400