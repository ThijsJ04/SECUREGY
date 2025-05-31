from flask import Flask, request

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def contents_dict():
    content = request.form.get('file_contents')
    if not content:
        return 'Please provide content in the form field.'

    # Remove anything before the first '{' and after the last '}'
    cleaned_content = content[content.find('{') + 1: content.rfind('}')]

    # Evaluate the cleaned content as a dictionary and return its contents
    try:
        data = eval(cleaned_content)
        return str(data)
    except Exception as e:
        return f'Error evaluating content: {e}'