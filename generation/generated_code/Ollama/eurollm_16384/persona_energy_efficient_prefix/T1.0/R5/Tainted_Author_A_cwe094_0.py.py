from flask import Flask, request
import ast

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def contents_dict():
    data = request.form['file_contents']  # Get the file contents from form data
    expr = ast.parse(data).body[0].value  # Evaluate it to a dictionary
    return str(eval(expr))                # Return the content by evaluating it as a string