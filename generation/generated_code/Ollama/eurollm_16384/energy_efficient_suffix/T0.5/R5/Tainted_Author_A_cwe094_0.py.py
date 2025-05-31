from flask import Flask, request

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_contents():
    data = request.form.get('file_contents')
    if not data:
        return "Missing file contents"

    # Remove anything before the first '{' and after the last '}'
    data = data[data.find('{')+1:data.rfind('}')]

    # Evaluate the content to a dictionary
    try:
        dict_contents = eval(data)
        return str(dict_contents)
    except Exception as e:
        return f"Error evaluating contents: {str(e)}"