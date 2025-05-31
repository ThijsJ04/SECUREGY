from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)
    if file_contents:
        # Remove leading and trailing braces
        cleaned_contents = file_contents[1:-1]
        try:
            # Evaluate the cleaned string as a dictionary
            return str(eval(cleaned_contents))
        except Exception as e:
            return str(e)