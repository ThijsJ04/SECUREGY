 from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)

    if not file_contents:
        return "Error: 'file_contents' parameter is missing.", 400

    # Remove anything before the first '{' and after the last '}'
    cleaned_contents = file_contents.strip('{}')

    try:
        content_dict = eval(cleaned_contents)
        return content_dict
    except Exception as e:
        return f"Error: {str(e)}", 400