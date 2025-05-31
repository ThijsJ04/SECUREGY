from flask import Flask, request
import re

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def contents_dict():
    file_contents = request.form['file']
    pattern = r"^(\{\{(.*?)\})?"  # matching { character and everything inside 
                                 # (matches everything except the closing ))
    matched = re.search(pattern, file_contents)
    if matched:
        group = matched.group(1).strip()
        try:
            return str(eval(group))  # eval function to evaluate group inside { } brackets
        except Exception as error:
            return "Error: {}".format(error)
    else: 
        return file_contents