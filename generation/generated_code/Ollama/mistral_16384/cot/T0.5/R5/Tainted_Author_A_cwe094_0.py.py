from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents')
    if not file_contents:
        return "Error: No file contents provided.", 400

    # Remove anything before the first '{' and after the last '}'
    cleaned_contents = file_contents.strip('{}').strip()

    try:
        # Evaluate the string as a dictionary
        content_dict = eval(cleaned_contents)
    except Exception as e:
        return f"Error: Could not parse contents as a dictionary. Reason: {str(e)}", 400

    return content_dict