from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)
    if file_contents:
        # Remove anything before the first '{' and after the last '}'
        cleaned_content = file_contents.strip('{}').strip()
        try:
            # Evaluate the string as a dictionary
            return {cleaned_content} if cleaned_content else {}
        except Exception as e:
            print(f'Error evaluating content: {e}')
            return {}